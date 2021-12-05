#!/usr/bin/env python

"""
Convert CSV file to libsvm format. Works only with numeric variables.
Put -1 as label index (argv[3]) if there are no labels in your file.
Expecting no headers. If present, headers can be skipped with argv[4] == 1.
"""

import sys
import csv
import operator
from collections import defaultdict

def construct_line(label, line, labels_dict):
	new_line = []
	new_line.append(label)
	for i, item in enumerate(line):
		new_item = "%s:%s" % (i + 1, item)
		new_line.append(new_item)
	new_line = " ".join(new_line)
	new_line += "\n"
	return new_line

# ---


input_file = "C:\\Users\\torres_fan\\Desktop\\CS586\\carPricePredict\\car-price-predict-model\\final_data3.csv"
output_file = "forthSelection.txt"

# try:
# 	label_index = int( sys.argv[3] )
# except IndexError:
# 	label_index = 0
label_index = 0

# try:
# 	skip_headers = sys.argv[4]
# except IndexError:
# 	skip_headers = 0
skip_headers = 1

i = open(input_file, 'rt')
o = open(output_file, 'wb')

reader = csv.reader(i)

if skip_headers:
	headers = reader.__next__()

labels_dict = {}
for line in reader:
	if label_index == -1:
		label = '1'
	else:
		label = line.pop(label_index)

	new_line = construct_line(label, line, labels_dict)
	if not new_line:
		continue
	o.write(new_line.encode('utf-8'))