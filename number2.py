import random
r = random.randint(1,100)
count = 0
while True:
	count = count+1 #簡寫: count += 1
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了!')
		break
	else :
		if num>r :
			print('答案更小')
		else :
			print('答案更大')
	print('這是你猜的第',count,'次') 