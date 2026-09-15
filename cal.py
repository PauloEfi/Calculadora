import tkinter as tk

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível divisão por zero")
    return a / b

def adicionar(valor):
    visor.insert(tk.END, valor)


def limpar():
    visor.delete(0, tk.END)


def calcular():
    try:
        expressao = visor.get()
        resultado = eval(expressao)

        visor.delete(0, tk.END)
        visor.insert(0, resultado)

    except ZeroDivisionError:
        visor.delete(0, tk.END)
        visor.insert(0, "Divisão por zero")

    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

def iniciar_calculadora():

    janela = tk.Tk()

    janela.title("Calculadora")
    janela.geometry("300x400")
    janela.resizable(False, False)

    global visor

    visor = tk.Entry(
        janela,
        font=("Arial", 24),
        justify="right"
    )

    visor.pack(
        padx=10,
        pady=10,
        fill="x"
    )

    botoes = [
        ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
        ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
        ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
        ("0", 3, 0), ("C", 3, 1), ("=", 3, 2), ("+", 3, 3)
    ]

    frame = tk.Frame(janela)
    frame.pack(expand=True, fill="both")

    for texto, linha, coluna in botoes:

        if texto == "C":
            comando = limpar

        elif texto == "=":
            comando = calcular

        else:
            comando = lambda valor=texto: adicionar(valor)

        botao = tk.Button(
            frame,
            text=texto,
            font=("Arial", 18),
            command=comando
        )

        botao.grid(
            row=linha,
            column=coluna,
            padx=5,
            pady=5,
            sticky="nsew"
        )

    for i in range(4):
        frame.columnconfigure(i, weight=1)
        frame.rowconfigure(i, weight=1)

    janela.mainloop()

if __name__ == "__main__":
    iniciar_calculadora()
