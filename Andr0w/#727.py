given_list = input("Give a list: ").split()

given_list.sort()

def calculate_median(input_list):
    if len(input_list) % 2 == 0:
        a= int(input_list[int(len(input_list)/2)])
        b=int(input_list[int(len(input_list)/2)-1])
        print((a+b)/2)
    elif len(input_list) % 2 == 1:
        a = int(input_list[int((len(input_list)-1)/2)])
        print(a)

temp=[]
for i in given_list:
    temp.append(i)
    calculate_median(temp)












