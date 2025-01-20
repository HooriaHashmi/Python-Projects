def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

def count_consonants(input_string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in input_string:
        if char in consonants:
            count += 1
    return count

def main():
    user_input = input("Enter a string: ")
    num_vowels = count_vowels(user_input)
    num_consonants = count_consonants(user_input)
    
    print("Number of vowels:", num_vowels)
    print("Number of consonants:", num_consonants)


if __name__ == "__main__":
    main()