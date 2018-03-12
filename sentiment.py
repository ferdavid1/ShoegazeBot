from textblob import TextBlob
from shoegazebot import Shoegaze 
import numpy as np
import matplotlib.pyplot as plt 

def main(number_of_lines):
	polarities = []
	for x in range(number_of_lines):
		text = TextBlob(Shoegaze())
		polarities.append(text.sentiment.polarity)
	return polarities

if __name__ == '__main__':
	means = []
	stdevs = []
	for x in range(10):
		polarities = main(100)
		means.append(np.mean(polarities))
		stdevs.append(np.std(polarities))
	print(np.mean(means), np.std(stdevs)) # 0.040137920875420875 0.025997312400035787
	plt.figure()
	plt.xlabel('Iterations')
	plt.ylabel('Mean Polarity')
	plt.plot(range(len(means)), means)
	plt.savefig("Mean_polarity.png")
	plt.figure()
	plt.xlabel('Iterations')
	plt.ylabel('Standard Deviation of Polarity')
	plt.plot(range(len(stdevs)), stdevs)
	plt.savefig("Std_Polarity.png")
	plt.show()