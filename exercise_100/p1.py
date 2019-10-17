a = [1,2,3,4]
count = 0
for i in  a:
        for j in a:
                for k in a:
                        if (i != j)and(i != k)and(j != k):
                                print(str(i)+str(j)+str(k))
                                count += 1 
print('\n' + str(count))

# for a in range(1, 5):
#     for b in range(1, 5):
#         for c in range(1, 5):
#             if a != b and b != c and a != c:
#                 print(a, b, c)
#         pass

# pass 是占位语句，不做任何事