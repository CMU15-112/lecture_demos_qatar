story = open("story.txt","r")
vocab = {}
aline = story.readline()
while aline != "":
    aline = aline.strip()
    words = aline.split()
    for word in words:
        word = word.lower()
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace(";","")
        word = word.replace("?","")
        word = word.replace("!","")
        word = word.replace("'","")
        word = word.replace('"',"")
        word = word.replace(".","")
        
        vocab[word] = vocab.get(word,0) + 1
    aline = story.readline()
mx = 0
wrd = ""
for key in vocab:
    if vocab[key] > mx:
        mx = vocab[key]
        wrd = key
print (wrd,mx)
print (vocab["is"])

with open("vocab.txt","w") as output:
    notvocab = ["is","was","and","he","the","a","an","she","it","on","in","there","this"]

    for key in vocab.keys():
        if key not in notvocab:
            output.write(key)
            output.write("\n")
