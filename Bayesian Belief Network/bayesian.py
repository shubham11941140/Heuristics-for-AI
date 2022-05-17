from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def build_model(edges):

	model = BayesianNetwork(edges)

	# Defining individual CPDs.
	cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.1], [0.9]])

	cpd_c = TabularCPD(variable='C', variable_card=2, values=[[0.5], [0.5]])

	cpd_b = TabularCPD(variable='B', variable_card=2,
					values=[[0.4, 0.9],
							[0.6, 0.1]],
					evidence=['A'],
					evidence_card=[2])

	cpd_d = TabularCPD(variable='D', variable_card=2,
					values=[[0.3, 0.6],
							[0.7, 0.4]],
					evidence=['C'],
					evidence_card=[2])

	cpd_e = TabularCPD(variable='E', variable_card=2,
					values=[[0.1, 0.2],
							[0.9, 0.8]],
					evidence=['B'],
					evidence_card=[2])

	cpd_h = TabularCPD(variable='H', variable_card=2,
					values=[[0.5, 0.7],
							[0.5, 0.3]],
					evidence=['E'],
					evidence_card=[2])

	cpd_i = TabularCPD(variable='I', variable_card=2,
					values=[[0.8, 0.7],
							[0.2, 0.3]],
					evidence=['E'],
					evidence_card=[2])

	cpd_f = TabularCPD(variable='F', variable_card=2,
					values=[[0.7, 0.4, 0.2, 0.0],
							[0.3, 0.6, 0.8, 1.0]],
					evidence=['B', 'D'],
					evidence_card=[2, 2])

	cpd_g = TabularCPD(variable='G', variable_card=2,
					values=[[0.9, 0.1],
							[0.1, 0.9]],
					evidence=['F'],
					evidence_card=[2])

	# Associating the CPDs with the network
	model.add_cpds(cpd_a, cpd_c, cpd_b, cpd_d, cpd_e, cpd_f, cpd_g, cpd_h, cpd_i)

	# check_model checks for the network structure and CPDs and verifies that the CPDs are correctly
	# defined and sum to 1.
	model.check_model()

	return model

def queries(model):

	infer = VariableElimination(model)

	a = infer.query(['I'], evidence={'C': 1})
	b = infer.query(['E'], evidence={'D': 0})
	c = infer.query(['G'], evidence={'B': 0, 'D': 1})

	return a, b, c

def main():

	# Defining the model structure.
 	# We can define the network by just passing a list of edges.
	edges = [
			('A', 'B'),
			('B', 'E'),
			('B', 'F'),
			('E', 'H'),
			('E', 'I'),
			('C', 'D'),
			('D', 'F'),
			('F', 'G')
	]

	model = build_model(edges)

	a, b, c = queries(model)

	print("Part A is", a)
	print("Part B is", b)
	print("Part C is", c)

# The Answers are variable associated with 0

if __name__ == '__main__':
    main()


