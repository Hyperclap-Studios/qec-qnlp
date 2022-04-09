def plotCircuit(n_noun, n_sentence, n_layer, plotcircuit=True):
    # Define atomic types
    N = AtomicType.NOUN
    S = AtomicType.SENTENCE

    # Convert string diagram to quantum circuit
    ansatz = IQPAnsatz({N: n_noun, S: n_sentence}, n_layers=n_layer)
    discopy_circuit = ansatz(diagram)
    
    if(plotcircuit == False):
        discopy_circuit.draw(figsize=(15,10))

    if(plotcircuit):
        tket_circuit = discopy_circuit.to_tk()
        render_circuit_jupyter(tket_circuit)