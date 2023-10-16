m,n = map(int, input().split())
a= list(map(int, input().split()))
max = 0
kol=0
max_k=0
rez = []
for h in a:
    if h> max:
        max=h
        ind = a.index(h) 
a.pop(ind)                
print('ind=',ind)
print(a)
for i in a:
    if i == max:
        kol+=1
        k= max+1
        rez.append(a.index(i))
        a.pop(a.index(i))
        a.append(k)
for i in a:
    if i == max:
        max_k+=1
if max_k==0:
    max =0
    for h in a:
        if h> max:
            max=h
            ind = a.index(h) 
    a.pop(ind)                
print(max)                                          
print(a)
print('rez=',rez)                
# k= 0
# kol=0
# max = 0
# for h in a:
#     if h> max:
#         max=h
#         ind = a.index(h) 
# print('ind=',ind)        
# for i in range(m):
#     if a[i] == a[ind]:
#         k= i+max
#         kol+=1
#         a.pop(i)
#         a.pop(a[ind])
#         a.append(k)
#         m-=1
# print('k=',k)
# print('max=',max)
# print('kol=',kol)          
# print('a=',a)          
          

                
