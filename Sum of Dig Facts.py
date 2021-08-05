#SUM OF DIGIT FACTORIALS
#(or)
#Sum of factorials of digits of a number

''' Example : 123 = 1! + 2! + 3! = 1 + 2 + 6 = 9'''

n=int(input("ENTER THE NUMBER :"))
def func(n):
    sum = 0
    l1=[]
    for dig in str(n):  
        l1.append(int(dig))
    return(l1)

l2 = func(n)

def gun(m):
    l3=[]
    for i in l2:
        if i == 0:
            l3.append(1)
        else :
            fact =1
            for j in range(1,i + 1):
                fact = fact*j
            l3.append(fact)
    return l3

l4=gun(n)
print(l4)
s=0
for k in l4:
    s+=k
    
print("SUM OF DIG FACTS IS :",s)
    





