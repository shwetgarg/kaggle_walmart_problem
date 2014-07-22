import numpy as np
import csv as csv

def read_file(filename):
	with open(filename, 'rb') as f:
		csv_file_object = csv.reader(f)
		header = csv_file_object.next()
		data = []
		for row in csv_file_object:
			data.append(row)			
	data = np.array(data).astype(np.float) 
	print "reading of file done"
	return data
	
def read_file_in_chunks(filename, no_of_rows):
	no_of_files = 0
	counter = 0
	data = []
	
	with open(filename, 'rb') as f:
    		csv_file_object = csv.reader(f)
		header = csv_file_object.next()		
		
		for row in csv_file_object:
			data.append(row)
			counter += 1
			if (counter == no_of_rows):
				print "\nprediction of ", no_of_files, " file started"
				data = np.array(data).astype(np.float)
				no_of_files += 1
				
				yield data
				data = []
				counter = 0
		
		if (counter > 0):
			data = np.array(data).astype(np.float)
			print "\nprediction of last file started"
			yield data

def generate_header(separator, *args):
	return separator.join(args) + "\n"

def write_file(filename, header, iterator):
	with open(filename, 'wb') as f:
		f.write(header)
    		csv_file_object = csv.writer(f)
		for block in iterator:
			csv_file_object.writerows(block)
			

		
	

