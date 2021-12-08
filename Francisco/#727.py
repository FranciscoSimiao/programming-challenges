import statistics
list = [2, 1, 5, 7, 2, 0, 5]
for i in range(len(list)):
    a = i+1
    list1 = (list[:a])
    s = statistics.median(list1)
    print(s)