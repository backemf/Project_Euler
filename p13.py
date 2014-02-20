f=open('./p13.txt','r')

num=[]
k=0

for k in range(0,50):
	n=0	
	f.seek(0)
	for line in f:
		n=n+int(line[k])
	num.append(n)

f.close()
	
print num

rem = 0
box=0
som=[]

for s in reversed(num[1:]):
	box=s+rem
	som.append(int(str(box)[-1]))
	rem= int(str(box)[0:-1])

wholesum=str(num[0]+rem)

for u in reversed(som):
	wholesum=wholesum+str(u)
	
print wholesum


