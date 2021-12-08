import string
global lists, lists_r

lists = []
lists_r = []
temp_list = []

def convertion(comp_input):
    lists = []
    scales_max = 10**(100)
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"
        ]
    
    tens = [
        "twenty", "thirty", "fourty", "fifty", "sixty", "seventy",
        "eighty", "ninety"
            ]
    
    scales = [
        "hundred", "thousand", "million", "billion", "trillion"
        ]

        
    current = result = 0
    
    try:
        for word in comp_input.replace("-"," ").split():    
            if "for" in word:
                word = word.replace("for","four")
            lists.append(word)


        for value in range(len(lists)):
            for i in range(len(units)):
                if lists[value] == units[i]:
                    lists[value] = i

            for i in range(len(tens)):
                if lists[value] == tens[i]:
                    lists[value] = i * 10 + 20

            for i in range(len(scales)):
                if lists[value] == scales[i]:
                    lists[value] = 10**(i+2)
                    if lists[value] >= scales_max:
                        raise Exception("Unorganized, please re-enter the value")
                    else:
                        scales_max = lists[value]


        for i in range(1,len(lists)):
            if lists[i] % 100 == 0:
                x = lists[i-1] * lists[i]
                lists[i-1] = 0
                lists[i] = x
            
                
        lists_r.append(sum(lists))


    except TypeError:
        raise Exception("Illegal words: " + word)


################################################################################

try:
    user_input = input("Enter\n")
    for word in user_input.replace(","," ").split():
        if word in string.digits:
            lists_r.append(int(word))
        else:
            convertion(word)

except:
    print("Error")

finally:
    for i in range(len(lists_r)):
        lists = []
        temp_list.append(int(lists_r[i]))
        temp_list.sort(key = int)
        if len(temp_list) % 2 == 0:
            for i in range(0,2):
                lists.append(temp_list[int(((len(temp_list)/2) + i)-1)])
            print(sum(lists)/2)
        else:
            print(temp_list[int(((len(temp_list) + 1)/ 2)-1)])
    
# User input --> 2, 1, 5, 7, 2, 0, 5
