a = input()
stackOP = []
stackDital =[]
if len(a) == 1:
    print(a)
else:
    for key in a:
        if key.isdigit():
            stackDital.append(key)
        else:
            if key =='+' or key == '-':
                if len(stackOP) == 0:
                    stackOP.append(key)
                elif(stackOP[-1] == '*'):
                    stackOP.pop()
                    v1 = stackDital.pop()
                    v2 = stackDital.pop()
                    stackDital.append(v1 * v2)
                elif(stackOP[-1] == '/'):
                    stackOP.pop()
                    v1 = stackDital.pop()
                    v2 = stackDital.pop()
                    stackDital.append(v2/v1*1.0)
                else:
                    stackOP.append(key)
            if key == '*'or key =='/':
                stackOP.append(key)
            for key in stackOP:
                if key == '+':


