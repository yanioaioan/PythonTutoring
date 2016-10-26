#4)create a program 'restock_ExecuteOrders.py' that parses and executes the orders from 'restockOrders.csv' so as to update the stock.csv


import csv

######################################################################################################
#re-read csv
r = csv.reader(open('restockOrders.csv'),delimiter=',') # Here your csv file
#lines will contain all rows of r
restocklines = [l for l in r]
print(restocklines)

s = csv.reader(open('stock.csv'),delimiter=',') # Here your csv file
#lines will contain all rows of r
stocklines = [l for l in s]
print(stocklines)
######################################################################################################

######################################################################################################
#Grab rows/columns of restockOrders.csv
restockrows=len(restocklines)
restockcolumns=len(restocklines[0])
print("restockrows="+str(restockrows))
print("restock columns="+str(restockcolumns))

#Grab rows/columns of stock.csv
stockrows=len(stocklines)
stockcolumns=len(stocklines[0])
print("stockrows="+str(stockrows))
print("columns="+str(stockcolumns))
######################################################################################################

######################################################################################################

#for each of the rows of restockOrders.csv..look up every row of stock.csv
#(the 1st column of the restockOrders.csv always need to match the product code of the stock.csv)
#(the 2nd column is just going to update the 4th column (currentStockLevel) of the stock.csv)

#for each row of restockOrders.csv
for rr in range(restockrows):
    #for each row of stock.csv
    for sr in range(stockrows):

        #skip the first row of stock.csv
        if sr!=0:
            ##if the product codes match 00000001 == 00000001
            if (restocklines[rr][0])==(stocklines[sr][0]):

                #here we update/increase the amount of the currentStockLevel by "targetStockLevel"

                print ("line to update in stock.csv file: "+str(stocklines[sr]))

                #update stocklines 4th column (currentStockLevel) based on the 2nd column of restockOrders.csv (amount of products to add to reach 'targetStockLevel')

                sum = int(stocklines[sr][3]) + int(restocklines[rr][1])
                stocklines[sr][3] = str(sum)

                #print ("line became="+str(lines[r]))


##################################################################################################################################################

#Now we are finished buying So we might as well update/ovewrite our stock file
###Update the contents of the already opened file 'ifile'
#read file
#change file in memory
#write out file (overwriting existing file)


print ('NOW update the actual update/overwrite of the stock.csv file ')

overWriteFilewriterofile  = open('stock.csv', "w")
overWriteFilewriter = csv.writer(overWriteFilewriterofile, delimiter=',')
#write all the orderList at once after we have read them and modified them
overWriteFilewriter.writerows(stocklines)
overWriteFilewriterofile.close()

