# Professor Wordlist
Professor Wordlist is a free open source command line tool written in python, With the aim of generating custom wordlists with a variety of unique parameters and functions providing many possibilities.

       ---------------------------------------------Positional arguments---------------------------------------------:

              string         The String is a required parameter.  [%d, %s, %l, %L, %w, %W, %X, %Y, %Z]

                 %d : digit [1-9]            %l : lowercase letter [a-z]   %w : Wordlist word's
                 %s : symbol [!@#$%^&?*]     %L : Uppercase letter [A-Z]   %W : Custom Word/s
                 %X : Custom List            %Y : Custom list #2           %Z : Custom list #3

       ---------------------------------------------Optional arguments---------------------------------------------:

          -h | --help            show this help message and exit
  
          -C | --custom          A custom list for characters of your choice, replace %X. 
          
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
          
          
 Any suggestions to improve the software please let me know!
 Open to all Ideas and Improvements!
 
        Discord #Oakzeh5250
        Email: byoakk@gmail.com
        twitter @Oakzeh

 The software is free to use! 
 Feel Free to support me below :)

        https://www.paypal.me/oakzeh 
        https://www.patreon.com/oakzeh 
        
## USAGE & EXAMPLES
                                                 
> pw.py test%d                     
       
       test0         test5         "digits"    
       test1         test6         range [0-9]       
       test2         test7
       test3         test8
       test4         test9
       
       
> pw.py test%l
       
       testa         testb         "lowercase"
       testc         testd          range [a-z]
       teste         testf         ...
       
       
> pw.py test%L
     
       testA         testB         "uppercase"
       testC         testD          range [A-Z]
       testE         testF         ...
             

> pw.py test%s
     
       test!         test@         "basic symbols"
       test#         test$          range [!@#$%^&?*]
       test%         test*          ...
             
   
> pw.py test%X -C ABC123
     
       testA         testB         "custom range"
       testC         test1          range [ABC123]
       test2         test3          ...

> pw.py %W_%d -W Red Blue Green
     
       Red_0          Red_1  ...       "custom Words"
       Blue_0         Blue_1  ...        -W --words
       Green_0        Green_1  ...              
             
             
> pw.py replace_input%s -S -r replace test
     
       test_input#         test_input!         "Replace"
       test_input@         test_input$          -r --replace
       test_input%         test_input^           ...
 
              
> pw.py %L%d%d%d%s --output outputfile.txt
          
          ...
          U999*           X999*
          V999*           Y999*
          W999*           Z999*
          
          234000 combinations have been successfully written to outputfile.txt
   
         
> pw.py %w_%L_%s -S -L --wordlist list.txt -o  outputfile.txt --noprint
     
       1664 combinations have been successfully written to outputfile.txt
       
       *Wordlist (--wordlist or -w), All letters (-L), Comprehensive Symbol range (-S or --symbols), 
       Output (-o or --output) and not print every combination (-np or --noprint)*

                    
       
