import pandas as pd
import copy
import openpyxl as pxl


def printTable(tab):
    for key, item in tab.items():
        print(key)
        for i, k in item.items():
            print("{}\t{}".format(i, k))
        print("\n")


def createNodeFromText(fileName):
    file = open(fileName)
    information = file.readlines()
    information = [element.strip() for element in information]

    nodes = information[0].split()
    nodeInformation = {}
    tempNodeInformation = {}
    flag = 1
    while flag < len(information):
        tempNodeList = information[flag].split()
        tempWeightList = information[flag + 1].split()
        node = tempNodeList[0]
        i = 1
        while i <= len(tempWeightList):
            tempNodeInformation.update({tempNodeList[i]: int(tempWeightList[i - 1])})
            i += 1
        nodeInformation.update({node: tempNodeInformation})
        tempNodeInformation = {}
        flag += 2
    return (nodes, nodeInformation)


def createTable(fileName):
    file = open(fileName)
    information = [element.strip() for element in file.readlines()]
    table = {}
    temp = {}
    emptytable = {}
    emptytemptable = {}
    line = 0
    while line < len(information):
        temp1 = information[line].split()
        temp2 = information[line + 1].split()
        node = temp1[0]
        i = 1
        while i < len(temp1):
            temp.update({temp1[i]: int(temp2[i - 1])})
            emptytemptable.update({temp1[i]: 10000})
            i += 1
        table.update({node: temp})
        emptytable.update({node: emptytemptable})
        temp = {}
        emptytemptable = {}
        line += 2
    return (table, emptytable)


def createManualTable(nodeInfo, node):
    table = {}
    emtab = {}
    tempNode = {}
    emptem = {}
    for item in node:
        nodeOfTable = nodeInfo[item].keys()
        for item1 in node:
            if item1 == item:
                tempNode.update({item1: 0})
            elif item1 in nodeOfTable:
                tempNode.update({item1: nodeInfo[item][item1]})
            else:
                tempNode.update({item1: 10000})
            emptem.update({item1: 10000})
        table.update({item: tempNode})
        emtab.update({item: emptem})
        tempNode = {}
        emptem = {}
    return (table, emtab)


def printTable(table):
    for keys, item in table.items():
        for value in item.values():
            if value == 900:
                print("-", end="\t")
            else:
                print(value, end="\t")
        print("")


def createExcel():
    excel_book = pxl.load_workbook('test.xlsx')
    with pd.ExcelWriter('test.xlsx', engine='openpyxl') as writer:
        writer.book = excel_book
        writer.sheets = {
            worksheet.title: worksheet
            for worksheet in excel_book.worksheets
        }
        secondMockDF = pd.DataFrame(table)
        secondMockDF.to_excel(writer, 'iteration{}'.format(iteration), index=False)
        writer.save()
def printIteration(temp):
    for i in temp.keys():
        t=copy.deepcopy(temp)
        t[i].update(table[i])
        print("**{}**".format(i))
        print(pd.DataFrame.from_dict(t, orient='index'))
        print("\n")




#key = A,B,C,D,E,F....
def findOptimal(tableVer,keys,vertex,tempInfo):
    minVal= tableVer[keys]
    temp=minVal
    result="min"
    output="min{{"
    for index,element in nodeInfo[vertex].items():
        result=result+"{{C({},{})+D{}({})+".format(vertex,index,index,keys)
        output=output+"({}+{}),".format(element,table[index][keys])
        if element+tempInfo[index][keys]<minVal:
            minVal=element+tempInfo[index][keys]
        result+=","
    output+="}}"
    result+="}}"

    #print(pd.DataFrame.from_dict(table, orient='index'))
    if minVal!=temp:
        print("from {} to {}".format(vertex,keys))
        print(result)
        print(output)
        print("{}".format(minVal))
        print("\n")
    return minVal
def routingTable(c):
    temp=copy.deepcopy(table)

    print("-------------------{}-------------------".format(c))
    for index in range(len(node)):

        vertex=node[index]
        tableVer=table[vertex] #dictionary
        #print("--------------{}------------".format(vertex))
        for keys,value in tableVer.items():
            tableVer[keys]=findOptimal(tableVer,keys,vertex,temp)
    #printIteration(temp)
node,nodeInfo=createNodeFromText("graph.txt")
#table=createTable("table.txt")
table,empty=createManualTable(nodeInfo,node)
print("-------------------0-------------------")
printIteration(empty)


def execute(iteration):
    routingTable(iteration)
    df=pd.DataFrame.from_dict(table, orient='index')
    createExcel()

iteration=0
createExcel()

for i in range(18):
    iteration+=1
    temp=execute(iteration)