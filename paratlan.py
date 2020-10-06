def szovegParatlan(szoveg):
szovegParos=""
	szovegParatlan = ("acegikmoqstvxz")
	for x in range(0,len(szoveg)-1,1):
		szovegParatlan+=szoveg[x]
	return SzovegParatlan