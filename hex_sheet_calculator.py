"""
Hexagonal Sheet Generator
"""

#declare global variables
layers = 0
numVertices = 0

def calculator(numBases, sheetThickness): #calculate hex parameters
	#computed values
	global numVertices
	numVertices=numBases/sheetThickness	#maximum number of verticies
	numRemainder=numBases-(numVertices*sheetThickness)	#number of bases unused at this step

	#calculate number of wraps in hexagon
	vertUnarranged=numVertices	#verticies not yet accounted for
	global layers
	layers=0	#layers (wraps) in design
	wrapChange=1 #1/6 of helices in current layer

	while (vertUnarranged / (wrapChange * 6)) >= 1:
		layers+=1
		vertUnarranged = vertUnarranged - (wrapChange*6)
		wrapChange+=2

	width=layers*2
	numRemainder += (vertUnarranged * sheetThickness)	#adjust remaining to reflect extra helices

	#output sheet data
	print "Hexagonal scaffold information:"
	print " Number of verticies: " + str(numVertices-vertUnarranged)
	print " Leftover bases: " + str(numRemainder)
	print " Distance across corners: " + str((width * 2) + ((width-1)*2)) + " nm"
	
#return values
def verts():
	return numVertices
def layer():
	return layers
