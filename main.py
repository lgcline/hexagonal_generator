"""
Main Generator Program
"""

#inputs (maybe make a GUI for this in the future?)
numBases=51400	#bases in scaffold
sheetThickness=29  #average thickness
name = "hex_automation_test"
#outTry=open("C:\Users\Leighton Cline\Documents\cadnano drawings\Sheet Generator\pythonSucks.txt",'w')
#outTry.write("fuck this")

#hexagonal sheet generation, kick an if-elsif in here when you add square
import hex_sheet_calculator
import hex_sheet_plotter

#get values from calculator
hexcalc=hex_sheet_calculator
hexcalc.calculator(numBases, sheetThickness)
sheetLayers = hexcalc.layer()
sheetVert = hexcalc.verts()

#run the slice plotter to get a 2D layout
hexplot = hex_sheet_plotter
hexplot.plot(sheetVert, sheetLayers, name)

