#Exercise 1

# def is_odd(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_odd(5))



#Exercise 2

# def isYearLeap(y):
#     if y % 4 == 0:
#         if y % 400 == 0:
#             return True
#         elif y % 100 == 0:
#             return False
#         else:
#             return True
#     else:
#         return False
#
# print(isYearLeap(2024))





#Exercise 3

# def print_triangular_tables(n):
#     a = 0
#     for i in range(1, n + 1):
#         a = a + i
#         print(i, a)
#
# print_triangular_tables(5)


#Exercise 4     #Missed this one, i will try it at home

# def is_prime(n):
#     if n < 2:
#         return False
#
#


#
#
# #Exercise 5

# def reverse(s):
#     result = ""
#     for ch in s:
#         result = ch + result
#     return result
#
# print(reverse("hello world"))
#
# def reverse_slice(s):
#     return s[::-1]
#
# print(reverse_slice("hello world"))
#

#Exercise 6

# def remove_all(sub, s):
#     return s.replace(sub, "")
#
# print(remove_all("an", "banana"))


#Exercise 7
# I will try this one at home too

# def substitute(message, key):
#     alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
#     result = ""
#
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index != -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "baçcedgfhğiıkjmlonpösrtşüuzyv"
#
# print(substitute("world", key))


# Exercise 8

def remove_dups(s):
    result = ""
    for ch in s:
        if ch not in result:
            result = result + ch
    return result

print(remove_dups("hello world"))