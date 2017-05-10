# -*-coding:Utf-8 -*

import sixpad as sp
page = sp.window.curPage

def delete_word_backward():
	"""Suprime le mots précédent ou le mots sous le curseur"""
	# Liste des caractère spéciaux où stoper la suppression
	char_stop = r""" .,:;!?=<>+-_)({}[]/\"'"""+"\n"
	
	# on identifie la position
	pos = page.position
	
	# Si on est au début du fichier, on emmet un bip
	if pos == 0 : 
		sp.window.messageBeep(0)
		return
	# end if
	# Cas particulier, si on est sur pos à 1, on suprime jusqu'au début du fichier
	if pos == 1 :
		sp.say(page.text[0], True)
		page.delete(0, 1)
		page.position = 0
		return
	# end if
	
	# On supprime jusqu'à trouver un des caractère spéciaux
	i = 2
	while True : 
		# Si on arrive au début du fichier on suprime jusque là.
		if pos-i == 0:
			sp.say(page.text[pos-i:pos], True)
			page.delete(pos-i, pos)
			page.position = 0
			return
		# end if
		# Si on trouve un caractère stop on supprime jusqu'à lui, mais en le conservant.
		if page.text[pos-i] in char_stop :
			sp.say(page.text[pos-i+1:pos], True)
			# Suppression de la chaine entre position de départ et caractère précédent
			page.delete(pos-i+1,pos)
			page.position = pos-i+1
			return
		# end if
		i += 1
	# end while
# end def

sp.window.addAccelerator(
		'Alt+Backspace', delete_word_backward)
