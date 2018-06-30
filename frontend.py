from Tkinter import *
import backend
import sqlite3

#selects Cancer_Name from cancer_types table when user inputs sequence that has a match with Gene_Sequence in genetic_mutations table
#example: input any sequence with "atgc" somewhere in between, should output breast cancer
def search_command():
    temp = e1.get()
    temp = temp.upper()
    errorText = " Please Enter Letters Only"
    notFound = " Not Found in Database"
    sizeError = " Input >20 nucleotides"
    totalText = temp.count('')-1

    if not temp.isalpha():
        list1.insert(0, errorText)
    else:
        if (totalText <= 20):
            list1.insert(0, sizeError)
        else:
            conn = sqlite3.connect("main.db")
            cur=conn.cursor()
            cur.execute("SELECT Cancer_Name FROM cancer_types JOIN genetic_mutations ON cancer_types.Gene_Name = genetic_mutations.Gene_Name WHERE instr(genetic_mutations.Gene_Sequence, ?)",(temp,))
            result = cur.fetchall()
            if not result:
                list1.insert(0, notFound)
            else:
                result2= str(result)[3:-4]
                list1.insert(0,result2)
                print("not null")
                cur.execute("SELECT Drug_Name FROM treatment JOIN genetic_mutations ON treatment.Gene_Name = genetic_mutations.Gene_Name WHERE instr(genetic_mutations.Gene_Sequence, ?)",(temp,))
                result3 = cur.fetchall()
                if not result3:
                    list2.insert(0, notFound)
                else:
                    result4= str(result3)[3:-4]
                    list2.insert(0,result4)
                    cur.execute("SELECT Function FROM treatment JOIN genetic_mutations ON treatment.Gene_Name = genetic_mutations.Gene_Name WHERE instr(genetic_mutations.Gene_Sequence, ?)",(temp,))
                    result5 = cur.fetchall()
                    result6 = str(result5)[3:-4]
                    list3.insert(0,result6)
                    print("not null")
            conn.commit()
            conn.close()

#Clearing the list box
def clearBox():
    list1.delete(0, END)
    list2.delete(0, END)
    list3.delete(0, END)

def clearEntry():
    e1.delete(0, END)


window = Tk()
window.title("Mutation Hunters")

canvas = Canvas(window, width=500, height=400)
canvas.pack()
#set background of window
image = PhotoImage(file="DNA.gif")
canvas.create_image(125,125, image=image)

#Main Label
label = Label(window, text="Enter Gene Sequence Here: ")
label_window = canvas.create_window(250, 90, anchor="n", window=label)

#Entry box
Gene_Sequence_text=StringVar()
e1=Entry(window, width=40,textvariable=Gene_Sequence_text)
e1_window = canvas.create_window(250, 120, anchor="n", window=e1)

#Cancer_name label
label2 = Label(window, text="Cancer name: ")
label2_window = canvas.create_window(130, 250, anchor="n", window=label2)

#Cancer_Name output
list1= Listbox(window, height=1, width=30)
list1_window = canvas.create_window(320, 250, anchor="n", window=list1)

#Treatment label
label3 = Label(window, width=11, text="Treatment: ")
label3_window = canvas.create_window(130, 280, anchor="n", window=label3)

#Treatment output
list2= Listbox(window, height=1, width=30)
list2_window = canvas.create_window(320, 280, anchor="n", window=list2)


#Function label
label4 = Label(window, width=11, text="Function: ")
label4_window = canvas.create_window(130, 310, anchor="n", window=label4)

#Function output
list3= Listbox(window, height=1, width=30)
list3_window = canvas.create_window(320, 310, anchor="n", window=list3)


#Buttons to submit and clear text area
b1=Button(window, text="Submit", width=12, command=search_command)
b1_window = canvas.create_window(175, 145, anchor="n", window=b1)
b2=Button(window, text="Clear", width=12, command=clearEntry)
b2_window = canvas.create_window(325, 145, anchor="n", window=b2)

#Button to clear the whole list box
b3=Button(window, text="Clear Box", width=12, command=clearBox)
b3_window = canvas.create_window(175, 340, anchor="n", window=b3)

#Button to Close the window
b4=Button(window,text="Close", width=12, command=window.destroy)
b4_window = canvas.create_window(325, 340, anchor="n", window=b4)

window.mainloop()
