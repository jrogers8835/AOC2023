from D03.inputData import inputObj

def fillSquareArray(rows,cols,graph,val):
    for r in range(rows):
        graph.append([])
        for c in range(cols):
            graph[r].append(val)

def evalBase(graph, minMaskR, maxMaskR, minMaskC, maxMaskC, key):
    for r in range(1,len(inputObj)):
        for c in range(1,len(inputObj[r])):
            if inputObj[r][c] in key:
                for dr in range(r+minMaskR,r+maxMaskR):
                    for dc in range(c+minMaskC,c+maxMaskC):
                        if inputObj[dr][dc].isdigit():
                            graph[dr][dc]=True


def eval(graph, minMaskR, maxMaskR, minMaskC, maxMaskC, key):
    deltaFound = False
    for r in range(1,len(inputObj)):
        for c in range(1,len(inputObj[r])):
            if graph[r][c]:
                for dr in range(r+minMaskR,r+maxMaskR):
                    for dc in range(c+minMaskC,c+maxMaskC):
                        if inputObj[dr][dc] in key:
                            if not graph[dr][dc]:
                                deltaFound = True
                            graph[dr][dc]=True
    return deltaFound

def runPart1():
    includeGraph = []
    fillSquareArray(len(inputObj), len(inputObj[0]), includeGraph, False)
    evalBase(includeGraph, -1, 2, -1, 2, '*@/+=%#&-$')
    while True:
        if not eval(includeGraph, 0, 1, -1, 2, '0123456789'):
            break

    for r in range(len(includeGraph)):
        for c in range(len(includeGraph[r])):
            if not inputObj[r][c].isdigit():
                includeGraph[r][c] = False

    total = 0
    for r in range(len(includeGraph)):
        subtotal = ''
        appending = False
        for c in range(len(includeGraph[r])):
            if includeGraph[r][c]:
                if not appending:
                    subtotal = ''
                appending = True
                subtotal += inputObj[r][c]
            elif appending:
                total += int(subtotal)
                appending = False
    print(total)

def evalGear(gr,gc):
    key = '0123456789'
    vals = []
    for a in range(gr-1,gr+2):
        for b in range(gc-1,gc+2):
            vals.append(0 if inputObj[a][b] not in key else 1)
    count=0
    if vals[0]==1 and vals[1]==0 and vals[2]==1:
        count+=2
    elif vals[0] == vals[1] == vals[2] == 0:
        count+=0
    else:
        count+=1

    if vals[6]==1 and vals[7]==0 and vals[8]==1:
        count+=2
    elif vals[6] == vals[7] == vals[8] == 0:
        count+=0
    else:
        count+=1

    if vals[3]==1:
        count+=1

    if vals[5]==1:
        count+=1

    return count==2


def runPart2():
    gearX=[]
    gearY=[]
    for r in range(1,len(inputObj)):
        for c in range(1,len(inputObj[r])):
            if inputObj[r][c]=='*':
                gearX.append(c)
                gearY.append(r)

    includeGraph = []
    fillSquareArray(len(inputObj), len(inputObj[0]), includeGraph, False)
    for v in range(len(gearY)):
        if evalGear(gearY[v],gearX[v]):
            includeGraph[gearY[v]][gearX[v]]=True
            list1 = list(inputObj[gearY[v]])
            list1[gearX[v]]='~'
            inputObj[gearY[v]]=''.join(list1)

    evalBase(includeGraph, -1, 2, -1, 2, '~')

    while True:
        if not eval(includeGraph, 0, 1, -1, 2, '0123456789'):
            break

    for r in range(len(includeGraph)):
        for c in range(len(includeGraph[r])):
            if not inputObj[r][c].isdigit():
                includeGraph[r][c] = False

    total = 0
    for r in range(len(includeGraph)):
        subtotal = ''
        appending = False
        for c in range(len(includeGraph[r])):
            if includeGraph[r][c]:
                if not appending:
                    subtotal = ''
                appending = True
                subtotal += inputObj[r][c]
            elif appending:
                total += int(subtotal)
                appending = False
    print(total)
    print('done')

def run(part):
    if part == 2:
        runPart2()
    else:
        runPart1()
