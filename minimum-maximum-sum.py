# This function print maximum sum and minimuum sum of array
# for example arr = [1, 2, 3, 4, 5]
# minimum_sum = (1 + 2+ 3+ 4) = 10
# maximum_sum = (2 + 3 + 4 + 5) = 14

def miniMaxSum(arr):
    # Write your code here
    sum = 0
    min = arr[0]
    max = arr[0]
    for x in arr:
        sum += x
        if min > x:
            min = x
        if max < x:
            max = x
    
    print(sum - max, sum - min)
