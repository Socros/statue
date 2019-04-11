age=[]
height=[]
builder=[]
sex=[]
x=input("How much statue do you want: ")
for i in range(x): 
    _age=input(" Since : " )
    _height=input(" Height statue : " )
    _builder=raw_input(" Builder : ")
    _sex=raw_input(" Sex statue : ")
    while _sex != "Kori" and _sex!= "Kouros":
        _sex=raw_input(" Sex statue : ")
    age.append(_age)
    height.append(_height)
    builder.append(_builder)
    sex.append(_sex)

N=len(height)
max=-1
for i in range(N):
    if height[i]>max:
        max=height[i]
        max_sex=sex[i]
print max , max_sex


sum=0
for i in range(x): 
    sum=height[i]+sum
mo=sum/float(x)
print "Average of statue height: ",mo


