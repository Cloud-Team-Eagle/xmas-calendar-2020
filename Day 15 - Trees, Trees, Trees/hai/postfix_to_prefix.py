# for binary operators only, no error handling
def postfix_to_prefix(expression):
    binary_operators = ['+', '-', '*', '/']
    tokens = expression.strip().split(' ')
    prefix_stack = []
    infix_stack = []
    for token in tokens:      
        if token in binary_operators:
            second_operant = prefix_stack.pop()
            first_operant = prefix_stack.pop()
            composed_prefix = '{} {} {}'.format(token, first_operant, second_operant)
            prefix_stack.append(composed_prefix)

            second_operant = infix_stack.pop()
            first_operant = infix_stack.pop()
            composed_infix = '{} {} {}'.format(first_operant, token, second_operant)
            infix_stack.append(composed_infix)
        else:
            prefix_stack.append(token)
            infix_stack.append(token)
    print('\n{} -> {}'.format(expression, prefix_stack[0]))
    print('({})'.format(infix_stack[0]))



postfix_to_prefix('a b *')
postfix_to_prefix('a b + c *')
postfix_to_prefix('1 2 3 * + 4 +')
postfix_to_prefix('10 20 * 30 40 * +')
postfix_to_prefix('A B * C D * +')
postfix_to_prefix('A B C * + D +')