#Exercise 1
# myList = [76, 92.3, "hello", True, 4, 76]
#
# print(myList)
# myList.append("apple")
# myList.append(76)
# myList.insert(0, 99)
# print(myList)
#
# print(myList.index("hello"))
#
# print(myList.count(76))
# myList.remove(76)
# print(myList)
#
# myList.pop(myList.index(True))
#


#Exercise 2



# def sum_of_squares(xs):
#     sum = 0
#     for i in xs:
#         sum = sum + i**2
#     return sum
#
# List = [2, 3, 4]
#
# print(sum_of_squares(List))



#Exercise 3

# List = [1,5,8,3,7,4,8,54,23,73]
#
# def sum_evens(ls):
#     sum = 0
#     for i in ls:
#         if i % 2 == 0:
#             sum += i
#     return sum
#
# print(sum_evens(List)



#Exercise 4


# def numberOfFiveLengths(s):
#     num = 0
#     for i in s:
#         if len(i) == 5:
#             num += 1
#     return num
# words = ["apple", "coyote", "hello", "phone", "clone", "allih"]
#
# print(numberOfFiveLengths(words))
#
#
#
# Exercise 5



# def exceptFirstEven(ls):
#     sum = 0
#     for i in ls:
#         if i % 2 == 0:
#             break
#         else:
#             sum += i
#     return sum
#
# List = [1, 3, 5, 7, 8, 9, 10]
#
# print(exceptFirstEven(List))



#Exercise 6

# def until_samn(ls):
#     a = 0
#     for i in ls:
#         if i == "Sam":
#             a += 1
#             return a
#             break
#         else:
#             a += 1
#
# List = ["Dottore", "Alucard", "Angel", "Sam", "Alex"]
#
# print(until_samn(List))


#Exercise 7

# def replace(s, old, new):
#     pieces = s.split(old)
#     print(pieces)
#     print(new.join(pieces))
#     return new.join(pieces)
#
# def test(actual, expected):
#     if actual == expected:
#         print("PASSED")
#     else:
#         print("FAILED")
#
# test(replace("Mississippi", "i", "I"), "MIssIssIppI")
#
#
#


#Exercise 8

# def max(ls):
#     max_val = ls[0]
#     for num in ls:
#         if num > max_val:
#             max_val = num
#     return max_val
#
#
#
# list = [5,7,45,6,345,76,34]
#
# print(max(list))
#
#
#
