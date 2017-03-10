#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

count = 0
countNan = 0
countPoi = 0
countPoiNan = 0

for k in enron_data:
	count += 1
	if enron_data[k]['poi'] == True:
		countPoi += 1
		if enron_data[k]['total_payments'] == 'NaN':
			countPoiNan += 1
	
	if enron_data[k]['total_payments'] == 'NaN':
		countNan += 1
		
		
print count
print countNan
print countPoi
print countPoiNan
