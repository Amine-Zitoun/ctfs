# Introduction
I participated in this at 11th of april 2020 and I got the rank of 198 out of 1076
link to ctftime: https://ctftime.org/event/932

# Boofy
it's a basic bufferoverflow to get to the get_flag function
flag:  `TG20{The real flag is much boofier than the other one}`

# Extract this
for this challenge we had to inject XML code to get the flag
flag: `TG20{never_trust_the_external_entities}`

# frequent
this is a cryptography challenge ,we were given an encrypted text 
using frequency analysis I was able to decode it
flag: `TG20{beginning_middle_end}`

# Key game
We were given a compiled python file, so I decompiled it and I got the code to the game
after bruteforcing Xs ,Ys,X1s,Y1s I got to the right flag
flag: `TG20{this flag should be on teh moon}`

# Number trouble
Noob cryptography challenge nothing much to it
flag: `TG20{numbers_and_text_goes_hand_in_hand}`

# Professor Doctrina
We were given a pickle file which is the model for the classification of the password on the 
website , and the model turned out to be a Decision tree model , I extracted the number of features
that the model trained on and they were five and I tried various numbers for these features
then when submitting a random password to the website turns out that these features were the length of 
the password which had to be 18 and the number of uppercase letters and the number of lowercase letters
and the number of digits and the number of special charachters 
flag:  `TG20{patterns_not_secured_by_AI}`

