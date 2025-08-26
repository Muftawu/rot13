alphabets_latin = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "x", "y", "z"]
alphabets_english = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(len(alphabets_english))
cutoff = 12

def get_rot13(letter: str, alphabet_type: str = "latin"):
    alphabets = alphabets_latin if type == "lating" else alphabets_english  
    out = None

    if not isinstance(letter, str):
        raise Exception("letter must be a str instance")

    if len(alphabets) < 23:
        raise Exception("rot13 requires alphabet size of 23")

    if not letter in alphabets:
        raise Exception("letter must be in the latin alphabets")

    try:
        letter_index = alphabets.index(letter)
        if letter_index:
            letters_before = alphabets[:letter_index]
            letters_after = alphabets[letter_index+1:]
            working_array = letters_after if len(letters_after) >= 13 else letters_after + letters_before
            out = working_array[cutoff]
    except Exception as e:
        print(f"Failed to get rot13 for {letter} => {str(e)}")
    return out

if __name__ == "__main__":
    letter = "hello"
    [print(f"{let} => {get_rot13(let, 'eng')}", sep=" ") for let in letter]
    


