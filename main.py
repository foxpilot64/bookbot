def main():
    with open("/home/bex/workspace/github.com/foxpilot64/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

        words = file_contents.split()
        print (f"{len(words)} words found in the document\n")

        #call charnum here, inside of main:
        result = charnum(file_contents)
        print("Character counts: ")
        print(result)
        #Convert the dictionary to a list of dictionaries using sorting
        alpha_count = [{"character": char, "num": count} for char, count in result.items()]

        #Sort the list of dictionaries by the "num" value in descending order:
        alpha_count.sort(reverse=True, key=lambda d: d["num"])

        #Print sorted character counts with formatting
        for entry in alpha_count:
            character = entry["character"]
            num = entry["num"]
            print(f"The '{character}' character was found {num} times")




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
#def sort_on(dict):
   # return dict["num"]

##alpha_count = [

#]
#alpha_count.sort(reverse=True, key=sort_on)
#print(alpha_count)


main()
