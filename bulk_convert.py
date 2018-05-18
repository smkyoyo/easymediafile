import os

def main():
	files = os.listdir('.')
	#files = os.listdir("/Users/misong/Documents/01.\ Deep\ Meta/Sound/sample_video/hyorine/")
	for f in files:
		if f.lower()[-2:] == 'ts':
			print ('processing', f)
			process(f)
	sys.exit(0)


def process(f):
	inFile = f
	outFile = f[:-2] + 'wav'
	cmd = 'ffmpeg -i {0} -ab 320k -ac 2 -ar 44100 -vn -f wav {1}'.format(inFile, outFile)
	os.popen(cmd)
#ffmpeg -i input file path/-f output file type/-ab encoded 192Kbps /-vn we don't want video /sample rate to 44100 Hz /-ac # of audio channel

main()
