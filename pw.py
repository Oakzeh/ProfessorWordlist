# Professor Wordlist
from itertools import product
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description='''
 ,ggggggggggg,                                                                            ,ggg,      gg      ,gg                                                           
dP"""88""""""Y8,                  ,dPYb,                                                 dP""Y8a     88     ,8P                             8I ,dPYb,                 I8   
Yb,  88      `8b                  IP'`Yb                                                 Yb, `88     88     d8'                             8I IP'`Yb                 I8   
 `"  88      ,8P                  I8  8I                                                  `"  88     88     88                              8I I8  8I gg           88888888
     88aaaad8P"                   I8  8'                                                      88     88     88                              8I I8  8' ""              I8   
     88""""",gggggg,    ,ggggg,   I8 dP  ,ggg,     ,g,      ,g,      ,ggggg,   ,gggggg,       88     88     88  ,ggggg,   ,gggggg,    ,gggg,8I I8 dP  gg     ,g,      I8   
     88     dP""""8I   dP"  "Y8gggI8dP  i8" "8i   ,8'8,    ,8'8,    dP"  "Y8gggdP""""8I       88     88     88 dP"  "Y8gggdP""""8I   dP"  "Y8I I8dP   88    ,8'8,     I8   
     88    ,8'    8I  i8'    ,8I  I8P   I8, ,8I  ,8'  Yb  ,8'  Yb  i8'    ,8I ,8'    8I       Y8    ,88,    8Pi8'    ,8I ,8'    8I  i8'    ,8I I8P    88   ,8'  Yb   ,I8,  
     88   ,dP     Y8,,d8,   ,d8' ,d8b,_ `YbadP' ,8'_   8),8'_   8),d8,   ,d8',dP     Y8,       Yb,,d8""8b,,dP,d8,   ,d8',dP     Y8,,d8,   ,d8b,d8b,__,88,_,8'_   8) ,d88b, 
     88   8P      `Y8P"Y8888P"   PI8"88888P"Y888P' "YY8P8P' "YY8P8P"Y8888P"  8P      `Y8        "88"    "88" P"Y8888P"  8P      `Y8P"Y8888P"`Y8P'"Y88P""Y8P' "YY8P8P8P""Y8 
                                  I8 `8,                                                                                                                                   
                                  I8  `8,                  Professor Wordlist v1.0                                                                                                 
                                  I8   8I           ---------------------------------------                                                                                                                       
                                  I8   8I           https://github.com/Oakzeh/ProfessorWordlist                                                                                                             
                                  I8, ,8'                                                                                                                                  
                                   "Y8P'                                                                                                                                                                                                                         
''', formatter_class=RawTextHelpFormatter)

parser._positionals.title = '--------------------------------------------------Positional arguments--------------------------------------------------'
parser._optionals.title = '--------------------------------------------------Optional arguments--------------------------------------------------'
parser.add_argument(dest='string',
                    help='''The String is a required parameter. ~ [%%d, %%s, %%l, %%L, %%w, %%W, %%X, %%Y, %%Z]
                
%%d : digit [1-9]            %%l : lowercase letter [a-z]    %%w : Wordlist word's
%%s : symbol [!@#$%%^&?*]     %%L : Uppercase letter [A-Z]    %%W : Custom Word/s
%%X : Custom List            %%Y : Custom list #2            %%Z : Custom list #3
''')

parser.add_argument('-C', '--custom', type=str, metavar='\b', default='',
                    help='    A custom list for characters of your choice, replace %%X. E.g. test_%%X -C "123"')

parser.add_argument('-C2', '--custom2', type=str, metavar='', default='',
                    help='A Second list for custom characters, replace %%Y.')

parser.add_argument('-C3', '--custom3', type=str, metavar='', default='',
                    help='A Third list for custom characters, replace %%Z.')

parser.add_argument('-W', '--words', type=str, nargs="+", default="[]", metavar='',
                    help="Replace %%W, please add words, -W word1 word2")

parser.add_argument('-w', '--wordlist', type=str, default='', metavar='', help="Replace %%w, file path: -w list.txt")

parser.add_argument('-r', '--replace', type=str, metavar='', default='',
                    nargs=2, help='Replace Any Character of your choice. -r a 1')

parser.add_argument('-L', '--letters', type=str, nargs='?', default=True, const=False, metavar='',
                    help="All Letters, %%L will represent lowercase and capital alphabet range [a-zA-Z]")

parser.add_argument('-S', '--symbols', type=str, nargs='?', default='!@#$%^&?*',
                    const='#!@$%^&*?()_-+={[}]|\:;"\'<,>.`/', metavar='',
                    help='Uses the full comprehensive symbol range when replacing %%s:  \nFull list:  #!@$%%^&*?()_-+={[}]|\:;"\'<,>.`/')

