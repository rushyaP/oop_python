
#print ('_|_|_')
##print ('_|_|_')
#print (' | | ')

import numpy as np

emp_array=np.empty((3,3),dtype='str')
print(emp_array)
print('updated array')
emp_array[1,0]='X'
emp_array[1,1]='X'
emp_array[1,2]='X'
print(emp_array)

#Across Match check
for i in range(0,3):#row
    print(i)
    c=0
    for j in range(0,3):#column
        if j!=2:
            print(i,j)
            if emp_array[i,j] ==emp_array[i,j+1]:
                c+=1
    if c==2:
        print(c)
        break
        
print('Matched')

"""
# Below Match check
for i in range(0,1):#column
    d=0
    for j in range(0,3):#row
        if j!=2:
            if emp_array[j,i] ==emp_array[j+1,i]:
                d+=1
print(d)
"""



        







