def bonAppetit(bill, k, b):
    # Write your code here
    bactual = (sum(bill)- bill[k])//2
    if b == bactual:
        print ("Bon Appetit")
    else:
        print( bill[k]//2 )
