"""TASK which was given on 16-12-2025

Yomadhan

"""
 #datas
stu_sce=[87,37,48,30,28,38,52,19,56,24]
shopping=["A","B",'C','D']
dict1={"x":233,"y":482,"z":39}
price=[4534,3115,1444,344,335,3002,442,2000]
attenance=["prcent","prcent","absent","prcent","prcent","prcent","absent"]
mobail_srceen=[4,6,4,2,6,1,0,8]

# Q1

print("class avg",sum(stu_sce)/len(stu_sce))


# Q2
no_m_f=[]
for i in stu_sce:
    if i>50:
        no_m_f.append(i)
       
print("there are ",len(no_m_f)," studence more then 50")
    
######

# Q3
f_stu =[]      #failed studence

for j in stu_sce:
    if j <= 40:
        f_stu.append(j)
       
print("Failed students:", f_stu)


# Q4

new_list=stu_sce
new_list.pop()
print(new_list)

# Q5

shopping.append("mango")
shopping.remove("A")
print(shopping)
print("\n")


#6 
 
print("total  of list",sum(stu_sce))
print("total of dict val",sum(dict1.values()))

#7

new_list=[]
for k in price:
    if k > 1000:
        new_list.append(k)
print(new_list)


#8

print(max(price))

#9 

less=[]

for l in price:
    if l<2000:
        less.append(l)
print(less)

#10
incre=[]
for m in price:
    n=m+(m*(10/100))
    incre.append(n)
print(incre)
print("\n")
    
#11
stu1=[1,1,0,1,1,1,0]
for n in stu1:
    if n==1:
        pd=stu1.count(n)
print(pd)


#12

s = 0          
nl = []        

for l in attenance:
    if l == "absent":
        nl.append(s)
    s += 1

print(nl)
        
#print(nl.append(attenance.index("absent")))
  
#13
print(max(stu_sce))

#14
q1=[]
for q in stu_sce:
    if q>=40:
        q2=q1.append(q)

#print(q1)
print((len(q1)/len(stu_sce))*100)
        
#15
print(sum(mobail_srceen)/len(mobail_srceen))


