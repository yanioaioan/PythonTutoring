#2)create a program that executes essentially brings down the stock levels (sell/buy) (optional)
# Updates the stocks file


import csv



#re-read csv
r = csv.reader(open('stock.csv'),delimiter=',') # Here your csv file
#lines will contain all rows of r
lines = [l for l in r]
print(lines)


'''Iterate through the file'''

#Grab the dimensions (rows, columns) of the stock.csv
rows=len(lines)
columns=len(lines[0])
print("rows="+str(rows))
print("columns="+str(columns))

continueBuying='y'


while (continueBuying == 'y'):

    pcodeSelectedToBuy=raw_input("which product would you like to buy (GTIN-8 product code)")
    quantity=input('how many of the '+str(pcodeSelectedToBuy)+' you would like to buy?')


    '''update csv file (update the 2nd elements)'''

    #start iterating rows of stock.csv
    for r in range(rows):
    #r goes from 0 to ..column number

        #make sure we skip the first line (as we only have titles and NOT actual data values)
        if r!=0:
            
            for c in range(columns):
                
		#c goes from 0 to ..column number
                if c==3:#talking about the 4th column element that contains the currentStockLevel in our csv file

		    #grab the product code of the current row we 're at from stock.csv
                    productCodeofCurrentRow=lines[r][0]

		    #check if this matces what the user selected to buy
                    if (productCodeofCurrentRow)==(pcodeSelectedToBuy):
                        
			#here we reduce the amount of the currentStockLevel by "quantity" (subtractic quantity from currentStockLevel in the stock.csv)

                        print ("line was="+str(lines[r]))

                        lines[r][c] = str( int(lines[r][c])-quantity )
                        
			print ("line became="+str(lines[r]))

    #ask the user if wants to continue buying stuff 
    continueBuying=raw_input("would you like to continue bying products (y/n)")

##################################################################################################################################################

#Now we are finished buying So we might as well update/ovewrite our stock file
###Update the contents of the already opened file 'ifile'
#read file
#change file in memory
#write out file (overwriting existing file)


print ('NOW update the actual update/overwrite of the stock.csv file ')

overWriteFilewriterofile  = open('stock.csv', "w")
overWriteFilewriter = csv.writer(overWriteFilewriterofile, delimiter=',')
#write all the lines at once after we have read them and modified them
overWriteFilewriter.writerows(lines)
overWriteFilewriterofile.close()

