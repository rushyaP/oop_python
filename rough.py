import numpy as np
r=3
c=3
arr =np.full((r,c),' ',dtype='str')
arr[0,0]='X'
arr[1,1]='X'
arr[2,2]='X'

print(arr.shape[1])
list_view = [[' ' for i in range(arr.shape[1])] for i in range(arr.shape[0])]
print("|".join(['f','k','p']))
print(list_view)

for row in list_view:
    print("|".join(row))
    print("-"*5)
what=[[arr[i,j] for j in range(3)] for i in range(3)]
for row in what:
    print("|".join(row))
    print("-"*5)




