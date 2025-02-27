#!/usr/bin/env python3
import sys 
import csv

def parse_csv(file, separator):
    keys = set()
    file = csv.reader(file, delimiter=separator, quotechar='|')
    _ = next(file) #skip header
    for line in file:
            id_ = line[0].replace('"', "")
            keys.add(id_)
    return keys

def main():
    gene_expression = sys.argv[1]
    ids = parse_csv(sys.stdin, "\t")

    with open(gene_expression, "r") as file:
        file = csv.reader(file, delimiter="\t", quotechar='|')
        header = next(file) 
        print("\t".join(header))
        #exit()
        for line in file:
            id_ = line[0].replace('"', "")
            if id_ in ids:
                print("\t".join(line))

if __name__=="__main__":
    main()