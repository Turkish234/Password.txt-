password = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

for i in password :

	for j in password:
		
		for k in password:

			for l in password:
				q = i + j + k + l
				f =open("password-0.txt","a")
				f.write(q+'\n')
				f.close()								