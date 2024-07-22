#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

#funtion define
def read_file_and_display(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Iterate through each line in the file
            for line in file:
                # Print the line, end='' to avoid adding extra newline characters
                print(line, end='')
    except FileNotFoundError:
        # Print an error message if the file is not found
        print(f"The file {file_name} does not exist.")

# Usage
read_file_and_display('ABC.txt')


#Output:-  Hi Om
