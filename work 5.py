#1)
q = str(input('enter the text: '))
w=0
if q[0]=='е':
    w+=1
for i in range(len(q)-1):
    if q[i] == ' ':
        if q[i+1]=='е':
            w+=1
    i+=1
print("words that starts with 'e': " + str(w))

#2)
q = str(input('enter the text: '))
w = 0
for i in q:
    if i == ':':
        a = a.replace(':', '%')
        w += 1
print(q)
print(w)

#3)
q = str(input('enter the text: '))
w = 0
for i in q:
    if i == '.':
        q = q.replace('.', ' ')
        w += 1
print(q)
print(w)

#4)

q = str(input('enter the text: '))
w = 0
for i in q:
    if i == 'a':
        q = q.replace('a', 'o')
        w += 1
print(w)

#5)

q = str(input('enter the text: '))
print(q.upper())

#6)
q = str(input('enter the text: '))
w = 0
for i in q:
    if i == 'a':
        q.replace('q', ' ')
    w += 1
print(w)

#8)
q = str(input('enter the text: '))
w = 1
for i in q:
    if i == ' ':
        newq = q.split(' ')
        w += 1
print(w)

#9)
word = str(input('enter word that will be counted: '))
q = str(input('enter the text: '))
w = q.count(word)
print(w)

#10)
q = str(input("Enter the text: "))
w = q.split(" ")
e = 0
r = list(q)
for i in range(len(r)):
    if r[i] == " ":
        if r[i-1] == "I":
            print(w[e])
            e+= 1
if r[len(r)-1] == "I":
    print(w[len(w)-1])

#14)

q = str(input('enter the text: '))
for i in q.split():
    if i.count('q') == True:
        if i.endswith('i') == True:
            print(i)

#15)
q = str(input('enter the text: '))
w = 0
for i in q:
    if i == 't':
        w += 1
print(w)

