f=open('./p11.txt','r')

grid=[]
i=0
for line in f:
	grid.append([]) #append empty list to fill
	for n in line.split():
		if n!='\n':
			n=int(n)
			grid[i].append(n)
	i=i+1
	
#print grid

r,c=0,0  #row & column number

largest=0

for row in grid:
	for col in row:
		if c<17:
			right=True
		else:
			right=False
		if c>2:
			left=True
		else:
			left=False
		if r<17:
			down=True
		else:
			down=False
		
		
		if right: #test if right is possible
			if grid[r][c]*grid[r][c+1]*grid[r][c+2]*grid[r][c+3]>largest: #horizontal
				largest=grid[r][c]*grid[r][c+1]*grid[r][c+2]*grid[r][c+3]
		if right and down:
			if grid[r][c]*grid[r+1][c+1]*grid[r+2][c+2]*grid[r+3][c+3]>largest: #right diagonal
				largest=grid[r][c]*grid[r+1][c+1]*grid[r+2][c+2]*grid[r+3][c+3]
		if left and down: # if left diag is possibe
			if grid[r][c]*grid[r+1][c-1]*grid[r+2][c-2]*grid[r+3][c-3]>largest: #left diagonal
				largest=grid[r][c]*grid[r+1][c-1]*grid[r+2][c-2]*grid[r+3][c-3] 
		if down: # test if down is possible:
			if grid[r][c]*grid[r+1][c]*grid[r+2][c]*grid[r+3][c]>largest:
				largest=grid[r][c]*grid[r+1][c]*grid[r+2][c]*grid[r+3][c]
		
		c=c+1
	r=r+1
	c=0
	
print largest




