"""
Extended simulation utilities:
- Transaction generation
- Toy PoW mining simulation (hashrate distribution)
- Toy PoS block selection (stake distribution)
- Monte Carlo runs to estimate double-spend success probability / confirmations
- Attack graph builder (toy)
"""

import random, math, hashlib, time
from datetime import datetime
import json

def generate_tx(sender, receiver, amount, nonce=None):
    """Create a deterministic tx hash from fields (toy)."""
    nonce = nonce if nonce is not None else random.randint(0, 1_000_000)
    s = f"{sender}|{receiver}|{amount}|{nonce}|{time.time()}"
    tx_hash = hashlib.sha256(s.encode()).hexdigest()
    return {
        "tx_hash": tx_hash,
        "sender": sender,
        "receiver": receiver,
        "amount": float(amount),
        "nonce": nonce,
        "timestamp": datetime.utcnow().isoformat()
    }

def simulate_pow_block(miners_hashrate, difficulty=1.0, block_time_target=10.0, txs=None):
    """
    Simplified PoW model:
    - miners_hashrate: list of hash power shares (they sum to some total)
    - difficulty: scaling factor (higher -> slower)
    - block_time_target: expected time (sec) per block for the whole network at given total hashrate
    Returns miner index that found the block and block_time.
    """
    total_power = sum(miners_hashrate)
    # time to next block is exponential with rate proportional to total_power/difficulty
    # lambda = total_power / difficulty -> mean = difficulty / total_power
    if total_power <= 0:
        return {"winner": None, "block_time": float('inf')}
    mean = difficulty / total_power * block_time_target
    # sample an exp; but keep deterministic-ish for reproducibility via random
    block_time = random.expovariate(1.0/mean)
    # winner is selected by proportional to hashrate
    r = random.random() * total_power
    cum = 0.0
    for i,p in enumerate(miners_hashrate):
        cum += p
        if r <= cum:
            return {"winner": i, "block_time": block_time, "txs_in_block": len(txs) if txs else 0}
    return {"winner": len(miners_hashrate)-1, "block_time": block_time, "txs_in_block": len(txs) if txs else 0}

def simulate_pos_epoch(stakes):
    """
    Simplified PoS validator selection:
    - stakes: list of stake values per validator
    Selects one validator proportionally to stake.
    """
    total = sum(stakes)
    if total <= 0: 
        return {"validator": None}
    r = random.random() * total
    cum = 0.0
    for i,s in enumerate(stakes):
        cum += s
        if r <= cum:
            return {"validator": i}
    return {"validator": len(stakes)-1}

def compute_confirmation_time(avg_latency_ms, confirmations=6):
    """Toy map latency to confirmation time"""
    # assume each confirmation ~ avg_latency * factor (network propagation + block time)
    return max(0.1, (avg_latency_ms/1000.0) * confirmations)

def single_double_spend_trial(num_nodes=50, honest_ratio=0.8, tx_rate=5.0, pow=True, miners_hash=None, stakes=None, seed=None):
    """
    Single Monte Carlo trial returning boolean success of attacker double-spend.
    - If pow=True, we use miners_hash as power distribution (list, attacker is index 0)
    - If pow=False, use stakes list (attacker index 0)
    This toy model returns True if attacker manages to produce a competing chain with enough work/stake.
    """
    if seed is not None: random.seed(seed + random.randint(0,10_000))
    # attacker share:
    if pow:
        if not miners_hash: raise ValueError("miners_hash required for pow")
        attacker_share = miners_hash[0] / sum(miners_hash)
    else:
        if not stakes: raise ValueError("stakes required for pos")
        attacker_share = stakes[0] / sum(stakes)
    # basic success heuristic: attacker success probability grows quickly if share>0.5
    # and also depends on tx rate & confirmation time
    avg_latency_ms = random.gauss(100, 20)
    conf_time = compute_confirmation_time(avg_latency_ms, confirmations=6)
    # noise factor for network variability
    network_noise = random.random() * 0.5 + 0.75
    # risk formula (toy): attacker success P = sigmoid(k*(share - 0.5))*modifier
    k = 12.0
    base = 1.0 / (1.0 + math.exp(-k * (attacker_share - 0.5)))
    throughput_factor = min(2.0, tx_rate / 5.0)
    time_factor = min(2.0, conf_time / 3.0)
    p = base * network_noise * throughput_factor * time_factor
    return random.random() < min(1.0, p)

