#!/usr/bin/python
import itertools

infile=open("cipher1.txt",'r')
ascii_code_list=list(map(int,(infile.read()).split(',')))
infile.close()



def convert(password):
	"""
	key is repition of password, output is code XOR'ed with key
	"""
	output=[]
	key=itertools.islice(itertools.cycle(password),len(ascii_code_list))
	for (ascii_code,key_nr) in zip(ascii_code_list,key):
		output.append(chr(ascii_code^key_nr))
	return(output)
		
		

def main():
	ascii_sum=0
	outfile=open("p59_output.txt",'w')
	for password in itertools.permutations(range(97,123),3):
		message=''.join(convert(password))
		if " and " in message and " have " in message and " the " in message:
			outfile.write(message)
			ascii_sum=sum(map(ord,message))
		print(password)
	print(ascii_sum)
	outfile.close()
	
if __name__=="__main__":
	main()