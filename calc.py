# function to perform calculations in string
def compute(expression):
	num0, operator, num1 = expression.split(' ')
	num0, num1 = int(num0), int(num1)
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
 	elif operator == '*':
        return num0 * num1
    elif operator == '/':
    	return num0 / num1
>>>>>>> add-division
    else:
        print('unknown operator!')
        return None 
        