def monte_carlo_double_spend(runs=1000, **kwargs):
    """Run many trials and estimate probability of attacker success."""
    succ = 0
    results = []
    for i in range(runs):
        ok = single_double_spend_trial(seed=i, **kwargs)
        results.append(1 if ok else 0)
        succ += 1 if ok else 0
    prob = succ / runs
    return {"runs": runs, "successes": succ, "probability": prob, "series": results}

def attack_graph_simple(num_nodes=10, attacker_index=0, honest_ratio=0.8):
    """
    Build a tiny directed graph where nodes are actors (attacker + honest)
    Edge weights indicate probability of successful attack step; this is mostly illustrative.
    """
    nodes = []
    edges = []
    for i in range(num_nodes):
        nodes.append({"id": i, "type": "attacker" if i==attacker_index else "honest", "capacity": (0.2 if i==attacker_index else (honest_ratio/(num_nodes-1)))})
    # connect attacker to some targets with higher weights
    for i in range(1, min(6, num_nodes)):
        edges.append({"from": attacker_index, "to": i, "weight": round(random.random()*0.6 + 0.2, 3)})
    # add some honest connectivity
    for i in range(1, num_nodes):
        for j in range(i+1, min(num_nodes, i+4)):
            edges.append({"from": i, "to": j, "weight": round(random.random()*0.3 + 0.05, 3)})
    return {"nodes": nodes, "edges": edges}

def estimate_max_throughput(num_nodes, tx_size_bytes=250, block_size_bytes=1_000_000, block_interval=10.0):
    """
    Rough throughput estimate:
      throughput_tx_per_s = (block_size_bytes / tx_size_bytes) / block_interval
    Scales with block interval and block size; it's a toy/approximation.
    """
    tx_per_block = block_size_bytes / tx_size_bytes
    tx_per_s = tx_per_block / block_interval
    return {"tx_per_block": tx_per_block, "tx_per_second": tx_per_s, "approx_per_node": tx_per_s / max(1, num_nodes)}

# helpers to convert to serializable
def to_json(obj):
    try:
        return json.dumps(obj)
    except Exception:
        return json.dumps(str(obj))




def run_sample_simulation(params):
    num_nodes = int(params.get('num_nodes', 50))
    honest = float(params.get('honest_ratio', 0.8))
    tx_rate = float(params.get('tx_rate', 5.0))
    latencies = [max(1.0, random.gauss(100, 20)) for _ in range(num_nodes)]
    fail_prob = max(0.0, 1.0 - honest)
    failed = [1 for _ in range(int(num_nodes * fail_prob))]
    alive = num_nodes - len(failed)
    avg_latency = sum(latencies) / len(latencies)
    confirmation_time = max(0.5, avg_latency/1000.0 * 6)
    dishonest_ratio = 1.0 - honest
    double_spend_risk = min(1.0, dishonest_ratio * (tx_rate/10.0) * (confirmation_time/2.0))
    duration = 30
    timeline = []
    for t in range(duration):
        active = max(1, alive - int(0.05 * t))
        throughput = active * tx_rate * max(0.1, 1.0 - random.random()*0.1)
        timeline.append({'t': t, 'throughput': throughput})
    return {
        'num_nodes': num_nodes,
        'honest_ratio': honest,
        'tx_rate': tx_rate,
        'avg_latency_ms': avg_latency,
        'alive_nodes': alive,
        'double_spend_risk': double_spend_risk,
        'timeline': timeline,
    }

def summarize_result(result):
    return {
        'nodes': result['num_nodes'],
        'alive': result['alive_nodes'],
        'avg_latency_ms': round(result['avg_latency_ms'], 2),
        'double_spend_risk_pct': round(result['double_spend_risk'] * 100, 2)
    }