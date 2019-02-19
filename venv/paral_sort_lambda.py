list1 = (1, 3, 5)
list2 = (4, 2, 6)
print(dir(list1))

data = zip(list1, list2)
print(data.__class__)
print(list(data))
# # data.sort()
# list1, list2 = map(lambda t: list(t), zip(*data))
# # data.sort()
#
# print(list1)
# print(list2)


# a = [(1, 2), (4, 1), (9, 10), (13, -3)]
# a.sort(key=lambda x: x[1])
#
# print(a)
# # Output: [(13, -3), (4, 1), (1, 2), (9, 10)]
