
"""Simple script to create a sample simulation and print a short markdown report to stdout.
Run: python scripts/generate_report.py
"""
import json, os, sys
from app.simulate import run_sample_simulation, summarize_result

def main():
    params = {'num_nodes': 100, 'honest_ratio': 0.85, 'tx_rate': 4.5}
    r = run_sample_simulation(params)
    s = summarize_result(r)
    md = []
    md.append('# Sample CNS Simulation Report')
    md.append('**Parameters**: ' + json.dumps(params))
    md.append('**Summary**: ' + json.dumps(s))
    md.append('\n**Time series (first 10 points):**')
    for p in r['timeline'][:10]:
        md.append(f"- t={p['t']}: throughput={p['throughput']:.2f}")
    print('\n'.join(md))

if __name__ == '__main__':
    main()
