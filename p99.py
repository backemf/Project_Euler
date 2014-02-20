f=open('./base_exp.txt','r')
base=[]
exp=[]
for line in f:
	base.append(int(line.split(',')[0]))
	exp.append(int(line.split(',')[1]))
	
exp.sort()



