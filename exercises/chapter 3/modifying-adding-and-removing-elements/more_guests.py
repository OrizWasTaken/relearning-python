# guest list
guests = ["Albert Einstein", "Maya Angelou", "Elon Musk"]

# dinner invitation
print(f"Dear {guests[0]}, let's talk about the universe over dinner")
print(f"Dear {guests[1]}, please join me for dinner!")
print(f"Dear {guests[2]}, hope you can make it!")

# I got a bigger table!
print("\nI got a bigger table. Now, I can I invite more guests!\n")

# adding more guests
guests.insert(0,"Leonardo da Vinci") # added to the beginning of the list
guests.insert(2, "Oprah Winfrey") # added to the middle of the list
guests.append("Nelson Mandela") # added to the end of the list

#new dinner invitation
print(f"Dear {guests[0]}, let's talk about the universe over dinner")
print(f"Dear {guests[1]}, please join me for dinner!")
print(f"Dear {guests[2]}, hope you can make it!")
print(f"Dear {guests[3]}, please join me for an evening of great conversation.")
print(f"Dear {guests[4]}, I would love to have you for dinner!")
print(f"Dear {guests[5]}, it would be an honor to dine with you!")


