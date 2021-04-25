from tkinter import *
import tkinter.messagebox
root = Tk()

root.geometry("900x600")
root.resizable(False, False)

bg = PhotoImage(file = "Alkane Calculator.png")

label1 = Label(root, image = bg)
label1.place(x = -2, y = -2)

label2 = Label(root, text = "Please fill in the information below then click the calculate button to determine the name of your diagram.",font=("Roboto",11),fg="white",bg='#40a4a6')
label2.pack(pady = 250)

label3 = Label(root, text = "How many chains?",font=("Roboto",9),fg="black",bg='#40a4a6').place(x = 300, y = 300)

chain = StringVar()
entry_box = Entry(root, textvariable = chain, width = 12).place(x = 530, y = 300)

label4 = Label(root, text = "Is there a cyclo chain?",font=("Roboto",9),fg="black",bg='#40a4a6').place(x = 300, y = 320)

cyclo = StringVar()
entry_box2 = Entry(root, textvariable = cyclo, width = 12).place(x = 530, y = 320)

label5 = Label(root, text = "How many methyl groups?",font=("Roboto",9),fg="black",bg='#40a4a6').place(x = 300, y = 340)

number_methyl = StringVar()
where_methyl = StringVar()
entry_box3 = Entry(root, textvariable = number_methyl, width = 12).place(x = 530, y = 340)
entry_box3_2 = Entry(root, textvariable = where_methyl, width = 12)

def callback0(name='', index='', mode=''):
    global entry_box3_2
    if number_methyl.get() != '' and int(number_methyl.get()) != 0:
        entry_box3_2.place(x = 610, y = 340)
    else:
        entry_box3_2.place_forget()
        where_methyl.set("")

number_methyl.trace_add("write", callback0)

label6 = Label(root, text = "How many ethyl groups? Where?",font=("Roboto",9),fg="black",bg='#40a4a6').place(x = 300, y = 360)

number_ethyl = StringVar()
where_ethyl = StringVar()
entry_box4 = Entry(root, textvariable = number_ethyl, width = 12).place(x = 530, y = 360)
entry_box4_2 = Entry(root, textvariable = where_ethyl, width = 12)

def callback1(name='', index='', mode=''):
    global entry_box4_2
    if number_ethyl.get() != '' and int(number_ethyl.get()) != 0:
        entry_box4_2.place(x = 610, y = 360)
    else:
        entry_box4_2.place_forget()
        where_ethyl.set("")

number_ethyl.trace_add("write", callback1)

label7 = Label(root, text = "How many propyl groups? Where?",font=("Roboto",9),fg="black",bg='#40a4a6').place(x = 300, y = 380)

number_propyl = StringVar()
where_propyl = StringVar()
entry_box5 = Entry(root, textvariable = number_propyl, width = 12).place(x = 530, y = 380)
entry_box5_2 = Entry(root, textvariable = where_propyl, width = 12)

def callback2(name='', index='', mode=''):
    global entry_box5_2
    if number_propyl.get() != '' and int(number_propyl.get()) != 0:
        entry_box5_2.place(x = 610, y = 380)
    else:
        entry_box5_2.place_forget()
        where_propyl.set("")

number_propyl.trace_add("write", callback2)

label8 = Label(root, text = "How many butyl groups? Where?",font=("Roboto",9),fg="black",bg='#40a4a6').place(x = 300, y = 400)

number_butyl = StringVar()
where_butyl = StringVar()
entry_box6 = Entry(root, textvariable = number_butyl, width = 12).place(x = 530, y = 400)
entry_box6_2 = Entry(root, textvariable = where_butyl, width = 12)

def callback3(name='', index='', mode=''):
    global entry_box6_2
    if number_butyl.get() != '' and int(number_butyl.get()) != 0:
        entry_box6_2.place(x = 610, y = 400)
    else:
        entry_box6_2.place_forget()
        where_butyl.set("")

number_butyl.trace_add("write", callback3)

