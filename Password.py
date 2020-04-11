import tkinter as tk
import tkinter.ttk as ttk
import pickle
import os

# global variables
frame = tk.Tk()
user = "Username"
passw = "Password"
open_labs = open("label.data", "rb")
open_users = open("user.data", "rb")
open_passwords = open("password.data", "rb")
top_button_pos = [125, 280]
top_back_color = "#80bfff"
add_back_color = "Teal"
edit_back_color = "Light Blue"
head_font_1 = "Arial, 35"
head_font_2 = "Arial, 20"
user_label_text = "Username: "
pass_label_text = "Password: "
add_edit_status = "normal"
add_edit_size = "400x400"
add_edit_field_pos = [200, 112]

#Login Class, main operator in program
class Login:
    '''
    Login class, stores usernames, passwords and a label
    organized by a common index
    relies on all aspects to be insterted into the lists in the same order
    '''
    def __init__(self):
        self.users = []
        self.passes = []
        self.labels = []
    def get_user(self, ind):
        v = self.labels.index(ind)
        return self.users[v]
    def get_pass(self, ind):
        v = self.labels.index(ind)
        return self.passes[v]
    def get_lab(self, ind):
        v = self.labels.index(ind)
        return self.labels[v]
    def get_ind(self, index):
        v = self.labels.index(index)
        return v
    def add_login(self, label, user, passw ):
        self.users.append(user)
        self.passes.append(passw)
        self.labels.append(label)
    def pull_lab(self):
        l_lst = list(self.labels)
        return l_lst
    def update_login(self, place, upd_lab, upd_use, upd_pas):
        self.labels[place] = upd_lab
        self.users[place] = upd_use
        self.passes[place] = upd_pas
    def get_lab_list(self):
        v = self.labels
        return v
    def get_user_list(self):
        v = self.users
        return v
    def get_pass_list(self):
        v = self.passes
        return v
    def upload_lab(self, labs):
        self.labels = labs
    def upload_use(self, user):
        self.users = user
    def upload_pas(self, pas):
        self.passes = pas
    def delete_login(self, ind):
        self.labels.pop(ind)
        self.users.pop(ind)
        self.passes.pop(ind)
    def get_entry_ind(self, ind):
        return self.labels[ind]

#Label class, easy setup of multiple labels
class Prgrm_labels(tk.Label):
    '''
    Takes a location, content and formatting to make custom labels in frame
    '''
    def __init__(self, parent, posx , posy, content, font, color = "Light Gray", font_color = "Black"):
        self.text_content = content
        tk.Label.__init__(self, parent)
        self.config(text = self.text_content, font = font, background = color, fg = font_color)
        self.place(x = posx, y = posy)

#Combobox for list of login labels
class Pass_list(ttk.Combobox):
    '''
    pulls values from Login class label list
    '''
    def __init__(self, parent):
        self.current_table = tk.StringVar(frame, "Select desired info")
        ttk.Combobox.__init__(self, parent)
        self.config(textvariable=self.current_table, state="readonly",
                    postcommand = self.check_vals)
        self.place(x=150, y=110, anchor = "w")
    def get_current(self):
        return self.get()
    def check_vals(self):
        self.config(values = new_log.pull_lab())
    def start_over(self):
        self.set(new_log.get_entry_ind(0))

#Field class, easy setup of multiple fields
class Field_entry(tk.Entry):
    '''
    Takes positional arguments, default displayed text and read/write only
    '''
    def __init__(self, parent, posx, posy, status, default):
        tk.Entry.__init__(self, parent)
        self.def_entry = tk.StringVar(frame, default)
        self.config(textvariable = self.def_entry,  state = status, width = 30)
        self.place(x = posx, y = posy)
    def re_fill(self, new):
        self.config(textvariable = new)
    def clear_entry(self):
        self.config(textvariable = "")

#Button class for creation of multiple buttons
class New_button(tk.Button):
    '''
    Takes positional arguments and a label
    '''
    def __init__(self, parent, posx, posy, label):
        tk.Button.__init__(self, parent)
        self.config(text = label, width = 25)
        self.place(x = posx, y = posy)

#Return login function on update of combobox
def ret_log(event):
    '''
    takes global user and passw varibles and assigns them to corresponding list entry
    '''
    global user, passw, user_field, pass_field, cmb_login
    user = tk.StringVar(frame, new_log.get_user(cmb_login.get_current()))
    user_field.re_fill(user)
    passw = tk.StringVar(frame, new_log.get_pass(cmb_login.get_current()))
    pass_field.re_fill(passw)

#Add login function, lets you add an entry to Login class
def add_login(event):
    '''
    Opens new window, with several fields, labels and a button to add to login class
    '''
    add_win = tk.Toplevel(frame)
    add_win.title("Add Login Info")
    add_win.geometry(add_edit_size)
    add_win.config(background = add_back_color)
    add_new_button = New_button(add_win, 110, 275, "Add")
    add_new_title = Prgrm_labels(add_win, 50, 15, "Add Login Info", head_font_1, add_back_color)
    add_new_label = Prgrm_labels(add_win, 25, 100, "Login Label: ", head_font_2, add_back_color)
    add_user_label = Prgrm_labels(add_win, 40, 150, user_label_text, head_font_2, add_back_color)
    add_pass_label = Prgrm_labels(add_win, 45, 200, pass_label_text, head_font_2, add_back_color)
    new_l_field = Field_entry(add_win, add_edit_field_pos[0], add_edit_field_pos[1], add_edit_status, "")
    new_u_field = Field_entry(add_win, add_edit_field_pos[0], add_edit_field_pos[1] + 50, add_edit_status, "")
    new_p_field = Field_entry(add_win, add_edit_field_pos[0], add_edit_field_pos[1] + 100, add_edit_status, "")
    #button handler for button press event, calls login class to add field entries
    def button_handler(event):
        new_log.add_login(new_l_field.get(), new_u_field.get(), new_p_field.get())
        add_win.destroy()
    add_new_button.bind("<Button-1>", button_handler)

