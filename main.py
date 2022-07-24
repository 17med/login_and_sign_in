from tkinter import *


from pages import loginpage,register,home_page

#window
root = Tk()
#x=register(root)
x=loginpage(root)
#x=home_page(root,"admin")
#x=menu(root)
#x=historique(root)

"""
mainpage(root,'800x500')
maincreation(root)

mainpage(root,'950x650')
menu(root)"""
root.mainloop()