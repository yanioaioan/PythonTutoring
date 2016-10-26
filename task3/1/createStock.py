#1)create a stock.csv containing product info/stock levels etc (either manually or automatically)

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

        currentStockLevel=input("enter  the amount of products of this type currently in the stock")
        reorderLevelLimit=input("enter  the lower limit at which we should restock this product")
        targetStockLevel =input("enter  the amount of products of this type that we should have after restocking")

        productsCounter-=1
        listToIterateAndWrite.append((code,description,price,currentStockLevel,reorderLevelLimit,targetStockLevel))


    print( listToIterateAndWrite)
    #https://docs.python.org/3/library/csv.html
    #write rows one by one by iterating the listToIterateAndWrite list

    with open('stock.csv', 'w') as f:
        f.write('PCode,Ds,Pr,currentStockLevel , reorderLevelLimit, targetStockLevel\n')
    with open('stock.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerows(listToIterateAndWrite)



if __name__ == "__main__":

        createStock()
