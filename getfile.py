#! /usr/bin/python

def openFileByDefault():
	"""
reads sys.argv and opens it's first arg for reading or returns stdin if no argument or file not readable.
"""
	import sys
	filename = ""
	fileObject = None
	if len(sys.argv) > 1:
		filename = sys.argv[1]
		#print "reading : " + filename
		fileObject = open(filename, "r")
	else:
		fileObject = sys.stdin
	return fileObject

