import re

string = 'abcbd abcdb'

find = re.findall('a[bcd]*b', string)

print(find)


import re

exampleString = '''
Jsscica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''

ages = re.findall('\d{1,3}', exampleString)
names = re.findall('[A-Z][a-z]*', exampleString)

print(ages)
print(names)


import re
example = '222222222222222222222233'
result = re.fullmatch('\S{3,20}', example)

if result:
    print('1')
else:
    print('2')

