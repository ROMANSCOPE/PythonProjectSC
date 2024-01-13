'''
    Code Crypter : It is capable to convert a value to Cipher Code & Cipher Code to original value
'''

# 1. Instead to write print, I wanna write myName there
roman = print

# 2. COLORS : dictinary to store color ANSI values
color = { 'CYAN': "\033[38;5;51m", 'RED': "\033[38;5;196m", 'ORANGE': "\033[38;2;255;165;0m", 'RESET': "\033[0m", 
          'MAGENTA': "\033[38;5;201m" }

# 3. TITLE : writing title of this program
roman (f"\n\t{color ['CYAN']} ---$--- Code Crypter ---$--- {color ['RESET']}")


# 6-(b). CIPHER KEY : dictionary to store key's cipher key
cipherKey = { 0: '/0', 1: 'xxx', 2: '$$', 3: '@!', 4: '__', 5: '?c', 6: 'ce', 7: '/_*', 8: '##', 9: '@|o'  }


# 6-(a). DIGIT COUNTER : function to check is this value have all the chars is digit
def isDigit (value) :
    # (i). Return True only when all the chars return True otherwise False
    return all (map (lambda x: x.isdigit(), value))


# 6. ENCODER : function to convert value to cipher code
def roseEncode () :

    # (i). LOOP : keep taking input from a user till the value is expected
    while True :

        # (ii). TAKE VALUE : take input & store to this variable
        value = input ("\n2. Enter Only Digits Here : ")

        # (v). ENCODING : store encode value here
        encode = ''

        # (iii). CATCH OR LEAVE : condition to catch unpected token otherwise Go Ahead
        if isDigit (value) :
            # (iv). CIPHER CODE LOOP : using for loop to convert value to cipher code
            for key in value :
                # (vi). encode storing
                encode += cipherKey [int (key)]

            # (vii). RESULT : now the time is to return the encode value
            roman (color ['MAGENTA'])
            roman (f"   Cipher Code : {encode}")

            # at the end break it
            break
            
        else :
            roman ( f"{color['ORANGE']}Capable only for whole numbers {color ['RESET']}" )


# 7. DECODER : function to decode the given encode
def sweetlyDecode () :
    roman ("I am Decoder.")


# 4. Main Function
def main () :
    # (i). CHOOSE MODE : take mode & store to this variable
    mode = input ("\n1. Want To Encode Or Decode (e/d) : ").lower ()

    # (ii). MODE COUNTER : using `match` statment to check the mode
    match mode :
        # (a). ENCODE MODE
        case 'e' :
            roseEncode ()

        # (b). DECODE MODE
        case 'd' :
            sweetlyDecode ()

        # (c). UNEXPECTED TOKEN
        case _ :
            roman ( f"\n{color['RED']}   MODE ERROR : choose valid mode ..." )
    



# 5. EXECUTE : run only these programs when this file will be excuted
if __name__ == '__main__' :
    main ()