"""
Hexagonal Scaffold Generator
"""

#declare lists
bases = []
helices = []

def generator(plotted_helices, num_bases, total_helices, thickness):	#generate hexagonal scaffod in list form (convert to caDNAno later)
	"""
	the form of the helices sublists are as follows:
	[x,y,angle(helix angle, not base angle),thickness,high/low(0 or 1),direction(5-3:1,3-5:0)]
	the helix number is indicated by the index of the list in array helices
	"""
	working_helix = []	#list used to temporarily hold sublists from plotted_helices
	current_helix = 0
	
	while current_helix <= total_helices:
		working_helix = plotted_helices(current_helix)
		#set thickness and high vs low
		if working_helix(3) == 45: 	#helix angle = 45deg
			working_helix(4)= thickness+7	#set thickness
			working_helix.append(0)	#set high
		elif working_helix(3) == 135:	#helix angle = 135deg
			working_helix(4)= thickness+7	#set thickness
			working_helix.append(0)	#set high
		elif working_helix(3) == 180:	#helix angle = 180deg
			working_helix(4)= thickness-14	#set thickness
			working_helix.append(0)	#set high
		elif working_helix(3) == 225:	#helix angle = 225deg
			working_helix(4)= thickness-14	#set thickness
			working_helix.append(0)	#set high
		elif working_helix(3) == 315:	#helix angle = 315deg
			working_helix(4)= thickness+7	#set thickness
			working_helix.append(1)	#set low
		else:				#helix angle = 0deg
			working_helix(4)= thickness+7	#set thickness
			working_helix.append(1)	#set low
		#set direction of helix scaffold
		if (working_helix(1)+working_helix(2))%2 == 0:	#even
			working_helix.append(1)	#5' to 3'
		else:						#odd
			working_helix.append(0)	#3' to 5'


