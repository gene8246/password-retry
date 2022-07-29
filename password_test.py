# password = 'a123456'
i = 1
i = int(i)
while i <= 3:
	password = input('please enter password')
	if password == 'a123456':
		print('access successfully')
		break
	else:
		print('wrong password you still have', 3 - i, 'chance')
		i = i + 1
