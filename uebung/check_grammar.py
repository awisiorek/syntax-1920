#!/usr/bin/env python
# coding: utf-8

import nltk
import argparse
import logging
logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("grammar")
args = parser.parse_args()

try:
    input = raw_input
except NameError:
    pass

grammar = nltk.data.load("file:{}".format(args.grammar))
rd_parser = nltk.RecursiveDescentParser(grammar)
logging.info("Loaded {}".format(args.grammar))

while(True):
    try:
        sent = input("Sentence~> ").decode("utf8").split()
    except EOFError:
        print("Goodbye.")
        break

    try:
        trees = rd_parser.parse(sent)
    except ValueError as e:
        logging.error(e.message)
        continue

    i = -1
    for i, tree in enumerate(trees):
        tree.draw()
    if i < 0:
        print("No analysis possible")
