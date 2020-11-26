nume=str(input(":"))
prenume=str(input(":"))
da=''
if (ord(nume[0])>=65 and ord(nume[0])<=95) and (ord(prenume[0])>=65 and ord(prenume[0])<=95):
    for x in range(1,len(nume)):
        if ord(nume[x]) not in range(97,133):
            da='NU'
        if da=='NU':
            print("Nu este nume sau caracterele nu sunt cu litera mica")
            break
    if da=='':
        print("Da este nume")
    da=''
    for x in range(1,len(prenume)):
        if ord(prenume[x]) not in range(97,133):
            da='NU'
        if da=='NU':
            print("Nu este prenume sau caracterele nu sunt cu litera mica")
            break
    if da=='':
        print("Da este prenume")
else:
    print("Nu se incepe cu litera mare")