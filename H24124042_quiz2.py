amount=int(input("Enter the shopping amount:"))#enter shopping amount
level=str(input("Enter the membership level(regular or gold):"))#enter membership level
if level=="gold":#whether the membership is gold
	if amount>=3000:#check the amount and gives different level of discount
		print(amount*0.75)
	elif 3000>amount>=2000:
		print(amount*0.8)
	elif 2000>amount>=1000:
		print(amount*0.85)
	else:
		print(amount)
elif level=="regular":#whether the membership is regular
	if amount>=3000:#check the amount and gives different level of discount
		print(amount*0.8)
	elif 3000>amount>=2000:
		print(amount*0.85)
	elif 2000>amount>=1000:
		print(amount*0.9)
	else:
		print(amount)
else:
	print("Invalid member level Please enter gold or regular")#output the outcome if the input content is neither Regular nor Gold