#Write a program that counts the number of vowels in a sentence.
def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

# Example usage
user_input = input("Enter a sentence: ")
vowel_count = count_vowels(user_input)
print(f"Number of vowels: {vowel_count}")
