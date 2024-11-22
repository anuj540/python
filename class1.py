# print("hello world")  
# print("hello how are you")
# print(123)
# print("a")


# print(1+1)
# print(20-3)
# print(20*8)
# print(20/2)



# a = 5
# a = 10
# b = 20

# print(a+b)
# print(a/b)
# print(a*b)


# a = "aman" 
# b = 10.2
# c = True
# print(type(a))
# print(type(b))
# print(type(c))




# a = 20
# b = 10
# print(a>=b)


# a = 10
# # a = a+2
# a = a*2
# print(a)


# logical operator

# print(4>2 and 5>4)

# print(10>8 and 44>34 and 23>60)
# print(34>60 or 23>200 or 34>120)
# print(not 12>30)
# print(12>22 or 2>1)



# a = 42
# b = 10
# c = 99
# print(a>b, b>c)



# print( 11==11)
# print(1<=12)


# a=88
# b=00
# print(a+b)


# a= "Anuj"

# b= "Rohilla"
# print(a  +"      "+ b)


# only if
# if-else
# elif
# nested if-else


# if 3>2:
#    print("hello")
#    print("kullu")

# print("world") 

# age = int(input("enter your age"))
# if age>18:
#     print("u r eligible for voting")
# else:
#     print("you are under age")    


# if 10>8:
#     print("hello")
# if 56>80:
#     print("world") 
# else:
#     print("byee")    
# 
#    



# if 10>20:
#     print("hello")
# elif 30>20:
#     print("world")
# elif 22>12:
#     print("kullu")
# else:
#     print("byee")            


# password = int(input("enter your password"))

# if password>5:
#     print("login successfully")
# else:
#     print("your password is less than 5 digit")    

# number = int(input("enter any number"))

# if number%2==0:
#     print("your numer is even")
# else:
#     print("your number is odd")  


# name = "anujj"
# if name=="anuj":
#     print("successfully login")
# else:
#     print("you cant login")    

# age = 4

# if age>10:
#     if age>17:
#         print("you can vote")
#     else:
#         print("you cant vote")  
# else:
#     print("you are baby")     
# 
#      



# age = 1

# if age>10:
#     if age>17:
#         print("you can vote")
#     else:
#         print("you cant vote")  
# else:
#     if age>2:
#         print("you can go outside")
#     else:
#         print("you can take milk")     




# if 34>200:
#     print("hello")
# elif 23>6:
#     print("world")
# elif 12>8:
#     print("kullu")
# else:
#     print("bye")            


# Number = 18
# if Number>18:
#    print("your eligible for license")
# else:
#    print("your not eligible for license")   


# if 12>1:
#     print("hello")
# elif 44>14:
#     print("world")   
# else:
#     print("good byy")    



# password= 6

# if password>5:
#     if  password > "@":
#        print("succesful login")
#     else:
#         print("please enter special chr")    
# else:        
#    print("your password less than 5")




password = (input("enter your password")) # Change this to a string

if any(char.isupper() for char in password): 
 if len(password) > 5:

    if any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/~" for char in password):
        print("you are login sucessfull ")
    else:
        print("please enter a special character")
 else:
    print("your password is less than 5 characters")
else:
   print("please first letter is Upper case")    
