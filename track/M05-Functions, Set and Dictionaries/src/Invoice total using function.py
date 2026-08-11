def invoice_total(price, quantity):
    total = price * quantity
    return total
    pass

# price = int(input())
# quantity = int(input())

print(f"Total: {(invoice_total(100, 2))}")

#total = price * quantity is stored in invoice_total(price, quantity) and when it is called, it is returned and printed

#print(f"Total: {(invoice_total(price,quantity))}") can be written as 
# x = invoice_total(price,quantity)
# print(f"Total: {x}") 