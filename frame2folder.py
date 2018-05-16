#Copy frames by frame number from start number to end number

import shutil, os

inputFolderPath = '/home/mg.song/Video2frame/videos/pixtree/'
inputFileName = 'PX_doggabi_2_sn_ru.txt'
sourceFolderPath = '/home/mg.song/Video2frame/videos/'
sourceFolderName = 'doggabi/'
outputFolderPath = '/home/mg.song/Video2frame/videos/pixtree/'
outputFolderName = 'doggabi_dv/'
lastFrameNumber = 132875

inputFilePath = inputFolderPath + inputFileName
outputFolderPath = outputFolderPath + outputFolderName
sourceFolderPath = sourceFolderPath + sourceFolderName

fi = open(inputFilePath, 'r')
lines = fi.readlines()
#string to integer
iLines = [int(i) for i in lines]

order=0
for order in range(0, len(iLines)-1, 1):
	frameNumber=iLines[order]
	print("frameNumber= " + str(iLines[order]))
	for frameNumber in range(frameNumber, iLines[order+1], 5):
		folderNumber = frameNumber/4999
	#	for folderNumber in range(folderNumber, folderNumber+1):
		if folderNumber <10:
			detailFolderName = '000000' + str(folderNumber)+ '/'
			if frameNumber<10: 
				fileName = '00000000' + str(frameNumber)			
			elif frameNumber<100: 
				fileName = '0000000' + str(frameNumber)
			elif frameNumber<1000:
				fileName = '000000' + str(frameNumber)
				print("fileName = "+fileName)
			elif frameNumber<10000:
				fileName = '00000' + str(frameNumber)
				print("fileName = "+fileName)
			elif frameNumber<100000: 
				fileName = '0000' + str(frameNumber)
        	        	print("fileName = "+fileName)
			elif frameNumber<1000000: 
				fileName = '000' + str(frameNumber)
                        else: 
				print("This is invalid frame number\n")
			if not os.path.exists(outputFolderPath+lines[order]+ '/'):
				os.mkdir(outputFolderPath+lines[order]+'/')
				print("Folder created")
			if os.path.isfile(sourceFolderPath+detailFolderName+fileName+'.jpg'):
				shutil.copy(sourceFolderPath+detailFolderName+fileName+'.jpg', outputFolderPath+lines[order]+'/')
				print("file existed")
			else: continue
		else:
			detailFolderName = '00000' + str(folderNumber) + '/'
			if frameNumber<10: fileName = '00000000' + str(frameNumber)
			elif frameNumber<100: fileName = '0000000' + str(frameNumber)
			elif frameNumber<1000: fileName = '000000' + str(frameNumber)
			elif frameNumber<10000: fileName = '00000' + str(frameNumber)
			elif frameNumber<100000: fileName = '0000' + str(frameNumber)
			elif frameNumber<1000000: fileName = '000' + str(frameNumber)
			else:
				print("This is invalid frame number\n")
			if not os.path.exists(outputFolderPath+lines[order]+ '/'):
				os.mkdir(outputFolderPath+lines[order]+'/')
				print("Folder created")
			if os.path.isfile(sourceFolderPath+detailFolderName+fileName+'.jpg'):
				shutil.copy(sourceFolderPath+detailFolderName+fileName+'.jpg', outputFolderPath+lines[order]+'/')
				print("file existed")
			else: continue

fi.close()
