# x = int(input('Please input x:'))
# y = int(input('Please input y:'))
# z = int(input('Please input z:'))

# if x > y:
#         a = x
#         x = y
#         y = a
# if y > z:
#         a = y
#         y = z
#         z = a
# print(' The sorted results are:')
# print(str(x) +' ' + str(y) +' ' + str(z))


'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''

arr_str = input('请输入三个整数：\n')

arr = arr_str.split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

arr.sort(reverse=False)

print('排序结果：\n' + str(arr))