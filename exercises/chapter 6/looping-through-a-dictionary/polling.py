favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

coders = ['david', 'michael', 'jen', 'franklyn', 'phil']

for coder in coders:
    if coder in favorite_languages:
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        print(f"{coder.title()}, what's your favorite programming language?")