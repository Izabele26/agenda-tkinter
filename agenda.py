from tkinter import *
from tkinter import messagebox
from tkinter import ttk

agenda = []

def adicionarcontato() -> None:
    #pegando valores digitado
    nome = txt_nome.get()
    telefone = txt_telefone.get()
    categoria = cb_categorias.get()
    contato = {'Nome': nome,
               'telefone': telefone,
               'categoria': categoria
    }
    agenda.append(contato)
    messagebox.showinfo('Adicionado!', 'Contato adicionado com sucesso!')
    limparCampos()
    atualizarTabela()

def editarcontato()-> None:
    contato_selecionado = tabela.selection()[0]
    if not contato_selecionado:
        return
    index = tabela.index(contato_selecionado)
    agenda[index] = {
        'Nome': txt_nome.get(),
        'telefone': txt_telefone.get(),
        'categoria': cb_categorias.get()
    }
    atualizarTabela()
    limparCampos()


def deletarcontato()->None:
    contato_selecionado = tabela.selection()[0]
    if not contato_selecionado:
        return
    index = tabela.index(contato_selecionado)
    del agenda[index]
    limparCampos()
    atualizarTabela()

def limparCampos() -> None:
    txt_nome.delete(0, END)
    txt_telefone.delete(0, END)
    cb_categorias.delete(0, END)

def atualizarTabela() -> None:
    #limpando a tabela
    #get_children: retorna uma lista com as linhas da tabela
    for linha in tabela.get_children():
        tabela.delete(linha)

    for contato in agenda:
        tabela.insert('', END, values=(contato['Nome'], contato['telefone'], contato['categoria']))

def tabelaClique(event) -> None:
    contato_selecionado = tabela.selection()[0]
    if not contato_selecionado:
        return
    index = tabela.index(contato_selecionado) #aparece o indice no terminal quando clicado.
    #preenchendo os campos com o contato index da tabela quando clicado
    contato = agenda[index]
    limparCampos()
    txt_nome.insert(0, contato['Nome'])
    txt_telefone.insert(0, contato['telefone'])
    cb_categorias.insert(0, contato['categoria'])

janela = Tk()
#adicionar titulo
#label -> rotulo identificação do que vai ter que preencher.
janela.title('Agenda telefonica')
#criando label
label_nome = Label(janela, text='Nome: ', fg='navy', font='Tahoma 14 bold')
#adicionar na janela
label_nome.grid(row=0, column=0)
#criar campo de texto - entry
txt_nome = Entry(janela,font='Tahoma 14',width=27)
txt_nome.grid(row=0, column=1)

label_telefone = Label(janela, text='Telefone: ', fg='navy', font='Tahoma 14 bold')
label_telefone.grid(row=1, column=0)
txt_telefone = Entry(janela,font='Tahoma 14',width=27)
txt_telefone.grid(row=1, column=1)

#combobox (caixa de opçoes/selecoes) adicionado aqui
label_categoria = Label(janela, text='Categoria: ', fg='navy', font='Tahoma 14 bold')
label_categoria.grid(row=2, column=0)
categorias = ['Amigos','Familia', 'Trabalho']
cb_categorias = ttk.Combobox(janela, values=categorias, width=25,
                             font='Tahoma 14')
cb_categorias.grid(row=2,column=1)


btn_adicionar = Button(janela, text='Adicionar', fg='navy', bg='white',
                       font='Tahoma 12 bold', width=8, height=1, command=adicionarcontato)
btn_adicionar.grid(row=3, column=0)

btn_editar = Button(janela, text='Editar', fg='navy', bg='white',
                       font='Tahoma 12 bold', width=8, height=1, command=editarcontato)
btn_editar.grid(row=3, column=1)

btn_excluir = Button(janela, text='Excluir', fg='navy', bg='white',
                       font='Tahoma 12 bold', width=8, height=1, command=deletarcontato)
btn_excluir.grid(row=3, column=2)

#criar tabela - TreeView
tabela = ttk.Treeview(janela, columns=('Nome','Telefone','Categoria'), show='headings')
tabela.heading('Nome', text='Nome')
tabela.heading('Telefone', text='Telefone')
tabela.heading('Categoria', text='Categoria')
#criando a ação bind pra quando clicar no contato da tabela
tabela.bind('<ButtonRelease-1>', tabelaClique)
tabela.grid(row=4,columnspan=3)#columnspan: quantas coluna ocupa de espaço, no caso ai é 3.



janela.mainloop() #cria a janela em looping