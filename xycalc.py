class xycalculator:

    def newycalculator(self ,dyorg, dxorg, x, y, newy):
        m = float(dyorg / dxorg)

        newx = x + (1 / m) * (newy - y)
        print(newx, newy)





    def newxcalculator(self ,dyorg, dxorg, x, y, newx ):
        m = float(dyorg / dxorg)
        #print(m)

        newy = y + m * (newx - x)
        print(newx, newy)

