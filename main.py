from modules import *


def expense_record():
    expense_des = expense_description.get()
    expense_val = expense_cost.get()
    expense_d = date.get()
    


root = tk.Tk()
root.title('Expense Tracker')
root.geometry('650x350')

title_label = tk.Label(root, text="Expense Tracker", font=("Arial", 16))
title_label.pack(pady=10)

#expense frame 
expense_frame = tk.Frame(root, bd=2, relief="raised")
expense_frame.place(x=20, y=70, width=300, height=160)
tk.Label(expense_frame, text="Add Expense").grid(row=0,columnspan=2, pady=8)

tk.Label(expense_frame, text="Expense: ").grid(row=1, column=0,padx=5, pady= 5, sticky="w")
expense_description = tk.Entry(expense_frame, width=30)
expense_description.grid(row=1, column=1 , padx=5, pady=5)

tk.Label(expense_frame, text="Amount: ").grid(row=2, column=0,padx=5, pady=5, sticky="w" )
expense_cost = tk.Entry(expense_frame, width=30)
expense_cost.grid(row=2, column=1, padx=5, pady=5)
tk.Label(expense_frame, text="Date: ").grid(row=3, column=0, padx=5, pady=5, sticky="w")
date = tk.Entry(expense_frame, width=30)
date.grid(row=3, column=1, padx=5, pady=5)

#record button
add_button = tk.Button(root, text="Add", command=expense_record, relief="raised")
add_button.place(x=125, y=230, width=70, height=30)


#expense list frame
view_frame = tk.Frame(root, bd=2, relief="raised")
view_frame.place(x=330, y=70, width=300, height=160)
tk.Label(view_frame, text="Expenses").pack(pady=5)
expense_list = tk.Listbox(view_frame, selectmode="single", width=40)
expense_list.pack(pady=5)



root.mainloop()

