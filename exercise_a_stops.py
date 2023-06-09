stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")

#2. Add "Glasgow Queen St" to the start of the list
stops = ["Glasgow Queen St"] + stops


#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")

#4. Print out the index position of "Linlithgow"
index = stops.index("Linlithgow")
print(index)

#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")

#6. Delete "Cumbernauld" from the list by index
Cumbernauld_index = 2
del stops[Cumbernauld_index]

#7. Print the number of stops there are in the list
num_stops = len(stops)
print(num_stops)

#8. Sort the list alphabetically
sorted_list = sorted(stops)
print(sorted_list)

#9. Reverse the positions of the stops in the list
stops.sort(reverse=True)
print(stops)

#10 Print out all the stops using a for loop
for stop in stops:
    print(stop)
