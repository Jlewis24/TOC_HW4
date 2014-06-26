#encoding: utf-8
#coding: utf-8

# Theory of Computation - Homework 4 -
# Name: 魏喬浩
# Student ID: F74007125
# Compilation: python2 TocHw4.py <URL> 
# Description: This program takes a JSON file, scans it and prints the address (being it road, street, etc.) with more 
# records and prints that street name, and its highest and lowest price


import sys
import re #for Regular Expressions
import json #to read the JSON object
import urllib2 #to fetch from URL

if len(sys.argv) != 2:  #check for correct number of arguments
        sys.exit('Error on imput, it must be as follows --> %s <URL>' % sys.argv[0])

URL = sys.argv[1]
info = json.load(urllib2.urlopen(URL)) #Get JSON object from URL

if not URL or not info: #if there's no JSON file or if it's empty throw error
	sys.exit('Error with input URL or JSON file is empty')
	
max['month'] = 0
address = max = dict() #set dictionaries

for data in info:
	regex = re.search(u'((?<=區).*大道)|((?<=區).*路)|((?<=區).*街)|((?<=區).*巷)', data[u'土地區段位置或建物區門牌']) #Regular expressions
	
	if address[regex.group(0)]['max'] < data[u'總價元']:
		address[regex.group(0)]['max'] = data[u'總價元']
	elif address[regex.group(0)]['min'] > data[u'總價元']:
		address[regex.group(0)]['min'] = data[u'總價元']
	if len(address[regex.group(0)]) > max['month']
		max['month'] = len(address[regex.group(0)])
		max['address'] = regex.group(0)
		result[regex.group(0)] = dict()
		result[regex.group(0)]['address'] = data[u'土地區段位置或建物區門牌']
		result[regex.group(0)]['max'] = address[regex.group(0)]['max'] #copies actual data to result
		result[regex.group(0)]['min'] = address[regex.group(0)]['min']
	elif len(address[regex.group(0)]) == max['month']:
		if regex.group(0) in max['address']:
			result[regex.group(0)]['max'] = address[regex.group(0)]['max']
			result[regex.group(0)]['min'] = address[regex.group(0)]['min']
		else:	
			max['address'] = max['address'] + regex.group(0) 
			result[regex.group(0)] = dict()
			result[regex.group(0)]['address'] = data[u'土地區段位置或建物區門牌']
			result[regex.group(0)]['max'] = address[regex.group(0)]['max']
			result[regex.group(0)]['min'] = address[regex.group(0)]['min']
for i in result.keys():
	print (u'%s, Highest Price: %s, Lowest Price: %s',(result[i]['address']).group(0), result[i]['max'], result[i]['min']))

