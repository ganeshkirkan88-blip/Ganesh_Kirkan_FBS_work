#syntax:- ()
tu = (10,)   # use comma for single value
tu = (10,20,30,'a', 3.14,10)

#Heterogeneous.

#Ordered.

#Immutable.
#ex :- 
#tu[0] = 50       # raise  error, value is not replaced.

#Duplication elements are allowed.
print(type(tu))
print(tu)

#Tuple is faster than list.
#example:-
'''import sys
li=[]
tu=()
print(tu)
print(type(tu))
print(sys.getsizeof(li))
print(sys.getsizeof(tu))'''