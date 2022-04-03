def midPoint(X1, Y1, X2, Y2):
    # calculate dx & dy
    dx = X2 - X1
    dy = Y2 - Y1

    # initial value of decision parameter d
    d = dy - (dx / 2)
    x = X1
    y = Y1
    f=d*2

    # Plot initial given point
    # putpixel(x,y) can be used to print pixel
    # of line in graphics
    print(x, ",", y,",","d=",f, "\n")
    # iterate through value of X
    while (x < X2):
        x = x + 1
        # E or East is chosen
        if (d < 0):
            d = d + dy
            ch = 'choose E'

            # NE or North East is chosen
        else:
            d = d + (dy - dx)
            y = y + 1
            ch = 'choose NE'

        # Plot intermediate points
        # putpixel(x,y) is used to print pixel
        # of line in graphics
        k = d*2
        print(x, ",", y,", d=",k,ch, "\n")

    # Driver program


if __name__ == '__main__':

    X1 = input('Enter x1')
    X1= int(X1)
    Y1 = input('Enter y1')
    Y1 = int(Y1)
    X2 = input('Enter x2')
    X2 = int(X2)
    Y2 = input('Enter y2')
    Y2 = int(Y2)
    midPoint(X1, Y1, X2, Y2)

