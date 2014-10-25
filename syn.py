import argparse
from nltk.corpus import wordnet as wn

def term_synset(term):
    synsets = wn.synsets(term)
    for x in synsets:
        print x.name, 'D:', x.definition
        for lemma in wn.synset(x.name).lemmas:
            print '-----', lemma.name
        print


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Output lemmas (based on synsets) for a given term.'
        )
    parser.add_argument('term', help='Term')
    args = parser.parse_args()
    term_synset(args.term)
    