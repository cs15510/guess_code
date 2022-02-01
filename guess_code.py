password = "a123456"
count = 0
while count < 3:
	guess_code = input("請輸入密碼:")
	if guess_code == password:
		print("登入成功")
		break
	else:
		print("密碼錯誤, 還有" + str(2-count) + "次機會")
		count+=1