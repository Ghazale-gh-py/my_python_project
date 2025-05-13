import tkinter as tk
from tkinter import simpledialog

victim = "Bonny"
suspects = ["Sam", "Robert", "Alex", "Jenny", "Austin"]
murderer = "Alex"
confession = {
    "Sam": "I've just found the corps, we were good friends.",
    "Robert": "My children always play with Bonny, I can't do it.",
    "Alex": "At that conflict I didn't say anything, I was silent at all. I didn't have any problem with her. How could I do this?",
    "Jenny": "I saw Alex near to warehouse at night. He was worried about something and talked to himself with stress.",
    "Austin":"I went hunting with my wife that night. We weren't near the village at all.",   
}

# --------------------------------Main function to run window-------------------------------------
def start_game():
    window = tk.Tk()
    window.title("Mysterious Village")
    window.geometry("420x420")

    title = tk.Label(window, text="Mysterious Village", font=("Helvetica", 16, "bold"))
    title.pack(pady=10)

    suspect_label = tk.Label(window, text="Suspects List:", font=("Helvetica", 12, "bold"))
    suspect_label.pack()

    for suspect in suspects:
        label = tk.Label(window, text=suspect, font=("Helvetica", 10))
        label.pack()

    result_box = tk.Text(window, height=6, width=50)
    result_box.pack(pady=10)

    def guess_murderer():
        name = simpledialog.askstring("Guess", "Enter murderer's name:")
        if name:
            if name.strip().capitalize() == murderer:
                result_box.insert(tk.END, "Congrats, you guessed right!\n")
                # window.quit()
            else:
                result_box.insert(tk.END, "You said it wrong.\n")

    def talk_to_suspect():
        name = simpledialog.askstring("Talk", "Who do you want to talk to?")
        if name:
            name = name.strip().capitalize()
            if name in confession:
                result_box.insert(tk.END, f"{name} says: {confession[name]}\n")
            else:
                result_box.insert(tk.END, "This name is not in suspect list.\n")

    guess_button = tk.Button(window, text="Guess", command=guess_murderer, width= 20)
    guess_button.pack(pady=5)

    talk_button = tk.Button(window, text="Talk", command=talk_to_suspect, width= 20)
    talk_button.pack(pady=5)

    exit_button = tk.Button(window, text="Exit", command=window.quit, width= 20)
    exit_button.pack(pady=10)

    window.mainloop()

start_game()
