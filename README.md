GOING TO ADD A GUI SOON!


# password_generator
This is a small side project I am building, bit by bit.

I plan to create a fully working password generator that I can use, features will be added gradually.

The entire script may change as I learn and dedicate more time towards the project, for now I am using the libraries: random, string and csv to generate a set of random strings, symbols and numbers, that are then written to a csv file.

#Update 1: 

Replaced the random module with the secrets, it seems that the random library is not so random afterall.
Also made it so that the generated password is hashed before being written to the csv file.

#Update 2:

Shortened the number of generated passwords to just one.
Added a while loop that lets the user decide if they want to include special characters or not.
Added a while loop that enforces a minimum of characters in a password (10 to be exact), although the way it is written now, the password function chooses a random number between 0 and 9, and adds whatever the user inputs, so if the user inputs the number 10, and the random number for the specific password is 5, the result will be 15 charcters.

Updated the read me, as I though the comment I added when I commited the changes will update the read me (??) lol.

#Update 3:

Added some comments, and fixed some typos.