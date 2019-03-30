def caluclate_bill_amount(gems_list,price_list,reqd_gems,reqd_quantity):
    bill_amount=0
    for i in range (0,len(reqd_gems)):
        k=0
        for j in range(0,len(gems_list)):
            if (reqd_gems[i]== gems_list[j]):
                bill_amt=(bill_amount+(price_list[i]*reqd_quantity[i]))
                print bill_amt
                k=1
    return (bill_amt)
gems_list=['emerald','ruby','pearl','ivory','garnet']
price_list=[1760,2119,1559,3920,3000]
reqd_gems=['ivory','emerald','garnet']
reqd_quantity=[3,10,12]
#bill_amount=(bill_amount+(price_list[i]*reqd_quantity[i]))
#print(bill_amount)
print caluclate_bill_amount(gems_list,price_list,reqd_gems,reqd_quantity)
