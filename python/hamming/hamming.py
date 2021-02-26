def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise Exception("DNA Strands do not match")
    else:
        length = range(0, len(strand_a))
        count = 0
        for i in length:
            if strand_a[i] != strand_b[i]:
                count += 1
    return count
