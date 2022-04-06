# message encode decode using a common key
import random
import tkinter

## encode a message using a common key
def encode(key: dict, message: str):
    encoded_msg = []
    for symbol in message:
        if symbol in key:
            encoded_msg.append(key[symbol])
        else:
            encoded_msg.append(symbol)
    return ''.join(encoded_msg)

## decode a message using a common key
def decode(key: dict, message: str):
    decoded_msg = []
    for symbol in message:
        if symbol in key.values():
            decoded_msg.append(list(key.keys())[list(key.values()).index(symbol)])
        else:
            decoded_msg.append(symbol)
    return ''.join(decoded_msg)


## create a key
def create_key(message):
    key = {}
    for symbol in message:
        if symbol not in key:
            key[symbol] = chr(random.randint(65, 90))
    return key


def submit(text: tkinter.Entry, frame: tkinter.Frame):
    key = create_key(text.get())
    encoded_msg = encode(key, text.get())
    decoded_msg = decode(key, encoded_msg)

    print(frame.children)


    # create a label
    label = tkinter.Label(frame, text="Encoded message:", font=("Helvetica", 20), bg="white")
    label.place(relx=0.5, rely=0.7, anchor="center")
    label.pack()

    # create a label
    label = tkinter.Label(frame, text=encoded_msg, font=("Helvetica", 20), bg="white")
    label.place(relx=0.5, rely=0.8, anchor="center")
    label.pack()

    # create a label
    label = tkinter.Label(frame, text="Decoded message:", font=("Helvetica", 20), bg="white")
    label.place(relx=0.5, rely=0.9, anchor="center")
    label.pack()

    # create a label
    label = tkinter.Label(frame, text=decoded_msg, font=("Helvetica", 20), bg="white")
    label.place(relx=0.5, rely=1, anchor="center")
    label.pack()
    
    




def play(frame: tkinter.Frame):
    # create text input
    text_input = tkinter.Entry(frame, font=("Helvetica", 20), bg="white")
    text_input.place(relx=0.5, rely=0.7, anchor="center")
    text_input.pack()
    text_input.focus()

    # create a button
    button = tkinter.Button(frame, text="Submit", font=("Helvetica", 20), bg="red", command=lambda: submit(text_input, frame))
    button.place(relx=0.5, rely=0.9, anchor="center")
    button.pack()


def start(name: str):
    # create a GUI
    root = tkinter.Tk()
    root.title(name)
    root.geometry("400x400")

    # create a canvas
    canvas = tkinter.Canvas(root, width=400, height=400)
    canvas.pack()

    # create a frame
    frame = tkinter.Frame(root, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # create a label
    label = tkinter.Label(frame, text=name, font=("Helvetica", 20), bg="white")
    label.place(relx=0.5, rely=0.1, anchor="center")
    label.pack()

    # create a button
    button = tkinter.Button(frame, text="Play", font=("Helvetica", 20), bg="red", command=lambda: play(frame))
    button.place(relx=0.5, rely=0.5, anchor="center")
    button.pack()

    # start the GUI
    root.mainloop()


start("Magic 8 Ball")
