input_list = input("Enter a list: ").split()


def get_median(l):
    l.sort()
    if len(l) % 2 == 0:
        return (int(l[int(len(l)/2-1)]) + int(l[int(len(l)/2)]))/2
    else:
        return l[int((len(l)-1)/2)]


temp = []
for i in input_list:
    temp.append(i)
    median = get_median(temp)
    print(median)
