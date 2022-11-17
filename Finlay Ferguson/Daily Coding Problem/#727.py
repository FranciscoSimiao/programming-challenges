arr = [2,1,5,7,2,0,5]

def find_median(arr):
    for i in range(len(arr)):
        n_arr = arr[0:i+1]
        n_arr.sort()
        num = (len(n_arr) - 1) / 2
        if int(num) == num:
            print(n_arr[int(num)])
        else:
            mid = (n_arr[int(num)]+n_arr[int(num)+1])/2
            if mid == int(mid):
                print(int((n_arr[int(num)]+n_arr[int(num)+1])/2))
            else:
                print((n_arr[int(num)]+n_arr[int(num)+1])/2)
        

find_median(arr)
