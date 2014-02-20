size=500

steps=range(3,2*size+3,2)

L=[[2]]

for i in range(0,size):
	L.append([L[i][0]+steps[i]])
	
	
for row in range(0,size):
	for col in range(0,size):
		L[row].append(L[row][col]+steps[col])

triplets=[]

for x in L:
	for y in x[L.index(x):]:
		if (y**0.5)%1==0:
			triplets.append((L.index(x)+1,x.index(y)+1,int(y**0.5)))
			
for t in triplets:
	if sum(t)==1000:
		break

print t


			
