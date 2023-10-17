m,n = map(int, input().split())
a= list(map(int, input().split()))
k=[]
num=[]
kol = len(k)
rez= 0
max_ =[]
dup=[]
b=[] 
c=[]      
while len(a)!=0 :
    print('next')
    print('a=',a)
    print('max_=',max_)
    print('dup=',dup)
    print('num=',num)
    print('rez=',rez    )
    if len(dup)==1:
        for i in max_:
            if i != dup[0]:
                b.append(i)
        max_=b
        b=[]        
        max_.append(dup[0]+1)
    if len(max_)!=1:
        dup = [x for i, x in enumerate(max_) if i != max_.index(x)]
        if len(dup)==1:
                for j in max_:
                    if j != dup[0]:
                        c.append(i)
                        max_=c
                        c=[]
                        max_.append(dup[0]+1)           
    if len(max_)==1:
            num=max_[0]            
    max_.append(max(a))
    k.append(max(a))
    a.pop(a.index(max(a)))
    print(a)
    num=max_[0]
    dup = [x for i, x in enumerate(max_) if i != max_.index(x)]
    rez= num
    print('max_=',max_)
    for i in max_:
        if i== 4:
            break
print(rez)

        
                                                
            