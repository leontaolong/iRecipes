#!/usr/bin/python
import long_info370_assignment1_scrape
import long_info370_assignment1_clean
import long_info370_assignment1_calculate

rawData_file_path = './long_info370_assignment1_rawData.csv'
cleanData_file_path = './long_info370_assignment1_cleanData.csv'
calculated_file_path = './long_info370_assignment1_calculate.csv'

long_info370_assignment1_scrape.scape(rawData_file_path)
long_info370_assignment1_clean.clean(rawData_file_path , cleanData_file_path)
long_info370_assignment1_calculate.culculate(cleanData_file_path, calculated_file_path)

