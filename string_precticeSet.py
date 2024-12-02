a = input("Enter your name dear user...\n")
print(f"Good moring {a}")

#TO change given name and date___________
letter = '''Dear  <|name|>,
            you are selected!
                            <|date|>'''

print(letter.replace("<|name|>","meet").replace("<|date|>","10,2,3"))

#to find double space___________________
print(letter.find("  "))
