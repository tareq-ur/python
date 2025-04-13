#set can data duplicate and serial wise. set is a un-ordered data type and it is can not address position.

value = {7,1,2,3,5,7,8,9,6,4,2,"c","a","b"}



value = list(value)

value.insert (0, 0)
print(value)