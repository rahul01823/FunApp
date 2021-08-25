from tkinter import *
import os
import tkinter.messagebox as tmsg
global cl
cl=0
def about():
    tmsg.showinfo("About","The Login page consist of user info , calculator and game.")

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnclearDisplay():
    global operator
    operator=""
    text_Input.set(operator)

def btnEqualsInput():
    global operator
    global sumup
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

def btndelete():
    global operator
    n=len(operator)
    operator=str(operator[0:n-1])
    text_Input.set(operator)

def btnAnswer():
    global operator
    operator=operator+sumup
    text_Input.set(operator)


def callback(r,c):
    global player
    if player=='X' and states[r][c]==0 and stop_game==False:
        b[r][c].configure(text='X', fg='blue',bg='white')
        states[r][c] ='X'
        player= 'O'
    if player=='O' and states[r][c]==0 and stop_game==False:
        b[r][c].configure(text='O', fg='orange',bg='black')
        states[r][c] ='O'
        player= 'X'
    check_for_winner()
    if stop_game==True:
               print("Game is Ended")



def check_for_winner():
    global stop_game
    for i in range(3):
        if states[i][0] == states[i][1]==states[i][2]!=0:
            b[i][0].configure(bg='green')
            b[i][1].configure(bg='green')
            b[i][2].configure(bg='green')
            stop_game=True


    for i in range(3):
        if states[0][i] ==states[1][i]==states[2][i]!=0:
            b[0][i].configure(bg='green')
            b[1][i].configure(bg='green')
            b[2][i].configure(bg='green')
            stop_game=True

        if states[0][0] == states[1][1] ==states[2][2]  !=0:
            b[0][0].configure(bg='green')
            b[1][1].configure(bg='green')
            b[2][2].configure(bg='green')
            stop_game=True


        if states[2][0] == states[1][1] ==states[0][2]  !=0:
            b[2][0].configure(bg='green')
            b[1][1].configure(bg='green')
            b[0][2].configure(bg='green')
            stop_game=True



    if stop_game==True:
         tmsg.showinfo("Game is Over","Start new game")
         game.destroy()
         screen3.title("Fun App -Home")
def tictac():
     global game
     game =Toplevel(screen)
     game.maxsize(590,470)
     game.title("Fun Game-Tic Tac Toe")
     global operator 
     operator = ""
     global c
     c=0
     global i
     i=0
     global b
     b=[[0,0,0],
     [0,0,0],
     [0,0,0]]
     global states
     states=[[0,0,0],
     [0,0,0],
     [0,0,0]]
     for i in range(3):
          for j in range(3):
               b[i][j]=Button(game,font=("Arial",60),width=4,bg='powder blue',command= lambda r=i, c=j: callback(r,c))
               b[i][j].grid(row=i,column=j)
               c=c+1
     global player
     player='X'
     global stop_game
     stop_game = False    

def calculator():
    global cal
    cal=Toplevel(screen)
    
    cal.title("Calculator")
    global operator
    operator=""

    global text_Input
    text_Input=StringVar()
    txtDisplay = Entry(cal,font=('arial',20,'bold'), textvariable=text_Input, bd=30,insertwidth=4,bg="powder blue",justify='right').grid(columnspan=4)
    btn7=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="powder blue",command=lambda:btnClick((7))).grid(row=1,column=0)
    btn8=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="powder blue",command=lambda:btnClick((8))).grid(row=1,column=1)
    btn9=Button(cal,padx=16,pady=16,bd=12,fg="black",font=('arial',20,'bold'),text="9",bg="powder blue",command=lambda:btnClick((9))).grid(row=1,column=2)
    C=Button(cal,padx=16,pady=16,bd=12,fg="black",font=('arial',20,'bold'),text="C",bg="powder blue",command=btnclearDisplay).grid(row=1,column=3)

    #=============================================================================================================================================================================
    btn4=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="powder blue",command=lambda:btnClick((4))).grid(row=2,column=0)
    btn5=Button(cal,padx=16,bd=8,pady=16,fg="black",font=('arial',20,'bold'),text="5",bg="powder blue",command=lambda:btnClick((5))).grid(row=2,column=1)
    btn6=Button(cal,padx=16,bd=12,pady=16,fg="black",font=('arial',20,'bold'),text="6",bg="powder blue",command=lambda:btnClick((6))).grid(row=2,column=2)
    add=Button(cal,padx=16,bd=12,pady=16,fg="black",font=('arial',20,'bold'),text="+",bg="powder blue",command=lambda:btnClick(("+"))).grid(row=2,column=3)

    #=============================================================================================================================================================================
    btn1=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="powder blue",command=lambda:btnClick((1))).grid(row=3,column=0)
    btn2=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="powder blue",command=lambda:btnClick((2))).grid(row=3,column=1)
    btn3=Button(cal,padx=16,pady=16,bd=12,fg="black",font=('arial',20,'bold'),text="3",bg="powder blue",command=lambda:btnClick((3))).grid(row=3,column=2)
    sub=Button(cal,padx=16,pady=16,bd=12,fg="black",font=('arial',20,'bold'),text="-",bg="powder blue",command=lambda:btnClick(("-"))).grid(row=3,column=3)

    #============================================================================================================================================================================
    btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="powder blue",command=lambda:btnClick((0))).grid(row=4,column=0)
    multiply=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="powder blue",command=lambda:btnClick(("*"))).grid(row=4,column=1)
    divide=Button(cal,padx=16,pady=16,bd=13,fg="black",font=('arial',20,'bold'),text="/",bg="powder blue",command=lambda:btnClick(("/"))).grid(row=4,column=2)
    equal=Button(cal,padx=16,pady=16,bd=12,fg="black",font=('arial',20,'bold'),text="=",bg="powder blue",comman=btnEqualsInput).grid(row=4,column=3)

    #=============================================================================================================================================================================
    mod=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="%",bg="powder blue",command=lambda:btnClick(("%"))).grid(row=5,column=0)
    dot=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text=".",bg="powder blue",command=lambda:btnClick(("."))).grid(row=5,column=1)
    answer=Button(cal,padx=14,pady=16,bd=8,fg="black",font=('arial',18,'bold'),text="ans",bg="powder blue",comman=btnAnswer).grid(row=5,column=2)
    back=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',18,'bold'),text="del",bg="powder blue",comman=btndelete).grid(row=5,column=3)
    cal.mainloop()


