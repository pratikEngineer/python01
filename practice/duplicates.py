
#
# def remove_duplicates(arr):
#
#     seen=set()
#     result= []
#
#     for num in arr:
#         if num not in seen:
#             seen.add(num)
#             result.append(num)
#
#     return result
#
# arr=[1,2,3,5,2,5,6,3,7]
# a = remove_duplicates(arr)
# print(a)



def remove_duplicates(arr):
    return list(dict.fromkeys(arr))
arr=[1,2,3,5,2,5,6,3,7]
a = remove_duplicates(arr)
print(a)