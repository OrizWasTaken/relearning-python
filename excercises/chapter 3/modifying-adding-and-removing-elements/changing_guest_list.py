# guest list
guests = ["Albert Einstein", "Maya Angelou", "Elon Musk"]

# dinner invitation
print(f"Dear {guests[0]}, let's talk about the universe over dinner")
print(f"Dear {guests[1]}, please join me for dinner!")
print(f"Dear {guests[2]}, hope you can make it!")

# Elon can't make it :(
print(f"\nIt's unfourtunate you can't make it, {guests[2]}\n")

# inviting Michael, instaed
guests[2] = "Michael Faraday"

#new dinner invitation
print(f"Dear {guests[0]}, let's talk about the universe over dinner")
print(f"Dear {guests[1]}, please join me for dinner!")
print(f"Dear {guests[2]}, hope you can make it!")
