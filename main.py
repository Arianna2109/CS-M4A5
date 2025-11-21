#1 part
import math
radius = (int(input("what is the radius?")))

area = (str(math.pi * (radius**2)))
print("your area is:"+str(area)) 

#2nd part
a=(int(input("What is the a value?")))
b=(int(input("What is the b value")))

answer = (str((a-b)+(a*b)))
print("Your answer is: "+str(answer))

#3rd part
choice = input ("Which picture would you like to see? (1 or 2): ")

ascii1 = r"""
 /\ _ /\
( 0 . 0 ) 
  > ^ <
"""

ascii2 = r"""
 ( \_/ )
(=' .'=)
("")_("")
"""

if choice == "1":
    print(ascii1)
elif choice == "2":
    print(ascii2)

else:
    print("Invalid choice. Please enter 1 or 2")