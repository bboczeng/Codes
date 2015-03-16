__author__ = 'bozeng'

def evalRPN(tokens):
        if not tokens:
            return 0

        stack=[]


        for each in tokens:
            if each=="+":
                op1=stack.pop()
                op2=stack.pop()
                stack.append(0.0+op1+op2)
            elif each=="-":
                op1=stack.pop()
                op2=stack.pop()
                stack.append(0.0+op2-op1)
            elif each=="*":
                op1=stack.pop()
                op2=stack.pop()
                stack.append(1.0*op1*op2)
            elif each=="/":
                op1=stack.pop()
                op2=stack.pop()
                stack.append(1.0*op2/op1)
            else:
                stack.append(int(each))

        if not stack:
            return 0
        return stack.pop()

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))