#from bitcode import newycalculator
from xycalc import xycalculator
#dx = input("Enter Diagonal corner xmin ")
dx= -108
dx = float(dx)
#dy = input("Enter Diagonal corner ymin ")
dy = -171
dy = float(dy)

#dx1 = input("Enter Diagonal corner xmax ")
dx1 = 295
dx1 = float(dx1)

#dy1 = input("Enter Diagonal corner ymax ")
dy1 = 110
dy1 = float(dy1)
x = input("enter x of the line you want to clip")
x= float(x)
y= input("enter y of the line you want to clip")
y= float(y)
ab = xycalculator()
arekx = input("enter another value x")
arekx = float(arekx)
areky = input("enter another value y")
areky = float(areky)
dxorg = float(arekx - x)
dyorg = float(areky - y)
inp = input("for which coordinate you want to calculate bitcode")
inp = int(inp)

if (inp == 1 or inp ==3):
        outcode = ""
        if y > dy1:
                outcode = outcode + "1"
                newy = dy1
                # ab.newycalculator(dyorg, dxorg, x, y, newy)

        else:
                outcode = outcode + "0"
        if y < dy:
                outcode = outcode + "1"
                newy = dy
                #ab.newycalculator(dyorg, dxorg, x, y, newy)

        else:
                outcode = outcode + "0"
        if x > dx1:

                outcode = outcode + "1"
                newx = dx1

                #ab.newxcalculator(dyorg, dxorg, x, y, newx)
        else:
                outcode = outcode + "0"
        if x < dx:

                outcode = outcode + "1"
                newx = dx

                #ab.newxcalculator(dyorg, dxorg, x, y, newx)
        else:
                outcode = outcode + '0'
        print('for x1y1',outcode)
if(inp == 2 or inp ==3 ):
        outcode = ""
        if areky > dy1:
                outcode = outcode + "1"
                newy = dy1
                #ab.newycalculator(dyorg, dxorg, arekx, areky, newy)

        else:
                outcode = outcode + "0"
        if areky < dy:
                outcode = outcode + "1"
                newy = dy
                #ab.newycalculator(dyorg, dxorg, arekx, areky, newy)

        else:
                outcode = outcode + "0"
        if arekx > dx1:

                outcode = outcode + "1"
                newx = dx1

                #ab.newxcalculator(dyorg, dxorg, arekx, areky, newx)
        else:
                outcode = outcode + "0"
        if arekx < dx:

                outcode = outcode + "1"
                newx = dx

                #ab.newxcalculator(dyorg, dxorg, arekx, areky, newx)
        else:
                outcode = outcode + '0'
        print('for x2y2',outcode)





