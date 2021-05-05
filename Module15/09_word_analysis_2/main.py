word = input('Введите слово: ')
word = list(word)
word_palindrome = []

len_word = len(word)
for i in range(1, len_word + 1):
    reverse_word = word[-1 * i]
    word_palindrome.append(reverse_word)
if word == word_palindrome:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')