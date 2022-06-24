import numpy as np

# RESHAPE 

x=np.array([1,2,3,4])
print(x)

y=np.reshape(x,(2,2))
print(y)

x=np.arange(20) # First 20 whole numbers
print(x)

y=np.reshape(x,(4,5))
print(y)

y=np.arange(20).reshape(4,5)
print(y)

x[3]=20
print(x)

# Strings are immutable
# Lists and arrays are mutable in nature

# Lists and contain different data types
# Arrays can only contain same data type

# ACESSING AND CHANGING

x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)

x[1,-1]=20
print(x)

print(x[0,0])
print(x[0,1])
print(x[2,2])

x=np.array([1,2,3,4,5])

y=np.array([[1,2,3],[4,5,6],[7,8,9]])

# DELETE

x=np.delete(x,(0,4))
print(x)

w=np.delete(y,0,axis=0)  # To delete a row
print(w)
v=np.delete(y,[0,2],axis=1) # To delete a column
print(v)

# APPEND

x=np.array([1,2,3,4,5])

y=np.array([[1,2,3],[4,5,6]])

x=np.append(x,6)
x=np.append(x,[7,8])
print(x)

w=np.append(y,[[7,8,9],[10,11,12]],axis=0)
print(w)
v=np.append(y,[[9,10],[11,12]],axis=1)
print(v)

# INSERT

x=np.array([1,2,5,6,7])

y=np.array([[1,2,3],[7,8,9]])

x=np.insert(x,2,[3,4])
print(x)

y=np.insert(y,1,[4,5,6],axis=0)
y=np.insert(y,1,5,axis=0)
y=np.insert(y,3,[3,9,0,1],axis=1)
print(y)
