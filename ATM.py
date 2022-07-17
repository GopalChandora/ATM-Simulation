from tkinter import *
from tkinter import Label
from tkinter import messagebox

global Username, Account_number, User_pin, Initial_balance
Username = 'USER'
Account_number = 87896532366456
User_pin = 1234
Initial_balance = 10000

def AccountBalance():
    balance_screen = Toplevel(root)
    balance_screen.title("Account Balance Window")
    Label(balance_screen, text='Net Balance is:' + str(Initial_balance), font=('Time new Roman', 14)).grid(pady=35)
    Button(balance_screen, text="Exit", command=quit, font=('Time new Roman', 12), activeforeground="yellow",
           activebackground="orange", bg='black', fg='Silver', relief=RIDGE, padx=25).grid(row=5, padx=65, pady=20)

# Statement
def Statement():
    statement_screen = Toplevel(root)
    statement_screen.title("Account Statement")
    statement_screen.geometry("350x200")
    Label(statement_screen, text='Name: '+ Username, font=('Time new Roman', 14)).grid(padx=10, pady=10, sticky=W)
    Label(statement_screen, text='Account Number: ' + str(Account_number), font=('Time new Roman', 14)).grid(padx=10, pady=10, sticky=W)
    Label(statement_screen, text='Net balance is:' + str(Initial_balance), font=('Time new Roman', 14)).grid(padx=10, pady=10, sticky=W)
    Button(statement_screen, text="Exit", command=quit, font=('Time new Roman', 12), activeforeground="yellow",
           activebackground="orange", bg='black', fg='Silver', relief=RIDGE, padx=25).grid(row=7, padx=65, pady=20)

# Withdrawal
def Withdrawal():
    global user_amount, w_notif
    withdrawal_screen = Toplevel(root)
    withdrawal_screen.title("Withdrawal Window")
    withdrawal_screen.geometry("280x250")
    Label(withdrawal_screen, text='Enter Amount', font=('Time new Roman', 14)).grid(row=0, padx=10, pady=10)
    w_notif = Label(withdrawal_screen, font=('Times New Roman', 14))
    notif.grid(row=3)
    user_amount = StringVar()
    Entry(withdrawal_screen, textvariable=user_amount, font=('Time new Roman', 14)).grid(row=1, padx=10, pady=10)
    Button(withdrawal_screen, text='Withdraw', command=amount, font=('Time new Roman', 12), activeforeground="yellow",
           activebackground="orange", bg='black', fg='Silver', relief=RIDGE, padx=50).grid(row=2, padx=50, pady=10)
    Button(withdrawal_screen, text="Exit", command=quit, font=('Time new Roman', 12), activeforeground="yellow",
           activebackground="orange", bg='black', fg='Silver', relief=RIDGE, padx=25).grid(row=7, padx=65, pady=20)

# user Amount
def amount():
    global w_notif, Initial_balance
    if user_amount.get() == "":
        w_notif.config(text='Amount is required!', fg="red")
        w_notif.grid(row=5)
    elif float(user_amount.get()) > Initial_balance:
        w_notif.config(text="Insufficient balance", fg="red")
        w_notif.grid(row=5)
    elif float(user_amount.get()) % 100 != 0:
        w_notif.config(text="Amount should be Multiple of 100", fg="red")
        w_notif.grid(row=5)
    else:
        Initial_balance = Initial_balance - float(user_amount.get())
        w_notif.config(text="Successfully withdrawal\n Remaining balance is: " + str(Initial_balance), fg="green")
        w_notif.grid(row=5)


def chk_pin():
    pin_value.get()
    if pin_value.get() == User_pin:
        transaction_screen = Toplevel(root)
        transaction_screen.geometry("300x300")
        transaction_screen.title("Dashboard",)
        Button(transaction_screen, text="Withdrawal", command=Withdrawal, font=('Time new Roman', 12), activeforeground="yellow",
               activebackground="orange", bg='black', fg='Silver', relief=RIDGE, padx=25).grid(row=0, padx=65, pady=20)
        Button(transaction_screen, text="Account Balance", command=AccountBalance, font=('Time new Roman', 12),  activeforeground="yellow",
               activebackground="orange", bg='black', fg='Silver', relief=RIDGE, padx=15).grid(row=1, padx=65, pady=20)
        Button(transaction_screen, text="Statement", command=Statement, font=('Time new Roman', 12), activeforeground="yellow",
               activebackground="orange", bg='black', fg='Silver', relief=RIDGE, padx=25).grid(row=2, padx=65, pady=20)
        Button(transaction_screen, text="Exit", command=quit, font=('Time new Roman', 12),  activeforeground="yellow",
               activebackground="orange", bg='black', fg='Silver', relief=RIDGE, padx=25).grid(row=3, padx=65, pady=20)
    else:
        messagebox.showerror('PIN', 'Invalid PIN')

def begin():
    global pin_value
    begin_screen = Toplevel(root,)
    begin_screen.geometry("250x200")
    begin_screen.title('Login window')
    Label(begin_screen, text="Enter PIN", font=('Time new Roman', 14)).grid(padx=10, pady=10)
    pin_value=IntVar()
    Entry(begin_screen, textvariable=pin_value, font=('Time new Roman', 14), show='*').grid(padx=10, pady=10)
    Button(begin_screen, text="Login", command=chk_pin, font=('Time new Roman', 12), activeforeground="yellow", activebackground="orange", bg='black'
           , fg='Silver', relief=RIDGE, padx=50).grid(row=5, sticky=N, pady=10, padx=50)

def card():
    card_screen = Toplevel(root,)
    card_screen.geometry("200x100")
    card_screen.title('Card Window')
    Label(card_screen, text='Card inserted successfully', font=('Times new roman', 12), fg='Green').grid(padx=20)
    Button(card_screen, text="Start Transaction", font=('Times new roman', 12), width=10, command=begin,
           activeforeground="yellow", activebackground="orange", bg='black', fg='silver', relief=RIDGE, padx=10).grid(row=5, sticky=N, pady=10)


root = Tk()
root.geometry("400x200")
root.title('ATM Simulation')

Label(root, text="Welcome to TEC ATM", font=('Time new roman', 18, 'bold'), pady=10).grid(row=0, sticky=N, padx=50)
Label(root, text="The best ATM service in India", font=('Time new Roman', 16), pady=10).grid(row=1, sticky=N, padx=50)

notif = Label(root, font=('Time new Roman', 16))
notif.grid(row=4)

f1 = Frame(bg='red', borderwidth=5)


Button(f1, text="Enter your card", font=('Time new Roman', 12), width=10, command=card, activeforeground="yellow",
       activebackground="orange", bg='black', fg='silver', bd='5', relief=RIDGE, padx=50).grid(row=3, sticky=N)
f1.grid()

root.mainloop()