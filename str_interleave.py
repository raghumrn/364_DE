def interleave_string(str1,str2):
	'''
	This functions interleaves two strings 

	parameters
	----------
	str1 - first string that needs to be intere=leaved
	str2 - second string that needs to be interleaved

	doctest
	-------------
	>>> interleave_string("AAAA","BBBB")
	string 1 = AAAA, string 2 = BBBB.Interleaved string = ABABABAB
	'ABABABAB'
	>>> interleave_string("ABCDEFG","----")
	string 1 = ABCDEFG, string 2 = ----.Interleaved string = A-B-C-D-EFG
	'A-B-C-D-EFG'
	>>> interleave_string("ABCD","1234567")
	string 1 = ABCD, string 2 = 1234567.Interleaved string = A1B2C3D4567
	'A1B2C3D4567'
	'''

	small_string,bigstring = (str1,str2) if len(str1) <= len(str2) else (str2,str1)
	i_string = "".join(str1[i]+str2[i] for i in range(0,len(small_string))) + bigstring[len(small_string)::]
	print(f"string 1 = {str1}, string 2 = {str2}." + f"Interleaved string = {i_string}")
	return i_string

if __name__ == "__main__":
	interleave_string("AAAA","BBBB")

