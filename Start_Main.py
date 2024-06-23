from tkinter import *
from tkinter import ttk
from ants import *
from bugs import arm



def start():
    start_asyncio(lable1, all_ants_progress, lable_larva, lable_count_food, lable_amount_mushroom, time_of_life_lable,
                  lable_amount_aphid, lvl_ant_lable, lvl_life_lable, arm, lable_attack, show_results,
                  lable_def_attack2)



root = Tk()
root.title("METANIT.COM")
root.geometry("1300x700")

lable_background = Label(root, bg="#ed9277", text="", height=100, width=70, relief="solid")
lable_background.place(x=0, y=0)

lable_background2 = Label(root, bg="#e3633d", text="", height=100, width=115, relief="solid")
lable_background2.place(x=490, y=0)



btn = Button(root, text="START", font=("Arial", 20, "bold"), bg="#6be88c", command=start)
btn.place(x=20, y=620)



time_of_life_frame = Frame(root, bg="#07f064")
time_of_life_frame.place(x=0, y=0)

time_of_life_lable = Label(time_of_life_frame, text="0", font=("Arial", 20, "bold"), bg="#74eda5", fg="black", height=3, width=4)
time_of_life_lable.pack(side=RIGHT)

time_of_life_lable2 = Label(time_of_life_frame, text='Количество прожитых дней', font=("Arial", 16, "bold"), bg="#1aed5d", fg="#39664b", height=3, width=27)
time_of_life_lable2.pack(side=LEFT)



lvl_life_frame = Frame(root, bg="#094454")
lvl_life_frame.place(x=0, y=120)

lvl_life_lable = Label(lvl_life_frame, text="low", font=("Arial", 16, "bold"), bg="#0493ba", fg="#800112", height=3, width=5)
lvl_life_lable.pack(side=RIGHT)

lvl_life_lable2 = Label(lvl_life_frame, text='Уровень жизни муравьёв', font=("Arial", 16, "bold"), bg="#126278", fg="white", height=3, width=25)
lvl_life_lable2.pack(side=LEFT)


LVL_ANTHILL_frame = Frame(root, bg="black")
LVL_ANTHILL_frame.place(x=0, y=240)

lvl_ant_lable = Label(LVL_ANTHILL_frame, text="0", font=("Arial", 20, "bold"), bg="#6e0519", fg="white", height=3, width=4)
lvl_ant_lable.pack(side=RIGHT)

lvl_ant_lable2 = Label(LVL_ANTHILL_frame, text='LVL муравейника', font=("Arial", 16, "bold"), bg="#e30505", fg="#f3f2f7", height=3, width=20)
lvl_ant_lable2.pack(side=LEFT)



all_ants = Frame(root, bg="black")
all_ants.place(x=550, y=200)


lable1 = Label(all_ants, text="0" + "/ 5000", font=("Arial", 20, "bold"), bg="#32635b", fg="white", height=3, width=12)
lable1.pack(side=BOTTOM)

lable2 = Label(all_ants, text='Всего муровьев', font=("Arial", 14, "bold"), bg="#0c1c19", fg="#42cf3a", height=1, width=14)
lable2.pack(side=TOP)

all_ants_progress = ttk.Progressbar(all_ants, orient="horizontal", length=150, mode="determinate",  maximum=5000)
all_ants_progress.pack(side=TOP)




frame_larva = Frame(root, bg="black")
frame_larva.place(x=800, y=200)

lable_larva = Label(frame_larva, text="0" + "/ 1000", font=("Arial", 20, "bold"), bg="#32635b", fg="white", height=3, width=12)
lable_larva.pack(side=BOTTOM)

lable_larva2 = Label(frame_larva, text='Кол-во личинок', font=("Arial", 14, "bold"), bg="#0c1c19", fg="#42cf3a", height=2, width=14)
lable_larva2.pack(side=TOP)




frame_count_food = Frame(root, bg="black")
frame_count_food.place(x=1050, y=200)

lable_count_food = Label(frame_count_food, text="5000", font=("Arial", 20, "bold"), bg="#32635b", fg="white", height=3, width=12)
lable_count_food.pack(side=BOTTOM)

lable_count_food2 = Label(frame_count_food, text='Кол-во еды', font=("Arial", 14, "bold"), bg="#0c1c19", fg="#42cf3a", height=2, width=14)
lable_count_food2.pack(side=TOP)




frame_amount_mushroom = Frame(root, bg="black")
frame_amount_mushroom.place(x=550, y=400)

