from lambeq import BobcatParser
from discopy import grammar

if __name__ == '__main__':
    sentence = 'He defecated through a sunroof'

    # Parse the sentence and convert it into a string diagram
    parser = BobcatParser()  # (GALLI TÜECHLI) will download Model so may take a while [1.5 GB]

    diagram = parser.sentence2diagram(sentence)

    grammar.draw(diagram, figsize=(14, 3), fontsize=12)