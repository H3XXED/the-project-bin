# Chapter 7 Writing clear prompts

# name = input("Please enter your name: ")

prompt = "If you share your name, we can personalize the message for you to see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
