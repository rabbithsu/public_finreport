# -*- coding: UTF-8 -*-
import slate
import os
import codecs

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for pdf in files:
	if ".pdf" in pdf:
		save = ""
		fp = open(pdf,"r")
		doc = slate.PDF(fp)
		for i in doc:
			print i
			save += i
		print save
		fw = open(pdf.split(".")[0]+".txt", "w")
		fw.write(save)
		fw.close()
		print "Convert "+pdf+ " to TXT."
