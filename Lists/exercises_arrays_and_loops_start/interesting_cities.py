cities = ["Edmonton", "Paris", "Munich","Berlin", "Amsterdam", "Prague"]
cities.remove("Edmonton")

interests = input("Enter a city that interests you:")

cities.insert(3 ,interests)
cities.sort()

print("Our list of interesting cities in alphabetical order is: ")
print(cities)