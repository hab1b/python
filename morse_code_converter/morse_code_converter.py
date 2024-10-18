# Dictionary for Morse code representation
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Function to convert a string to Morse code
def text_to_morse(text):
    morse_code = ""
    for char in text.upper():  # Convert input text to uppercase
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "  # Add space between Morse symbols
        else:
            morse_code += ""  # Handle characters not in Morse dictionary
    return morse_code.strip()

# Main Program
def main():
    print("Welcome to the Morse Code Converter!")
    user_input = input("Enter a message to convert to Morse Code: ")
    result = text_to_morse(user_input)
    print(f"Morse Code: {result}")

if __name__ == "__main__":
    main()