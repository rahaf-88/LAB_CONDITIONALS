wieght:int=input("user to provide his wieght")
height:int=input("user to provide his height")
x = weight / (height*height/100)
print(x)
if x < 18.5:
    print('You are overwieght you need to work out more and watch your diet')
elif x>=18.5 and x<25:
    print("You are fit & healthy")
elif x >= 25 and x < 30:
   print('You are underweight. Watch your health')
else:
   print("rong value")
