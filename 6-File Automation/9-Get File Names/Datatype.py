#1. Number Data type

#1.1 Integer - Whole Number
a=15
print("Data type of a is ",type(a))


#1.2 Float  - Decimal Number
b=3.5 
print("Data type of b is", type(b))

#1.3 Complex
c=3+4j
print("Data type of c is", type(c))

#Calculation on complex datat type
z1 = 1+3j
z2 = 2+4j
z3 = z1+z2
print(z3)
print("Data type of z3 is", type(z3))

#2. String - Text Data type
name="Satish"
name1='Rajesh'
print("Data type of name is", type(name))
print("Data type of name1 is", type(name1))

#3. Boolean(bool) - True or false
status=True
print("Data type of status is", type(status))

#Sequence Types - List, Tuple, Range

#4.1 List
subject1=['Maths', 'Science', 'English', 'Biology']
print("Data type of subject1 is", type(subject1))


#4.2 tuple
subject2=('Maths', 'Science', 'English', 'Biology',36)
print("Data type of subject2 is", type(subject2))

#4.3 - Range
r=range(1,21)
print(list(r))
print("Data type of r is", type(r))

#5. Dictionary (dict) - Key value Pair
my_data={'name':'satish','age':25}
print("Data type of my_data is", type(my_data))

#6. Set
marks={85,97,99,83,79,75}
print("Data type of marks is", type(marks))

#7. None
response=None

print("Data type of response is", type(response))

user_input=input("are you agree with this? :")

if user_input=="yes":
    response="Accepted"
else:
    response="Rejected"

print(response)
