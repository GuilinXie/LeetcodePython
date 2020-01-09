from math import log2

a = [0.5, 0.5]
b = [0.3, 0.7]
# average total bits of b from a, a->ground true, b->predict result
cross_entropy = -sum(a[i] * log2(b[i]) for i in range(len(a)))
# average extra bits of b from a
KL_divergency = -sum(a[i] * log2(b[i]/a[i]) for i in range(len(a)))
# total bits needed for a
entropy = -sum([a[i] * log2(a[i]) for i in range(len(a))])