# -*-coding:Utf-8 -*

import sixpad as sp
page = sp.window.curPage

def move_up():
	"""Move up one line and read it, 
	return True if they position has changed, False otherwise"""
	
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

sp.window.addAccelerator(
		'CTRL+p', move_up)
