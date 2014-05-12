ru=[1]
lu=[1]
rd=[1]
ld=[1]



for c in range(8,((1001-1)/2)*8+1,8):
	ru.append(ru[-1]+c)
	lu.append(lu[-1]+c-2)
	ld.append(ld[-1]+c-4)
	rd.append(rd[-1]+c-6)
	
ld.remove(1)
rd.remove(1)
ru.remove(1)

print sum(ld)+sum(ru)+sum(rd)+sum(lu)
