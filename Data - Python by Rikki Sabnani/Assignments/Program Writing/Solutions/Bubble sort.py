lst1 = [100,10,1,298,65,483,49876,2,80,9,9213]

#Solution 1, easier to understand:

'''for outer in range(len(lst1)):
    for num in range(len(lst1)-outer-1): #last elements are already in place so no need for extra processing
        temp = float('-inf')
        if lst1[num] > lst1[num+1]:
            temp = lst1[num]
            lst1[num] = lst1[num+1]
            lst1[num+1] = temp
        
print(lst1)'''
                 
                 
#Solution 2: If you are comfortable swapping the numbers in one line:

for outer in range(len(lst1)):
    for num in range(len(lst1)-outer-1):
        temp = float('-inf')
        if lst1[num] > lst1[num+1]:
            lst1[num], lst1[num+1] = lst1[num+1], lst1[num]


print(lst1)