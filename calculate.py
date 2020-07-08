def calculate(s:str)-> int:
    def helper(s:List)-> int:
        stack[]
        sign ='+'
        num =0
        while len(s)>0:
            c = s.pop(0)
            if c.isdigit():
                num = 10 *num + int(c)
            if c=='(':
                num = helper(s)
            if (not c.isdigit() and c != ' ') or len(s) == 0:
                if sign =='+':
                    stack.append(num)
                elif sign =='-':
                    stack.append(-num)
                elif sign =='*':
                    stack[-1] = stack[-1] * num
                elif sign =='/':
                    stack[-1] = int(stack[-1]/float(num))
            num = 0
            sign = c
            if c ==')': break
        return sum(stack)
return helper(list(s))