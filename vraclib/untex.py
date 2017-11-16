# -*-coding:Utf-8 -*

import re
import sixpad as sp
page = sp.window.curPage

listReplace = (
	(r'\^e', 'ê'),
	(r'\`e', 'è')
)

def compil(list_sub):
	listCompil = [];
	for pattern, sub in list_sub :
		listCompil.append( (re.compile(pattern, 0), sub) )
	return listCompil
# end def compil

def untexPage():
	text = page.text
	for old, new in listReplace :
		text = text.replace(old, new)
	# end for
	page.text = text
# end def

sp.window.addAccelerator(
		'ALT+F6', untexPage)
