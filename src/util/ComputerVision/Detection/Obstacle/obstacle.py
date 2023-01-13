    # scan top to bottom, left to right and compute the 'width' of each black stripe.
# if its too narrow - being < 0.45 times the row number then turn it to white - thus cancelling it as a navigable area
# the factor was computed in excel and represents a trapezium - narrow at the top (far away), wide at the bottom (up close)
# (1st plan) the furthest acceptable area is our target - we need, eventually, a bearing to stear
import cv2

factor = 0.45
targetArea = [maxRow, minCol, maxCol]  # thats row, start-col, end-col
for row in range((minRow + 2), (maxRow - 2), 1):      
    minWidthForRow = max(int(row*factor), 40) # dont accept stupid widths - in infinite distance its the eye of a needle
    inClearSpace = 0
    widthCount = 0
    startCol = minCol
    endCol = maxCol
    for col in range (minCol, maxCol, 1):  #for the width of image array
        if inClearSpace == 0 :
            if NavigableArea[row, col] == Grayscale_black:   #check to see if the pixel is black(0) which indicates start of clear-space
                inClearSpace = 1                             # turn counting mode on
                startCol = col                               # remember where it started
        else:                                                # in inClearSpace 
            if NavigableArea[row, col] != Grayscale_black:   # if the next pixel has gone to white we are the end of the clearspace
                endCol = col                                 #so see if it was wide enough
                if (endCol - startCol) <= minWidthForRow :   # too narrow so zap it 
                    NavigableArea[row, startCol:endCol] = Grayscale_white
                else:                                       # else: leave it alone its valid, see if its our best guess yet
                    if row < targetArea [0] :
                        targetArea [0] = row
                        targetArea [1] = startCol
                        targetArea [2] = endCol
                    elif row == targetArea [0] and ((endCol - startCol) > (targetArea [2] - targetArea [1] )) : # same row but wider target
                        targetArea [1] = startCol
                        targetArea [2] = endCol
                inClearSpace = 0                             # regardless, say we are out of ClearSpace
# If we found something draw a line from middle of target to 'base' to prove which way we are going
if targetArea [0] != maxRow:  # not its start value
    # I think lines use x,y - backwards from the row,col we have been using ie x=col and y=row
    NavigableAreaColor = cv2.cvtColor(NavigableArea,cv2.COLOR_GRAY2BGR)
    fromx = int(targetArea[1] + ((targetArea[2] - targetArea[1]) / 2))  # start col + half width
    fromy = int(targetArea [0])
    tox = int(maxCol / 2)        # middle of the array
    toy = int(maxRow)            # last line
    cv2.line(NavigableAreaColor, (fromx, fromy), (tox, toy), (0,0,255),2)
    #                              From           to        colour   thichness
# show result
tempNavigableArea2 = NavigableArea.copy()
cv2.imshow('Win 4-4', tempNavigableArea2)
cv2.imshow('Win 4-5', NavigableAreaColor)