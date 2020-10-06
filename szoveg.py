def szovegFordit(szoveg):
	fordSzoveg=""
	for x in range(len(szoveg)-1,-1,-1):
		fordSzoveg+=szoveg[x]
	return szovegFordit
	
szoveg=input("Írj be egy szöveget: ")
print(szovegFordit(szoveg))


