def sandwich(*items):
    """Displays summary of a sandwich to be made"""
    print("\nLet's make you a delicious sandwich.")
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

sandwich('mustard')
sandwich('hard boiled eggs', 'cucumber', 'tomatoes', 'lettus')
sandwich('mustard', 'cucumber')