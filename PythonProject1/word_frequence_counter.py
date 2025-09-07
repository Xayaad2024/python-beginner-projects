def word_count(sentence):
    words = sentence.lower().split()
    count ={}
    for word in words:
        count[word] = count.get(word, 0)+1
    return count
text = input("Enter a sentence:")
print(word_count(text))