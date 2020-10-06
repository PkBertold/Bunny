"""
PUSKA

A szöveg hossza: len(szoveg)
A szöveg utolsó karater: szoveg[len(szoveg)-1]
Csere a szövegben : szoveg.replace("H", "J") // a nagy "H"-kat nagy "J"-re cserélem
A szöveg tartalmazza az alma karaktereket?: logikaiValtozo = "alma" in szoveg // not in - nem tartalmazza

Ciklus:
ujSzoveg=""
for x in range(0,len(szoveg)-1,2):
	ujSzoveg=ujSzoveg+szoveg[x] 

Eljáras:
def szovegFordit(szöveg):
	...
	return vissza
"""
# Az eljárást készítette:
def szovegFordit(szoveg):
FordSzoveg=""
	for x in range(0,len(szoveg)-1,-1,-1):
	fordSzoveg+=szoveg[x]
	return fordSzoveg
	
# Az eljárást készítette: Sipos Péter	
def szovegCsere(szoveg):
	maganHango="aáeéoóöőuúüűiíAÁEÉEÉOÓÖŐUÚÜŰIÍ2
	for x in range(0, len(maganHango)):
		szoveg.replace(maganhangzo[x],"e");
	return ""
	
def szovegParos(szoveg):
szovegParos=""
	szovegParos = ("bdfhjlnqsuwy")
	for x in range(0,len(szoveg)-1,2):
		szovegParos+=szoveg[x]
	return SzovegParos
	
def szovegParatlan(szoveg):
szovegParos=""
	szovegParatlan = ("acegikmoqstvxz")
	for x in range(0,len(szoveg)-1,1):
		szovegParos+=szoveg[x]
	return SzovegParatlan
	
# Itt kezdődik a főprogram
szoveg=input("Írj be egy szöveget:")
print(szovegFordit(szoveg))
