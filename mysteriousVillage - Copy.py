import tkinter as tk
# print("در یک دوره خشکسالی و آخر زمانی، روستایی خیلی کوچک وجود دارد به اسم Dagger. این روستا شامل ۵ خانواده است که دچار بحران پیدا کردن غذا شده‌اند. آن‌ها در یک انبار آذوقه جمع کردند که هر بار مقدار این انباشته ها کمتر از حدی که باید باشه میبینند.این ۵ خانواده به شدت با هم دعواشون میشه. دو روز بعد Sam که یکی از ساکنین این روستا هست جنازه Bonny رو نزدیک به انبار لای بوته ها پیدا میکنه و حراسون میره پیش بقیه و میگه که بانی کشته شده. همه به فکر فرو میرند و به هم شک می کنند.من کارآگاه این روستا هستم و با تمام این  اشخاص به تنهایی صحبت کردم و کلی مدارک جمع کردم. حالا میدونم که قاتل کیه. میتونی حدس بزنی که قاتل کیه؟ ")
victim = "Bonny"
Suspects = ["Sam", "Robert", "Alex", "Jenny", "Austin"]
murderer = "Alex"
Confession = {
    "Sam": "I've just found the corps, we were good friends.",
    "Robert": "My children always play with Bonny, I can't do it.",
    "Alex": "At that conflict I didn't say anything, I was silent at all. I didn't have any problem with her. How could I do this?",
    "Jenny": "I saw Alex near to warehouse at night. He was worried about something and talked to himself with stress.",
    "Austin":"I went hunting with my wife that night. We weren't near the village at all.",   
}
# Show list of Suspects
x = 0
while x < len(Suspects):
    if x == 0:
        print('Suspects List:')
    print(Suspects[x])
    x += 1

#Main function to run window
def start_game():
    window = tk.Tk()
    window.title("Mysterious Village")
    window.geometry("400x300")

    title = tk.Label(window, text="Mysterious Village", font= ("Helvetica", 16, "bold"))
    title.pack(pady=10)




# ---------------------------------------------------------------------
print("Do you want to guess or talk to suspects?", "Guess/Talk/Exit")
def guess_murderer():
    murderer_name = input("Murderer name:")
    if murderer_name == murderer:
        print('Yes, you guessed it right.')
        return True 
      
    else:
        print('You said it wrong.')
        return False

def talk_to_killer():
    talk_to = input("Who do you want to talk?")
    if talk_to in Confession:
        print(Confession[talk_to])

while True:     
    user_answer = input().lower() 
    if user_answer == "guess":
        if guess_murderer():
            break
    elif user_answer == "talk":
        talk_to_killer()
    elif user_answer == "exit":
        print("GoodBye")
        break

    


    





