a = frozenset([1, 2, 3])
b = frozenset([3, 4])

print(a.union(b))                 # frozenset({1, 2, 3, 4})
print(a.intersection(b))          # frozenset({3})
print(a.difference(b))            # frozenset({1, 2})
print(a.symmetric_difference(b))  # frozenset({1, 2, 4})
print(a.isdisjoint(b))            # False
print(a.issubset(b))              # False
print(a.issuperset(b))            # False