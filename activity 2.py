a=float(input('Enter the real product price: '))
b=float(input('Enter the Sale amount: '))
if b>a:
    profit=b-a
    print('Profit: ',profit)
else:
    print('No Profit!!!')