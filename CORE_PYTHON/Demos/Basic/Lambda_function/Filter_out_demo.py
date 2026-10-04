#filter_out : 1) it is used to filter/select elements from a sequence based on a condition.
#             2) consider true/false
#             3) falsy : 0 , None , false , '' , [].
#Ex: 
'''data =[1,2,3,4,5,6,7,8,9,10]
res = tuple(filter(lambda num:num%2==0,data))
print(res)
'''
#Ex:
data =[1,2,3,4,5,6,7,8,9,10]
res = tuple(filter(lambda num:num*num,data))
print(res)