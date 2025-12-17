
try:
    num = eval(input("Enter a number: "))
    print("You entered:", num)
except:
    print("Error: Invalid input. Please enter a number.")




new_tuple = tuple(set(t))
print(new_tuple)


new_tuple = ()
for i in t:
    if i not in new_tuple:
        new_tuple += (i,)

print(new_tuple)

t = (1, 2, 3, 2, 4, 1, 5)

new_tuple = tuple(dict.fromkeys(t))
print(new_tuple)


     
nl = []
for index, value in enumerate(attenance):
    if value == "absent":
        nl.append(index)

print(nl)

f_s= [j for j in stu_sce if j<=40]
print(f_s)








p=1
while p<6:
    print(p)
    p+=1
    
    
    
for o in attenance:
if attenance=="absent":
            print("")
            
            
            
            print(attenance.index("absent"))



x=l.index("absent")

print(x)






s = 0          
nl = []        

for l in attenance:
    if l == "absent":
        nl.append(s)
    s += 1

print(nl)




#12

s = 0          
nl = []        

for l in attenance:
    if l == "absent":
        nl.append(s)
    s += 1

print(nl)