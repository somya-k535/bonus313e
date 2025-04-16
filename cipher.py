"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Somya Krishna and Iniya Vidyashankar, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1:sk55256
UT EID 2:iv3976
"""


def rail_fence_encode(string, key):
    """
    pre: string is a string of characters and key is a positive
        integer 2 or greater and strictly less than the length
        of string
    post: returns a single string that is encoded with
        rail fence algorithm
    """
    grid = [["" for _ in range(len(string))] for _ in range(key)]
    direction = 1
    row = 0

    for col in range(len(string)):
        grid[row][col] = string[col]
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1

    return ''.join(''.join(r) for r in grid)

def rail_fence_decode(string, key):
    """
    pre: string is a string of characters and key is a positive
        integer 2 or greater and strictly less than the length
        of string
    post: function returns a single string that is decoded with
        rail fence algorithm
    """
    pattern = [0] * len(string)
    rail = 0
    dir_down = 1

    for i in range(len(string)):
        pattern[i] = rail
        rail += dir_down
        if rail == 0 or rail == key - 1:
            dir_down *= -1

    counts = [pattern.count(r) for r in range(key)]
    positions = [0] * key
    pos = 0
    for i in range(key):
        positions[i] = pos
        pos += counts[i]

    output = [''] * len(string)
    rail_indices = [0] * key

    for i, r in enumerate(pattern):
        index = positions[r] + rail_indices[r]
        output[i] = string[index]
        rail_indices[r] += 1

    return ''.join(output)


def filter_string(string):
    """
    pre: string is a string of characters
    post: function converts all characters to lower case and then
        removes all digits, punctuation marks, and spaces. It
        returns a single string with only lower case characters
    """
    cleaned = []
    for char in string.lower():
        if 'a' <= char <= 'z':
            cleaned.append(char)
    return ''.join(cleaned)

def encode_character(p, s):
    """
    pre: p is a character in the pass phrase and s is a character
        in the plain text
    post: function returns a single character encoded using the
        Vigenere algorithm. You may not use a 2-D list
    """
    shift = ord(p) - 97
    new = ord(s) + shift
    if new > 122:
        overflow = new - 122
        new = overflow + 96
    return chr(new)
def decode_character(p, s):
    """
    pre: p is a character in the pass phrase and s is a character
        in the encrypted text
    post: function returns a single character decoded using the
        Vigenere algorithm. You may not use a 2-D list
    """
    shift = ord(p) - ord('a')
    total = ord(s) - shift
    if total < ord('a'):
        total += 26
    return chr(total)


def vigenere_encode(string, phrase):
    """
    pre: string is a string of characters and phrase is a pass phrase
    post: function returns a single string that is encoded with
        Vigenere algorithm
    """
    cleaned_text = filter_string(string)
    extended = []
    i = 0
    while len(extended) < len(cleaned_text):
        extended.append(phrase[i])
        i = (i + 1) % len(phrase)
    return ''.join(encode_character(k, c) for k, c in zip(extended, cleaned_text))


def vigenere_decode(string, phrase):
    """
    pre: string is a string of characters and phrase is a pass phrase
    post: function returns a single string that is decoded with
        Vigenere algorithm
    """
    cleaned_cipher = filter_string(string)
    extended = []
    i = 0
    while len(extended) < len(cleaned_cipher):
        extended.append(phrase[i])
        i = (i + 1) % len(phrase)
    return ''.join(decode_character(k, c) for k, c in zip(extended, cleaned_cipher))


def main():
    """Main function that reads stdin and runs each cipher"""
    # read the plain text from stdin (terminal/input)

    # read the key from stdin (terminal/input)

    # encrypt and print the encoded text using rail fence cipher

    # read encoded text from stdin (terminal/input)

    # read the key from stdin (terminal/input)

    # decrypt and print the plain text using rail fence cipher

    # read the plain text from stdin (terminal/input)

    # read the pass phrase from stdin (terminal/input)

    # encrypt and print the encoded text using Vigenere cipher

    # read the encoded text from stdin (terminal/input)

    # read the pass phrase from stdin (terminal/input)

    # decrypt and print the plain text using Vigenere cipher
    import sys
    import sys
    input_data = sys.stdin.read().splitlines()
    plaintext_rf = input_data[0]
    key_rf = int(input_data[1])
    encoded_rf = rail_fence_encode(plaintext_rf, key_rf)
    print("Rail Fence Encoded:", encoded_rf)
    decoded_rf = rail_fence_decode(encoded_rf, key_rf)
    print("Rail Fence Decoded:", decoded_rf)
    plaintext_vig = input_data[4]
    phrase_vig = input_data[5]
    encoded_vig = vigenere_encode(plaintext_vig, phrase_vig)
    print("Vigenere Encoded:", encoded_vig)
    decoded_vig = vigenere_decode(encoded_vig, phrase_vig)
    print("Vigenere Decoded:", decoded_vig)
# Do NOT modify the following code.
if __name__ == "__main__":
    main()
