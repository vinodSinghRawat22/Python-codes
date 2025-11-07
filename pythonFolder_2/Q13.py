# 13. Create a set and perform union, intersection, and difference. 

set1 = { 1, 9, 5, 4}
set2 = { 10, 6, 1, 2, 5}

print(f"\n{set1} Union {set2}: {set1.union(set2)}") 

print(f"\n{set1} intersection {set2} : {set1.intersection(set2)} ")

print(f"\n{set1} - {set2} : {set1.difference(set2)} ")
print(f"\n{set2} - {set1} : {set2.difference(set1)} ")