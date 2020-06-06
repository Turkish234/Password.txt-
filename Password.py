password = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i"] #you can also add alphabets to Z and symbols like @,#.

for i in password :

	for j in password:
		
		for k in password:

			for l in password:
				
				for m in password:
					
					for n in password:
						
						q = i + j + k + l +m + n
						f =open("password-0.txt","a")
						f.write(q+'\n')
						f.close()											
