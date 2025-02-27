#!/usr/bin/env python3
import sys 
import csv

def parse_csv(file, separator):
    pvalues = dict()
    file = csv.reader(file, delimiter=separator, quotechar='|')
    _ = next(file) #skip header
    for line in file:
        if line[-1] != "NA":
            id_ = line[0].replace('"', "")
            pvalues[id_] = float(line[-1])
    return pvalues

def main():
    file_a = sys.argv[1]
    file_b = sys.argv[2]
    with open(file_a, "r") as f:
        p_values_a = parse_csv(f, "\t")
    with open(file_b, "r") as f:
        p_values_b = parse_csv(f, "\t")
    
    #print(p_values_a.keys())
    #print(p_values_b.keys())
    
    diff = dict()
    for k in p_values_a.keys():
        if (k in p_values_b):
            diff[k] = p_values_b[k]-p_values_a[k]
    to_list = [(k, diff[k], p_values_a[k], p_values_b[k]) for k in diff.keys()]
    sorted_list = sorted(to_list, key=lambda x: x[1], reverse=True)
    for l in sorted_list:
        print(f"{l[0]}\t{l[1]}\t{l[2]}\t{l[3]}")

if __name__=="__main__":
    main()