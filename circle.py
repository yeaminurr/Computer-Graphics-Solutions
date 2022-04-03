def circle(x,y, r):
    # calculate dx & dy
    x1 = x
    y1= y


    # initial value of decision parameter d
    d = 1-r
    x = 0
    y = r

    # Plot initial given point
    # putpixel(x,y) can be used to print pixel
    # of line in graphics
    print(x+x1, ",", y+y1,",","d=",d, "\n")
    # iterate through value of X
    while (x < y):


        # E or East is chosen
        if (d < 0):
            d = d + 2* x + 3
            ch = 'choose E'
            x = x + 1


            # NE or North East is chosen
        else:
            d = d + 2*x - 2*y + 5
            ch = 'choose SE'
            x = x + 1
            y = y - 1


        # Plot intermediate points
        # putpixel(x,y) is used to print pixel
        # of line in graphics
        if(x>y):
            print(x + x1, ",", y + y1, "End")
            break


        print(x+x1, ",", y+y1,", d=",d,ch, "\n")

    # Driver program


if __name__ == '__main__':

    X = input('Enter x')
    X= int(X)
    Y = input('Enter y')
    Y = int(Y)
    R = input('Enter Radius')
    R = int(R)
    circle(X, Y, R)

