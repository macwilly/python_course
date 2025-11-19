# Count all the vowels in a given string
def count_vowels(sentence):
    sentence = sentence.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    count_2 = 0
    for letter in sentence:
        if letter in vowels:
            count += 1

    return count

print(count_vowels("Hello World"))