import json


def some_things():
    my_list = [(v, v) for v in range(1, 20) if v % 2 == 0]
    print(my_list)

    in_file = "input.json"
    out_file = "output.json"

    with open(in_file, "r") as f:
        contents = f.read()
        second_content = json.load(f)
        lines = f.readlines()

    with open(out_file, "w") as f:
        json.dump("some lines")


def load_user_name():
    # Load the username, if it has been stored previously.
    # Otherwise, prompt for the username and store it.
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")


def get_formatted_name(name, surname):
    formatted = name + " " + surname
    return formatted.title()
