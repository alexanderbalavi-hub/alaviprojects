#Second Challenge: Read text from text file and create a dictionory, where the key is the word and the value is the amount of times the word appears in the text
def create_word_count_dict(file_path):
    word_count = {}
    print("hello")
    try:
        with open((file_path), 'r') as file:
            print ("hello2")
            text = file.read()
            words = text.split()
            for word in words:
                word = word.lower().strip('.,!?;"()[]{}')  # Normalize the word
                if word in word_count:
                    word_count[word] += 1
                    print(word_count)
                else:
                    word_count[word] = 1
             
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    return word_count

create_word_count_dict(src\uebung\Python_Coding_Challenges\test.txt)





