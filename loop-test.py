#loop testing
animals_array = ['dog', 'cat', 'mouse']

for this_animal in animals_array:
    print(this_animal)

animals_dict = {'cat': 'griffin', 'dog': 'pretzel', 'lizard': 'verbena'}

for this_key in animals_dict:
    if this_key == 'cat':
        print(animals_dict[this_key])



animals_set = {'dog', 'cat', 'mouse'}

for the_animals in animals_set:
    print(the_animals)



name_array = ['zack', 'nathan', 'ethan', 'zack']

name_set = {'zack', 'nathan', 'ethan', 'zack'}

array_name = len(name_array)
set_name = len(name_set)

print(array_name)
print(set_name)
