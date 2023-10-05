m=[]
ff=[]#abrakadabra
x=input()
y=input()
y1=len(y)
n=x.split()
for i in range(len(n)):
     m.append(int(n[i]))
f=[]
for i in range(m[1],m[2]+1):
     f.append(int(i))
if((m[0]*m[1])>y1 or (m[0]*m[2])<y1):
   print('no solution')
elif(m[0]==1):
   print(y)
else:
   for j in f:
       if(( y1//j)==(m[0]-1) and (y1%j <= m[2])):
            for k in range(1,m[0]+1):
                c=0
                yy=''
                c=y[0:j]
                print(c)
                ff.append(c)
                #print(ff)
                for s in range(j,len(y)):
                     yy=yy+y[s]
                print (yy)
                y=yy  
                print(y)
            break 
   ff.append(y)
for i in range(len(ff)):
     print(ff[i])
                    
                   
      
             

        
