import sys

braille_chars = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

braille_unique = {'capital': '.....O', 'number': '.O.OOO'}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

def english_to_braille(string):
    result = ''
    is_number = False

    for char in string:
        if char.isdigit():
            if not is_number:
                is_number = True
                result += braille_unique['number']
            result += braille_numbers[char]
        elif char == ' ':
            is_number = False
            result += braille_chars[' ']
        elif char.isalpha():
            if char == char.upper():
                result += braille_unique['capital']
            result += braille_chars[char.lower()]
        else:
            result += '......'  # Fallback for unmapped characters

    return result

def main():
    message = ' '.join(sys.argv[1:])
    print(english_to_braille(message))

if __name__ == "__main__":
    main()
