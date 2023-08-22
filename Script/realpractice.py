
program = {1: 6}
print()



# prgram 19
# kgintonne = 0.001
# kginpound = 2.20462
#
# def kgtotonne(number ):
#     global kgintonne
#     return kgintonne * number
# def tonnetokg(number ):
#     global kgintonne
#     return number / kgintonne
# def kgtopound(number ):
#     global kginpound
#     return number * kginpound
# def poundtokg(number ):
#     global kginpound
#     return number / kginpound


# program 18
# mileinkm = 1.609344
# feetininches = 12.
# def miletokm( number ):
#     global mileinkm
#     return mileinkm * number
# def kmtomile(number):
#     global mileinkm
#     return number / mileinkm
# def feettoinches(number):
#     global feetininches
#     return number *  feetininches
# def inchestofeet(number):
#     global feetininches
#     return number /  feetininches

# program 17
# def remove_letter(sentence, letter):
#     empty = ""
#     for each in sentence:
#         if each == letter:
#             continue
#         else:
#             empty+= each
#     return empty
#
# sentence = str(input("Enter a sentence: "))
# letter = str(input(" Enter a letter : "))
# print( remove_letter(sentence, letter))

# program 16
# binary search
#
# Adm = [1, 2, 3, 4, 5, 6, 7, 8]
# n = len(Adm) - 1
#
#
# def binarysearch(searched, high=n, low=0, mid=n // 2):
#     global Adm
#     if searched > Adm[mid]:
#         low = mid
#         mid = (high + low) // 2
#         return binarysearch(searched, high, low, mid)
#     elif searched < Adm[mid]:
#         high = mid
#         mid = (high + low) // 2
#         return binarysearch(searched, high, low, mid)
#     else:
#         return (mid + 1)
#
#
# print(binarysearch(3))


# program 15
# def sum_sq_digits(x):
#     s = 0
#     for each in str(x):
#         s += int(each) ** 2
#     return s
#
#
# _list = []
#
#
# def ishappy(m):
#     global _list
#     n = sum_sq_digits(m)
#     if m == 1:
#         return True
#     elif sum_sq_digits(m) in _list:
#         return False
#     else:
#         _list += [n]
#         return ishappy(n)
#
#
# print(ishappy(68))


# program 14

# def hailstone(n):
#     print(n)
#     if n == 1:
#         return 1
#     elif n %2 == 0:
#         return hailstone(n//2)
#     else:
#         return hailstone(3*n+1)
# hailstone(7)

# program 13

# def gcd(m,n, i = 1):
#     if i > m :
#         return 1
#     elif (m% i == 0) and (n % i == 0):
#         return i* gcd(m , n, i+i)
# print(gcd(2,6))


# program 12

# def product(m,n):
#     if n == 0:
#         return 0
#     else:
#         return m + product(m,n-1)
# print(product(3,3))


# program 11
# def prime(n, i=2):
#     if n == 1:
#         return False
#
#     if n % i == 0 and i != n:
#         return False
#     if i > int(n ** 0.5) :
#         return True
#
#
#     else:
#         return prime(n, i + 1)
#
# print(prime(1))
# print(prime(2))
# print(prime(3))
# print(prime(4))
# print(prime(5))


# 1
# 0,1 = 1, 1,1 = 2
# 1,1 = 2 , 1,2 = 3 , 2,3 = 5, 3,5 = 8
# 1 , 1 , 2 , 3 , 5 , 8, 13 , 22, 35 , 57 , 82

# def func(a, b):
#     if b == -1:
#         return ""
#     else:
#         return a[b] + func(a, b - 1)
# hello = func("hello",len("hello")-1)
# print(hello)

# def func1(string):
#     if len(string) == 0:
#         return string
#     else:
#         return func1(string[1:]) + string[0]
#
#
# a = "hello"
# print(func1(a))
#
