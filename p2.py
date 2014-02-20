prev=0
temp=0
cur=1
fibs=[]
som=0

fibs.append(prev)
fibs.append(cur)

while (cur+prev)<4E6:
	temp=cur
	cur+=prev
	prev=temp
	fibs.append(cur)
	
for i in fibs:
	if i%2==0:
		som+=i

print fibs
print som
