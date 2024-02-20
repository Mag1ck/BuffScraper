def clear():
    lines_seen = set()  # holds lines already seen
    outfile = open('cleared_prices.txt', "w")
    for line in open('pices.txt', "r"):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
