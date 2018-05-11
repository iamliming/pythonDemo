from math import floor
print('hello world')

i = 1 + 2
print(i)
i = 9 - 7
print(i)
i = 2 * 8
print(i)
i = 9 / 3
print(i)
i = 9 / -7.0
print(i)
i = 9 / 7.0
print(i)
i = 2 ** 3
print(i)
a = b = c = i
print (a)
print (b)
print (b.imag)
print ('===')

a = -4j
print(a.real)
print(a.imag)
print abs(a)

word = 'Hello' + 'World'
print word
print word * 3

print word[1]
print word[0:2]
print word[2:11]
print word[:2]
print word[2:]

print word[-1]
print word[-10]

print('feibinaqishulie')
a, b = 0, 1

while b < 500:
    print a + b
    a, b = b, a + b

a = 0

x = int(raw_input("please input some int"))

if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'One'
else:
    print 'More'

a = a + 1

a = ['abc', 123]

for i in a:
    print i


print floor(32.9)