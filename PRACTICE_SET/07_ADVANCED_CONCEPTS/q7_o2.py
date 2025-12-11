word_list = ["python", "rocks", "ai"]


longer_than_four = [n for word in word_list if (n:= len(word)) >= 4]
print(longer_than_four)
