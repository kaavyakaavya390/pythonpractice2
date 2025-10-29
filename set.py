# ********** SET **************
set1 = ()
set2 = {2, 3, 2, 3, 3, 3, 3, 3}
set3 = {1, 2, 4, 4, 5, 5, 1, 3, 2}
set4 = ()  # {[1,2,3],[1,2,3],[4,3,1],[3,2,1]}
set1 = set((x for x in range(0, 20) if x % 2 == 0))
print(type(set2))
print("set1 : ", set1, "\nset2 : ", set2, "\nset3 : ", set3, "\nset4 : ", set4)

# -------operations---------
union = set1 | set2
print("union of set1 | set2 : ", union)
intersect = set1 & set2
print("Intersection of set1 & set2 : ", intersect)
diff = set1 - set2
print("Difference of set1 - set2 : ", diff)
set1.add(11)
set2.add(1222)
print(set2)
set2.remove(2)
print(set2)
