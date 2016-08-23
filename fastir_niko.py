import os, shutil

DSTDIR = "./"

def makefolder:
	if not os.path.isdir("./niko"):
		os.mkdir("./niko")
	else:
		print "Already existed!!!"
		pass

def copyfile:
	for path,dirs,files in os.walk("C:/"):
		for file in files:
			if file.split(".")[-1] == "icon":
				total_filename = ""
				total_filename = DSTDIR + file
				shutil.copy2(file,total_filename)

if __name__ == '__main__':
	makefolder()
	copyfile()

