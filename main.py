from lambeq import BobcatParser, Rewriter, AtomicType, IQPAnsatz
from pytket.circuit.display import render_circuit_as_html
from discopy import grammar

if __name__ == '__main__':
    print("START")

    # STEP 1: PARSE INPUT

    sentence = 'What is the dog doing'

    # Parse the sentence and convert it into a string diagram
    parser = BobcatParser()  # (GALLI TÜECHLI) will download Model so may take a while [1.5 GB]

    diagram = parser.sentence2diagram(sentence)

    grammar.draw(diagram, figsize=(14, 3), fontsize=12)

    # STEP 2: ENCODING

    # IDK

    # STEP 3: REWRITE

    rewriter = Rewriter(['prepositional_phrase', 'determiner'])
    rewritten_diagram = rewriter(diagram)

    normalised_diagram = rewritten_diagram.normal_form()
    normalised_diagram.draw(figsize=(9, 4), fontsize=13)

    # STEP 4: PARAMETERIZATION

    # Define atomic types
    N = AtomicType.NOUN
    S = AtomicType.SENTENCE

    ansatz = IQPAnsatz({N: 1, S: 1}, n_layers=2)
    discopy_circuit = ansatz(normalised_diagram)
    discopy_circuit.draw(figsize=(15, 10))

    tket_circuit = discopy_circuit.to_tk()

    render_circuit_as_html(tket_circuit)

    # STEP 5: TRAINING

    print("END")
