

# morse code equivalents 
morse_codes = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', 

    '0': '-----', '1': '.----', '2': '..---',
     '3': '...--', '4': '....-', '5': '.....','6': '-....', '7': '--...', 
     '8': '---..', '9': '----.', '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', 
     '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
    '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }

# message = 'AB # BC'

class Morse_Message_Vice_versa:

    def __init__(self, message):
        super().__init__()
        # Define the global message variable.
        self.message = message

    def Morse_encoder(self):
        # how to split words based on spaces - ['AB', '"', 'CD']
        message_upper = self.message.upper()
        print(message_upper)
        list_1 = message_upper.split()

        #Now to access each letter in words - 'AB' - ['A', 'B']
        final_morse_letters = []
        for i in range(len(list_1)): 
            temp = list(list_1[i])
            # print(temp)
            new_list = []
            for letter in temp:
                # Assign equalivalent morse code value from dictonary Key to Variable.
                try:
                    temp_letter = morse_codes[str(letter)]
                    new_list.append(temp_letter)
                except KeyError:
                    print("You seem to have entered a Character having no equivalent Morse code.")
                    new_list.append(str(letter))
                    break
            # Join the individual letters back to words with spaces between each letter Morse code.
            morse_letter = ' '.join(new_list)
            # Combine it finally back to Morse code equivalent message.
            final_morse_letters.append(morse_letter)
        final_morse_message = '|'.join(final_morse_letters)
        return self.message, final_morse_message  


