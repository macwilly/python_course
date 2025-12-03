try:
    a= 350 / 0
except Exception as e:
    print(e)
else:
    print("All numbers good1")
finally:
    print("We finally made it1")

# This else will run after the try
try:
    a= 350 / 10
except Exception as e:
    print(e)
else:
    print("All numbers good2")
finally:
    print("We finally made it2")