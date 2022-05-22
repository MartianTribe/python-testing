#this is different containers in python

#this is lists
animals = ['dog', 'cat', 'birds']

#lists are indexed -every object in the list has a related number starting at0
#for the list above 0 = dog 1 = cat 2 = birds
#how to refrence them
#print(animals[0])

#how to add another object to list
#whats going on?
#callig the append function of the list class that lets you add an item to the list
animals.append('fish')

#lists go in sequential order
#looping through n list
for this_animal in animals:
    #print(this_animal)

#finding an items index number
cat_index = animals.index('cat')
#print(cat_index)

##########################################################
#dictionaries
#another type of container but it has keys and values and they are not in a certain order
family = {'brother_1': 'Ethan', 'brother_2': 'Zach', 'brother_3': 'Nathan', 'mother': 'Bridget', 'father': 'Steve'}

#must know what the keys are ex: brother_1
#print(family['brother_1'])

#can loop through dictionaries, but you re looping through the keys
for this_key in family:
    print(family[this_key])

animals.append(family)
#print(animals)

###########################################################
#Sets
# A set is a collection which is unordered, unchangeable*, and unindexed.


###########################################################
#Tuples
