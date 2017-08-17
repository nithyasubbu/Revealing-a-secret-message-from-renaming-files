import os

def renaming_files():

	#Get all the files in the prank folder from the specific location
	file_list = os.listdir("/Users/nithysub/Desktop/FSWD")

	#Print the file list (with the numbers in them)
	print(file_list)

	#Print the current working directory to know if the files are looked at correctly
	saved_path = os.getcwd()

	#Print the current working directory
	print(saved_path)

	os.chdir("/Users/nithysub/Desktop/FSWD")

	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,'0123456789'))
		print(file_name)

	os.chdir(saved_path)

renaming_files()