def login_sucess():
    global screen3
    screen3=Toplevel(screen)
    screen2.destroy()
    screen3.title("Fun App -Home")
    screen3.geometry("400x200")
    Label(screen3,text="Welcome",font="regular 18 bold").grid(row=1,column=0)
    Label(screen3,text=n,font="regular 18 bold underline").grid(row=1,column=1)

    mainmenu=Menu(screen3)
    m1 = Menu(mainmenu, tearoff=0)
    m1.add_command(label="calculator", command=calculator)
    m1.add_command(label="tictac game", command=tictac)
    m1.add_separator()
    m1.add_command(label="about",command=about)
    m1.add_command(label="exit",command=screen3.destroy)
    screen3.config(menu=mainmenu)
    mainmenu.add_cascade(label="Menu", menu=m1)

def invalid_pass():
    global screen4
    screen4=Toplevel(screen)
    screen4.title("sucess")
    screen4.geometry("150x100")
    Label(screen4,text="Invalid Password").grid(row=0,column=0)
    Label(screen4,text="").grid(row=1,column=0)

    Button(screen4,text="ok",command=screen4.destroy).grid(row=2,column=0)


def not_found():
    global screen5
    screen5=Toplevel(screen)
    screen5.title("sucess")
    screen5.geometry("250x100")
    Label(screen5,text="Please Sign Up before Login").grid(row=0,column=0)
    Label(screen5,text="").grid(row=1)
    Button(screen5,text="ok",command=screen5.destroy).grid(row=2,column=0)

def reg_user():
    user_info=username.get()
    pass_info=password.get()
    file=open(user_info,"w")
    file.write(user_info+"\n")
    file.write(pass_info)
    file.close

    user_entry.delete(0,END)
    pass_entry.delete(0,END)

    Label(screen,text="Registeration Succesufull",fg='green',font="cambria 16 bold").grid(row=8,column=0)
    screen1.destroy()

def log_verify():
    username1= user_verify.get()
    password1= pass_verify.get()
    user_entry1.delete(0,END)
    pass_entry1.delete(0,END)

    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,'r')
        global n
        n=username1

        verify=file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            invalid_pass()
    else:
        print("User not found!")
        not_found()
def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("resgister")
    screen1.geometry("300x250")

    global username
    global password
    global user_entry
    global pass_entry


    username=StringVar()
    password=StringVar()

    Label(screen1,text="Please Enter Detail Below").grid(row=0,column=0)
    Label(screen1,text="").grid(row=1,column=0)
    Label(screen1,text="Username * ").grid(row=2,column=0)
    user_entry= Entry(screen1,textvariable=username)
    user_entry.grid(row=3,column=0)
    Label(screen1,text="Password * ").grid(row=4,column=0)
    pass_entry=Entry(screen1,textvariable=password)
    pass_entry.grid(row=5,column=0)
    Label(screen1,text="").grid(row=6,column=0)
    Button(screen1,text="Register",width="15",height="1",bg="powder blue",command=reg_user).grid(row=7,column=0)

def login():
    global screen2,cl
    screen2=Toplevel(screen)
    screen2.title("Fun App-Login")
    screen2.geometry("300x250")
    screen2.maxsize(400,250)
    screen2.minsize(300,250)
    if (screen2 == True):
         print("h")
    Label(screen2,text="Please Enter Detail Below to Login").grid(row=0,column=0)
    Label(screen2,text="").grid(row=1,column=0)

    global user_verify
    global pass_verify

    user_verify=StringVar()
    pass_verify=StringVar()

    global user_entry1
    global pass_entry1

    Label(screen2,text="Username * ").grid(row=2,column=0)
    user_entry1= Entry(screen2,textvariable=user_verify)
    user_entry1.grid(row=3,column=0)
    Label(screen2,text="").grid(row=4,column=0)
    Label(screen2,text="Password * ").grid(row=5,column=0)
    pass_entry1= Entry(screen2,textvariable=pass_verify)
    pass_entry1.grid(row=6,column=0)
    Label(screen2,text="").grid(row=7,column=0)
    Button(screen2,text="Login",width="15",height="1",bg="powder blue",command=log_verify).grid(row=8,column=0)


def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x200")
    screen.maxsize(300,200)
    screen.maxsize(300,200)
    screen.title("Fun App")

    print("Main Screen")
    Button(text="Login",width="30",height="2",bg="powder blue",command=login).grid(row=2,column=2)
    Label(text="").grid(row=1,column=1)
    Button(text="Register",width="30",height="2",bg="powder blue",command=register).grid(row=3,column=2)
    screen.mainloop()
main_screen()
