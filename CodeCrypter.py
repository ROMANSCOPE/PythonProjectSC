'''
    Code Crypter : It is capable to convert a value to Cipher Code & Cipher Code to original value
'''

# 1. Instead to write print, I wanna write myName there
roman = print

# 2. COLORS : dictinary to store color ANSI values
color = { 'CYAN': "\033[38;5;51m", 'RED': "\033[38;5;196m", 'ORANGE': "\033[38;2;255;165;0m", 'RESET': "\033[0m", 
          'MAGENTA': "\033[38;5;201m", 'BLUE': "\033[38;5;33m" }

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

    # (i). MODE PRINTER : print the mode 
    roman ( f"\n\t{color ['BLUE']} $ ENCODE MODE $ {color ['RESET']}" )

    # (ii). LOOP : keep taking input from a user till the value is expected
    while True :

        # (iii). TAKE VALUE : take input & store to this variable
        value = input ("\n2. Enter Only Digits Here : ")

        # (vi). ENCODING : store encode value here
        encode = ''

        # (v). CATCH OR LEAVE : condition to catch unpected token otherwise Go Ahead
        if isDigit (value) :
            # (vi). CIPHER CODE LOOP : using for loop to convert value to cipher code
            for key in value :
                # (vii). encode storing
                encode += cipherKey [int (key)]

            # (viii). RESULT : now the time is to return the encode value
            roman (f"{color ['MAGENTA']}   CIPHER CODE : {encode}")

            # at the end break it
            break
            
        else :
            roman ( f"{color['ORANGE']}Capable only for whole numbers {color ['RESET']}" )


# 7. DECODER : function to decode the given encode
def sweetlyDecode () :
    # (i). MODE PRINTER : print the mode on the terminal
    roman ( f'\n\t {color ['BLUE']} $ DECODE MODE $ {color ['RESET']}' )
    
    # (ii). INPUT ENCODE : keep taking encode till the encode is expected
    while True :
        # (iii). ENCODE TAKER : take encode from a user & store to this variable
        cipherCode = input ("\n2. Enter Encode Super Carefully : ")

        # DECODE : save decode value to this variable
        decode = ''

        # (iv). REPEAT THE DECODE PROCESS : keep repeating the decoding process till it will not decode it
        while True :
            # (v). ask each iteration to make sure need to break or not
            needToBreak = True

            # (vi). MATCHER LOOP : try to decode the encode
            for key in range (0, 10) :

                # (a). MATCH LENGTH : try to match encode length to cipher code key's length
                if len (cipherKey [key]) <= len (cipherCode) :

                    # (b). store key's value to this variable
                    code = cipherKey [key]

                    # (c). MATCH KEY : try to match key to cipher code
                    if cipherCode [:len (code)] == code :
                        decode += str (key)
                        needToBreak = False
                        
                        # (d). Remove matched code
                        cipherCode = cipherCode [len (code) : len (cipherCode)]

            # (vii). Check It : after completing each iteration check is this encode is unexpected
            if needToBreak :
                roman ( f'{color ['ORANGE']}enter valid cipher code ... {color ['RESET']}' )
                break

            # (viii). Break this loop when it is get resolved
            if len (cipherCode) == 0 :
                break

        
        # (viii). RESULT : print result if encode is completely decode
        if len (cipherCode) == 0 :
            roman ( f'{color ['MAGENTA']}  ORIGINAL VALUE : {decode}', color ['RESET'] )
            break


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