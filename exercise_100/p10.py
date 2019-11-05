# import time

# localtime = time.asctime(time.localtime(time.time()))


# localtime = localtime.split()
# format_time = localtime[4] + '-' + localtime[1] + '-' + localtime[2] + ' ' + localtime[3]
# print("当前时间为：", format_time)

'''
题目：格式化输出当前时间。
'''

import time

format = '%Y-%m-%d %H:%M:%S'
local = time.localtime(time.time())

print(time.strftime(format, local))