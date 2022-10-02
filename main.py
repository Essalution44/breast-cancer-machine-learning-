alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("type 'encode' to encrypt type 'decode' to decrypt:\n")
text=input("type your message\n").lower()
shift=int(input("type shift number\n"))
def caeser(direction,text,shift):
        Endtext=""
        shift=shift%26
        if direction == "decode":
            shift *= -1
        for letter in text:
            position=alphabet.index(letter)
            new_position=position+shift
            Endtext+=alphabet[new_position]
        print(f"the {direction}d text is {Endtext}")
caeser(direction,text,shift)
#essalution44
