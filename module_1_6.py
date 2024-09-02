my_dict = {'Kos': 2000, 'Lee': 1999}
print('Dict:', my_dict)
print('Existing value:', my_dict['Kos'])
print('Not existing value:', my_dict.get('Sam'))
my_dict.update({'Nil': 2001, 'Pop': 1998})
print('Deleted value:', my_dict.pop('Lee'))
print('Modified dictionary:', my_dict)

my_set = {1, 1, 2, 1, True, 'String'}
print('Set:', my_set)
my_set.update({'pool', 'pump'})
print('Modified set:', my_set)