
numberOfCoins = input("Enter number of coins: ")

num = 1
sumN = 0

while True:
    sumN = int(num*(num+1)/2)
    if sumN == int(numberOfCoins):
        break
    elif sumN < int(numberOfCoins):
        num+= 1
    else:
        break

print(num)
print("**********************")
if (sumN- int(numberOfCoins)) == 0:
    print("complete")       
'''
while True:
    temp = int(numberOfCoins)-num
    print("int(numberOfCoins)-num is {}".format(temp))
    if int(numberOfCoins)-num >= num+1:
        sum1 = sum1 + num
        num = num + 1
        print("num is {}".format(num))
    else:
        sum1 = sum1 + int(numberOfCoins)-num
        break
print("Final num is {}".format(num))
print("Final sum is {}".format(sum1))
'''