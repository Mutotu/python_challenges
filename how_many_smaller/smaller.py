# def smaller(arr):
#     result = []
#     for i in range(len(arr)):
#         count = counter(arr[i:], arr[i])
#         result.append(count)
#     return result
#
#
# def counter(arr,num):
#     count = 0
#     for i in arr:
#         if num > i: count += 1
#     return count


##################

def smaller(arr):
    result = []
    for i in range(len(arr)):
        count = sum(1 for j in range(i+1, len(arr)) if arr[j] < arr[i])
        result.append(count)
    return result



print(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
print(smaller([1, 2, 0]), [1, 1, 0])