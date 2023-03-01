import tkinter as tk
from random import randint

def start_button_click():
    global i
    i = 1
    start.destroy()
    setUp_entries()

def new_Word(): 
    if wordEntry.get() and defEntry.get():
        save_entries()
        updateNum_entries()
        clear_entries()

def done():
    global i
    if wordEntry.get() and defEntry.get():
        save_entries()
        clear_entries()
        i+=1
    
    wordEntry.destroy()
    defEntry.destroy()
    wordLabel.destroy()
    defLabel.destroy()
    cardNum.destroy()
    newWordButton.destroy()
    doneButton.destroy()
    top_frame.destroy()
    bottom_frame.destroy()
    middle_frame.destroy()
    display_card()
    
    
       
def setUp_entries():
    global i, cardNum
    global wordEntry, defEntry, wordLabel, defLabel, newWordButton, doneButton
    global top_frame, bottom_frame, middle_frame

    number = tk.IntVar()
    number.set(i)
    cardNum = tk.Label(textvariable = number, **arrow_button_properties)
    cardNum.pack()
    
    top_frame = tk.Frame(window, height=30, bg="black")
    top_frame.pack()
    
    wordLabel = tk.Label (text = "Word", **edit_label_properties)
    wordLabel.pack()
    wordEntry = tk.Entry(width = 107)
    wordEntry.pack()
    
    middle_frame = tk.Frame(window, height=20, bg="black")
    middle_frame.pack()
    
    defLabel = tk.Label (text = "Definition", **edit_label_properties)
    defLabel.pack()
    defEntry = tk.Entry(width=107)
    defEntry.pack()
    
    bottom_frame = tk.Frame(window, height=20, bg="black")
    bottom_frame.pack()
    
    newWordButton = tk.Button(text= "New Word", command = new_Word, **move_button_properties)
    newWordButton.pack(side=tk.LEFT, anchor=tk.SW)

    doneButton = tk.Button(text= "Done", command = done, **move_button_properties)
    doneButton.pack(side=tk.RIGHT, anchor=tk.SE)
    
def save_entries():
    word.append(wordEntry.get())  
    definition.append(defEntry.get())   

def updateNum_entries():
    global i
    i+=1
    number = tk.IntVar()
    number.set(i)
    cardNum.config(textvariable=number)
       
def clear_entries():    
    wordEntry.delete(0,tk.END)
    defEntry.delete(0,tk.END)

 
def random_number():
    global randNum 
    numWord = len(word)
    a = randint(0,numWord-1) 
    
    while a == randNum:
        a = randint(0,numWord-1)

    randNum = a

def add_new_card():
    nextWordButton.destroy()
    lastWordButton.destroy()
    addButton.destroy()
    deleteButton.destroy()
    cardButton.destroy()
    middle_frame.destroy()
    
    
    setUp_entries()

def delete_card():
    global i
    i -=1
    
    if len(word) > 1:
        next_word()
        del word[oldRandNum]
        del definition[oldRandNum]
        
    else:
        add_new_card()

    
def display_card():
    global nextWordButton, randNum, lastWordButton, cardButton, addButton, deleteButton, middle_frame
    randNum = 1
    random_number()
    
    addButton = tk.Button(text = "Add New Card", command = add_new_card, **move_button_properties)
    addButton.pack(side=tk.LEFT, anchor=tk.NW)
    
    deleteButton = tk.Button(text = "Delete Card", command = delete_card, **move_button_properties)
    deleteButton.pack(side=tk.RIGHT, anchor=tk.NE)
    
    middle_frame = tk.Frame(window, height=75, bg="black")
    middle_frame.pack()
    
    cardButton = tk.Button(text = word[randNum], command = show_new_def,  **card_button_properties)
    cardButton.pack()
    
    lastWordButton = tk.Button(text = "<", command = last_word,  **arrow_button_properties)
    lastWordButton.pack(side=tk.LEFT, anchor=tk.SW)
    
    nextWordButton = tk.Button(text = ">", command = next_word,  **arrow_button_properties)
    nextWordButton.pack(side=tk.RIGHT, anchor=tk.SE)
    
    
def show_new_word():
    global cardButton
    cardButton.configure(text = word[randNum], command = show_new_def) 

def show_old_word():
    global cardButton
    cardButton.configure(text = word[oldRandNum], command = show_old_def) 
    
def show_new_def():
    global cardButton
    cardButton.configure(text = definition[randNum], command = show_new_word)

def show_old_def():
    global cardButton
    cardButton.configure(text = definition[oldRandNum], command = show_old_word)

def last_word():
    show_old_word()
    
def next_word():
    global oldRandNum
    oldRandNum = randNum
    random_number()
    show_new_word()


    

font = "Comic Sans MS"

start_button_properties = {
    "fg": "black", 
    "bg": "white",
    "font" : (font, 60, "bold"),
    "width": 10,
    "height": 1,
    "borderwidth": 5
    }

edit_label_properties = {
    
    "fg": "black",
    "bg": "white",
    "font" : (font, 10, "bold"),
    "width": 80,
    "height": 2,
    "bd": 1
}

move_button_properties = {
    
    "fg": "black",
    "bg": "white",
    "font" : (font, 10, "bold"),
    "width": 15,
    "height": 2,
    "borderwidth": 5
}

arrow_button_properties = {
    "fg": "black",
    "bg": "white",
    "font" : (font, 10, "bold"),
    "width": 5,
    "height": 2,
    "borderwidth": 5
}

card_button_properties = {
    "fg": "black", 
    "bg": "white",
    "font" : (font, 20, "bold"),
    "width": 30,
    "height": 5,
    "borderwidth": 5
}

window = tk.Tk()
window['bg'] = 'black'
window.geometry("700x400")

word = [] 
definition = []

start = tk.Button(text= "Start", command = start_button_click, **start_button_properties)
start.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



window.mainloop()
 
 
