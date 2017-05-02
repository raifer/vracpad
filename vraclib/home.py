# -*-coding:Utf-8 -*

import sixpad as sp

#VK codes des touches
VK_HOME = 36
VK_ALT = 2048

def onKeyDown(activePage, vk):
	# Décommentez les 2 lignes suivantes pour connaître le VKCode de n'importe quelle touche ou combinaison de touches.
	#sp.say(str(vk), True)
	#return True
	#sp.say(activePage.selectionStart)
	#sp.say(activePage.selectionEnd)
	# On vérifie si la touche origine a bien été pressée
	if vk == VK_HOME:
		#On vérifie si la ligne commence sans espace ou tab
		if activePage.lineStartOffset(activePage.curLine) == activePage.lineSafeStartOffset(activePage.curLine):
			activePage.position = activePage.lineStartOffset(activePage.curLine)
			sp.window.beep(220, 100)
			sp.window.beep(220, 100)
		# On vérifie si le curseur est au début du texte
		elif activePage.position == activePage.lineSafeStartOffset(activePage.curLine):
			# On se positionne au début de la ligne sur n'importe quel caractère
			activePage.position = activePage.lineStartOffset(activePage.curLine)
			sp.window.beep(220, 100)
		else:
			# On se positionne sur le premier caractère qui n'est pas une espace ou une tabulation
			activePage.position = activePage.lineSafeStartOffset(activePage.curLine)
			sp.window.beep(330, 100)
			sp.window.beep(440, 100)
		return False
	return True	#Tempo en attendant correctif
	
	# On vérifie si la touche Alt+Origine a bien été pressée
	if vk == VK_ALT + VK_HOME:
		# On vérifie si le curseur est au début du texte
		if activePage.selectionEnd == activePage.lineSafeStartOffset(activePage.lineOfOffset(activePage.selectionEnd)):
			# On se positionne au début de la ligne sur n'importe quel caractère
			activePage.selectionEnd = activePage.lineStartOffset(activePage.lineOfOffset(activePage.selectionEnd))
			sp.window.beep(220, 100)
		else:
			# On se positionne sur le premier caractère qui n'est pas une espace ou une tabulation
			activePage.position = activePage.lineSafeStartOffset(activePage.lineOfOffset(activePage.selectionEnd))
			sp.window.beep(330, 100)
			sp.window.beep(440, 100)
		return False

	return True

def pageOpened(openedPage):
	openedPage.addEvent("keyDown", onKeyDown)

sp.window.addEvent("pageOpened", pageOpened)
sp.window.curPage.addEvent("keyDown", onKeyDown)

