my_dict = {'Pasha': 1976, 'Oleg': 1979, 'Yura': 1973}
print('Dict:', my_dict)
print('Existing value:', my_dict['Oleg'])
print('Not existing value:', my_dict.get('Lena'))
my_dict.update({'Sasha': 1980, 'Zhenya': 1983})
a = my_dict.pop('Yura')
print('Deleted value:', a)
print('Modified dictionry:', my_dict)
print()
my_set = {1, 5, 'Tort', 5, 'Vasya', 'Tort'}
print('Set:', my_set)
my_set.update([14, 'boss'])
my_set.remove(1)
print('Modified set:', my_set)
