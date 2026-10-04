import csv

totalinvoices=0
invoices_over100k=0
invoices_invalidamount=0
with open('Data/homework_invoices.csv',mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        totalinvoices+=1
        print(f'Vendor: {row["vendor"]}, Amount: {row["amount"]}, Status: {row["status"]}')
        try:
            invoice_amout=float(row['amount'])
        except ValueError:
            print(f"Error: Invalid value for amount, but got {row['amount']}")
            invoices_invalidamount+=1
            if invoice_amout>100000:
                print(f'Invoice amount {invoice_amout} is greater than 100,000')
                invoices_over100k+=1
print(f'Total invoices: {totalinvoices}')
print(f'Total invoices with amount greater than 100,000: {invoices_over100k}')
print(f'Total invoices with invalid amount:{invoices_invalidamount}')