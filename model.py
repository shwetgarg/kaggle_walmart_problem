import numpy
import sys
import csv as csv
import itertools

from sklearn.preprocessing import Imputer
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

import utils


def preprocessing(feature_vector):
	imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)
	imp.fit(feature_vector)
	feature_vector = imp.transform(feature_vector)
	print "missing variable imputed"
	return feature_vector
	
def train(train_filename):
	data = utils.read_file(train_filename)

	x = data[:,[0,1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17]]
	y = data[:,[6]]
	y = numpy.ravel(y)
	print "initialisation of variables done"

	x = preprocessing(x)

	#model = svm.SVC()
	model = RandomForestClassifier(n_estimators=10)
	model.fit(x,y)
	print "model fitting done"
	
	return model

def test():
	pass
		
def predict(model, test_filename, no_of_rows_in_testfile_chunks):
	for x_test in utils.read_file_in_chunks(test_filename, no_of_rows_in_testfile_chunks):
		x_test = preprocessing(x_test)

		y_test = model.predict(x_test)
		print "prediction done"
		
		x_test_output = [str(int(x[0]))+"_"+str(int(x[5]))+"_"+str(int(x[1]))+"-"+str(int(x[2]))+"-"+str(int(x[3])) for x in x_test]
		yield zip(x_test_output, y_test)

def main(argv):
	train_filename = argv[0]
	test_filename = argv[1]
	output_filename = argv[2]
	no_of_rows_in_testfile_chunks = argv[3]
	
	model = train(train_filename)
	utils.write_file(output_filename, ["Id","Weekly_Sales"], predict(model, test_filename, no_of_rows_in_testfile_chunks))

if __name__ == "__main__":
	main(sys.argv[1:])

