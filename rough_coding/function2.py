#positional argument
def sum1(a,b):
    c=a-b
    print(c)
sum1(4,7)

#keyword argument
def kw_arg(a,b):
    c=a-b
    print(c)
kw_arg(b=4,a=5)

#default
def sub(a,b=3):
    c=a-b
    print(c)
sub(a=1)
sub(a=5,b=2)

#var len arg
def detail (name, *outher):
    print(name,outher)
detail("yomadhan")
detail("yomadhan",34)
detail("yomadhan",45)

#keyword var length argument
def detail10 (**outher):
    print(outher)
detail10(a=23,ab=34,yoma="df")
