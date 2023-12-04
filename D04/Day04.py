from D04.inputData import inputObj


def run():
    total = 0
    b = {}
    for i in range(len(inputObj)):
        b[i+1]=1
    for cidx, card in enumerate(inputObj):
        cardPart = list(map(lambda d : list(filter(lambda x: x != '', d.strip().split(" "))), card[9:].split('|')))
        p = len(list(filter(lambda d : d in cardPart[0],cardPart[1])))
        for i in range(cidx+2,min((cidx+p)+2,len(inputObj))):
            b[i]=b[i]+b[cidx+1]
        # total += 0 if p == 0 else 2**(p-1)
    for key in b:
        total+=b[key]
    print(total)