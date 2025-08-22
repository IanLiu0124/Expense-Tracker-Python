from modules import *

# with open("SampleResult.tSxt", "w", encoding="utf-8") as f:
#     for field_name, value in result_set.items():
#         f.write(f"{field_name}: {value}\n")

try:
    with open("expenese.json", "r") as j:
        expenses = json.load(j)
        #json.load(j) = 
except FileNotFoundError:
    expenses = []
except:
    expenses = []

def clear_entries():
    expense_description.delete(0, 'end') #from index 0 to end
    expense_cost.delete(0, 'end')
    date.set_date(datetime.date.today())
    expense_comment.delete("1.0", "end") #First line, index 0
    

def expense_record():
    if expense_description.get().strip() == "":
        messagebox.showerror("Invalid Input", "Please enter description")
    else:
        expense_des = expense_description.get().strip()
        try:
            expense_val = float(expense_cost.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for the amount.")
            return
        expense_d = date.get()
        comment = expense_comment.get("1.0","end").strip() or '' #the param ("1.0" = Line 1, character 0), "end" til the end of the textbox
        
        new_expense = {} #initiate a dictionary
        new_expense['Expense Description'] = expense_des
        new_expense['Expense Cost'] = expense_val 
        new_expense['Expense Date'] = expense_d
        new_expense['Comment'] = comment
        
        expenses.append(new_expense)
        with open("expenese.json", "w") as f:
            json.dump(expenses, f, indent =4)
        expense_list.insert(tk.END, f"{new_expense['Expense Date']} | {new_expense['Expense Description']} - {new_expense['Expense Cost']}$")
        
    clear_entries()
    

    # messagebox.showinfo('test', new_expense)
    



    #Writing to file
    #----
    # with open("Expenses.txt", "a", encoding="utf-8") as E:
    #     E.write(f"Expense: {expense_des} | {expense_val}$ | {expense_d}\n {new_expense}")
    #Using w will overwrite.
    #Using a will APPEND.



def delete_expense():
    return

root = tk.Tk()
root.title('Expense Tracker')
root.geometry('650x350')

title_label = tk.Label(root, text="Expense Tracker", font=("Arial", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

#expense frame 
expense_frame = tk.Frame(root, bd=2, relief="groove")
# expense_frame.place(x=20, y=70, width=300, height=160)
#Changing to .grid to test
expense_frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")
tk.Label(expense_frame, text="Add Expense").grid(row=0,columnspan=2, pady=8)

#Expense Description
tk.Label(expense_frame, text="Expense: ").grid(row=1, column=0,padx=5, pady= 5, sticky="w")
expense_description = tk.Entry(expense_frame, width=30)
expense_description.grid(row=1, column=1 , padx=5, pady=5)

#Expense Amount
tk.Label(expense_frame, text="Amount: ").grid(row=2, column=0,padx=5, pady=5, sticky="w" )
expense_cost = tk.Entry(expense_frame, width=30)
expense_cost.grid(row=2, column=1, padx=5, pady=5)

#Expense Date
tk.Label(expense_frame, text="Date: ").grid(row=3, column=0, padx=5, pady=5, sticky="w")
# date = tk.Entry(expense_frame, width=30)
#Changing it to DateEntry object from tkcalendar
date = DateEntry(expense_frame, width= 30, date_pattern="mm-dd-yy")
date.grid(row=3, column=1, padx=5, pady=5)

#Expense Comment
tk.Label(expense_frame, text="Comment: ").grid(row=4, column=0, padx=5, pady=5, sticky="w")
expense_comment = tk.Text(expense_frame, width=25, height=2 )
expense_comment.grid(row=4, column=1, padx=5, pady=5, sticky="w")


#record button
add_button = tk.Button(root, text="Add", command=expense_record, relief="raised")
add_button.place(x=125, y=240, width=70, height=30)


#expense list frame
view_frame = tk.Frame(root, bd=2, relief="groove")
# view_frame.place(x=330, y=70, width=300, height=160)
#Changing to .place to test
view_frame.grid(row=1, column=1, padx=20, pady=10, sticky="n")
tk.Label(view_frame, text="Expenses").pack(pady=5)
expense_list = tk.Listbox(view_frame, selectmode="single", width=40)
expense_list.pack(pady=2)

#Inserting Exsisting Expenses to the list
for expense in expenses:
    expense_list.insert(tk.END, f"{expense['Expense Date']} | {expense['Expense Description']} - {expense['Expense Cost']}$")

#Delete Button
delete_button = tk.Button(root, text="Delete",command = delete_expense, relief="raised")
delete_button.place(x=435, y= 265, width=70, height=30)


root.mainloop()

