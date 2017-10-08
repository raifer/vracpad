# -*-coding:Utf-8 -*

import sixpad as sp



def move_up():
	"""Move up one line and read it, 
	return True if they position has changed, False otherwise"""
	
	page = sp.window.curPage
	line, col = page.licol(page.position)
	
	if line == 0:
		sp.window.messageBeep(0)
		return False
	# end if
	
	# On regarde si la ligne destination n'est pas plus courte.
	if page.lineLength(line-1) < col:
		col = page.lineLength(line-1)
	# end if
	
	page.position = page.licol(line-1, col)	
	sp.say(page.curLineText, True)
	return True
# end def

def move_down():
	"""Go to the next line and read it, 
	return True if they position has changed, False otherwise"""
	
	page = sp.window.curPage
	line, col = page.licol(page.position)
	
	if line == page.lineCount-1:
		sp.window.messageBeep(0)
		return False
	# end if
	
	# On regarde si la ligne destination n'est pas plus courte.
	if page.lineLength(line+1) < col:
		col = page.lineLength(line+1)
	# end if
	
	page.position = page.licol(line+1, col)	
	sp.say(page.curLineText, True)
	return True
# end def

def move_start():

	page = sp.window.curPage
	#On vérifie si la ligne commence directement avec du texte
	if page.lineStartOffset(page.curLine) == page.lineSafeStartOffset(page.curLine):
		page.position = page.lineStartOffset(page.curLine)
		#sp.window.beep(220, 100)
		#sp.window.beep(220, 100)
	# On vérifie si le curseur est au début du texte
	elif page.position == page.lineSafeStartOffset(page.curLine):
		# On se positionne au début de la ligne sur n'importe quel caractère
		page.position = page.lineStartOffset(page.curLine)
		#sp.window.beep(220, 100)
	else:
		# On se positionne sur le premier caractère qui n'est pas une espace ou une tabulation
		page.position = page.lineSafeStartOffset(page.curLine)
		#sp.window.beep(330, 100)
		#sp.window.beep(440, 100)
	if (page.textLength) : sp.say(page.text[page.position], True)
	else : sp.say("vide");



# Main
# Ajout des raccourcis
# Move up : CTRL P
sp.window.addAccelerator(
		'CTRL+p', move_up)

# Move down : CTRL N
# On modifi le raccourci ctrl + n de nouveau en ctrl + t
item_new = sp.window.menus['file'][0]['new']
item_new.accelerator = "CTRL+t"

# Ajout accelerator move down
sp.window.addAccelerator(
		'CTRL+n', move_down)

# Move start : CTRL P
sp.window.addAccelerator(
		'CTRL+a', move_start)

# On modifi le raccourci ctrl + a
item_select_all = sp.window.menus['edit']['selectAll'] #['select all']
item_select_all.accelerator = "ALT+a"


