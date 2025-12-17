
"""
Dec 17 2025 Assessment

Yomadhan
 
"""

#
print('1 question output')
stu=[64,73,25,63,74,24,73,46,27,95]
print("average: ",sum(stu)/len(stu))
j=[]
for i in stu:
    if i >=50:
        
        j.append(i)
        
print("no of student who took more then 50 is ",len(j))


#2 question
print("")
print('2 question output')

user_name=input(str("ENDER USER NAEM (mim 6 charactor):"))
if len(user_name)>=6:
    print("wellcome to home page😊")
else:
    print("should ender 6 char")
    
   

#3  question
print("")
print('3 question output')

t=(5,434,53,6,34,6,33)
t1=tuple(set(t))
print(t1)

 
#4  question
print("")
print('4 question output')

dict1={"user name":"yomadhan","password":"3*jhi9GH"}

un=str(input("user name:"))
pw=str(input("password: "))

if un == dict1.get("user name") and pw==dict1.get("password"):
    print("Log in success🎉 ", un)
else:
    print("Invlide log in 🔃")



#5 question
print("")
print('5 question output')

string="small is beautyful"
print(len(string.split()))



#6 question
print("")
print('6 question output')

num = [35,3,55,901,740,9,7,65,5,3246,49,36]

odd = []
even = []

for k in num:
    if k % 2 == 0:
        even.append(k)
    else:
        odd.append(k)

print("Even numbers are:", even)
print("Odd numbers are:", odd)



#7 question
print("")
print('7 question output')


text_file = ''' In 2025, "normal speech" about politics focuses on
 open dialogue, active listening, and finding common ground rather 
 than winning a debate. To have a productive conversation, experts
 recommend shifting from "defensive" communication (like saying "You're wrong") 
 to "descriptive" communication (sharing why you feel a certain way) '''

lines = text_file.strip().split("\n")
print("Number of lines:", len(lines))


#8 question
print("")
print('8 question output')

def add(a,y):
    return a+y    


def sub(a,y):
    return a-y  

def mul(a,y):
    return a*y  

user=str(input("what operation, add|sub|mul: "))
n1=int(input("1st :"))
n2=int(input("2nd: "))

if user=="add":
    print(add(n1,n2))
    
elif user=="sub":
    
    print(sub(n1,n2))
elif user=="mul":
   
    print(mul(n1,n2))

else:
    print("")
    


#9 question
print("")
print('9 question output')

price=int(input("ender price: "))
discount=int(input("ender discount: "))    
print("final price is : ", price-(price*(discount/100)))

#10 question
print("")
print('10 question output')

numbers=eval(input("ender num as string ex: '7' "))
print(numbers)

print('\n\t---------END-----------')


