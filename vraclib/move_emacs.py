# -*-coding:Utf-8 -*

import sixpad as sp
page = sp.window.curPage

def move_up():
	id = sp.window.findAcceleratorByKey("")
	sp.say(id, True)
# end def

sp.window.addAccelerator(
		'CTRL+q', move_up)
