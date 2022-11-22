from numpy import median
import statistics

arr = [2,1,5,7,2,0,5]

# finding median using numpy module this reduces the amount of code that is needed to be writen and is much faster on larger arrays
def find_median_with_numpy(arr):
    for i in range(len(arr)):
        n_arr = arr[0:i+1]
        n_arr.sort()
        mid = median(n_arr)
        if mid == int(mid):
            print(int(mid))
        else:
            print(mid)

# provides same benefits as numpy but is slightly slower although it only uses built in modules so no need to download 
def find_median_with_statistics(arr):
    for i in range(len(arr)):
        n_arr = arr[0:i+1]
        n_arr.sort()
        mid = statistics.median(n_arr)
        if mid == int(mid):
            print(int(mid))
        else:
            print(mid)

# shows how you can find median without the use of any modules/packages
def find_median_without_modules(arr):
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
        

find_median_with_numpy(arr)
print('-------------------------------------')
find_median_with_statistics(arr)
print('-------------------------------------')
find_median_without_modules(arr)
