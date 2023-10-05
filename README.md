# Abracadabra
Dave has just watched the Planet of the Apes. He wants to train a monkey and experiment with him. He gets a monkey and names her Juliet. After one year of training Juliet learns to type. She is yet unfamiliar with the "space" key and can only type in lower-case Latin letters. Having typed for a fairly long line, Juliet understood that it would be great to divide what she has written into k lines not shorter than a and not longer than b, for the text to resemble human speech more. Help Juliet.

INPUT

The first line contains three integers k, a and b (1≤ks 200, 1 ≤ asb 200). The second line contains a sequence of lowercase Latin letters-the text typed by Juliet. It is guaranteed that the given line is not empty and its length does not exceed 200 symbols.

OUTPUT

Print & lines, each of which contains no less than a and no more than b symbols Juliet's text divided into lines. It is not allowed to perform any changes in the text, such as: deleting or adding symbols, changing their order, etc. If the solution is not unique. print any of them. If there is no solution, print "No solution" (without quotes).

EXAMPLES

Input

3 2 5 
abrakadabra

Output

ab

rakad

abra

Input

4 1 2 
abrakadabra

Output

No solution
