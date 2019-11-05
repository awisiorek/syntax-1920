import nltk

def test_grammar(grammar, sentences):
    grammar1 = nltk.data.load("file:{}".format(grammar))
    rd_parser = nltk.RecursiveDescentParser(grammar1)
    for i, sent in enumerate(sentences):
        print("Satz {}: {}".format(i, sent))
        for tree in rd_parser.parse(sent.split()):
            tree.draw()  # oder tree.pretty_print()

test_sentences = [
    "der Mann gibt der Frau das Buch"
]

test_grammar("grammar1.cfg", test_sentences)
