from D05.Node import Node
from D05.inputData import inputObj


def process(name, val, nodes):
    for n in nodes[name]:
        if n.is_in_range(val):
            return n.get_child(), n.convert(val)
    return nodes[name][0].get_child(), val


def run_process(name, val, nodes):
    while name != 'location':
        [name, val] = process(name, val, nodes)
    return val

def run():
    nodes = {}
    for m in inputObj:
        if m == "seeds":
            continue
        names = m.split('-to-')
        if names[0] not in nodes:
            nodes[names[0]] = []
        for data in inputObj[m]:
            nodes[names[0]].append(Node(names[0], names[1], data[0], data[1], data[2]))
    minLoc = 9_999_999_999_999
    for idx,x in enumerate(inputObj['seeds']):
        print(idx)
        if idx%2==0:
            for seed in range(x,inputObj['seeds'][idx+1]+x+1):
                v = run_process('seeds',seed,nodes)
                minLoc = v if v<minLoc else minLoc

    print(minLoc)
