def reverse_string(ip_string):
	'''
	This function reverses the given string 

	parameters:
	-------------
	ip_string - input string to reverse
	'''

	print(f"reverse of {ip_string} is {ip_string[::-1]}")


def interleave_string(str1,str2):
	'''
	This functions interleaves two strings 

	parameters
	----------
	str1 - first string that needs to be intere=leaved
	str2 - second string that needs to be interleaved
	'''
	print(f"Strings to interleave - string 1 = {str1}, string 2 = {str2}")
	small_string,bigstring = (str1,str2) if len(str1) <= len(str2) else (str2,str1)
	print("interleaved string = " + "".join(str1[i]+str2[i] for i in range(0,len(small_string))) + bigstring[len(small_string)::])


if __name__ == "__main__":
	reverse_string('ABCDEF')
	interleave_string("AAAA","BBBB")

