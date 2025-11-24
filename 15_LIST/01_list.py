# Lists are like a simple array
# They can store multiple data types as well.
# Lists are ordered (Meaning that they have an index that is persistent unless changed) and
#  mutable (will change the original list)

marks = [54, 23, 64, 93, 32]
# Using Split to get specific indexes
print(marks[2:4])
mixed = [43, False, "Hello"]
print(marks)
marks.sort( reverse=True)
print(marks)
print(mixed)

marks.append(100)
print(marks)

