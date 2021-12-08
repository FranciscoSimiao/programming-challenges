def calculate_median(input_list):
    input_list.sort()
    if len(input_list) % 2 != 0:
        b = len(input_list)
        middle = int((b - 1) / 2)
        return input_list[middle]
    elif len(input_list) % 2 == 0:
        middle1 = int((len(input_list) / 2))
        middle2 = int((len(input_list) / 2) - 1)
        return int((input_list[middle1] + input_list[middle2])) / 2


given_list = input("give numbers: ").split()
print(given_list, " is your list.")
integer_map = map(int, given_list)
integer_list = list(integer_map)

for x in range(0, len(integer_list)):
    temp_list = integer_list[0:x+1]
    print(calculate_median(temp_list))
