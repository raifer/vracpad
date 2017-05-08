# -*-coding:Utf-8 -*

import sixpad as sp

def onKeyDown(page, vk):
	#sp.say(str(vk))
	# si la touche est FLH, CTRL+FLH, CTRL+HOME, PGUp
	if vk in[38, 550, 548, 33]:
		# et qu'on est à la première ligne
		if page.curLine == 0: sp.window.messageBeep(0)
	# end if
	# si la touche est FLB, CTRL+FLB, CTRL+END, PGDown
	if vk in[40, 552, 547, 34]:
		# et qu'on est à la dernière ligne
		if page.curLine == page.lineCount - 1: sp.window.messageBeep(0)
	# end if
	return True
# end def

def load():
	
	# Ajout des événement pour capter les down
	sp.window.addEvent("pageOpened", load_page_events)
	# Et on l'appel pour cette page
	load_page_events(sp.window.curPage)
	
def load_page_events(page) :
	page.addEvent("keyDown", onKeyDown)
# end def

load()
	




