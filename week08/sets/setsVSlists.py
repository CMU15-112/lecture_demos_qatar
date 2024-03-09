def unique_words_list(text):
    words = text.split()
    
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
 
    return  unique_words

# Example usage:
text = "hello world hello hello world world"
print("List: ", unique_words_list(text))














def unique_words_set(text):
                       
    words = text.split()
                       
    unique_words = set(words) 

    return unique_words

print("Set: ", unique_words_set("hello world hello hello world world"))







##############################################

def word_frequency_list(text):
    words = text.split()
    unique_words = []
    word_counts = []
    
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
            word_counts.append(1)
        else:
            index = unique_words.index(word)
            word_counts[index] += 1
    
    print(f" unique_words: {unique_words}")
    print(f" word_counts: {word_counts}")
    return list(zip(unique_words, word_counts)) 

# Example usage:
text = "hello world hello hello world world hello"
#print("Using Lists--------: ", word_frequency_list(text))
print()












def word_frequency_set(text):
                 
    words = text.split()
    #print("words:", words)
    print("num Words: ", len(words))
                       
    unique_words = set(words) 
    print("unique words set: ", unique_words) # if we try to print the set, this is how it will look like
    print("num unique words: ", len(unique_words))
    
    word_counts=[]
    for word in unique_words:
        word_counts.append((word, words.count(word)) )
        
    return word_counts

#print("Using Sets ----------: ", word_frequency_set("hello world hello hello world world hello"))


