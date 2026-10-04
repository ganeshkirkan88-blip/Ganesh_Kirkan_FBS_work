#
'''data = [1,2,3,4,5,6,7,8,9,10]

res = list(filter(lambda num : num%2==0,data))   # consider 1-F,2-T,3-F,4-T,5-F,6-T,......10-T.
print(res)'''

#
data = [1,2,3,4,5,6,7,8,9,10]

res = tuple(filter(lambda num: num*num ,data))
print(res)