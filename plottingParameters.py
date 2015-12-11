
		
import numpy as np
import colorsys
from collections import OrderedDict
from scipy.interpolate import interp1d

class pltParam:
	'''
	class to handle parameters for graphs
	'''
	def __init__(self):
		self.width = .3
		self.fontsize = 15
		self.padding =.1

	
	#http://stackoverflow.com/questions/470690/how-to-automatically-generate-n-distinct-colors
	def getColors(self,num_colors):
		'''
		input is an integer, output is a list of distinct colors in rgb format.
		
		'''
		colors=[]
		for i in np.arange(0., 360., 360. / num_colors):
		    hue = i/360.
		    lightness = (50 + np.random.rand() * 10)/100.
		    saturation = (90 + np.random.rand() * 10)/100.
		    colors.append(colorsys.hls_to_rgb(hue, lightness, saturation))
		return colors

	def alternatingDictionary(self, unSortedDic):
		'''
		This is for plotting data on a pie Chart.  We want the values of big and small items to alternate
		so there is no labeling overlap issues. 
		returns list of keys
		'''
		sortedDic = OrderedDict(sorted(unSortedDic.items(), key=lambda t: t[1]))
		keys = sortedDic.keys()
		numKeys= len(keys)
		firstHalf= keys[:int(.5*numKeys)]
		secondHalf= keys[int(.5*numKeys):]
		secondHalf=secondHalf[::-1]  #reverse order of second list
		
		target = []
		for i in range(len(firstHalf)):
			target= target + [firstHalf[i]] + [secondHalf[i]]
		
		if numKeys%2==1:
			target+= [secondHalf[-1]] 

		return target
	

	def getTickFontSize(self,numTicks):
		'''
		input: int, output float
		helper function for picking appropriate font size for graphs with ticks 
		'''
		if numTicks <15:
			return 15

		maxFont = 15
		minFont = 4
		fontSizeFunction = interp1d([14,75],[maxFont,minFont])  #maps linearly range in [14,75] to [15,4]
		fontsize= float( fontSizeFunction(numTicks) )
		return fontsize



if __name__ == '__main__':
	p = pltParam()
	print p.getTickFontSize(22)




