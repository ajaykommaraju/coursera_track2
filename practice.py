def OrganizeList(myList):
    
    for item in myList:
        assert type(myList[item]) == str, "Word list must be a list of strings?"
    myList.sort()
    return myList
my_new_list = [6, 3, 8, "12", 42]
print(OrganizeList(my_new_list))