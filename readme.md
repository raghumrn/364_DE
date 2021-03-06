String manipulator quick start guide

## What is in this repository ?
This repository contains modules for string manipulations like string reversing and interleaving two strings

## what each module does ?
1. str_reverse - contains a function to reverse a string.
2. str_interleave - contains a function to interleave two strings.
3. str_manipulator - main function which calls the above two functions. 

## How do i provide my inputs ?
Configure your inputs in conf\inputs.cfg  file

## How do I start ?
1. Configure your inputs in above mentioned file
2. If you want to only reverse a string run the below command
	* python str_reverse.py
3. If you want to interleave two strings run the below command
	* python str_interleave.py
4. If you want to reverse a string and interleave two strings use one of the below commands
	* python str_manipulator.py
	* str_manipulator.bat

## How do I do Unit testing ? 
1. doctest
	* python -m doctest str_reverse.py -v
	* python -m doctest str_interleave.py -v
	* python -m pytest --doctest-modules -v
2. pytest
	* python -m pytest -v

## How do I generate test coverage report?
	* pytest coverage 
		* pytest --cov-report html:cov_html   --cov=str_reverse . 
	* Unit test coverage
		* coverage run -m unittest
		* coverage html