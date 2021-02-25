# rosalind_random_strings
Given a DNA sequence and a list of GC contents, calculates how likely the the sequence is to occur by random for each GC content.

This is a solution to the Introduction to Random Strings (ID = PROB) problem on the bioinformatics website Rosalind.

The program takes a text file with a DNA squence on the first line and a list of GC contents on the second line.

For each GC content it calculates how likely the provided DNA sequence would form if every nucleotide were selected by chance.
The log10 of each probability is then stored in a text file. 
