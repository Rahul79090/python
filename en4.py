from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the network
model = DiscreteBayesianNetwork([('A', 'C'), ('B', 'C')])

# Define CPDs
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_c = TabularCPD(
    variable='C',
    variable_card=2,
    values=[[0.9, 0.6, 0.7, 0.1],
            [0.1, 0.4, 0.3, 0.9]],
    evidence=['A', 'B'],
    evidence_card=[2, 2]
)

# Add CPDs to the model
model.add_cpds(cpd_a, cpd_b, cpd_c)

# Check if the model is valid
model.check_model()

# Perform inference
inference = VariableElimination(model)
result = inference.query(variables=['C'], evidence={'A': 1, 'B': 0})

print(result)
