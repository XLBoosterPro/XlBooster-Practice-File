# 1.What is List

# 2. Create List
fruits =["apple", "banana", "cherry"]
print(fruits)

# Mix List
employee =["Ajay", 25, True, 55000]
print(employee)

#Empty List
my_list=[]
my_list=list()

# From values
numbers=[10,20,30,40,50,60]

# From a string 
chars = list("Satish")
print(chars)

# From Range
nums=list(range(1,6))
print(nums)

# 3. List Indexing

name ="Satish Dhawale"
letters=list(name)
print(letters)


# Item	S	a	t	i	s	h		D	h	a	w	a	l	e
# +Idx	0	1	2	3	4	5	6	7	8	9	10	11	12	13
# -Idx	-14	-13	-12	-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1

fruits1 = ["apple", "banana", "cherry"]

print(fruits1[-3])

# 4.List Slicing
# Syntax : list[start:stop:step]
nums=[10,20,30,40,50,60,70]

# nums[0,1,2,3,4,5]

print(nums[1:5])    # start and end Position
print(nums[:3])     # End Position
print(nums[2:])     # Starting Position positive index
print(nums[-3:])    #Starting poistion negative index
print(nums[::3])    # step
print(nums[::-1])  # Reverse List






