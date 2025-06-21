def create_new_list(given_list):
    new_list=set()
    temp=[]
    for item in given_list:
        if item in temp:
            if item not in new_list:
                new_list.add(item)
            
            else:
                temp.append(item)
    return new_list

given_list=[1,5,6,5,1,2,3]
new_list=create_new_list(given_list)
print(new_list)