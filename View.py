import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from Models import Users
from Models import Products
from Controller import Account
from Controller import ProductsController


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.setFrame(LoginWindow)

    def setFrame(self, frame_class):
        """
        This function set the frame which will be displayed on window.
        """
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class LoginWindow(tk.Frame):
    """
    This is the login window, here you can login in.
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Login")
        self.master.geometry("300x200")
        self.master.resizable(False, False)
        self.master.eval('tk::PlaceWindow . center')

        self.usernameLabel = tk.Label(
            self, text="User Name:", bg="grey", fg="white").pack(pady=10, fill="x")
        self.username = tk.StringVar()
        self.usernameEntry = tk.Entry(
            self, textvariable=self.username).pack(pady=10)

        self.passwordLabel = tk.Label(
            self, text="Password:", bg="grey", fg="white").pack(pady=10, fill="x")
        self.password = tk.StringVar()
        self.passwordEntry = tk.Entry(
            self, textvariable=self.password, show='*').pack(pady=10)

        self.btnLogin = tk.Button(
            self, text="Login", command=self.btnLogin_Click).pack(pady=10)

    def btnLogin_Click(self):
        """
        The login button's click event, this code will be runned, when the button is pressed.
        """
        self.u = Users()
        self.acc = Account()

        self.u.setUsername(self.username.get())
        self.u.setPassword(self.password.get())
        self.acc.Login(self.u)

        if self.u.getId() != None:
            messagebox.showinfo(
                "Login", self.u.getMessage())
            self.master.setFrame(MainWindow)
        else:
            messagebox.showinfo(
                "Login", self.u.getMessage())


class MainWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Main")
        self.master.geometry("1024x864")
        self.master.resizable(False, False)
        self.master.eval('tk::PlaceWindow . center')

        ### Labels and entrys
        self.lblName = tk.Label(self, text="Phone's name:", font=(
            "Century Gothic", 10), bg="blue", fg="yellow").pack(pady=10)
        self.entName = tk.Entry(self)
        self.entName.pack()
        self.lblBrand = tk.Label(self, text="Phone's brand:", font=(
            "Century Gothic", 10), bg="blue", fg="yellow").pack(pady=10)
        self.entBrand = tk.Entry(self)
        self.entBrand.pack()
        self.lblReleased = tk.Label(self, text="Released date:", font=(
            "Century Gothic", 10), bg="blue", fg="yellow").pack(pady=10)
        self.entReleased = tk.Entry(self)
        self.entReleased.pack()
        self.lblDisplaySize = tk.Label(self, text="Display size:", font=(
            "Century Gothic", 10), bg="blue", fg="yellow").pack(pady=10)
        self.entDisplaySize = tk.Entry(self)
        self.entDisplaySize.pack()
        self.lblDisplayType = tk.Label(self, text="Display type:", font=(
            "Century Gothic", 10), bg="blue", fg="yellow").pack(pady=10)
        self.entDisplayType = tk.Entry(self)
        self.entDisplayType.pack()
        self.lblCPU = tk.Label(self, text="CPU:", font=(
            "Century Gothic", 10), bg="blue", fg="yellow").pack(pady=10)
        self.entCPU = tk.Entry(self)
        self.entCPU.pack()
        self.lblRAM = tk.Label(self, text="RAM (gb):", font=(
            "Century Gothic", 10), bg="blue", fg="yellow").pack(pady=10)
        self.entRAM = tk.Entry(self)
        self.entRAM.pack()
        self.lblNoCameras = tk.Label(self, text="Number of cameras:", font=(
            "Century Gothic", 10), bg="blue", fg="yellow").pack(pady=10)
        self.entNoCameras = tk.Entry(self)
        self.entNoCameras.pack()
        ###

        ### Table
        columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9")
        self.tvProducts = ttk.Treeview(
            self, show="headings", height="5", columns=columns)
        self.tvProducts.pack(pady=10, fill="x")
        self.tvProducts.heading('#1', text='ID', anchor='center')
        self.tvProducts.column('#1', width=60, anchor='center', stretch=False)
        self.tvProducts.heading('#2', text='Name', anchor='center')
        self.tvProducts.column('#2', width=100, anchor='center', stretch=False)
        self.tvProducts.heading('#3', text='Brand', anchor='center')
        self.tvProducts.column('#3', width=100, anchor='center', stretch=False)
        self.tvProducts.heading('#4', text='Released date', anchor='center')
        self.tvProducts.column('#4', width=100, anchor='center', stretch=False)
        self.tvProducts.heading('#5', text='Display size', anchor='center')
        self.tvProducts.column('#5', width=100, anchor='center', stretch=False)
        self.tvProducts.heading('#6', text='Display type', anchor='center')
        self.tvProducts.column('#6', width=100, anchor='center', stretch=False)
        self.tvProducts.heading('#7', text='CPU', anchor='center')
        self.tvProducts.column('#7', width=100, anchor='center', stretch=False)
        self.tvProducts.heading('#8', text='RAM', anchor='center')
        self.tvProducts.column('#8', width=100, anchor='center', stretch=False)
        self.tvProducts.heading(
            '#9', text='Number of cameras', anchor='center')
        self.tvProducts.column('#9', width=150, anchor='center', stretch=False)

        vsb = ttk.Scrollbar(self, orient=tk.VERTICAL,
                            command=self.tvProducts.yview)
        vsb.place(x=895, y=500, height=120)
        self.tvProducts.configure(yscroll=vsb.set)
        self.tvProducts.bind("<<TreeviewSelect>>", self.show_selected_record)
        ###

        ### Buttons
        self.btnAdd = tk.Button(self, text="Add", font=(
            "Century Gothic", 11), bg="green", fg="white", command=self.btnAdd_Click).pack(side="left", padx=5, pady=50)
        self.btnUpdate = tk.Button(self, text="Update", font=(
            "Century Gothic", 11), bg="blue", fg="white", command=self.btnUpdate_Click).pack(side="left", padx=5, pady=50)
        self.btnDelete = tk.Button(self, text="Delete", font=(
            "Century Gothic", 11), bg="red", fg="white", command=self.btnDelete_Click).pack(side="left", padx=5, pady=50)
        self.btnClear = tk.Button(self, text="Clear Form", font=(
            "Century Gothic", 11), bg="white", fg="black", command=self.clear_form).pack(side="left", padx=5, pady=50)
        ###

        self.load_products()

    def load_products(self):
        """
        This code load the data from the database, and it will be displayed in the table.
        """
        self.tvProducts.delete(*self.tvProducts.get_children())
        p = ProductsController()
        rows = p.getAllProducts()
        for row in rows:
            self.tvProducts.insert("", 'end', text="ID", values=(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    def show_selected_record(self, event):
        """
        This code fill the form with the data from the table, which is selected.
        """
        self.clear_form()
        global id

        for selection in self.tvProducts.selection():
            item = self.tvProducts.item(selection)
        id, name, brand, release, dsize, dtype, cpu, ram, nocameras = item["values"][0:9]
        self.entName.insert(0, name)
        self.entBrand.insert(0, brand)
        self.entReleased.insert(0, release)
        self.entDisplaySize.insert(0, dsize)
        self.entDisplayType.insert(0, dtype)
        self.entCPU.insert(0, cpu)
        self.entRAM.insert(0, ram)
        self.entNoCameras.insert(0, nocameras)

        return id

    def clear_form(self):
        """
        This code clear the forms.
        """
        self.entName.delete(0, 'end')
        self.entBrand.delete(0, 'end')
        self.entReleased.delete(0, 'end')
        self.entDisplaySize.delete(0, 'end')
        self.entDisplayType.delete(0, 'end')
        self.entCPU.delete(0, 'end')
        self.entRAM.delete(0, 'end')
        self.entNoCameras.delete(0, 'end')

    def btnUpdate_Click(self):
        """
        This is the update button's click event, this will update the row in the database.
        """
        self.p = Products()
        self.pc = ProductsController()

        self.p.setName(self.entName.get())
        self.p.setBrand(self.entBrand.get())
        self.p.setReleaseDate(self.entReleased.get())
        self.p.setDisplaySize(self.entDisplaySize.get())
        self.p.setDisplayType(self.entDisplayType.get())
        self.p.setCPU(self.entCPU.get())
        self.p.setRAM(self.entRAM.get())
        self.p.setNoCameras(self.entNoCameras.get())

        self.pc.UpdateProduct(self.p, id)
        self.load_products()
        self.clear_form()
        messagebox.showinfo("Update", self.p.getMessage())

    def btnDelete_Click(self):
        """
        This is the delete button's click event, this will be delete the selected row from the datebase.
        """
        self.p = Products()
        self.pc = ProductsController()
        self.pc.DeleteProduct(self.p, id)
        self.load_products()
        messagebox.showinfo("Delete", self.p.getMessage())

    def btnAdd_Click(self):
        """
        This is the add button's click event, this will be add a new row, with the datas from the forms.
        """
        self.p = Products()
        self.pc = ProductsController()

        self.p.setName(self.entName.get())
        self.p.setBrand(self.entBrand.get())
        self.p.setReleaseDate(self.entReleased.get())
        self.p.setDisplaySize(self.entDisplaySize.get())
        self.p.setDisplayType(self.entDisplayType.get())
        self.p.setCPU(self.entCPU.get())
        self.p.setRAM(self.entRAM.get())
        self.p.setNoCameras(self.entNoCameras.get())

        self.pc.AddProduct(self.p)
        self.load_products()
        self.clear_form()
        messagebox.showinfo("Insert", self.p.getMessage())


if __name__ == '__main__':
    app = App()
    app.mainloop()
