# Professor Wordlist
Professor Wordlist is a free open source command line tool written in python, With the aim of generating custom wordlists with a variety of unique parameters and functions providing many possibilities.

--------------------------------------------------Positional arguments--------------------------------------------------:

  string                The String is a required parameter.  [%d, %s, %l, %L, %w, %W, %X, %Y, %Z]

                        %d : digit [1-9]            %l : lowercase letter [a-z]   %w : Wordlist word's
                        %s : symbol [!@#$%^&?*]     %L : Uppercase letter [A-Z]   %W : Custom Word/s
                        %X : Custom List            %Y : Custom list #2           %Z : Custom list #3

--------------------------------------------------Optional arguments--------------------------------------------------:

  -h | --help            show this help message and exit
  
  -C | --custom          A custom list for characters of your choice, replace %X. Example: test_%X -C "ÀÐÈ123&!"
  
  -C2 | --custom2        A Second list for custom characters, replace %Y.
  
  -C3 | --custom3        A Third list for custom characters, replace %Z.
  
  -W | --words           Replace %W, please add words
                        
  -w | --wordlist        Replace %w, file path: -w list.txt
  
  -r | --replace         Replace Any Character of your choice. -r a 1
  
  -L | --letters         All Letters, %L will represent lowercase and capital alphabet range [a-zA-Z]
  
  -S | --symbols         Uses the full comprehensive symbol range when replacing %s:
                         Full list: -->   #!@$%^&*?()_-+={[}]|\:;"'<,>.`/  
                        
  -np | --noprint        No Print: Will not print each combination.
  
  -o | --output          file path: -o test.txt

