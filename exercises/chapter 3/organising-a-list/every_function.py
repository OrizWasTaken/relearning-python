# my desire list
desire = ['jesus', 'peace', 'usa', 'uapb', 'harvard', 'women', 'fish', 'success']
print("my desire list:")
print(desire)

# list.append()
desire.append('fun')
print("\nappended 'fun' to the end of my desire list:")
print(desire)

# list.insert()
desire.insert(2, 'happiness')
print("\ninserted 'happiness' before 'usa' in my desire list:")
print(desire)

# del
del desire[5]
print("\nremoved 'harvard' from my desire list:")
print(desire)


# list.pop()
print(f"\nremoving '{desire.pop(5)}' from my desire list:")
print(desire)

# list.remove()
desire.remove("fish")
print ("\nremoved 'fish' from my desire list:")
print(desire)

# sorted()
print("\nmy desire list in alphabetical order:")
print(sorted(desire))

# list.reverse()
desire.reverse()
print("\nreversed the order of my desire list:")
print(desire)

# list.sort()
desire.sort(reverse=True)
print("\nsorted my desire list in reverse-alphabetaicl order:")
print(desire)


# len()
print(f"\nthere are currently {len(desire)} desires in my desire list")


