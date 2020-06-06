costprice=float(input("enter the cost price of the product:"))
sellprice=float(input("enter the sell price of the product: "))
profit=sellprice-costprice
Newsellprice=1.05*profit+costprice
print("The profit from this sell is ",profit)
print("To increase the profit by 5% the selling price should be",Newsellprice)
