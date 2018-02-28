'''
simple program for reading a csv file.
csv stand for comma-separated values.
'''
import csv

with open('example.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')

	dates = []
	colors = []

	for row in readCSV:
		color = row[3]
		date = row[0]

		colors.append(color)
		dates.append(date)

	print(colors)
	print(dates)

	try:
		whatColor = input('What color do you wish to know the date of?\n')
		
		if whatColor in colors:			
			coldex = colors.index(whatColor.lower())
			print('the date of the color %s is %s' % (whatColor, dates[coldex]))
		else:
			print('Color not found, or is not a color!')

	except Exception as e:
		print(e)

	print('continuing')