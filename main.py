def main():
    with open("/home/bex/workspace/github.com/foxpilot64/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()

        #Print only the first 1000 characters to preview content instead of all
        print(file_contents)

        #Split the content into words and count them
        words = file_contents.split()
        print (f"\n{len(words)} words found in the document\n")

        #call charnum here, inside of main:
        result = charnum(file_contents)
        
        
        #Convert the dictionary to a list of dictionaries using sorting
        alpha_count = [{"character": char, "num": count} for char, count in result.items()]

        #Sort the list of dictionaries by the "num" value in descending order:
        alpha_count.sort(reverse=True, key=lambda d: d["num"])
        
        #The beginning of sorted report:
        print("\n---Begin report of sorted character counting---\n")
        
        #Print sorted character counts with formatting
        for entry in alpha_count:
            character = entry["character"]
            num = entry["num"]
            print(f"The '{character}' character was found {num} times")

    print("\n--- End report ---")




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
    
  
   
main()
