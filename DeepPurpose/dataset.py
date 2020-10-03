import pandas as pd
import numpy as np
import wget
from zipfile import ZipFile 
from DeepPurpose.utils import convert_y_unit
import json
import os 



def read_file_training_dataset_bioassay(path = 'Users/louis/desktop/Ebola_research/data/ebola', binary = True, threshold = 15, balanced = True, oversample_num = 30, seed = 1):
	# a line in the file is SMILES score, the first line is the target sequence
	try:
		file = open(path , "r")
	except:
		print('Path Not Found, please double check!')
	target = file.readline()
	if target[-1:] == '\n':
		target = target[:-1]        
	X_drug = []
	y = []
	for aline in file:
		values = aline.split()
		X_drug.append(values[0])
		y.append(float(values[1]))
	file.close()
	return np.array(X_drug), target, np.array(y)

def read_file_training_dataset_drug_target_pairs(path = 'Users/louis/Desktop/Ebola_research/data/ebola/ebola.txt'):
	# a line in the file is SMILES Target_seq score    
	try:
		file = open(path, "r")
	except:
		print('Path Not Found, please double check!')
	X_drug = []
	X_target = []
	y = []
	for aline in file:
		values = aline.split()
		X_drug.append(values[0])
		X_target.append(values[1])
		y.append(float(values[2]))
	file.close()
	return np.array(X_drug), np.array(X_target), np.array(y)

def read_file_virtual_screening_drug_target_pairs(path):
	# a line in the file is SMILES Target_seq    
	try:
		file = open(path, "r")
	except:
		print('Path Not Found, please double check!')
	X_drug = []
	X_target = []
	for aline in file:
		values = aline.split()
		X_drug.append(values[0])
		X_target.append(values[1])
	file.close()
	return np.array(X_drug), np.array(X_target)


def read_file_repurposing_library(path = '/Users/louis/Desktop/Ebola_research/data/for_antiebola_drugs.txt'):
	# a line in the file is drug names and SMILES 
	try:
		file = open(path, "r")
	except:
		print('Path Not Found, please double check!')    
	X_drug = []
	X_drug_names = []
	for aline in file:
		values = aline.split()
		X_drug.append(values[1])
		X_drug_names.append(values[0])
	file.close()
	return np.array(X_drug), np.array(X_drug_names)

def read_file_target_sequence(path):
	# a line in the file is target name and target sequence 
	try:
		file = open(path, "r")
	except:
		print('Path Not Found, please double check!')    
	values = file.readline().split()
	file.close()
	return values[1], values[0]




