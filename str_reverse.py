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


if __name__ == "__main__":
	reverse_string('ABCDEF')

