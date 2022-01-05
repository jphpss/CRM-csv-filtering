#!/usr/bin/env python3
# The above line specifies path to your python executable.
# Refines CRM csv file search criterion, for the purpose of selective targetting for sales pipeline 'reach' initiatives
# Written by Jyri Hamalainen, (with help from Ari Hamalainen), https://thehub.io/startups/100ximpact
import os
import csv
import sys

# path to source file
PATH = 'output.csv'
# case-insensitive string to search for
STRING = 'German'
# list of fieldnames to output (empty [] for all fields)
FIELDS = ['Company name', 'Lifecycle Stage', 'Last Contacted', 'Company owner', 'LinkedIn Bio']
# output file
OUTFILE = 'output2.csv'

i = 0 # counter

assert os.path.isfile(PATH)

with open(PATH, newline='') as f:
    reader = csv.DictReader(f)
    with open(OUTFILE, 'w', newline='') as g:

        if FIELDS and set(FIELDS).issubset(set(reader.fieldnames)):
            # subset of fields
            writer = csv.DictWriter(g, FIELDS, extrasaction='ignore')
        elif not FIELDS:
            # all fields
            writer = csv.DictWriter(g, reader.fieldnames)
        else:
            # incorrect fieldname
            print('FIELDS contains an incorrect field name')
            sys.exit(1)

        writer.writeheader()
        for d in reader:
            if STRING.lower() in ','.join(list(d.values())).lower():
                writer.writerow(d)
                i += 1

        print(f'{i} records matched and written')

