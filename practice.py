# Day 01
# # variable operators

# a = 5
# c = 4
# print(a*c)

# # arithmatic operators
 
# print (a + c)
# print (a - c)
# print (a / c)
# print (a // c)
# print (a * c)
# print (a ** c)
# print (a % c)

#   #comparison operators

# b = 50
# d = 40
# if b == d:
#      print ("False")
# elif b >= d:
#     print("True") 

# # logical operators
 

# print ((a>=c) and (b>d)) #and condition
# print ((a<b) or (c>d))   # or condition
# x = False
# print (not x) #not condition

# # membershiop operators]

# print ('teacher' in "i am a teacher") 
# print ('student' in "i am a teacher") 
# print ('student' not in "i am a teacher") 
# print ('teacher' not in "i am a teacher") 


# #user input
# # type costing
# Name = int (input('Enter your number:'))
# print(Name + 5)

# #another costing
# id_1 = 20
# id_2 = '25'
# print (str(id_1) + id_2)


#Day 2
 #variables
Day_01 = 22
Day_02 = 32
print(Day_01 + Day_02)

#arithmatic 
day_3 = 12
day_4 = 6
print(day_3 + day_4)
print(day_3 - day_4)
print(day_3 / day_4)
print(day_3 // day_4)
print(day_3 * day_4)
print(day_3 ** day_4)

 # cpmparison 


price = int(input( 'Enter your price: '))
Budget= 50
if price <= Budget:
    print("buy ")
else:
    print("Don't buy")


#logical 
senior = 100
junior = 50
middel_age = 500
old_man = 10000
print((senior > junior)  and (middel_age < old_man))
print((senior == junior)  or  (middel_age < old_man))
old_man_1 = "True"
print(not old_man_1)


#membership

print('tareq' in "sakil rahman tareq")
print('tareq' not in "sakil rahman tareq")

# user input 

Bill = int (input("Enter your bill: "))
print (Bill + 10%( Bill) )