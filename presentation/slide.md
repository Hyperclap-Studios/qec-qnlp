% Quantum Stuff
% Hyperposition
% April 2022

# test

```python
from lambeq import AtomicType, IQPAnsatz, remove_cups

ansatz = IQPAnsatz({AtomicType.NOUN: 1, AtomicType.SENTENCE: 0},
                   n_layers=1, n_single_qubit_params=3)

train_circuits = [ansatz(remove_cups(diagram)) for diagram in train_diagrams]
# val_circuits =  [ansatz(remove_cups(diagram))  for diagram in val_diagrams]

train_circuits[0].draw(figsize=(9, 10))


```

# 2nd slide

* snags
* $$ | \Psi \rangle = \alpha |0\rangle + \beta | 1 \rangle $$
