# passwordentropy
Calculate the entropy of your password with the help of compression.

# Idea
The idea is to be able to validate a humangenerated password against a dictionary-attack.
This is done by using a known passwordfile.
1. Append your password to the end of the file
2. Compress both the file with your password and the original passwordfile. 
3. The amount of entropy your password has is the difference in filesize. This is approximately the entropy if the given passwordlist is used in a dictionaryattack. 

# Restrictions
Of course, this measurement is very dependent on the passwordlist. The passwordlist used currently is not long enough.
Usually the attackers has more information about the password:
* >8 characters
* exists at least 1 uppercase letter
* exists at least 1 specialcharacter
Maybe the attacker has information about you as well, but if assumed that the password is not connected to you, this should be a lot better than the NISTstandard at least. 

# NIST
The NIST standard gives "Password123" (4 + 2x7 + 3x1.5 + 6) = 28.5 bits of entropy, while my program achieves 16 bits of entropy with a small passwordlist, and Password123 wasn't even in there. A random generated password like '5Zc1ZstssUT' with the same length, which would achieve the same NIST entropy, achieved 88 bits. 
Here is a link to the NIST-standard: https://en.wikipedia.org/wiki/Password_strength#NIST_Special_Publication_800-63

# Thanks
Idea for this I thank ahn solo for!
