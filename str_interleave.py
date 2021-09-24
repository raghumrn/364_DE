def interleave_string(str1,str2):
	'''
	This functions interleaves two strings 

	parameters
	----------
	str1 - first string that needs to be intere=leaved
	str2 - second string that needs to be interleaved
	'''
	small_string,bigstring = (str1,str2) if len(str1) <= len(str2) else (str2,str1)
	print(f"string 1 = {str1}, string 2 = {str2}." + " Interleaved string = " + "".join(str1[i]+str2[i] for i in range(0,len(small_string))) + bigstring[len(small_string)::])

if __name__ == "__main__":
	interleave_string("AAAA","BBBB")

