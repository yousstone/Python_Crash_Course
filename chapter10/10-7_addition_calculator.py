#!/usr/bin/python3
# coding=utf8
'''
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.
'''
print('If you want to quit,just type "q" ')
while True:
    try:
        a = input('Give me a number for a (type q to quit ):')
        if a == 'q':
            break
        else:
            a = int(a)

        b = input('Give me b number for a (type q to quit ):')
        if b == 'q':
            break
        else:
            b = int(b)
    except ValueError:
        print('Sorry, i need  a number not a string. ')

    else:
        sum = a + b
        print('a + b = %s'%str(sum))