label9 = Label(root, text = "How many bromine groups? Where?",font=("Roboto",9),fg="black",bg='#40a4a6').place(x = 300, y = 420)

number_bromo = StringVar()
where_bromo = StringVar()
entry_box7 = Entry(root, textvariable = number_bromo, width = 12).place(x = 530, y = 420)
entry_box7_2 = Entry(root, textvariable = where_bromo, width = 12)

def callback4(name='', index='', mode=''):
    global entry_box7_2
    if number_bromo.get() != '' and int(number_bromo.get()) != 0:
        entry_box7_2.place(x = 610, y = 420)
    else:
        entry_box7_2.place_forget()
        where_bromo.set("")

number_bromo.trace_add("write", callback4)

def calculate(chain, cyclo, number_methyl, number_ethyl, number_propyl, number_butyl, number_bromo, where_methyl, where_ethyl, where_propyl, where_butyl, where_bromo):
    if chain == '0' or chain == '':
        pass
    elif chain == '1':
        chain = 'methane'
    elif chain == '2':
        chain = 'ethane'
    elif chain == '3':
        chain = 'propane'
    elif chain == '4':
        chain = 'butane'
    elif chain == '5':
        chain = 'pentane'
    elif chain == '6':
        chain = 'hexane'
    elif chain =='7':
        chain = 'heptane'
    elif chain == '8':
        chain = 'octane'
    elif chain == '9':
        chain = 'nonane'
    elif chain == '10':
        chain = 'decane'
    else:
        chain = 'Invalid input'
    
    if cyclo == 'yes':
        chain = 'cyclo' + chain
        
    # methyl and ethyl and propyl chains
    if number_methyl == '0' or number_methyl == '':
        x = ''
    if number_methyl == '1':
        x = '-methyl-'
    if number_methyl	== '2':
        x = '-dimethyl-'
    elif number_methyl == '3':
        x = '-trimethyl-'
    elif number_methyl == '4':
        x = '-tetramethyl-'
    
    if number_ethyl == '0' or number_ethyl == '':
        a = ''
    elif number_ethyl == '1':
        a = '-ethyl-'
    elif number_ethyl	== '2':
        a = '-diethyl-'
    elif number_ethyl == '3':
        a = '-triethyl-'
    elif number_ethyl == '4':
        a = '-tetraethyl-'
    
    if number_propyl == '0' or number_propyl == '':
        b = ''
    if number_propyl == '1':
        b = '-propyl-'
    if number_propyl	== '2':
        b = '-dipropyl-'
    elif number_propyl == '3':
        b = '-tripropyl-'
    elif number_propyl == '4':
        b = '-tetrapropyl-'
    
    if number_butyl == '0' or number_butyl == '':
        c = ''
    if number_butyl == '1':
        c = '-butyl-'
    if number_butyl	== '2':
        c = '-dibuytl-'
    elif number_butyl == '3':
        c = '-tributyl-'
    elif number_butyl == '4':
        c = '-tetrabutyl-'
    
    if number_bromo == '0' or number_bromo == '':
        d = ''
    if number_bromo == '1':
        d = '-bromo-'
    if number_bromo	== '2':
        d = '-dibromo-'
    elif number_bromo == '3':
        d = '-tribromo-'
    elif number_bromo == '4':
        d = '-tetrabromo-'
    return where_bromo + d + where_butyl  + c +  where_ethyl+  a  + where_methyl  + x + where_propyl + b + chain

answer_text = StringVar()
Label(root, textvariable=answer_text, font=("Roboto",15),fg='#ADFF2F',bg='#40a4a6').place(x=450, y=480, anchor="center")

def result():
    name = calculate(chain.get(), cyclo.get(), number_methyl.get(), number_ethyl.get(), number_propyl.get(), number_butyl.get(), number_bromo.get(), where_methyl.get(), where_ethyl.get(), where_propyl.get(), where_butyl.get(), where_bromo.get())
    answer_text.set(name)

# Add buttons
button1 = Button(text = "Calculate", command = result)
button1.pack(pady = 1)

# Execute tkinter
root.mainloop()