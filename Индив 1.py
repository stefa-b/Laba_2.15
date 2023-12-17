def find_sentences_with_word(file_name, word):
    with open(file_name, 'r') as file:
        text = file.read()
        sentences = text.split('.')
        for sentence in sentences:
            if word in sentence:
                print(sentence.strip() + '.')

file_name = 'Кот.txt'
word = input("Введите слово: ")
find_sentences_with_word(file_name, word)


