exit1=" "
while exit1 !='no' :
	homework1=input("Chose the homework number: ")


	if homework1 == '1' :

		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

		f= open("zen_of_python1.txt","r")

		count_better=0
		count_never=0
		count_is=0

		for x in f:
			
			zen_of_python = x.split()

			for y in zen_of_python:
				if y == 'better':
					count_better = count_better + 1
				if y == 'never':
					count_never = count_never + 1
				if y == 'is':
					count_is = count_is + 1



		print("The amount of word 'better' is: '",count_better)
		print("The amount of word 'never' is: '",count_never)
		print("The amount of word 'is' is: '",count_is)

		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

		f= open("zen_of_python1.txt","r")



		for z in range(20):
			zen_to_upper=f.readline()
			print(zen_to_upper.upper())

		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

		f= open("zen_of_python1.txt","r")

		for z in range(20):
			zen_to_upper=f.readline()
			print(zen_to_upper.replace('i','&'))

		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")


	if homework1 == '2' :

		number=int(input("The number with 4 digits: "))

		int(number)
		multipl_num=1

		print("Your number is: ",number)

		while number != 0:
			
			q=int(number)%10
			if q != 0 :
				multipl_num=int(q)*int(multipl_num)
			
			number=int(number)/10
			


		print("The resuklt of multiplication is: ",multipl_num)

	if homework1 == '3' :
		
		a=input("Input a: ")
		b=input("Input b: ")

		print("a=",a)
		print("b=",b)
		
		print("\n ~~~~~ \n")
		a,b=b,a

		print("a=",a)
		print("b=",b)



	exit1= input("Do you want to chose another homework? (yes/no):")
	if exit1=='no':
		break
	print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")