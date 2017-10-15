def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError  # the two strings need to be of the same length
    else:
        hammond_distance = 0
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                hammond_distance += 1
        return hammond_distance

