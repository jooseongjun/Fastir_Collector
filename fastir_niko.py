import os, shutil

DSTDIR = "C:\Users\Seongjun\Desktop/niko"

def makefolder:
	if not os.path.isdir("C:\Users\Seongjun\Desktop/niko"):
		os.mkdir("C:\Users\Seongjun\Desktop/niko")
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

