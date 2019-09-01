sp = ' '
line = 50 * sp
x = 'X'
lineX = line[1:] + x
W = '|'
lineXW = W + lineX + W
print('Press ''a'' for LEFT, ''s'' for RIGHT, ''q'' for QUIT \n')
while True:
    V = input()
    if V == 'a':
        #left
        lineX = (lineX.find('X')-1)* sp + x + (50 - lineX.find('X')) * sp
        if len(lineX) > 50:
            lineX = x + 49 * sp
            print(W + lineX + W)
        else:
            print(W + lineX + W)
    if V == 's':
        #right
        lineX = lineX1 =  (lineX.find('X')+1)* sp + x + (48 - lineX.find('X')) * sp
        if len(lineX) > 50:
            lineX = 49 * sp + x
            print(W + lineX + W)
        else:
            print(W + lineX + W)
    if V == 'q':
        break
