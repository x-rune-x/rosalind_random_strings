import math


# Function to calculate probability of DNA sequence given a particular GC content.
def string_prob(dna_input, gc_prob):
    g_prob = gc_prob / 2
    # Probability of a C is the same as G.
    a_prob = (1-gc_prob) / 2
    # Probability of T is the same as A.

    str_prob = 1

    # Multiply the probabilities of each nucleotide to find the probability of obtaining the whole string by chance.
    for nucleotide in dna_input:
        if nucleotide == "A" or nucleotide == "T":
            str_prob = str_prob * a_prob
        elif nucleotide == "G" or nucleotide == "C":
            str_prob = str_prob * g_prob

    str_prob = math.log10(str_prob)
    str_prob = round(str_prob, 3)
    return str_prob


# Function to get DNA string to test against and list of GC contents from Rosalind dataset in text format.
def get_probs(input_file):
    file = open(input_file, "r")
    # Get the DNA sequence on the first line.
    seq = file.readline().strip()
    # Get the list of GC contents on the second line.
    prob_list = file.readline().strip().split()
    file.close()
    prob_list = list(map(float, prob_list))

    str_prob_list = []

    # Cycle through the GC contents, calculate how likely they are to result in the DNA sequence and store each
    # probability in a new list.
    for prob in prob_list:
        str_prob_list.append(string_prob(seq, prob))

    output_string = ""
    output_file = open("probability_list.txt", "w")
    for position in str_prob_list:
        output_string += str(position) + " "

    output_file.write(output_string.strip())


get_probs("rosalind_prob.txt")
