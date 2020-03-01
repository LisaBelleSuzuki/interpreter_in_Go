# coding: utf-8

int_numbers = ['0', '1','2','3','4','5','6','7','8','9']
operators_list = ['+', '-', '*', '/']

class Node:
	def __init__(self, val):
		self.val = val
		self.parents = []
		self.children = []

	def addChild(self, child):
		self.children.append(child)
		child.parents.append(self)

	def hasChildren(self):
		if self.children == []:
			return False
		else:
			return True

	def hasParents(self):
		if self.parents == []:
			return False
		else:
			return True


def lexer(sentence):
	tokens = []
	for i in range(len(sentence)):
		cur_char = sentence[i]
		if cur_char == 'f':
			tokens.append(['fn', 'f'])
		elif cur_char == '+':
			tokens.append(['plus', '+'])
		elif cur_char == '-':
			tokens.append(['minus', '-'])
		elif cur_char == '*':
			tokens.append(['mul', '*'])
		elif cur_char in int_numbers:
			tokens.append(['int', cur_char])
		elif cur_char == '(':
			tokens.append(['r_paren', cur_char])
		elif cur_char == ')':
			tokens.append(['l_paren', cur_char])
		else: #for now
			tokens.append(['var', cur_char])
	return tokens

def parser(tokens):
	expression = Node('expression')
	operands = []
	operator = Node(None)
	for i in range(len(tokens)):
		token = tokens[i]
		token_type = token[0]
		token_val = token[1]
		if token_val in operators_list:
			operator = Node(token)
		else:
			operands.append(Node(token))
	for operand in operands:
		operator.addChild(operand)
	expression.addChild(operator)
	return expression



# def test(case):



if __name__ == '__main__':
	sentence = '(1+2)*3'
	tokens = lexer(sentence)
	import pdb; pdb.set_trace()
	expression = parser(tokens)
	print("operator node:")
	print(expression.children[0].val)
	print("operands:")
	for operand in expression.children[0].children:
		print(operand.val)
	# test_cases = [
	# 	['1','+','2']
	# ]
	# for case in test_cases:
	# 	test(case)