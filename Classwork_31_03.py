'''
1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

2.  В інтервалі від 1 до 10 визначити числа 
•  парні, які діляться на 2,
•  непарні, які діляться на 3, 
•  числа, які не діляться на 2 та 3.

3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)

4.  Напишіть скрипт, який перевіряє логін, який вводить користувач. 
Якщо логін вірний (First), то привітайте користувача. 
Якщо ні, то виведіть повідомлення про помилку. 
(використайте цикл while)
'''

'''
list_int=[]
n= int(input("The number of elements in list: "))

for x in range(n):
    elem=int(input("Input elements: "))
    list_int.append(elem)

print(list_int)

print(max(list_int))
print(min(list_int))
'''

'''
print("even:")
for value in range(1,10):
    if value%2==0:
        print(f"{value}")
print("odd:")
for value in range(1,10):
    if value%3==0:
       print(f"{value} ")
print("others:")
for value in range(1,10):
    if value%2!=0 and value%3!=0:
        print(f"{value} ")

'''

'''
fact= int(input("Enter factorial number: "))

fact1=1
for x in range(1,fact+1):
    fact1=fact1*x
   
print(f"The factorial of {fact} is",fact1)
'''
'''
login=" "

while login!='First':
    
    login= str(input("Enter your login: "))
    if login =="First" :
        print(f"Hello {login} o/")
        break
    print("Error.Incorrect login")

'''

'''
5.  Перший випадок. 
Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

6.  Другий випадок. 
На початку на вхід подається кількість елементів послідовності, а потім самі елементи. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

7.  Знайти прості числа від 10 до 30, а всі решта чисел представити у вигляді добутку чисел 
(наприклад 10 equals 2 * 5
                    11 is a prime number
                    12 equals 2 * 6
                    13 is a prime number
                    14 equals 2 * 7
                     ………………….)
8.  Відсортувати слова в реченні в порядку їх довжини (використати List Comprehensions)
'''

'''
num=1

while num>=1 :
    num=int(input("Enter a number: "))

print("You inputed a wrong number")
'''

'''
lst=[]

n=int(input("Enter the number of elements: "))

for x in range(n):
    elem=int(input("Enter a number: "))
    lst.append(elem)
    if lst[x]<=0 :
        print("You entered a wrong number")
        break
'''


'''
#недороблена~~~~~~~~~~~~~
y1=1

for x in range(11,30):
    print(f"{x} = ",end=" ")
    for y in range(2,30):
        if x%y==0:
            if (y1*y)==x:
                print(f"{y1}*{y}")
                break
            
            if y==30:
                print("is primary number")
            y1=y

           
           
        
    print("")
'''

'''
line=input("Enter your words: ")

line_splited=line.split()

line_splited.sort(key=len)

print(line_splited)
'''


    

    




