str='''afsf
sfdgd
dbddjjdd
hdjjdd'''
print(str)

list1=list(str)
print(list1)

str=''.join(list1)
print(str)

list2=["a","b"]
str2="".join(list2)
print(str2)

age=input()
print(age)
print(type(age))

def sum_func(a,b):
    result=a+b
    return result
res=sum_func(2,3)