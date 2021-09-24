import configparser

from str_reverse import *
from str_interleave import *

if __name__ == "__main__":

	# reverse_string("ABCDEF")
	# interleave_string("AAAA","BBBB")

	config_file=r"conf\inputs.cfg"

	#reading inputs from config file 
	raw_cfg_parser = configparser.RawConfigParser()
	raw_cfg_parser.read(config_file)
	string_to_reverse = raw_cfg_parser.get('INPUTS','string_to_reverse')
	first_string_to_interleave = raw_cfg_parser.get('INPUTS','first_string_to_interleave')
	second_string_to_interleave = raw_cfg_parser.get('INPUTS','second_string_to_interleave')

	reverse_string(string_to_reverse)
	interleave_string(first_string_to_interleave,second_string_to_interleave)	
