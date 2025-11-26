friends = { "Dave": "555-123-3214",
           "Stacy": "555-123-3214",
           "Hanky": "555-123-3214"}

print(friends)
names = friends.keys()
print(names)
phone_numbers = friends.values()
print(phone_numbers)
for person, number in friends.items():
    print(person, number)
