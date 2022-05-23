# #this is different containers in python
#two types of containers
#   mutable- they can change (array and dictionaries)
#   immutable- they cant change (sets and tuples)
#
#they can be:
#   ordered or not ordered
#   ordered- arrays and tuples
#   not ordered- sets and dictionaries
#
#they can also be:
#   indexed or hashed (keys) or neither
#   index- number that corresponds with the position in the order starting at 0
#   hashed- type in key word to get the value, doesnt go in any ordered
#   sets dont have any
#
#arrays and tuples have dups
#set cant have dups
#dictionaries can have dup values but not same keys
#
#they all share:
#   you can get the length/ number of items in container
#   len(object)

#   get the type o object

#   loop through containers
#       loops goes through each object in the container
#       arrays and tuples are ordered, so they come out in order
#       dictionaries and sets are unordered, they come out randomly
#       for arrays tupes and sets when you loop through them you get out the object that is there (ex: string)
#       for dicitionary when you loop through you get the key, you must loop through the key to get the value out
#       dictionary = {'item1': 'item1value'}
#       for this_key in dictionary:
#           the_value = dictionary[this_key] <-- this is the value


#what goes in container? Almost any object
#   array of dictionaries Ex: a_array = [{'item1': 'item1value'}]
#   they can also have mixed objects
#   array of dictionaries Ex: a_array = [{'item1': 'item1value'}, 'hllo']


# #this is lists
animals = ['dog', 'cat', 'birds']
#
# #lists are indexed -every object in the list has a related number starting at0
# #for the list above 0 = dog 1 = cat 2 = birds
# #how to refrence them
# #print(animals[0])
#
# #how to add another object to list
# #whats going on?
# #callig the append function of the list class that lets you add an item to the list
# animals.append('fish')
#
# #lists go in sequential order
# #looping through n list
# for this_animal in animals:
# #    print(this_animal)
#
# #finding an items index number
# #cat_index = animals.index('cat')
# #print(cat_index)
#
#
# ##########################################################
# #dictionaries
# #another type of container but it has keys and values and they are not in a certain order
family = {'brother_1': 'Ethan', 'brother_2': 'Zach', 'brother_3': 'Nathan', 'mother': 'Bridget', 'father': 'Steve'}
#
# #must know what the keys are ex: brother_1
# #print(family['brother_1'])
# #print(family['brother_1'])
#
#
# #can loop through dictionaries, but you re looping through the keys
# for this_key in family:
#     #print(family[this_key])

#animals.append(family)
#print(animals)

###########################################################
#Sets
# A set is a collection which is unordered, unchangeable*, and unindexed.
#cant have more than one item, cant add to sets
fruit_set = {'apple', 'grape', 'orange', 'apple'}

###########################################################
#Tuples
# ordered (indexed), duplicates, cant be added to,
a_tuple = ('nathan', 'suranie', '17', 'needs a haircut', '17')
#print(a_tuple[0])

#lengths
print(len(animals))
print(len(fruit_set))
print(len(family))
print(len(a_tuple))

#types
print(type(animals))

#loops
