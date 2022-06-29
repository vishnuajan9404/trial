#task 3
#vishnu R

# Type 1 , program works as per example


while True:
        try:
                total_rupees=int(input("Enter total number of rupees="))
                x=int(input("Enter the value of X="))
                y=int(input("enter the value of Y="))
                z=int(input("Enter the value of Z="))
                eq=int((total_rupees*100)/(x*100+y*50+z*25))
                p=eq*2
                q=eq*4
                print(" Number of 1 rupees coins=",eq)
                print("Number of 50 paisa coins=",p)
                print("Number of 25 paisa coins=",q)
        except:
                print('Error,input real numbers only')


# Type 2, Program works as per question.

while True:
        try:
                total_rupees=int(input("Enter total number of rupees="))
                x=int(input("Enter the value of X="))
                y=int(input("enter the value of Y="))
                z=int(input("Enter the value of Z="))
                p=x+y+z
                q=round(total_rupees/p)
                print("number of 1 rupees coins=",(q*x))
                print("number of 50 paisa coins=",(q*y))
                print("number of 25 paisa coins=",(q*z))

        except:
                print('Error,input real numbers only')


