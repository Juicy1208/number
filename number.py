import random
r = random.randint(1,100)
while True:
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了!')
	else :
		if num>r :
			print('答案更小')
		else :
			print('答案更大')