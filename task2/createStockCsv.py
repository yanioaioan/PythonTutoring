'''
Create a suitable text file to use with a high-level programming language containing a list of product
details, including a GTIN-8 product code, a product description and price.
'''

import csv

def createStock():
    print( 'STOCK OVERWRITE')
    #code=input("enter  GTIN-8 product code")
    #description=raw_input("enter product description ")
    #price=raw_input("enter price")

    productsCounter=input("How many product codes would you want to add to the csv database?")
    listToIterateAndWrite=[]
    while productsCounter > 0:
        code=raw_input("enter  GTIN-8 product code")
        description=raw_input("enter product description ")
        price=raw_input("enter price")
        productsCounter=productsCounter-1
        listToIterateAndWrite.append( (code,description,price) )


    print( listToIterateAndWrite)
    #https://docs.python.org/3/library/csv.html
    #write rows one by one by iterating the listToIterateAndWrite list
    with open('stock.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(listToIterateAndWrite)



if __name__ == "__main__":

    #function call to create the stock if chosen to do so
    createStockInput=raw_input("Would you like to create new stock csv file?")

    if createStockInput == 'y':

        createStock()

    elif createStockInput=='n':


        continueShopingUserInput='n'

        #read csv once before the while loop in lines
        r = csv.reader(open('stock.csv')) # Here your csv file
        lines = [l for l in r]

        productsPurchased=[]

        totalOrderSum=0

        while continueShopingUserInput != 'y':
            print( '\n..NOW..\n')
            code=raw_input('enter  GTIN-8 product code of product to buy')
            quantity=input('how many of the '+str(code)+' you would like to buy?')


            #check if product code exists or not and inform the user

            '''Iterate throught the file and find if product code is in the csv'''
            rows=len(lines)
            columns=len(lines[0])
            print( "rows="+str(rows))
            print( "columns="+str(columns))

            #a couple variable initializations
            #initialize 'found' product flag to zero
            found=False
            #initialize 'productSelected' flag to zero
            productSelected=0

            for r in range(rows):
                #r goes from 0 to 1
                for c in range(columns):
                    #c goes from 0 to 1

                    #if we are checking 1st element AND the code entered matches, then the item exists in our csv file
                    if c==0:

                        #print( (lines[r][c])==(code) )

                        #CHECK IF 'code' ENTERED BY THE USER MATCHES ONE OF THE stock.csv ROWS
                        if (lines[r][c])==(code):
                            print( "lines matched="+str(lines[r]) )
                            print( lines[r][c] )
                            print( 'code '+str(code)+': found as a product code in the csv' )

                            #flag the 'found' variable to true,
                            #to indicate the if statement at line 84 was TRUE
                            #(practically this means that the code from the user input
                            #matches one of the lines at our stock.csv file)

                            found=True

                            #store row of the product match
                            productSelected=lines[r]

                            #break out of the inner for loop: (line 76) 'for c in range(columns):'
                            break;


                if found==True:
                    #break out of the outter for loop: (line 74) 'for r in range(rows):'
                    #and continue executing code from line 109 onwards
                    break;

            #if code from the user input not found in our stock.csv, then inform the user
            if found!=True:
                print( 'NO SUCH PRODUCT CODE EXISTS IN THE CSV' )
            else:
                #otherwise append to the productsPurchased list,
                #the 'productSelected' which contains the row from the stocks.csv file that matched the user input
                productsPurchased.append( (productSelected[0], productSelected[1], quantity, productSelected[2], quantity*int(productSelected[2]) ) )

                #sum the total cost so far
                totalOrderSum=totalOrderSum+quantity*int(productSelected[2])


            #ask the user if wants to continue shopping or not
            continueShopingUserInput=raw_input('are you done bying stuff products? (y/n)')

        #while loop ends
        #now print the receipt


        with open('receipt.csv', 'w') as f:
            f.write('PCode,Ds,Pr,Qnt,,Total\n')

        with open('receipt.csv', 'a') as f:
            writer2 = csv.writer(f, delimiter=",")
            writer2.writerows(productsPurchased)

        with open('receipt.csv', 'a') as f:
            writer2 = csv.writer(f)#, delimiter=":" not needed
            f.write('Total Cost of Order,,,,, '+str(totalOrderSum))

    else:
        print('unrecognised input')



