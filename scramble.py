import itertools

# Function to generate all possible substrings of a word
def generate_substrings(word):
    substrings = set()
    for i in range(2, len(word) + 1):
        for perm in itertools.permutations(word[1:-1], len(word) - 2):
            substr = word[0] + ''.join(perm) + word[-1]
            substrings.add(substr)
    return substrings

def count_substrings(str1,str2):
    # Read the dictionary file and create a set of valid dictionary words and their scrambled forms
    dictionary = set()
    with open(str1, "r") as dict_file:
        for line in dict_file:
            word = line.strip()
            dictionary.add(word)
            dictionary.update(generate_substrings(word))

    # Read the input file and search for dictionary words
    with open(str2, "r") as input_file:
        input_lines = input_file.read().splitlines()

    # Process each input line
    for i, line in enumerate(input_lines, start=1):
        count = 0
        for j in range(len(line)):
            for k in range(j + 1, len(line) + 1):
                substring = line[j:k]
                if substring in dictionary:
                    count += 1
        print(f"Case #{i}: {count}")

if __name__ == "__main__":
    count_substrings("dictionary.txt", "input.txt")

