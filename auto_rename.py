import os 

# change directory to that of file
def paths():
	path = input("Paste path to file here:\n")
	os.chdir(path)

def new_name():
	global new_file_name
	new_name = input("Enter new name:\n")
	new_name_extension = input("Enter the file extension:\n")
	new_file_name = new_name+'.'+new_name_extension

def list_files():
	print("---------------------------")
	global files
	for files in os.listdir():
		files = files
		print(files)
		name, extention = os.path.splitext(files)
		print("---------------------------")

def rename_file():
	response = input("Are you sure you want to rename the above files?\npress 'y' to continue: ")
	if response == "y" or 'Y':
		os.rename(files, new_file_name)

def load():
	try:
		paths()
	except FileNotFoundError as e:
		print(f"No such file or directory:{os.getcwd()}")
	except NameError as name_error:
		print('name_error')  
	else:
		list_files()
		new_name()
		rename_file()

	finally:
		try_again = input("Try again? Press 'y' to continue or any key to quit: ")
		if try_again == "y" or try_again == "Y":
			load()
		else:
			os.sys.exit()


if __name__ == '__main__':
	load()