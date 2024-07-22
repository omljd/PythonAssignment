# Write a function in Python to count and display the total number of words in a text file “ABC.txt”

# function define
def count_words_in_file(file_name):
    try:
        # Initialize the word count to zero
        word_count = 0
        
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Iterate through each line in the file
            for line in file:
                # Split the line into words using whitespace as the delimiter
                words = line.split()
                # Add the number of words in the current line to the total count
                word_count += len(words)
        
        # Display the total word count
        print(f"Total number of words in {file_name}: {word_count}")
    except FileNotFoundError:
        # Print an error message if the file is not found
        print(f"The file {file_name} does not exist.")

# Usage
count_words_in_file('ABC.txt')


#Output:-Total number of words in ABC.txt: 2
