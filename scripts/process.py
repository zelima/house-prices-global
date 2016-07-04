#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import urllib
import datetime
import csv
import xlrd


source = 'http://www.bis.org/statistics/pp/pp.xlsx'

def setup():
	'''Crates the directorie for archive if they don't exist
	
	'''
	if not os.path.exists('archive'):
		os.mkdir('archive')

def retrieve(source):
	'''Downloades xls data to archive directory
	
	'''
	urllib.urlretrieve(source,'archive/external-data.xls')

			
if __name__ == '__main__':
	setup()
	retrieve(source)
	