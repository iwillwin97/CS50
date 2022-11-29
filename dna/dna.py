import csv
import sys


def main():


    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv textfile.txt")
        sys.exit(1)
    # TODO: Read database file into a variable

    with open(sys.argv[1], "r") as file:
        STRs = csv.DictReader(file)
        list_STRs = list(STRs)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as file:
        sequence = file.read()


    # TODO: Find longest match of each STR in DNA sequence
    count_sequence = {}
    for i in list_STRs[0]:
        count_sequence[i] = longest_match(sequence, i)


    # TODO: Check database for matching profiles
    dummy_match = 'No Match'
    dummy_match_counter = 1
    for i in range (1, len(list_STRs)):
        for j in count_sequence:
            if str(count_sequence[j]) == list_STRs[i][j]:
                dummy_match_counter += 1
        if dummy_match_counter == len(count_sequence):
            dummy_match = list_STRs[i]['name']
            break
        else:
            dummy_match_counter = 1
    print(dummy_match)
    return

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
