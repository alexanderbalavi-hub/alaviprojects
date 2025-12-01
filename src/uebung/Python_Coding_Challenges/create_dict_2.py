#Second Challenge: Read text from text file and create a dictionory, where the key is the word and the value is the amount of times the word appears in the text
def create_word_count_dict(file_path):
    word_count = {}
    try:
        with open((file_path), 'r') as file:
            text = file.read()
            words = text.split()
            for word in words:
                word = word.lower().strip('.,!?;"()[]{}')  # Normalize the word
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
             
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    return word_count
#Example usage:
file_path = 'src/uebung/Python_Coding_Challenges/test.txt'  # read in file path
word_count_dict = create_word_count_dict(file_path)
print(word_count_dict)
#sort dict from lowest to higehst value
sorted_word_count = dict(sorted(word_count_dict.items(), key=lambda item: item[1])) # sort by value
print(sorted_word_count)





