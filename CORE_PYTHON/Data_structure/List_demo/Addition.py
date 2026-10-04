#
'''li =[10,20,30,40,50,60,70]
sum=0

#Method 1:  iterating value.
for ele in li:
    sum += ele
print(sum)


#Method 2: using indexing.

for ind in range (0,len(li)):
  sum += li[ind]
print(sum)
'''

# WAP to find out the maximum element in the list?

li = [40,50,30,60,20,10]
max = li[0]
for ind in range (1,len(li)):
    if(li[ind] > max):
        max = li[ind]
print('maximum number',max)