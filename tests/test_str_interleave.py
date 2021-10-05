import pytest
from str_interleave import interleave_string 


def test_str_interleave_same_length_strings():
	assert "ABABABAB" == interleave_string("AAAA","BBBB")

def test_str_interleave_first_string_bigger():
	assert "A-B-C-D-EFG" == interleave_string("ABCDEFG","----")

def test_str_interleave_second_string_bigger():
	assert "A1B2C3D4567" == interleave_string("ABCD","1234567")


#Parameterized tests with pytest 

@pytest.mark.parametrize("interleaved_string, first_string, second_string",
						[("ABABABAB", "AAAA", "BBBB"),
						 ("A-B-C-D-EFG", "ABCDEFG", "----"),
						 ("A1B2C3D4567", "ABCD", "1234567")
						])
def test_str_interleave(interleaved_string,first_string,second_string):
	assert interleaved_string == interleave_string(first_string,second_string)