#Edit login function, opens window to edit current selection
def edit_login(event):
    '''
    opens a new window, with several text fields to update current combobox selection
    '''
    edit_win = tk.Toplevel(frame)
    edit_win.title("Edit Login Info")
    edit_win.geometry(add_edit_size)
    edit_win.config(background = edit_back_color)
    edit_new_button = New_button(edit_win, 110, 275, "Save Changes")
    edit_new_title = Prgrm_labels(edit_win, 50, 15, "Edit Login Info", head_font_1, edit_back_color)
    edit_new_label = Prgrm_labels(edit_win, 25, 100, "Login Label: ", head_font_2, edit_back_color)
    edit_user_label = Prgrm_labels(edit_win, 40, 150, user_label_text, head_font_2, edit_back_color)
    edit_pass_label = Prgrm_labels(edit_win, 45, 200, pass_label_text, head_font_2, edit_back_color)
    edit_l_field = Field_entry(edit_win, add_edit_field_pos[0], add_edit_field_pos[1],
                               add_edit_status, new_log.get_lab(cmb_login.get_current()))
    edit_u_field = Field_entry(edit_win, add_edit_field_pos[0], add_edit_field_pos[1] + 50,
                               add_edit_status, new_log.get_user(cmb_login.get_current()))
    edit_p_field = Field_entry(edit_win, add_edit_field_pos[0], add_edit_field_pos[1] + 100,
                               add_edit_status, new_log.get_pass(cmb_login.get_current()))
    #edit button even handler, calls login class to update the selected entry
    def edit_button_handler(event):
        new_log.update_login(new_log.get_ind(cmb_login.get_current()), edit_l_field.get(),
                             edit_u_field.get(), edit_p_field.get())
        edit_win.destroy()
    edit_new_button.bind("<Button-1>", edit_button_handler)

#Function to load pickled files
def load_info():
    #intiates lists
    load_labels = []
    load_users = []
    load_passwords = []

    #populates lists with opened pickle files
    if os.path.getsize("label.data") > 0:
        load_labels = list(pickle.load(open_labs))
    if os.path.getsize("user.data") > 0:
        load_users = list(pickle.load(open_users))
    if os.path.getsize("password.data") > 0:
        load_passwords = list(pickle.load(open_passwords))

    #calls Login class to upload lists
    new_log.upload_lab(load_labels)
    new_log.upload_use(load_users)
    new_log.upload_pas(load_passwords)

#Function to save data into pickled files
def save_info():
    #pulls lists from Login class
    add_lab_list = new_log.get_lab_list()
    add_use_list = new_log.get_user_list()
    add_pas_list = new_log.get_pass_list()

    #dumps lists into pickled files
    pickle.dump(add_lab_list, pick_labs)
    pickle.dump(add_use_list, pick_users)
    pickle.dump(add_pas_list, pick_passwords)

#Delete info function, called from delete button
def delete_info(event):
    '''
    Deletes current selection from Login class
    updates combobox and text fields after deletion
    '''
    global user, passw, user_field, pass_field, cmb_login
    new_log.delete_login(new_log.get_ind(cmb_login.get_current()))
    cmb_login.start_over()
    user = tk.StringVar(frame, new_log.get_user(cmb_login.get_current()))
    user_field.re_fill(user)
    passw = tk.StringVar(frame, new_log.get_pass(cmb_login.get_current()))
    pass_field.re_fill(passw)


new_log = Login()

load_info()
cmb_login = Pass_list(frame)
title = Prgrm_labels(frame, 25, 15, "Password Storage", head_font_1, top_back_color)
user_label = Prgrm_labels(frame, 25, 150, user_label_text, head_font_2, top_back_color)
pass_label = Prgrm_labels(frame, 30, 200, pass_label_text, head_font_2, top_back_color)
add_button = New_button(frame, top_button_pos[0], top_button_pos[1] + 40, "Add Login")
edit_button = New_button(frame, top_button_pos[0], top_button_pos[1], "Edit Current Selection")
delete_button = New_button(frame, top_button_pos[0], top_button_pos[1] + 80, "Delete Current Selection")
user_field = Field_entry(frame, 200, 161, "readonly", user)
pass_field = Field_entry(frame, 200, 211, "readonly", passw)

cmb_login.bind("<<ComboboxSelected>>", ret_log)
add_button.bind("<Button-1>", add_login)
edit_button.bind("<Button-1>", edit_login)
delete_button.bind("<Button-1>", delete_info)
frame.title("Password Reference")
frame.geometry("450x450")
frame.config(background = top_back_color)
frame.mainloop()
pick_labs = open("label.data", "wb")
pick_users = open("user.data", "wb")
pick_passwords = open("password.data", "wb")
save_info()
pick_labs.close()
pick_users.close()
pick_passwords.close()
