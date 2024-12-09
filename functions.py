# def greet_users(**kwargs):
#     print(f"Hello my dear {kwargs.title()}")
# greet_users("Meet")

def combined_function(*args,**kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

combined_function(1, 2, 3, name="Bhai", age=20,meet = "Badshah")
