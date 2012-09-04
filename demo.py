import sys

def func1():
	print "hello world"
	return

def func2(arg1):
	print arg
	return

def main():
	if(len(sys.argv) == 1):
		return

	if(sys.argv[1] == "1"):
		func1()
	elif(sys.argv[1] == "2"):
		func2("func2")

if __name__=="__main__":
	main()
