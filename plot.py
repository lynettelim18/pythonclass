#python script import libraries needed
import numpy
import os
import glob
import matplotlib.pyplot
from os.path import basename

# filenames = glob.glob('inflammation*.csv')
# filenames = filenames [0:2]

#defining function
def analyze(filename):
	print(filename)
    data = numpy.loadtxt(fname=filename, delimiter=',')


def detect_problems (filename):
	data = numpy.loadtxt(fname=filename, delimiter=',')
	if data.max(axis =0)[0] ==0 and data.max(axis=0)[20] ==20:
		print ("suspicious looking maxima!")
	elif data.min(axis =0).sum() ==0:
		print("Minima add up to zero!")
	else:
		print("seems ok!")

def plot (data):
	'''plots data as you pass an array...
	you datar is pass so that you can plot
	 over'''
    print (data.shape)
    savebase = os.path.splitext(f)
    path = "plotfigs/"
    output = path + savebase[0] + ".eps"
    print(output)
    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('MEAN')
    axes1.plot(data.mean(axis=0))

    axes2.set_ylabel('max')
    axes2.plot(data.max(axis=0))

    axes3.set_ylabel('min')
    axes3.plot(data.min(axis=0))

    fig.tight_layout()
    #matplotlib.pyplot.show()
    fig.savefig(output);

def center(data, desired):
	return (data - data.mean ()) + desired
