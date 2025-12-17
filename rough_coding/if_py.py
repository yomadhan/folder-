a=int(input("enter your age"))

c=float(input("ender your cgp"))

if a>17 and a<45 and c>9:
 
    
    for i in range(1,7):
        score=int(input("Ender your Score"))
        
        if score >=90 and score <100:
        
            print("A grade")
        
        elif score >= 80 and score <90:
            print("B grade")
        
        elif score >= 70 and score <80:
            print("C grade")
        elif score >= 60 and score <70:
            print("D grade")
        
        elif score >= 50 and score <60:
            print("E grade")
        
        else:
            print("fail❌")




user_name="YOMADHAN"
p_w="**8whpKN3***"
ender_UN=str(input("ender your user name"))
ender_p_w=str(input("ender your user PASSWORD"))
if user_name==ender_UN:
    
    if p_w==ender_p_w:
        print("wellcome to you login page😊")
    else:
        print("your password is invalid⚠️")
else:
    print("it is not your User naem")
    
    
    
a=float(input("1st no "))
b=float(input("2st no "))
c=float(input("3st no "))

if a>=b:
    if a>=c:
        largest=a
    else:
        largest=b
    
else:
    if b>=c:
        largest=b
    else:
        largest=c
print("the largest no is", largest)