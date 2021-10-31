def reverse_string(ip_string):
	'''
	This function reverses the given string 

	parameters:
	-------------
	ip_string - input string to reverse

	doctest
	-------------
	>>> reverse_string("ABCDEF")
	reverse of ABCDEF is FEDCBA
	'FEDCBA'
	>>> reverse_string("1234567")
	reverse of 1234567 is 7654321
	'7654321'
	'''
	rev_str = ip_string[::-1] 
	print(f"reverse of {ip_string} is {rev_str}")

	return(rev_str)


class test():
	__slots__=['a','b']
	def __init__(self,asdf):
		self.a=asdf


if __name__ == "__main__":
	reverse_string('ABCDEF')
	a=5
	#print(dir(a))
	t=test("asdf")
	print(dir(t))

	print(t.__dict__)

	#print(test.__dict__)

#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a']


