cuvant=str(input(":"))
litera=str(input(":"))
for x in range(0,len(cuvant)):
    print(f'{cuvant[:x]}{litera}{cuvant[x+1:]}')