from os import rename, listdir

#IMPORTANT: 
# 1. Place this file is the directory where you want to rename the files
# 2. Execute it and check that the output matches the name files you want to rename
# 3. Comment the 'print fname' line, uncomment 'rename(fname, fname + '.pdf')' and execute again  
fnames = listdir('./')

for fname in fnames:
	print fname
	#rename(fname, fname + '.pdf')