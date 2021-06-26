from simpleimage import SimpleImage
import seaborn as sns
import matplotlib.pyplot as plt
import csv 
import json


def main():
	intensity = 1.5
	query = input('Which city social trend analysis do you want?(click enter to end) ')
	query_dict = {
		'Beijing' : 'given city',
		'Washington' : 'given city',
		'Gent port' : 'given city'
	}
	while query != '':
		if query_dict.get(query) != None:
			slowdown = slowdown_analysis(query + '_slowdown.png', intensity)
			recovery = recovery_analysis(query + '_recovery.png', intensity)
			recovery_sign = recovery - slowdown
			recovery_rate = (recovery_sign / recovery) * 100 
			print('')
			print('The recovery rate in this area is ' + str(recovery_rate) + '% more than the slowdown rate.')
		else:
			print('Please provide a valid input.')
		query = input('Which city social trend analysis do you want?(click enter to end) ')
	
	print('The program has ended.')



def slowdown_analysis(imagefile, intensity):
	slowdown_image = SimpleImage(imagefile)
	slowdown_image.show()
	pics_num = 0
	pics_blue = 0

	for pixel in slowdown_image:
		pics_num += 1
		if ((pixel.red + pixel.blue + pixel.green) // 3) * intensity < pixel.blue :
			pics_blue += 1

	percentage_area_slowdown = (pics_blue / pics_num) * 100
	print('Number of blue pixels are ' + str(pics_blue))
	print('Total number of Pixel are ' + str(pics_num))
	print('Percentage of area slowed down ' + str(percentage_area_slowdown) + '%')
	return percentage_area_slowdown

def recovery_analysis(imagefile, intensity):
	recovery_image = SimpleImage(imagefile)
	recovery_image.show()
	pics_num1 = 0
	pics_yellow = 0

	for pixel in recovery_image:
		pics_num1 += 1
		if pixel.red > ((pixel.blue + pixel.green) // 2) * intensity:
			pics_yellow += 1

	percentage_area_recovery = (pics_yellow / pics_num1) * 100
	print('Number of yellow pixels are ' + str(pics_yellow))
	print('Total number of Pixel are ' + str(pics_num1))
	print('Percentage of area recovered ' + str(percentage_area_recovery) + '%')
	return percentage_area_recovery


if __name__ == '__main__':
	main()
