#while loop
count = 0
while(count < 3):
    count += 1
    print("Hello Geek")
    # Single statement while block
#count = 0
#while(count==0): print("Hello Geek")
#It is an infinite loop because the condition is always true.
#for in loop
print('List Iterations')
l = ["geeks", "for", "geeks"] #square braces for list
# it can be resized and elements can be changed dynamically
for i in l:
    print(i)
    print('\nTuple Iterations')
t = ("geeks", "for", "geeks") #round braces for tuple
# its size is fixed and elements cannot be changed 
for i in t:
    print(i)
    print('\nString Iterations')
s = "Geeks"
for i in s:
    print(i)
    list = ["geeks", "for", "geeks"]
#range(start, stop, step) OR (start, stop) OR (stop) 
for index in range(len(list)):
    print(list[index])
for letter in "geeksforgeeks":
    if letter == 'e' or letter == 's':
         continue
    print('Current Letter:', letter)
for letter in "geeksforgeeks":
    if letter == 'e' or letter == 's':
         break
    print('Current Letter:', letter)
def my_function():
    print("Hello from function")

my_function()
def my_function(f_name):
    print(f_name + "Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
def my_function(country = "Norway"): #default parameter value is Norway
# if u cant pass a parameter, it will take the default value
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"] 
my_function(fruits) #fruits works as food in function
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
def my_function(child3, child2, child1): 
    print("The youngest child is " + child3)
# it cant confuse bcz we chose the name(keyword argument) of the parameter
# it simply assign child3 value to the parameter child3 first...
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
class MyClass:
    x = 5
p1 = MyClass() 
print(p1.x)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()