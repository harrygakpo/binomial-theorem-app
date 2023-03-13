import tkinter as tk

window = tk.Tk()
window.geometry('600x400')
window.title('Binomial theorem app')

head = tk.Label(text = 'Enter your values of the form (a + bx)^n')
text_a = tk.Label(window, text = 'Enter a')
text_b = tk.Label(window, text = 'Enter b')
text_n = tk.Label(window, text = 'Enter n')
entry_a = tk.Entry(window)
entry_b = tk.Entry(window)
entry_n = tk.Entry(window)


def solution():
    
    value1 = int(entry_a.get())
    value2 = int(entry_b.get())
    power = int(entry_n.get())
    
    def factorial(x):
        if x != 0:
            a = int(1)
            for i in range(1, int(int(x)+ 1)):
                a = int(a) * int(i)
            return int(a)
        else:
            return 1
    
    def combination(power, term):
        return (factorial(int(power)))/ (factorial(int(power)- int(term))* (factorial(int(term))))
    
    def binomial(value1, value2, power, term):
        return combination(int(power), int(term))* (int(value1)** (int(power)- int(term)))* (int(value2)** (int(term)))

    def binomial_terms(value1, value2, power):
        a = []
        for chr in range(0, int(int(power)+ 1)):
            
            if chr != int(int(power)):
                a.append(str(binomial(value1, value2, power, chr)) + ' + ')
            else:
                # return a + str(binomial(value1, value2, power, chr))
                a.append(binomial(value1, value2, power, chr))  
        return a
        
    def binomial_sum(value1, value2, power):
        res = 0
        for i in range(0, int(int(power)+ 1)):
            res = res + int(binomial(value1, value2, power, i))
        return (res)
        
    def res(value1, value2, power):
        return (binomial_terms(value1, value2, power))

    return (res(value1, value2, power))

def show_answer():
    ans = solution()
    text = tk.Text(master = window, height = 1, width = 40)
    text.grid(column = 0, row = 5)
    text.insert(tk.END, ans)



def solution_sum():
    
    value1 = int(entry_a.get())
    value2 = int(entry_b.get())
    power = int(entry_n.get())
    
    def factorial(x):
        if x != 0:
            a = int(1)
            for i in range(1, int(int(x)+ 1)):
                a = int(a) * int(i)
            return int(a)
        else:
            return 1
    
    def combination(power, term):
        return (factorial(int(power)))/ (factorial(int(power)- int(term))* (factorial(int(term))))
    
    def binomial(value1, value2, power, term):
        return combination(int(power), int(term))* (int(value1)** (int(power)- int(term)))* (int(value2)** (int(term)))

    def binomial_terms(value1, value2, power):
        a = []
        for chr in range(0, int(int(power)+ 1)):
            
            if chr != int(int(power)):
                a.append(str(binomial(value1, value2, power, chr)) + ' + ')
            else:
                a.append(binomial(value1, value2, power, chr))  
        return a
        
    def binomial_sum(value1, value2, power):
        res = 0
        for i in range(0, int(int(power)+ 1)):
            res = res + int(binomial(value1, value2, power, i))
        return (res)
        
    def res(value1, value2, power):
        #return (binomial_terms(value1, value2, power))
        return (binomial_sum(value1, value2, power))

    return (res(value1, value2, power))

def show_sum():
    ans = solution_sum()
    text = tk.Text(master = window, height = 1, width = 20, bg = 'blue')
    text.grid(column = 1, row = 5)
    text.insert(tk.END, ans)


solve = tk.Button(window, text = 'Solve', command = show_answer)
give_sum = tk.Button(window, text = 'Provide sum', command = show_sum)

head.grid(row = 0)
text_a.grid(row = 1, column = 0)
text_b.grid(row = 2, column = 0)
text_n.grid(row = 3, column = 0)
entry_a.grid(row = 1, column = 1)
entry_b.grid(row =2, column = 1)
entry_n.grid(row = 3, column = 1)
solve.grid(row = 4)
give_sum.grid(row = 4, column = 2)


window.mainloop()