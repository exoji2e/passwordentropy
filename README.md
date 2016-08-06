# passwordentropy
Calculate the entropy of your password with the help of compression.

## Idea
The idea is to be able to validate a human generated password against a dictionary attack.
This is done by using a known password file.

1. Append your password to the end of the file
2. Compress both the file with your password and the original password file. 
3. The amount of entropy your password has is the difference in file size. This is approximately the entropy if the given password list is used in a dictionary attack. 

## Restrictions
Of course, this measurement is very dependent on the password list. The password list used currently is not long enough.
Usually the attackers has more information about the password, there are usually:
* >=8 characters
* at least 1 uppercase letter
* at least 1 special character

Maybe the attacker has information about you as well, but if assumed that the password is not connected to you, this should be a lot better than the NIST standard at least. 

## NIST
The NIST standard gives "Password123" (4 + 2x7 + 3x1.5 + 6) = 28.5 bits of entropy, while my program achieves 16 bits of entropy with a small password list, and Password123 wasn't even in there. A randomly generated password like '5Zc1ZstssUT' with the same length, which would achieve the same NIST entropy, achieved 88 bits. 
Here is a link to the NIST-standard: https://en.wikipedia.org/wiki/Password_strength#NIST_Special_Publication_800-63

## Plans
* Start using an internal, deterministic compressional gorithm, which assumes a specific character set.
* Find a larger more reliable password list
* Connect password lists to language
* Use password lists that are more like dumps, making common passwords more common in the list => encryption cost depends more on "commonness".

## Thanks
Idea for this I thank ahn solo for!

## Notes
* Right now I'm using gzip compression, which will overestimate the entropy, since all unicode characters are supported. Maybe I'll implement a compression algorithm, that can restrict to only [a-z],[A-Z],[0-9],' ', or maybe even a modifiable character set. 
