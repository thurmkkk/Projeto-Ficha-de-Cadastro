#importando o Tkinter
from tkinter import *
from tkinter import font

from tkinter import ttk
from tkcalendar import Calendar, DateEntry


co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################### criando Janela ############

janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background = co9)
janela.resizable(width=FALSE, height=FALSE)



################# dividindo a Janela
frame_cima = Frame(janela, width=310, height=50, bg = co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg = co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg = co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

################## label cima #################
app_nome = Label(frame_cima,text='Formulário de Consultoria',anchor= NW, font=('Ivy 13 bold') , bg=co2,fg=co1, relief='flat')
app_nome.place(x=10, y=20)

################## Configurando frame baixo #################
l_nome = Label(frame_baixo,text='Nome*',anchor= NW, font=('Ivy 10 bold') , bg=co1,fg=co4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=10, y=40)

### email

l_email = Label(frame_baixo,text='Email * ',anchor= NW, font=('Ivy 10 bold') , bg=co1,fg=co4, relief='flat')
l_email.place(x=10, y=70)
e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)

### telefone
l_tel = Label(frame_baixo,text='Telefone* ',anchor= NW, font=('Ivy 10 bold') , bg=co1,fg=co4, relief='flat')
l_tel.place(x=10, y=130)
e_tel = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_tel.place(x=15, y=160)


### Data da consulta
l_cal = Label(frame_baixo,text='Data da consulta* ',anchor= NW, font=('Ivy 10 bold') , bg=co1,fg=co4, relief='flat')
l_cal.place(x=10, y=190)
e_cal = DateEntry(frame_baixo, width=12, background='darkblue', foreground="white",borderwidth =2)
e_cal.place(x=15, y=220)


### Estado da consulta
l_estado = Label(frame_baixo,text='Estado da Consulta* ',anchor= NW, font=('Ivy 10 bold') , bg=co1,fg=co4, relief='flat')
l_estado.place(x=160, y=190)
e_estado = Entry(frame_baixo, width=20, justify='left', relief='solid')
e_estado.place(x=160, y=220)

### Sobre
l_sob = Label(frame_baixo,text='Estado da Consulta* ',anchor= NW, font=('Ivy 10 bold') , bg=co1,fg=co4, relief='flat')
l_sob.place(x=15, y=260)
e_sob = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_sob.place(x=15, y=290)

###Botao inserir
b_inserir = Button(frame_baixo,text='Inserir*',width=10,font=('Ivy 9 bold') ,bg=co6,fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=340)

###Botao atualizar
b_atualizar = Button(frame_baixo,text='Atualizar* ',width=10,font=('Ivy 9 bold') ,bg=co2,fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=340)

###Botao deletar
b_deletar = Button(frame_baixo,text='Deletar* ',width=10,font=('Ivy 9 bold') ,bg=co7,fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=200, y=340)

janela.mainloop()


lista = [[1,'Joao Futi Muanda','joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
           [2,'Fortnato Mpngo', 'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
           [3,'Usando Python',  'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
           [4,'Clinton Berclidio', 'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
           [5,'A traicao da Julieta','joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente']
           ]

#lista para cabecario
tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']

#criando a tabela
tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

#vertical scrollbar
vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

#horizontal scrollbar
hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

frame_direita.grid_rowconfigure(0, weight=12)

hd=["nw","nw","nw","nw","nw","center","center"]
h=[30,170,140,100,120,50,100]
n=0

for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    #adjust the column's width to the header string
    tree.column(col, width=h[n],anchor=hd[n])
   
    n+=1

for item in lista:
    tree.insert('', 'end', values=item)
