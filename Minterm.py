

print("\t \t \t    ---------MINTERM-------------")
print("             \t \t\t     ~~~~~~~")
print("\n\t \t|--------------------------------------------------|")
print("\t \t|Enter your Variables In this format               |")
print("\t \t|Eg: Abar=Ab A=a this is aplicable for all Variable|")
print("\t \t|--------------------------------------------------|\n")
def minterm():      
 A=str(1)
 Ab=str(0)
 B=str(1)
 Bb=str(0)
 C=str(1)
 Cb=str(0)
 print("Enter your firsterm:");
 x=eval(input())+eval(input())+eval(input())
 print("Enter your second Term:");
 y=eval(input())+eval(input())+eval(input())
 print("Enter your third Term:");
 z=eval(input())+eval(input())+eval(input())
 Y=int(input(" Are you want your code in 0 and 1 say Yes in 0 and No in 1: "))
 
 if (Y==0):
   print(x+y+z)
   

#Condition for First term 
 if (x=="000"):
   x= "1"
 elif(x=="010"):
    x=2
 elif(x=="011"):
    x=3
 elif(x=="100"):
    x=4
 elif(x=="101"):
    x=5
 elif(x=="110"):
    x=6
 elif(x=="111"):
    x=7
 else:
     x=1000

#codition for second term
 if (y=="000"):
   y= "1"
 elif(y=="010"):
    y=2
 elif(y=="011"):
    y=3
 elif(x=="100"):
    y=4
 elif(y=="101"):
    y=5
 elif(y=="110"):
    y=6
 elif(y=="111"):
    y=7
 else:
    y=1000


 #condition for Third term
 if (z=="000"):
   z= "1"
 elif(z=="010"):
    z=2
 elif(z=="011"):
    z=3
 elif(z=="100"):
    z=4
 elif(z=="101"):
    z=5
 elif(z=="110"):
    z=6
 elif(z=="111"):
    z=7
 else:
    z=1000


 if(x==1000 or z==1000 ):
     print("Enter your correct term in 0 and 1 and use 3 digit")
 elif(x==1000 or y==1000):
     print("Enter your correct term in 0 and 1 and use 3 digit")    
 else:
     print("sum of minterm:;",x,y,z)  

minterm()

