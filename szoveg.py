def szovegFordit(szoveg):
	fordSzoveg=""
	for x in range(len(szoveg)-1,-1,-1):
		fordSzoveg+=szoveg[x]
	return fordSzoveg
	
def szovegCsere(szoveg):
	maganHangzo="aáéoöüóiíÍAÁÉOÖÜÓIÍ"
	for x in range(0,len(maganHangzo)):
		szoveg=szoveg.replace(maganHangzo[x],"e");
	return szoveg
	
def szovegParos(szoveg):
	parosSzoveg = ""
	for x in range (0,len(szoveg),2):
		parosSzoveg += szoveg[x]
	return parosSzoveg
	
szoveg=input("Írj be egy szöveget:")
print(szovegFordit(szoveg))
print(szovegCsere(szoveg))
print(szovegParos(szoveg))
print(szovegParatlan(szoveg))