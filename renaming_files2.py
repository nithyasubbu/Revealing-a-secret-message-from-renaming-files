import os

def renaming_files():

	#Get all the files in the prank folder from the specific location
	file_list = os.listdir("/Users/nithysub/Desktop/FSWD/prank")

	#Print the file list (with the numbers in them)
	print('Before changing file names',file_list)

	#Print the current working directory to know if the files are looked at correctly
	saved_path = os.getcwd()

	#Print the current working directory
	print(saved_path)

	#Changing the directory to the path inside the folder from where the file names are changed
	os.chdir("/Users/nithysub/Desktop/FSWD/prank")

	#For each file name, remove the numbers in them
	for file_name in file_list:
		#using os.rename('old','new') -> renames old to new name 
		os.rename(file_name,file_name.translate(None,'0123456789'))
		#Print the file names after the change
		print('After changing file names',file_name)

	#Change the directory path back to the saved path
	os.chdir(saved_path)

renaming_files()