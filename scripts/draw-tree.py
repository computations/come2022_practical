#!/usr/bin/env python3

# Until Biopython gets their shit together and stops being obnoxious, I have to
# turn off all warnings

import warnings
warnings.filterwarnings("ignore")

from Bio import Phylo
import argparse
import io

parser = argparse.ArgumentParser()
parser.add_argument("treefile")
parser.add_argument("--draw", action="store_true", default=False)

formats = ['newick', 'nexus', 'nexml', 'phyloxml']

def make_string_from_tree(tree):
    strio = io.StringIO()
    Phylo.draw_ascii(tree, file=strio)
    return strio.getvalue()

def draw_tree(tree):
    Phylo.draw(tree)

def print_trees(trees, draw):
    for t in trees:
        if draw:
            draw_tree(t)
        else:
            print(make_string_from_tree(t))

def parse_trees(filename):
    trees = None
    for f in formats:
        try:
            trees = Phylo.parse(filename, f)
        except:
            pass
        else:
            break
    if trees is None:
        raise Exception("No format that can parse that tree")
    return trees

args = parser.parse_args()
print_trees(parse_trees(args.treefile), args.draw)
