import os
#import re

def renamingFiles_miniProject():

	#Get the folder path containing the files
	folder_name = os.listdir("/Users/nithysub/Desktop/FSWD/new_alphabets")

	#Print the folder containing the secret message
	print('Before removing numerical characters - ',folder_name)

	#Get the current working directory -> if it points to the previous working directory, point it to the correct one

	saved_path = os.getcwd()
	print(saved_path)

	os.chdir("/Users/nithysub/Desktop/FSWD/new_alphabets")

	#Print After the file name change
	print('After removing the numerical characters - revealing the secret message..1..2..3')
	for file_name in folder_name:
		#Use the os.rename fuction to rename the older file names with numerical characters to new file names without the characters
		os.rename(file_name,file_name.translate(None, '0123456789'))
		print(file_name)	
		
		#print the file name change on the terminal for the user to see
		#filename_Change = re.sub('[0-9]','',file_name)
		#print(filename_Change)


	os.chdir(saved_path)

renamingFiles_miniProject()
