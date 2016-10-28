#3)create a program 'checkStockAndCreateOrders.py' that checks stock levels (reads to stock.csv at any stage),
#  and creates a file to re-stock orders so as to top up stock (called restockOrders.csv)
'''
The program should, when instructed to do so, calculate which products are out
of stock or below the re-order level and create a file. This file will contain orders for re-stocking that will
bring the current stock level of these products up to the target stock level.

The output of this program should/could be a csv file containing orders. ex. restockOrders.csv

Then these orders (restockOrders.csv) could be parsed and executed so as for the restocking to be completed
'''



import csv


#re-read csv
r = csv.reader(open('stock.csv'),delimiter=',') # Here your csv file
#lines will contain all rows of r
lines = [l for l in r]
print(lines)


'''Iterate throught the file'''
rows=len(lines)
columns=len(lines[0])
print("rows="+str(rows))
print("columns="+str(columns))

#this list is going to contain what orders need to be executed from restock_ExecuteOrders.py
orderList=[]

#start iterating rows to check if the 'stocks.csv' file and create 'restockOrders.csv' out of it
#for each row..if the 4th column < 5th column ..update the 4th to match the number specifies in the 6th column (targetStockLevel)
for r in range(rows):

    #make sure we skip the first line as we only have titles and NOT actual data values
    if r!=0:

        ##if the 4th column < 5th column
        if int(lines[r][3]) <= int(lines[r][4]) :

            #print '(%s)<=(%s)'%(lines[r][3],lines[r][4])
            #here we sum the amount  to add to the currentStockLevel to reach "targetStockLevel"

            amountToAdd = ( int(lines[r][5]) - int(lines[r][3]) )

            #append order (save productCode & amount of products to update this product with)
            orderList.append( ( lines[r][0] ,amountToAdd) )

##################################################################################################################################################

#Now we are finished buying So we might as well update/ovewrite our stock file
###Update the contents of the already opened file 'ifile'
#read file
#change file in memory
#write out file (overwriting existing file)


print ('NOW create the restockOrders.csv file to contain the orders to process for restocking at the next step ')

overWriteFilewriterofile  = open('restockOrders.csv', "w")
overWriteFilewriter = csv.writer(overWriteFilewriterofile, delimiter=',')
#write all the orderList at once after we have read them and modified them
overWriteFilewriter.writerows(orderList)
overWriteFilewriterofile.close()

