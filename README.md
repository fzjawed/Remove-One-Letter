# Remove-One-Letter

>11 June 2021 01:41 AM

Man I've fallen back into the Kpop rabbit hole - accepting my fate. There's this song called Red Lipstick by BOL4 💄 - S O G O O D

Anyway for this question I'd actually been thinking about it for a few days. Didn't get it on my first attempt or fifth 💆‍♀️

***Question: Given two strings s0 and s1, return whether you can obtain s1 by removing 1 letter from s0.***

I asked a friend and he recommended using sets but that didn't work either so today I was thinking of adding all the modified words (each ith letter removed) to a list and checking if s1 was in that list. But that obviously ran into a runtime error.

Brain tiny. 🧠🕳️

So the final solution checks if the lengths of both strings has a difference of one because only one letter is removed. If that's true then we iterate through s1 and check if each letter between the two strings is the same. When we get to a place where they aren't the same we check if the rest of the word after that letter is the same.

