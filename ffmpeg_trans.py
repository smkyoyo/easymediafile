import os
import sys

"""
@file ffmpeg_trans.py
@brief code for bulk converting media file
@author Min Gyung Song
@contact mg.song@sk.com
@data 2018.03.14
"""

def main():
	
	number = input('옵션 번호를 선택해 주세요. 1:파일 변환, 2:파일 쪼개기')
	if number=='1':
		print('변환하고자 하는 입력 파일의 형식을 적어 주세요.')
		inputFileType = input()
		print('변환하고자 하는 출력 파일의 형식을 적어 주세요.')
		outputFileType = input()
		lensOfInputType = len(inputFileType)
		lensOfOutputType = len(outputFileType)
		if (lensOfInputType<2 or lensOfInputType>3):
			print('지원하는 입력 파일이 아닙니다. 다른 파일을 이용해 주세요')
			print('프로그램이 종료됩니다.')
			sys.exit(1)
		else: 
			files = os.listdir('.')
			for f in files:
				if f.lower()[-(lensOfInputType):] == inputFileType:
					print('processing', f)
					convert_process(f, outputFileType)
		
	elif number=='2':
		print('처리할 파일의 형식을 입력해 주세요.')
		fileType = input()
		lensOfFileType = lens(fileType)
		if (lensOfFileType<2 or lensOfFileType>3):
			print('지원하는 입력 파일이 아닙니다. 다른 파일을 이용해 주세요')
			print('프로그램이 종료됩니다.')
			sys.exit(1)
		else:
			seconds = input('쪼개고자 하는 초 단위를 입력해 주세요.')
			if (seconds<5 or seconds>3600):
				print('쪼개고자 하는 초 단위가 너무 작거나 큽니다.')
				sys.exit(1)
			else: 
				files = os.listdir('.')
				#files = os.listdir("/Users/misong/Documents/01.\ Deep\ Meta/Sound/sample_video/hyorine/")
				for f in files:
					if f.lower()[-(len(fileType)):] == fileType:
						print('splitting process', f)
						split_process(f, fileType, seconds)

	else:
		print('지원하는 옵션 번호가 아닙니다.')
		print('프로그램을 종료합니다')

#Convert input files to output files type
def convert_process(f, outputFileType):
	inputFile = f
	outputFile = f[:-(len(outputFileType))] +  outputFileType
	#write ffmpeg log to ffmpeg.log file
	cmd = 'ffmpeg -i {0} -ab 320k -ac 2 -ar 44100 -vn -f {1} {2} 2>&1'.format(inputFile, outputFileType, outputFile)
	os.popen(cmd)
#ffmpeg -i input file path/-f output file type/-ab encoded 192Kbps /-vn we don't want video /sample rate to 44100 Hz /-ac # of audio channel

#Split a input file to multiple files 

def split_process(f, fileType, seconds):
	inputFile = f
	outputFile = f[:-len(fileType)]
	cmd = 'ffmpeg -i {0} -f segment - segment_time {1} -c copy {2}_%04d.{3} > ffmpeg_split.log 2>&1'.format(inputFile, seconds, outputFile, fileType)
	os.popen(cmd)


main()
