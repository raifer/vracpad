# -*-coding:Utf-8 -*

import sixpad as sp

# Variables globales.
mode = 2
read_indent_if_dif = 1
lastDifferentIndentLevel = 0

def sayCurIndentLevel():
	""" say the current indent level """
	page = sp.window.curPage
	sp.say("Niveau " + str(page.lineIndentLevel(page.curLine)) +". ")
# end def

def getLineHeading(line):
	indentation = getIndentation() + ". "
	level = "niveau " + str(sp.window.curPage.lineIndentLevel(line)) + ". "
	if mode == 0:
		return sp.window.curPage.line(line)
	elif mode == 1:
		return indentation + sp.window.curPage.line(line)
	elif mode == 2:
		return level + sp.window.curPage.line(line)
# end def


def getIndentation():
	iIndent = 0
	sIndent = ""
	if sp.window.curPage.line(sp.window.curPage.curLine) == "":
		return "Vide"
	if sp.window.curPage.lineStartOffset(sp.window.curPage.curLine) != sp.window.curPage.lineSafeStartOffset(sp.window.curPage.curLine):
		iFirstChar = sp.window.curPage.lineStartOffset(sp.window.curPage.curLine)
		sIndentChar = sp.window.curPage.text[iFirstChar]
		if sIndentChar == " ":
			sMarker =  " espaces"
		elif sIndentChar == "\t":
			sMarker = " tabs"
		sTemp = sp.window.curPage.line(sp.window.curPage.curLine)
		i = 100
		while len(sTemp) > 0 and i > 0:
			i -= 1
			sFirstChar = sTemp[:1]
			sTemp = sTemp[1:]
			if sFirstChar != " " and sFirstChar != "\t":
				sIndent = sIndent + "|" + str(iIndent) + sMarker
				return sIndent[1:]
			if sFirstChar == sIndentChar:
				iIndent += 1
			else:
				sIndent = sIndent + "|" + str(iIndent) + sMarker
				iIndent = 1
				sIndentChar = sFirstChar
				if sMarker == " espaces":
					sMarker = " tabs"
				else:
					sMarker = " espaces"
		if iIndent != 0:
			sIndent = sIndent + "|" + str(iIndent) + sMarker
		if i == 0:
			return ""
		return sIndent[1:]
	else:
		return ""


def readIndentOnlyWhenChange():
	""" activate or deactivate the reading  of indents if change """
	global menuReadIndentOnlyWhenChange
	global read_indent_if_dif
	global lastDifferentIndentLevel
	# bug #menuReadIndentOnlyWhenChange.checked = not(menuReadIndentOnlyWhenChange.checked)
	read_indent_if_dif = not(read_indent_if_dif)
	if read_indent_if_dif :
		#sayLevel()
		sp.say("Activation de la lecture du niveau d'indentation si changement")
	else:
		#sayNothing()
		sp.say("Désactivation de la lecture du niveau d'indentation si changement")
	# end if
	lastDifferentIndentLevel = sp.window.curPage.lineIndentLevel(sp.window.curPage.curLine)
# end def

def toggleMode():
	if mode == 0:
		sayIndentation()
		sp.say("Dire les indentations", True)
	elif mode == 1:
		sayLevel()
		sp.say("Dire les niveaux", True)
	elif mode == 2:
		sayNothing()
		sp.say("Ne rien dire", True)
		# end if
# end def

def sayNothing():
	global mode, menu_line_headings
	mode = 0
	menu_line_headings.nothing.checked = True
	menu_line_headings.indentation.checked = False
	menu_line_headings.level.checked = False

def sayIndentation ():
	global mode, menu_line_headings
	mode = 1
	menu_line_headings.nothing.checked = False
	menu_line_headings.indentation.checked = True
	menu_line_headings.level.checked = False

def sayLevel ():
	global mode
	mode = 2
	menu_line_headings.nothing.checked = False
	menu_line_headings.indentation.checked = False
	menu_line_headings.level.checked = True

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

