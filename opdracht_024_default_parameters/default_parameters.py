def greet(name, greeting="Hello"):
    print(f"{greeting} {name}!")


greet("Daan", "Sup")


def greet_complete(name, greeting_sentence=" I hope you are well?"):
    print(greeting_sentence.replace("*name*", name))


greet_complete("Hank", "Hey *name*! How are you?")
