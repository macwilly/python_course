coordinates = (10, 20)
a,b = coordinates
print(a)
print(b)

# coordinates[0] = 50 cannot add to the tuple
coord_list = list(coordinates)
coord_list[0] = 50
coord_tuple = tuple(coord_list)
print(coord_tuple)