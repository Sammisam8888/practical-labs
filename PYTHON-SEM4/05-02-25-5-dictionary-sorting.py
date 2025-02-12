# Original dictionary
D = {
    'T1': ['E', 'K', 'M', 'N', 'O', 'Y'],
    'T2': ['D', 'E', 'K', 'N', 'O', 'Y'],
    'T3': ['A', 'E', 'K', 'M'],
    'T4': ['C', 'K', 'M', 'U', 'Y'],
    'T5': ['C', 'E', 'I', 'K', 'O', 'O']
}

# A) Calculate support count
support_count = {}
for items in D.values():
    for item in items:
        support_count[item] = support_count.get(item, 0) + 1

print("Support count (D1):", support_count)

# B) Sort by decreasing order
D1 = dict(sorted(support_count.items(), key=lambda x: x[1], reverse=True))
print("Sorted D1:", D1)

# C) Remove items with support count < 3
D1 = {k: v for k, v in D1.items() if v >= 3}
print("D1 after removing items with support count < 3:", D1)

# D) Update original dictionary D
frequent_items = set(D1.keys())
D = {k: [item for item in v if item in frequent_items] for k, v in D.items()}
print("Updated dictionary D:", D)