lable_amount_mushroom = Label(frame_amount_mushroom, text="0", font=("Arial", 20, "bold"), bg="#32635b", fg="white", height=3, width=12)
lable_amount_mushroom.pack(side=BOTTOM)

lable_amount_mushroom2 = Label(frame_amount_mushroom, text='Ферма грибов', font=("Arial", 14, "bold"), bg="#0c1c19", fg="#42cf3a", height=2, width=14)
lable_amount_mushroom2.pack(side=TOP)



frame_amount_aphid = Frame(root, bg="black")
frame_amount_aphid.place(x=800, y=400)

lable_amount_aphid = Label(frame_amount_aphid, text="0", font=("Arial", 20, "bold"), bg="#32635b", fg="white", height=3, width=12)
lable_amount_aphid.pack(side=BOTTOM)

lable_amount_aphid2 = Label(frame_amount_aphid, text='Ферма тлей', font=("Arial", 14, "bold"), bg="#0c1c19", fg="#42cf3a", height=2, width=14)
lable_amount_aphid2.pack(side=TOP)




frame_queen = Frame(root, bg="black")
frame_queen.place(x=1050, y=400)

lable_queen = Label(frame_queen, text="1", font=("Arial", 20, "bold"), bg="#e1ed39", fg="black", height=3, width=12)
lable_queen.pack(side=BOTTOM)

lable_queen2 = Label(frame_queen, text='Королева', font=("Arial", 16, "bold"), bg="#0c1c19", fg="#52f50c", height=2, width=14)
lable_queen2.pack(side=TOP)



frame_attack = Frame(root, bg="black")
frame_attack.place(x=1008, y=0)

lable_attack = Label(frame_attack, text="30", font=("Arial", 25, "bold"), bg="#e81a0c", fg="black", height=1, width=12, relief="solid")
lable_attack.pack(side=BOTTOM)

lable_attack2 = Label(frame_attack, text='Нападение жуков через:', font=("Arial", 16, "bold"), bg="#e85c54", fg="#800b03", height=2, width=22, relief="solid")
lable_attack2.pack(side=TOP)


frame_def_attack = Frame(root, bg="#501463")
frame_def_attack.place(x=515, y=1)

lable_def_attack = Label(frame_def_attack, text="Отражено  атак:", font=("Arial", 14, "bold"), bg="#8527a3", fg="white", height=2, width=14, relief="solid")
lable_def_attack.pack(side=TOP)
lable_def_attack2 = Label(frame_def_attack, text='0', font=("Arial", 13, "bold"), bg="#cfb8d6", fg="black", height=2, width=12, relief="solid")
lable_def_attack2.pack(side=TOP)






frame_attack_inf = Frame(root, bg="black")
frame_attack_inf.place(x=700, y=0)

lable_attack_inf = Label(frame_attack_inf, text="Результаты \n прошлого \n нападения:", font=("Arial", 14, "bold"), bg="#84d99b", fg="black", height=4, width=13, relief="solid")
lable_attack_inf.pack(side=BOTTOM)


frame_attack_inf2 = Frame(root, bg="black")
frame_attack_inf2.place(x=860, y=0)

lable_attack_inf2 = Label(frame_attack_inf2, text="", font=("Arial", 14, "bold"), bg="#84d99b", fg="#2a5938", height=4, width=11, relief="solid")
lable_attack_inf2.pack(side=BOTTOM)



def show_results(dead_ants, dead_mushroom, dead_aphid):
    frame_attack_ant = Frame(root, bg="black")
    frame_attack_ant.place(x=865, y=0)

    lable_attack_ant = Label(frame_attack_ant, text="-" + str(dead_ants) + " муравьёв", font=("Arial", 13, "bold"), bg="black", fg="#dff700", height=1, width=12, relief="solid")
    lable_attack_ant.pack(side=BOTTOM)

    frame_attack_mushroom = Frame(root, bg="black")
    frame_attack_mushroom.place(x=865, y=29)

    lable_attack_mushroom = Label(frame_attack_mushroom, text="-" + str(dead_mushroom) + " грибов", font=("Arial", 13, "bold"), bg="black", fg="#dff700", height=1, width=12, relief="solid")
    lable_attack_mushroom.pack(side=BOTTOM)

    frame_attack_aphid = Frame(root, bg="black")
    frame_attack_aphid.place(x=865, y=58)

    lable_attack_aphid = Label(frame_attack_aphid, text="-" + str(dead_aphid) + " тлей", font=("Arial", 13, "bold"), bg="black", fg="#dff700", height=1, width=12, relief="solid")
    lable_attack_aphid.pack(side=BOTTOM)


root.mainloop()
