greeting = "Hi!"
print(greeting)

username = input("What's your name?")
print(f"Its nice to meet you, {username}.")

print("What is your favorite food?")
print("My favorite food is sushi.")
fav_food = input()
print(f"I like to eat {fav_food} too!")

print("What is your favorite number?")
fav_number = input()
print("My favorite number is 7.")

print(f"It was nice talking to you, {username}!")


# 8. Try out branching
want_cookies = True
want_chips = True

if want_cookies and want_chips:
    print("You get both!")
else:
    print("You get none.")  # this will print
