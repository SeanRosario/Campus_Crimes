'''Class that contains all answers pertaining to a college'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import handlers
import college
import matplotlib.patches as mpatches

class Answers:
	'''Class definition'''
	
	
		
	def __init__(self, answer1):
		'''Constructor'''
		self.answer1=answer1
		
		

	def visualize_answer1(self):
		'''Code to visualize answer to question 1'''

		crimes_list = ['MURD', 'NEG_M', 'FORCIB', 'NONFOR', 'ROBBE', 'AGG_A', 'BURGLA', 'VEHIC', 'ARSON']
		crimeNames= ["Forcible Rape", "Arson", "Manslaughter", "Murder", "NonForcible Rape", "Vehicle Theft","Burglary", "Aggravated Assault" ,"Robbery"]
		ax = plt.subplot(111)
		w = .3		
		padding =.1
		fontsize=15

		x = np.array(range(1, len(crimes_list) + 1))
		
		#seperate data by year instead of crime
		y_10=[]
		y_11=[]
		y_12=[]
	    
		for crime in crimes_list:
			y_10.append(self.answer1[crime][0].tolist()[0]*10000)   #multiply by 10000 y-axis is per 10000
			y_11.append(self.answer1[crime][1].tolist()[0]*10000)
			y_12.append( self.answer1[crime][2].tolist()[0]*10000)

		
		#bar for each year
		rect1 = ax.bar( x - w, y_10 , width = w, color='r', align='center')
		rect2 = ax.bar(x, y_11, width = w, color='g', align='center')
		rect3 = ax.bar(x + w, y_12, width = w, color='b', align='center')

		plt.xticks([ a + w/2 for a in  x],[name for name in crimeNames], rotation= 30, ha='right')


		ax.set_xlabel('Particular Crime by Year ', fontsize=fontsize)
		ax.set_ylabel('Crime Rate (per 10,000 students)', fontsize=fontsize)

		ax.set_title(college_name + " Crime By Year ", fontsize=fontsize)
		ax.autoscale(tight=True)

		#add padding
		plt.subplots_adjust(left=0.15,top=0.85)
		#legends
		r_patch = mpatches.Patch(color='red', label='2010')
		g_patch = mpatches.Patch(color='g', label='2011')
		b_patch = mpatches.Patch(color='b', label='2012')
		ax.legend([r_patch,g_patch,b_patch],['2010','2011','2012'])

		#adjust limits of yaxis to make room for annointed text
		maxData=max(y_10+y_11+y_12)
		plt.ylim(0,maxData * 1.15)
		
		def autolabel(rects):
			# attach some text labels
			for rect in rects:
				height = rect.get_height()
				print height
				ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
				        '%.1f' % height,
				        ha='center', va='bottom')

		autolabel(rect1)
		autolabel(rect2)
		autolabel(rect3)
		plt.tight_layout()
		plt.show()


if __name__ == '__main__':
	
	dataframe, crimes_obj = handlers.data_initialization("data/oncampuscrime101112.csv")
	college_name = "Harvard University"
	college_instance = dataframe[dataframe.INSTNM == college_name]
	crime_per_student = handlers.all_crimes_per_student_over_years("On Campus", "Crime", college_instance, crimes_obj)

	g=Answers(crime_per_student)
	#print len(g.answer1)
	print g.answer1['FORCIB'][0].tolist()[0]
	print "lfkajsdl;fkj"
	g.visualize_answer1()
