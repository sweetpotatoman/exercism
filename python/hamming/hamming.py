# def distance(strand_a, strand_b):
#     if len(strand_a) != len(strand_b):
#         raise ValueError("Lengths of the given strands aren't equal!")

#     hamming_distance = 0
#     for i, nucleotid in enumerate(strand_a):
#         if strand_b[i] != nucleotid:
#             hamming_distance += 1
#     return hamming_distance


def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands are of unequal lengths.")
    return sum(a != b for a, b in zip(strand_a, strand_b))
