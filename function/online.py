def calculatebill(customername, discount, *items):

    if len(items) == 0:
        items = (100, 200, 300,500,400)

    total = sum(items)
    discountamount = total * discount / 100
    finalamount = total - discountamount

    print(f"Customer Name: {customername}")
    print(f"Items: {items}")
    print(f"Total Amount: {total}")
    print(f"Discount Amount: {discountamount}")
    print(f"Final Amount: {finalamount}")



name = input("Enter customer name: ")
discount = float(input("Enter discount %: "))

calculatebill(name, discount)