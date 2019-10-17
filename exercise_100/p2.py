# str = input("Enter the Profit: "); 
# I = int(str)
# if I < 0:
#         print("Please re-enter the correct profit! ")
# elif (I >= 0) and (I <= 100000):
#         bonus = I*0.1
# elif (I >= 100000) and (I <= 200000):
#         bonus = 100000*0.1 + (I - 100000)*0.075
# elif (I >= 100000) and (I <= 200000):

'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%；
高于100万元时，超过100万元的部分按1%提成；
从键盘输入当月利润I，求应发放奖金总数？
'''

arr = (0, 10, 20, 40, 60, 100)
rat = (0, 10, 7.5, 5, 3, 1.5, 1)

pro = float(input('净利润（万元）：'))
fit = 0

for i in range(1, len(arr)):
    if (pro > arr[i]):
        fit += (arr[i] - arr[i - 1]) * (rat[i] / 100)
    else:
        fit += (pro - arr[i - 1]) * (rat[i] / 100)
        break

print('奖金（元）：', fit * 10000)