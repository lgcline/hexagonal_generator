"""
Hexagonal slice plotter rev1
"""

"""
vertexmap = {
	0:(-1,0),
	1:(0,1),
	2:(1,0),
	3:(1,0),
"""	
	
def plot(sheetVert, sheetLayers, name):
	out= open (name + "_automated.txt", 'w')
	totalVerts = sheetVert - 1	#start numbering at 0 rather than 1
	plottingLayer = 1	#layer being plotted
	layerVerts = 5 #verts in current layer, starting at 0
	wrapChange = 3 #see calculator for information
	xcoord = 0	#x coordinate
	ycoord = 0	#y coordinate
	vertNum = 0 #vertex number
	alternate = 0
	
	while plottingLayer <= sheetLayers:
		if plottingLayer == 1:
			out.write(str(vertNum) + "	" + str(xcoord) + "	" + str(ycoord) + "	" + str(plottingLayer)+"\n")
			if vertNum == 0:
				xcoord -= 1
			elif vertNum == 1:
				ycoord += 1
			elif vertNum == 2:
				xcoord += 1
			elif vertNum == 3:
				xcoord += 1
			elif vertNum == 4:
				ycoord -= 1
			elif vertNum == 5:
				xcoord += 1
				plottingLayer += 1
			vertNum += 1		
		else:
			layerVerts += (wrapChange * 6)
			stepCount = 1	#steps completed in layer
			plotted = 0	#steps plotted in previous sides
			angle = 135
			
			while vertNum <= layerVerts:
				#alternate = 0
				out.write(str(vertNum) + "	" + str(xcoord) + "	" + str(ycoord) + " "+ str(plottingLayer)+ "	" + str(angle)+"\n")
				if angle == 135:	#135 deg
					if alternate == 0:
						ycoord -= 1
						alternate = 1
					elif alternate == 1	:
						alternate = 0
						xcoord -= 1
					if stepCount == ((plottingLayer - 1)):
						if alternate == 0:
							xcoord += 1
						else:
							alternate = 0
						plotted += (plottingLayer - 1)
						angle = 180
				elif angle == 180:	#180 deg
					xcoord -= 1
					if (stepCount) == ((2*plottingLayer) + plotted):
						plotted += (2*plottingLayer)
						angle = 225
				elif angle == 225:	#225 deg
					if alternate == 0:
						ycoord += 1
						alternate = 1
					elif alternate == 1:	
						xcoord -= 1
						alternate = 0
					if (stepCount) == ((plottingLayer - 1) + plotted):
						alternate = 0
						plotted += (plottingLayer - 1)
						angle = 315
				elif angle == 315:	#315 deg
					if alternate == 0:
						ycoord += 1
						alternate = 1
					elif alternate == 1:	
						xcoord += 1
						alternate = 0
					if (stepCount) == ((plottingLayer - 1) + plotted):
						#if alternate==1
							#ycoord += 1
						altenate = 0						
						plotted += (plottingLayer - 1)
						angle = 0
				elif angle == 0:	#0 deg
					xcoord += 1
					if stepCount == ((2 * plottingLayer) + plotted):
						plotted += (2 * plottingLayer)
						angle = 45
				elif angle == 45:	#45 deg
					if alternate == 0:
						ycoord -= 1
						alternate = 1
					elif alternate == 1:	
						xcoord += 1	
						alternate = 0
					if (stepCount) == (plottingLayer + plotted):
						alternate = 0
						plotted = 0
						stepCount = 0
						angle = 135
						verNum=layerVerts
				stepCount += 1
				vertNum += 1
			plottingLayer += 1
			wrapChange += 2