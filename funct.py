def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()
def alphanumber(ch):
    ch=ch.upper()
    i=0
    while(i<len(ch)):
        if(ord(ch[i]) in range(ord("A"),ord("Z")+1) or ord(ch[i]) in range(ord("0"),ord("9")+1)):
            i+=1
        else:
            return False
    return True
def name(chaine,leng):
    return len(chaine)>=leng and alphanumber(chaine)
