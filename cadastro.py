import tkinter as tk



janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("1000x600")  

aaa = ""

cadastro = []

class Estudante:

    def __init__(self, aluno):

        self.aluno = aluno



def mostrar_nome():

    aluno = entrada_nome.get()
    nome.config(text=aluno)    

    nra = entrada_ra.get()
    ra.config(text=nra)

    ncurso = entrada_curso.get()
    curso.config(text=ncurso)

    nnivel = entrada_nivel.get()
    nivel.config(text=nnivel)



    cadastro.append(aluno)
    cadastro.append(nra)
    cadastro.append(ncurso) 
    cadastro.append(nnivel)

    cadas.config(text=cadastro)

    aaa = Estudante(aluno)

    res.config(text=aaa.aluno)

#Entradas


texto = tk.Label(janela, text="Digite o nome do aluno: ", font=("Arial", 16))
texto.place(x=10, y=10)

entrada_nome = tk.Entry(janela,  font=("Arial", 16))
entrada_nome.place(x=10, y=50)

entrada_ra = tk.Entry(janela, font=("Arial", 16))
entrada_ra.place(x=10,y=100)

entrada_curso = tk.Entry(janela, font=("Arial", 16))
entrada_curso.place(x=10, y=150)

entrada_nivel = tk.Entry(janela, font=("Arial", 16))
entrada_nivel.place(x=10, y=200)

botao = tk.Button(janela, command= mostrar_nome)
botao.place(x=10, y=250)



#Listagem na tela dos alunos (nome, ra, curso, nivel)


nome = tk.Label(janela, font=("Arial", 16))
nome.place(x=600, y=50)

ra = tk.Label(janela, font=("Arial", 16))
ra.place(x=600, y=100)

curso = tk.Label(janela, font=("Arial", 16))
curso.place(x=600, y=150)

nivel = tk.Label(janela, font=("Arial", 16))
nivel.place(x=600, y=200)

cadas = tk.Label(janela, font=("Arial", 16))
cadas.place(x=10, y=400)

res =  tk.Label(janela, font=("Arial", 16))
res.place(x=10, y=300)
 

print(aaa)



janela.mainloop()