parser.add_argument('-np', '--noprint', type=str, nargs='?', default=True, const=False, metavar='',
                    help="No Print: Will not print each combination.")

parser.add_argument('-o', '--output', type=str, default='', metavar='', help="file path: -o test.txt")

args = parser.parse_args()

string = args.string
custom = args.custom  # Custom List 1
custom2 = args.custom2  # Custom List 2
custom3 = args.custom3  # Custom List 3
symbols = args.symbols  # Symbol range increase
output = args.output  # output for file save
noprint = args.noprint
letters = args.letters  # %L [a-zA-Z]
word_location = args.wordlist  # %w wordlist
words_input = args.words  # %W word input
replace = args.replace
# Variables being set
# ---------------------------------------------------------------------------------------------------------------------

commands = ["%d", "%s", "%l", "%L", "%w", "%W", "%X", "%Y", "%Z"]


def wordlist(location):
    wordlist_array = []
    try:
        f = open(location, "r")
        for line in f:
            wordlist_array.append(line.strip("\n"))
        if wordlist_array:
            return wordlist_array
    except FileNotFoundError as error:
        if word_location:
            print(error, "\nPlease specify wordlist path when using %w")
            # Error prevention only if user entered a location

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if not letters:
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # -L Command changes character range for %L

if output != '':
    file = open(output, "a")
# openfile for adding wordlist
# --------------------------------------------------------------------------------------
if any(x in string for x in commands):
    # Checks to see if any commands are in the string
    count = 0

    wlist = wordlist(word_location)

    if not words_input:
        words_input = ["%W"]

    if not wlist:
        wlist = ["%w"]

    if not custom:
        custom = ["%X"]

    if not custom2:
        custom2 = ["%Y"]

    if not custom3:
        custom3 = ["%Z"]

    word_input_parts = string.split("%W")
    num_custom_words = len(word_input_parts) - 1

    for custom_words in product(words_input, repeat=num_custom_words):
        word = ("".join(word_part + word for word_part, word in zip(word_input_parts, custom_words))) + \
               word_input_parts[-1]

        word_parts = word.split("%w")
        num_words = len(word_parts) - 1

        for words in product(wlist, repeat=num_words):
            word = ("".join(word_part + word for word_part, word in zip(word_parts, words))) + word_parts[-1]

            parts = word.split("%d")
            num_digits = len(parts) - 1

            for digits in product("0123456789", repeat=num_digits):
                word = ("".join(part + digit for part, digit in zip(parts, digits))) + parts[-1]

                symbol_parts = word.split("%s")
                num_symbols = len(symbol_parts) - 1

                for symbol in product(symbols, repeat=num_symbols):
                    word = ("".join(symbol_part + symbol for symbol_part, symbol in zip(symbol_parts, symbol))) + \
                           symbol_parts[
                               -1]

                    letter_parts = word.split("%l")
                    num_letters = len(letter_parts) - 1

                    for letter in product("abcdefghijklmnopqrstuvwxyz", repeat=num_letters):
                        word = ("".join(letter_part + letter for letter_part, letter in zip(letter_parts, letter))) + \
                               letter_parts[-1]

                        cap_parts = word.split("%L")
                        num_cap = len(cap_parts) - 1

                        for cap in product(alphabet, repeat=num_cap):
                            word = ("".join(cap_part + cap for cap_part, cap in zip(cap_parts, cap))) + cap_parts[-1]

                            cus_parts = word.split("%X")
                            num_cus = len(cus_parts) - 1

                            for cus in product(custom, repeat=num_cus):
                                word = ("".join(cus_part + cus for cus_part, cus in zip(cus_parts, cus))) + \
                                       cus_parts[
                                           -1]

                                cus2_parts = word.split("%Y")
                                num_cus2 = len(cus2_parts) - 1

                                for cus2 in product(custom2, repeat=num_cus2):
                                    word = ("".join(
                                        cus2_part + cus2 for cus2_part, cus2 in zip(cus2_parts, cus2))) + \
                                           cus2_parts[-1]

                                    cus3_parts = word.split("%Z")
                                    num_cus3 = len(cus3_parts) - 1

                                    for cus3 in product(custom3, repeat=num_cus3):
                                        word = ("".join(
                                            cus3_part + cus3 for cus3_part, cus3 in zip(cus3_parts, cus3))) + \
                                               cus3_parts[-1]

                                        count += 1

                                        if replace:
                                            word = word.replace(str(replace[0]), str(replace[1]))

                                        if output != '':
                                            file.write(f'{word}\n')

                                        if noprint:
                                            print(word)

    if output != '':
        print(f"{count} combinations have been successfully written to {output}")
        file.close()
    else:
        print(f"\nTotal Combinations is : {count}")

else:
    print("\nNo parameters have been added. \n\n-h or --help, for usage details.")
    exit()