def onKeyUp(page, vk):
	global lastDifferentIndentLevel
	# Pour les touches tab et Shift + Tab.
	if vk in [9, 1033] and page.position <= page.lineSafeStartOffset(page.curLine) and not page.selectedText:
		sp.say("Niveau " + str(page.lineIndentLevel(page.curLine)) + ". " + page.line(page.curLine), True)
		# Comme on a changé l'indentation, on met à jour la variable global
		lastDifferentIndentLevel = page.lineIndentLevel(page.curLine)
		return True
	
	# Pour la touche BackSpace.
	if vk == 8 and not page.selectedText: 
		if page.position <= page.lineSafeStartOffset(page.curLine) :
			# Si les paramètres d'indentation sont de 1 Tab ou de 1 espace, on donne le niveau.
			if page.indentation in [0, 1]:
				sp.say("Niveau " + str(page.lineIndentLevel(page.curLine)) + ". " + page.line(page.curLine), True)
			else:
				# Le niveau d'indentation est fixé sur plus d'une espace, on donne donc le nombre d'indentations.
				sp.say(getIndentation() + ". " + page.line(page.curLine), True)
			# end if
			# Comme on a changé l'indentation, on met à jour la variable global
			lastDifferentIndentLevel = page.lineIndentLevel(page.curLine)
		# end if
		return True
	
	# Lecture de l'indentation
	# Si la touche est FLH, FLB, CTRL+Home, CTRL+END, PGUp, PGDown, CTRL+Up, CTRL+Down.
	# On donne les informations sur le mode de lecture d'entêtes utilisé.
	if vk in[33, 34, 38, 40, 547, 548, 550, 552] and not page.selectedText:
		# lecture seulement sur changement
		if read_indent_if_dif : 
			if lastDifferentIndentLevel != page.lineIndentLevel(page.curLine):
				sp.say(getLineHeading(page.curLine), True)
			# end if
		# end if
		# Mode de lecture sans restriction
		else:
			sp.say(getLineHeading(page.curLine), True)
		# end if
	lastDifferentIndentLevel = page.lineIndentLevel(page.curLine)
	return True
# end def



def load():
	global menu_say, menu_line_headings, menuReadIndentOnlyWhenChange
	global idTmrLineMove
	global g_key1, g_key2
	# Vérification de la pré-existence du menu
	if not sp.window.menus['say'] :
		menu_say = sp.window.menus.add(label = "Assistance &vocale", action=None, index=2, submenu=True, name="say")
	else :
		menu_say = sp.window.menus['say']
	# les modes de lecture des en-têtes de ligne
	menu_line_headings = menu_say.add(label = "Lecture des entêtes de &lignes", submenu = True, name = "lineHeadings")
	menu_line_headings.add(label = "Ne &rien dire", action = sayNothing, name = "nothing")
	menu_line_headings.add(label = "Dire les &indentations", action = sayIndentation, name = "indentation")
	menu_line_headings.add(label = "Dire les ni&veaux", action = sayLevel, name = "level")
	menu_line_headings.add(label = "&Basculer le mode de lecture des entêtes de ligne", action = toggleMode, name = "toggleMode", accelerator = "CTRL+SHIFT+i")
	menu_line_headings.indentation.checked = True
	# lecture du niveau d'indentation courant
	menu_say.add(label = "Lire le niveau d'&indentation courant", action = sayCurIndentLevel, name = "sayCurrentIndentLevel", accelerator = "CTRL+i")
	# lecture de l'indentation seulement si changement
	menuReadIndentOnlyWhenChange = menu_say.add(label = "Activer la lecture du niveau d'&indentation seulement si changement", accelerator = "ALT+i", action = readIndentOnlyWhenChange)
	
	# Ajout des événement pour capter les keyUp
	sp.window.addEvent("pageOpened", load_page_events)
	# Et on l'appel pour cette page
	load_page_events(sp.window.curPage)
	
def load_page_events(page) :
	page.addEvent("keyDown", onKeyDown)
	page.addEvent("keyUp", onKeyUp)
# end def

load()
	




