import configparser
import threading

from str_reverse import *
from str_interleave import *

if __name__ == "__main__":

	config_file=r"conf\inputs.cfg"

	#reading inputs from config file 
	raw_cfg_parser = configparser.RawConfigParser()
	raw_cfg_parser.read(config_file)
	string_to_reverse = raw_cfg_parser.get('INPUTS','string_to_reverse')
	first_string_to_interleave = raw_cfg_parser.get('INPUTS','first_string_to_interleave')
	second_string_to_interleave = raw_cfg_parser.get('INPUTS','second_string_to_interleave')

	t1 = threading.Thread(target=reverse_string, args=(string_to_reverse,))
	t2 = threading.Thread(target=interleave_string, args=(first_string_to_interleave,second_string_to_interleave))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
