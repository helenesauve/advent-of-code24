with open('input.txt', 'r') as my_file:
    data_into_list = my_file.read().splitlines()

list1=[]
list2=[]

for element in data_into_list:
    split_line = element.split()
    list1.append(int(split_line[0]))
    list2.append(int(split_line[1]))

list1.sort()
list2.sort()

count=0
for i, j in zip(list1, list2):
    if i>j:
        difference=i-j
        count+=difference
    else: 
        difference=j-i
        count+=difference



    

        




