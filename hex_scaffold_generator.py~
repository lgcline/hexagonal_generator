"""
Hexagonal Scaffold Generator
"""

#declare lists
bases = []
helices = []

def generator(plotted_helices, num_bases, total_helices):	#generate hexagonal scaffod in list form (convert to caDNAno later)
	"""
	the form of the helices sublists are as follows:
	[x,y,angle(helix angle, not base angle),thickness,high/low(0 or 1),direction(up:1,down:0)]
	the helix number is indicated by the index of the list in array helices
	"""
	working_helix = []	#list used to temporarily hold sublists from plotted_helices
	current_helix = 0
	
	while current_helix <= total_helices:
		working_helix = plotted_helices(current_helix)
		if working_helix(3) == 45: 	#helix angle = 45deg
			
