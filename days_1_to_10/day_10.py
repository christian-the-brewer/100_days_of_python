#Day 10

def format_name(f_name, l_name):
    """"An example of a function that titles a first and last name"""
    if f_name == "" or l_name == "":
        return print("invalid inputs")

    return f"{f_name.title()} {l_name.title()}"

print(format_name( "", "brewer"))

format_name()

