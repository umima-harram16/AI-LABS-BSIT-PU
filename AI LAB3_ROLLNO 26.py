import random

# Temperature Converter
def conv_temp(val, u):
    res = 0
    if u == 'c':
        res = (val * 9 / 5) + 32
        print(str(res) + 'F')
    elif u == 'f':
        res = (val - 32) * 5 / 9
        print(str(res) + 'C')

conv_temp(60, 'c')
conv_temp(45, 'f')

# Find numbers divisible by both 5 and 7
for n in range(1500, 2701):
    if n % 7 == 0 and n % 5 == 0:
        print(n)

# Number Guessing Game
num = random.randint(1, 9)
while True:
    g = int(input("Guess a number between 1 and 9: "))
    if g == num:
        print("Well guessed!")
        break
    else:
        print("Wrong!")

# Pattern printing
n = 5
s = 1
maxed = False
for r in range(0, 2 * n):
    for _ in range(0, s):
        print("*", end="")
    print("")
    if s < n and not maxed:
        s += 1
    elif s == n and not maxed:
        maxed = True
        s -= 1
    else:
        s -= 1

# Reverse string (slice method)
w = input("Enter a word: ")
print(w[::-1])

# Reverse string (loop method)
w = input("Enter a word: ")
rev = ""
for i in range(1, len(w) + 1):
    rev += w[-i]
print(rev)

# Count even and odd
lst = [1, 3, 12, 14, 35, 24]
even = 0
odd = 0
for x in lst:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)

# Show type of each item
data = [123, 1.24, 1+2j, True, "Hi", (2, 5), [2, 5], {"a": 1, "b": 2}]
for x in data:
    print(x, type(x))

# Skip certain numbers
for x in range(7):
    if x == 3 or x == 6:
        continue
    print(x, end=" ")

# Fibonacci until >50
a = 0
b = 1
while True:
    print(a)
    a, b = b, a + b
    if b > 50:
        break

#10
def gen_arr(m, n):
    result = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(i * j)
        result.append(row)
    return result

# Example
rows = 3
cols = 4
print(gen_arr(rows, cols))

#11 
lines = []
while True:
    line = input("Enter a line (blank to stop): ")
    if not line:
        break
    lines.append(line.lower())

for l in lines:
    print(l)


#12
data = input("Enter binary numbers separated by commas: ")
binaries = data.split(',')

for b in binaries:
    decimal = int(b, 2)
    if decimal % 5 == 0:
        print(b)


#13

text = input("Enter a string: ")

letters = 0
digits = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)
#14 password validation 

def validate_password(password):
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    special_chars = "$#@"

    if len(password) < 6 or len(password) > 16:
        return False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    return has_lower and has_upper and has_digit and has_special

password = input("Enter password: ")
if validate_password(password):
    print("Valid password")
else:
    print("Invalid password")