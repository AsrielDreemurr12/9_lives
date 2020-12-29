from tkinter import*
from tkinter import messagebox
from time import*
from random import*

game_flag=True

def fun():
    global game_flag, secret_word, clue_text, secret_word
    if game_flag:
        game_flag=False
        clue_text['text']=secret_word
        messagebox.showerror('Печаль...',f'К сожалению, вы сдались, было загадано слово {secret_word}')    

def main():        
    global clue, secret_word, entry, lives_text, wa
    global lives, symbol, clue_text, wrong_answers,game_flag
    answer=entry.get().lower()
    lower_secret=secret_word.lower()
    if game_flag:
        if lives>0:
            if len(answer)>1:
                if answer==lower_secret:
                    clue_text['text']=secret_word
                    messagebox.showinfo('Победа!',f'Вы угадали, было загадано слово {secret_word}')
                    game_flag=False
                else:
                    messagebox.showerror('Ой...','Вы теряете жизнь... ')
        
            else:
                if answer in lower_secret:
                    for i in range(len(secret_word)):
                        if lower_secret[i]==answer:
                            clue[i]=answer
                        if lower_secret[i]=='ё' and answer=='е':
                            clue[i]=lower_secret[i]
                            
                    clue_text['text']=f'{clue}'
                    messagebox.showinfo('Ура!','Вы угадали одну букву!')                
                else:
                    if not (answer in wrong_answers):
                        lives-=1
                        lives_text['text']=lives*symbol
                        wrong_answers.append(answer)
                        wa['text']=f'Неправильные ответы: {wrong_answers}'
                        messagebox.showerror('Ой...','Вы теряете жизнь... ')                                        
                    else:
                        messagebox.showinfo('Введите другую букву','Вы уже вводили этот ответ)')
        else:        
            messagebox.showerror('Упс...',f'К сожалению, вы не угадали, было загадано слово {secret_word}')
            game_flag=False
        
        if clue==list(secret_word):
            clue_text['text']=clue
            messagebox.showinfo('Победа!',f'Вы угадали, было загадано слово {secret_word}')
            game_flag=False
        
a=Tk()
a.title('9 жизней')
a.resizable(width=False, height=False)
a.iconbitmap('images/icon.ico')

symbol=['♥']
lives=9

wrong_answers=[]

words=['кукушка','цапля','щука','аконит','молекула','протон',
       'калужница','шалфей','трилобит','меганевра',
       'монарх','магнолия','тис','ланцетник','янтарь',
       'мечехвост','светлячок','инфузория','шмель','главк',
       'тиктаалик','ихтиостега','гаттерия','глюкоза','нереис',
       'протоптер','мегалодон','аммонит','кирпич','гликоген',
       'полушник','папоротник','каракатица','ихтиозавр','фруктоза',
       'галактоза','археоптерикс','транзакция','Эльбрус','дронт',
       'аргентавис','мамонт','окопник','латимерия','крахмал',
       'ракоскорпион','мандрагора','птеродактиль','нарцисс','вираж',
       'дупло','бухта','адонис','ирис','шиповник','беладонна','зенит',
       'залив','буревестник','гоацин','дельфин','нарвал','орешек','ёлка',
       'нейтрон','электрон','хорда','пижма','зубатка','омела']

secret_word=choice(words).lower()
clue=['?']*len(secret_word)

lab=Label(text='Введите букву или слово целиком:',fg='mediumvioletred',font='Arial 14')
lab.pack()

btn2=Button(text='Сдаться',command=fun)
btn2.pack(side=BOTTOM,anchor=W)

btn=Button(text='Ответить',command=main)
btn.pack(side=BOTTOM,anchor=W)

entry=Entry(bd=3)
entry.pack(anchor=W,pady=5)

label=Label(text='Осталось жизней: ',fg='mediumvioletred',font='Arial 14')
label.pack(anchor=W)

wa=Label(text=f'Неправильные ответы: {wrong_answers}',fg='mediumvioletred',font='Arial 14')
wa.pack(anchor=W,side=BOTTOM,pady=7)

lives_text=Label(text=[symbol]*lives,fg='mediumvioletred',font='Arial 14')
lives_text.pack(anchor=W)

clue_text=Label(text=f'{clue}',fg='mediumvioletred',font='Arial 14')
clue_text.pack(anchor=W)

a.mainloop()
