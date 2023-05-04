print("Exercise 1")
a1 = input('Write a word:')
n=0
for i in a1:
     if i=="a":
        n+=1
print("а=",n)

print(" ")
print("Exercise 2")
b = input('Write a word:')
a=0
o=0
l=0
y=0
e=0
u=0
for i in b:
    if i=='a':
        a+=1
    elif i=='o':
        o+=1
    elif i=='i':
        l+=1
    elif i=='y':
        y+=1
    elif i=='e':
        e+=1
    elif i=='u':
        u+=1
key = a+o+u+l+e+y
print("Number of vowels:", key, "Here is: a =",a, 'o=',o, 'i=',l, 'y =',y, 'e =',e, 'u =',u)

print('')
print('Exercise 3')
c = input('Write a phrase:')
z = 0
x = 0
v = 0
m = o
g = 0
h = 0
for i in c:
    if i == 'a':
        z += 1
    elif i == 'o':
        x += 1
    elif i == 'i':
        v += 1
    elif i == 'y':
        m += 1
    elif i == 'e':
        g += 1
    elif i == 'u':
        h += 1
    lock = len(c) - (x + z + v + m + g + h)
print('Number of consonants:', lock)

print(' ')
print('Exercise 4')
phrase1 = input('Give me a phrase:')
phrase2 = phrase1[::-1]
print(phrase2)

print(' ')
print('Exercise 5')
number = int(input('Give me a positive number'))
p=0
for i in range(number):
    if number-p>0:
        p = p+1
        t = str(number-number+p)
        print(p*t)
