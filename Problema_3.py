n=str(input(':'))
spatiu=" "
sp="  "
if len(n)<=50:
    for k in range(1,len(n)//2+1):
        print(sp+n[k:-k])
        sp+=spatiu