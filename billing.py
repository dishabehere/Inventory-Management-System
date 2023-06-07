from tkinter import*
from PIL import Image, ImageTk  #to deal with images


class IMS:
    def __init__(self, root): 
        self.root = root 
        self.root.geometry("1350x700+0+0") 
        self.root.title("Inventory Management System | Developed by Disha") 
        self.root.config(bg="white")
        
        #title
        self.icon_title = PhotoImage(file = "images/logo1.png") 
        title = Label(self.root, text = "Inventory Management System", image = self.icon_title, compound = LEFT, font = ("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)
        
        #Logout Button
        btn_logout = Button(self.root, text = "Logout", font = ("Times New Roman", 15, "bold"), bg = "yellow", cursor="hand2").place(x=1150, y=10, height=50, width=150)

        #Clock
        self.lbl_clock = Label(self.root, text = "Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font = ("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

if __name__=="__main__":
    root = Tk() #make an object to use Tk class in Tkinter 
    obj = IMS(root) #make an object to pass IMS #to attach my window to this class
    root.mainloop() #to make the window stay unitll closed otherwise program will run and exit
        