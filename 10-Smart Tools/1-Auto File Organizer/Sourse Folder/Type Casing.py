# Explicit Type Casting

#1. String to Integer
x="10"
print("type of x is :",type(x))
z=x+x
print(z)

y=int(x)                            #type cast to integer
print(y+y)
print("type of y is :",type(y))

#2. Integer to Float
a=5
print("type of a is :",type(a))
b=float(a)
print(b)
print("type of b is :",type(b))

#3. Float to Integer
f=3.9
print("type of f is :",type(f))
i=int(f)
print("type of i is :",type(i))

# Implicit type Casting
z1=4.6   #Float
z2=5     #int

z3=z1+z2
print("Output of Z3:",z3)
print("type of z3 is :",type(z3))

#4. integer to string
num=100
text=str(num)

print("My score is " +text)

#Real life use case:

age=int(input("Enter your age: "))     #Asking input from user
#age=int(age)
print(age+5)