import sys

alphabets_latin = list("abcdefghijklmnopqrstvxyz")
alphabets_english = list("abcdefghijklmnopqrstuvwxyz")
cutoff = 12

def get_rot13(letter: str, alphabet_type: str = "latin"):
    alphabets = alphabets_latin if type == "latin" else alphabets_english  
    out = None

    if not isinstance(letter, str):
        raise Exception("letter must be a str instance")

    if len(alphabets) < 23:
        raise Exception("rot13 requires alphabet size of 23")

    if not letter in alphabets:
        raise Exception("letter must be in the latin alphabets")

    try:
        letter_index = alphabets.index(letter)
        if letter_index.is_integer():
            letters_before = alphabets[:letter_index+1] 
            letters_after = alphabets[letter_index+1:]
            working_array = letters_after if len(letters_after) >= 13 else letters_after + letters_before
            out = working_array[cutoff] if working_array[cutoff] is not None else alphabets[cutoff]
    except Exception as e:
        print(f"Failed to get rot13 for {letter} => {str(e)}")
    return out

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(f"Running rot13 for {sys.argv[1]} with type {sys.argv[2]}")
        letter = sys.argv[1]
        alphabet_type = sys.argv[2]
    else:
        print("sys args less than 2. Using default string 'hello' with type 'latin'")
        letter = "hello"
        alphabet_type = "latin"
    res = ''.join([f"{get_rot13(let, {alphabet_type})}" for let in letter])
    print(f"{letter} => {res}")
    


