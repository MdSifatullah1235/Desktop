cost = float(input("Enter the actual product price : "))
sales = float(input("Enter the sale amount : "))

if (sales > cost):
    amount_1 = sales - cost
    print("The profit is {} ".format(amount_1))

else:
    amount_2 = cost - sales
    print("The loss is {} ".format(amount_2))