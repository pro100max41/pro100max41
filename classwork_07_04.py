
import calc



a=int(input("Enter first number: "))

b=int(input("Enter second number: "))

c=str(input("What are we going to do today?: "))


if c=="addition":
    print(calc.plus(a,b))


if c=="subtraction":
    print(calc.minus(a,b))


if c=="multiolication":
    print(calc.mult(a,b))

