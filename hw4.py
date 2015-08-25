import math

listX = []
with open("hw4_x.txt", 'r') as f:
    for line in f:
        intX_list = [int(i) for i in line.split()]
        listX.append(intX_list)

listY = []
with open("hw4_y.txt", 'r') as r:
    for line in r:
        listY.append(int(line))

TiList = [0]*(23)
for tup in listX:
    for num in range(len(tup)):
        if tup[num] == 1:
            TiList[num] += 1

pList = [float(2)/23]*(23)
copy_p_list = [0]*(23)
iterationList = [0, 1, 2, 4, 8]
iterationListB = [16, 32, 64]

print " iteration" + " "*(19-len("iteration")) +  "mistake" + " "*(20-len(str('mistake'))) + "   likelihood" 
print "-----------" + " "*(17-len("iteration")) +  "---------" + " "*(19-len(str('mistake'))) + "-----------------" 
for a in range(257):
    mistake = 0
    for i in range(len(pList)): # i 
        tSum = 0
        for t in range(len(listY)): #loop t=1 to T
            jProduct = 1
            for j in range(len(pList)): # j 
                jProduct *= math.pow(float(1-pList[j]),listX[t][j])

            tSum += float(listY[t])*listX[t][i]*pList[i]/(1 - jProduct)
        copy_p_list[i] = float(tSum)/TiList[i]

    logSum = 0
    for t in range(len(listY)):
        yProd = 1
        for i in range(len(pList)):
            yProd *= math.pow(1-pList[i],listX[t][i])
            # print yProd
        if listY[t] == 1:
            logSum += math.log(1-yProd)
            if (1-yProd) <= .5:
                mistake += 1
        else:
            logSum += math.log(yProd)
            if (1-yProd) >= .5:
                mistake += 1

    # print logSum
    logLikelihood = logSum/len(listY)

    for i in range(len(pList)):
        pList[i] = copy_p_list[i];

    if a in iterationList:
        
        print "    "+ str(a) + " "*(26-len(str("iteration"))) +  str(mistake) + " "*(24-len(str('mistake'))) + str(logLikelihood)  

    if a in iterationListB:
        # print "iteration" + " "*(20-len("iteration")) +  "mistake" + " "*(20-len(str('mistake'))) + "likelihood" 
        # print "---------" + " "*(20-len("iteration")) +  "-------" + " "*(20-len(str('mistake'))) + "----------------" 
        print "    "+ str(a) + " "*(25-len(str("iteration"))) +  str(mistake) + " "*(24-len(str('mistake'))) + str(logLikelihood)

    if a in [128, 256]:
        print "    "+ str(a) + " "*(24-len(str("iteration"))) +  str(mistake) + " "*(24-len(str('mistake'))) + str(logLikelihood)

    if a == 256:
        print pList



