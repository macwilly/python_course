import re

#it will return the first
text = "The quick brown fox jumps over the lazy dog."
match = re.search("brown", text)
all_matches = re.findall("the", text, re.IGNORECASE) # case insensitive
if match:
    print("Match found")
    print(f"Match start: {match.start()}")
    print(f"Match end: {match.end()}")

if all_matches:
    print("All matches found")
    print(f"All matches : {all_matches}")
