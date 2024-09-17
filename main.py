def main():
    with open("/home/bex/workspace/github.com/foxpilot64/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

        words = file_contents.split()
        print (len(words))

        #call charnum here, inside of main:
        result = charnum(file_contents)
        print("Character counts: ")
        print(result)

def charnum(text):
    lowered_text = text.lower()
    char_counts = {} #Store counts in a dictionary
   

    #Count each char in lowered_text:
    for char in lowered_text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    
    
    return char_counts
    
   # list_of_dict(): []


main()
