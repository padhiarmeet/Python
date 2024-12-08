alien = {'color':'white','size':'xl'}
# print(alien['color'])

aliens = {
    'type': {
        'st': {
            's3':'Demogorgon',
            's2':'Demodog',
            's3':'Mindfleyer',
            's4':'Vecna'
        }
    }
}
print(aliens['type']['st']['s3'])

aliens['hero'] = 'Hopper...hop..hop...'

# print(aliens)

del aliens['hero']

# print(aliens['type'].get('st','this is not exist')) #if you dont provide second arg it will return none.

for key,value in aliens.items():
    print(key)
    print(value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for key,value in favorite_languages.items():
    print(f"{key} loves to learn {value}.")

for name in favorite_languages:
    print(name)

if 'meet' not in favorite_languages.keys():
    print("Meet is not in list bro..")

for key in sorted(favorite_languages.keys()): #You can also use it like this..
    print(key)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
  }

for name,language in favorite_languages.items():
    print(f"\n {name}'s favourite language is ")
    for lan in language:
        print(f"\t{lan}")
