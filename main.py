import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('akshay')

name_label = tk.Label(win, text='Enter your name : ')
name_label.grid(row=0, column=0, sticky=tk.W)

email_label = tk.Label(win, text = 'Enter your Email : ')
email_label.grid(row=1, column=0, sticky=tk.W)

age_label = tk.Label(win, text ='Enter your age : ')
age_label.grid(row=2, column=0, sticky=tk.W)

gender_label = tk.Label(win, text='select your gender : ')
gender_label.grid(row=3, column=0, sticky=tk.W)

#entery box
name_var = tk.StringVar()
name_entrybox = tk.Entry(win, width=16, textvariable = name_var)
name_entrybox.grid(row=0, column=1)

email_var = tk.StringVar()
email_entrybox = tk.Entry(win, width=16, textvariable = email_var)
email_entrybox.grid(row=1, column=1)

age_var = tk.StringVar()
age_entrybox = tk.Entry(win, width=16, textvariable = age_var)
age_entrybox.grid(row=2, column=1)

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=13, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('male','female','other')
gender_combobox.grid(row=3, column=1)

usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text='student',value='student',variable=usertype)
radiobtn1.grid(row=4, column=0)

radiobtn2 = ttk.Radiobutton(win, text='teacher',value='techer',variable=usertype)
radiobtn2.grid(row=4, column=1)

checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text='check if you want to join', variable=checkbtn_var)
checkbtn.grid(row=5, columnspan=3)
#BUTTON
def action():
    username = name_var.get()
    userage = age_var.get()
    useremail = email_var.get()
    usergender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        subcribed = 'NO'
    else:
        subcribed = 'YES'
    print(username,userage,useremail,usergender,user_type, subcribed)

    with open('file.txt', 'a') as f:
        
        f.write(f'{username},{userage},{useremail},{usergender},{user_type},{subcribed}')
        
    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    

submit_button = tk.Button(win, text='submit', command=action)
submit_button.grid(row=6, column=3)




win.mainloop()
