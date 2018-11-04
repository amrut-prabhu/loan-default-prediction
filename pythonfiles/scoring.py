import numpy as np

def import_accuracy(y_test, predictions):
	errors = abs(predictions - y_test)
	mape = 100 * (errors / y_test)
	accuracy = 100 - np.mean(mape)
	return accuracy
