import sys


def setcolor():
    color1 = sys.argv[1]
    color2 = sys.argv[2]
    color3 = sys.argv[3]

    # check range for input color
    if int(color1) >= 0 and int(color1) <= 255:
        print ("In range")
    else:
        color1 = "0"
        
    if int(color2) >= 0 and int(color2) <= 255:
        print ("In range")
    else:
        color2 = "0"


    if int(color3) >= 0 and int(color3) <= 255:
        print ("In range")
    else:
        color3 = "0"


    # write color in file
    output = open('color.ini', 'w')

    output.write('[COLOR]\n')
    try:
        output.write('ccolor = '+ color1 +',' + color2 + ',' + color3 +'\n')
    except:
        print ("could not write color.ini")

    print ('ccolor = '+ color1 +',' + color2 + ',' + color3 +'\n')

    output.close()

if __name__ == '__main__':
    setcolor()
