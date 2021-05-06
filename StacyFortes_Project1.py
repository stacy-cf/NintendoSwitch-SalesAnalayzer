#Stacy Fortes 
#Python Project #1 CPS3320
#Due March 3, 2021

#used for finding the previous month 
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
'August', 'September', 'October', 'November', 'December']

#Data Set 1: total number of nintendo switch sales key: month/year, value: number of sales in MILLLIONS
nintendo_sales = {'March 2017': 1.5, 'April 2017': 2.74, 'May 2017': 3.94, 'June 2017': 5.14, 'July 2017': 6.34, 'September 2017': 7.63, 'October 2017': 8.815, 'December 2017': 10,
'March 2018': 15.5, 'April 2018': 17.79, 'May 2018': 18.56,'June 2018': 19.67, 'September 2018': 22.86, 'October 2018': 27.86, 'November 2018': 30.1,'December 2018': 32.27,
'January 2019': 33.64,'February 2019': 34.1,'March 2019': 34.74, 'June 2019': 36.87, 'July 2019': 36.21, 'August 2019': 37.2, 'September 2019': 38.75, 'October 2019': 40.74,'November 2019': 44.59,'December 2019': 49.81,
'January 2020': 50.51, 'February 2020': 51.52, 'March 2020': 53.73, 'April 2020': 55.76, 'May 2020': 57.63, 'June 2020': 59.32,'July 2020': 62.08, 'August 2020': 63.4, 'September 2020': 65.71, 'October 2020': 67.77, 'November 2020': 70.92}

#Data Set 2: most popular switch games and their respective announcement dates 
announcement_date = {'Mario Kart 8 Deluxe': 'January 2017' , 'Animal Crossing: New Horizons': 'September 2018', 
'Super Smash Bros. Ultimate': 'March 2018', 'The Legend of Zelda: Breath of the Wild': 'January 2017',
'Pokemon Sword/Shield': 'February 2019', 'Super Mario Odyssey': 'January 2017', 'Super Mario Party': 'June 2018', 
'Pokemon: Let\'s Go, Pikachu!': 'May 2018','Splatoon 2': 'January 2017', 
'New Super Mario Bros. U Deluxe': 'September 2018', 'Super Mario Makers 2': 'February 2019'} 

#Data Set 3: most popular switch games and their respective release dates 
release_date = {'Mario Kart 8 Deluxe': 'April 2017', 'Animal Crossing: New Horizons': 'March 2020', 
'Super Smash Bros. Ultimate': 'December 2018', 'The Legend of Zelda: Breath of the Wild': 'March 2017',
'Pokemon Sword/Shield': 'November 2019', 'Super Mario Odyssey': 'October 2017', 'Super Mario Party': 'October 2018', 
'Pokemon: Let\'s Go, Pikachu!': 'November 2018','Splatoon 2': 'July 2017',
'New Super Mario Bros. U Deluxe': 'January 2019', 'Super Mario Makers 2': 'June 2019'} 
#Months needed: 

#function to get the previous month and year
def getPrevMonth(monthAndYear):
	#split the month and year to refer to months list and get previous month
	monthYearSplit = monthAndYear.split(" ")
	prevMonth = " "
	year = int(monthYearSplit[1]) #convert year string into an int in order to be able to decrement

	#subtract 1 from the year if the original month is January because the previous month is in a different year 
	if monthYearSplit[0] == 'January':
		year = year - 1
	for i in range(len(months)):
		if months[i] == monthYearSplit[0]:
			#assign month equal to previous month
			prevMonth = months[i-1]
	prevMonth = prevMonth + " " + str(year)
	return str(prevMonth)

#function to calculate the total sales increase in units which correspond to announcement dates 
def announcementTotal():
	announcement_total = 0
	for key, value in announcement_date.items(): 

		#if the announcment date is January, get March numbers since the switch was not available in January
		if value == 'January 2017': 
			announcement_total += nintendo_sales.get('March 2017')

		#get the previous month and subtract its unit sales to determine the increase 
		elif value in nintendo_sales:
			previousMonth = str(getPrevMonth(value))

			while(previousMonth not in nintendo_sales):
				previousMonth = getPrevMonth(previousMonth)

			increase = (nintendo_sales.get(value) - nintendo_sales.get(previousMonth))
			announcement_total = announcement_total + increase
		else:
			print(value + " is not in nintendo_sales") #for debugging purposes 
	
	return announcement_total

#function to calculate the total sales increase in units which correspond to release dates 
def releaseTotal():
	release_total = 0
	for key, value in release_date.items():

		#if the announcment date is March, get March numbers since the switch was not available previously
		if value == 'March 2017': 
		 	release_total += nintendo_sales.get('March 2017')

		 #get the previous month and subtract its unit sales to determine the increase 
		elif value in nintendo_sales:
			previousMonth = str(getPrevMonth(value))

			while(previousMonth not in nintendo_sales):
				previousMonth = getPrevMonth(previousMonth)

			increase = (nintendo_sales.get(value) - nintendo_sales.get(previousMonth))
			release_total = release_total + increase
		else:
			print(value + " is not in release_date") #for debugging purposes 

	return release_total

#function to compare both sales totals and determine which had biggest increases
def determineWinner(totalSales_Announcement, totalSales_Release):
	winner = " "
	if totalSales_Announcement > totalSales_Release:
		winner = "Announcement Dates!"
	elif totalSales_Release > totalSales_Announcement:
		winner = "Release Dates!"
	else:
		winner = "Tie!"
	return winner


totalSales_Announcement = announcementTotal()
totalSales_Release = releaseTotal()
winner = determineWinner(totalSales_Announcement, totalSales_Release)

print("The total unit sales increase in the months of the ANNOUNCEMENT of highly anticipated games : %.2f Million Units" %(totalSales_Announcement))
print("The total unit sales increase in the months of the RELEASE of highly anticipated games : %.2f Million Units" %(totalSales_Release))
print("*** THEREFORE ***")
print("The data determined that the following caused the most sales increase in the Nintendo Switch: " + winner)
