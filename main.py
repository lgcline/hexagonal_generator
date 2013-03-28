"""
Main Generator Program
"""

#inputs (maybe make a GUI for this in the future?)
numBases=51400	#bases in scaffold
sheetThickness=29  #average thickness
name = "hex_automation_test"


#hexagonal sheet generation, kick an if-elsif in here when you add square
import hex_sheet_calculator
import hex_sheet_plotter
import hex_scaffold_generator

#get values from calculator
hexcalc=hex_sheet_calculator
hexcalc.calculator(numBases, sheetThickness)
sheetLayers = hexcalc.layer()
sheetVert = hexcalc.verts()

#run the slice plotter to get a 2D layout
hexplot = hex_sheet_plotter
hexplot.plot(sheetVert, sheetLayers, name)

#run the scaffold generator
plotted_helices = hexplot.2dplot()
hexscafgen=hex_scaffold_generator
hexscafgen.generator(plotted_helices, numBases, sheetVert)
