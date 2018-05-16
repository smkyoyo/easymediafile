#Round up by multiple 5 

inputFolderPath = '/home/mg.song/Video2frame/videos/pixtree/'
inputFileName = 'PX_busanhang_2_sn.txt'
outputFolderPath = '/home/mg.song/Video2frame/videos/pixtree/'
outputFileName = 'PX_busanhang_2_sn_ru.txt'

inputFilePath = inputFolderPath + inputFileName
outputFilePath = outputFolderPath + outputFileName

#Create New file
#fo = open(outputFilePath, 'w')
#fo.close()

# read input file
fi = open(inputFilePath, 'r')
fo = open(outputFilePath, 'w')

lines = fi.readlines()
iLines = [int(i) for i in lines]

for iline in iLines:
        iline=((iline +4)/5)*5
        print(iline)
	fo.write(str(iline)+'\n')

fi.close()
fo.close()
