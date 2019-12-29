#centre
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import StringVar
from tkinter import IntVar
from tkinter import BooleanVar
from tkinter import Listbox
from tkinter import Frame

def centre(frm):
    frm.update()
    sw=frm.winfo_screenwidth()
    sh=frm.winfo_screenheight()
    w=frm.winfo_width()
    h=frm.winfo_height()
    x=(sw-w)/2
    y=(sh-h)/2
    frm.geometry('%dx%d+%d+%d' %(w,h,x,y))



def strvar():
    return StringVar()

def intvar():
    return IntVar()

def boolvar():
    return BooleanVar()
#!!!!!!!!!!!!!!!!!!!!!!!!!    

def form(geometry='350x200',title='',is_center=True):
    frm=Tk()
    frm.geometry(geometry)
    frm.title(title)
    if is_center:centre(frm)
    return frm

def toplevel(geometry='350x200',title='',is_center=True):
    frm=Toplevel()
    frm.geometry(geometry)
    frm.title(title)
    if is_center:centre(frm)
    return frm

def frame(form,bg=None):
    if bg!=None:
        return Frame(form,bg=bg)
    else :
        return Frame(form)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def bgall(frm,bg):
    frm.update()
    ctrls=frm.winfo_children()
    frm.config(bg=bg)
    my=ttk.Style()
    my.configure('TRadiobutton',background=bg)
    my.configure('TCheckbutton',background=bg)    
    for c in ctrls:
        if c.winfo_class()=='Frame' :
            bgall(c,bg)
        try:
            c['background']=bg
        except:
            pass
        
def fontall(frm,font):
    frm.update()
    ctrls=frm.winfo_children()
    my=ttk.Style()
    my.configure('TButton',font=font)
    my.configure('TRadiobutton',font=font)
    my.configure('TCheckbutton',font=font)
    for c in ctrls:
        if c.winfo_class()=='Frame' : fontall(c,font)
        try:
            c['font']=font
        except:
            pass
       

def fgall(frm,fg):
    frm.update()
    ctrls=frm.winfo_children()
    my=ttk.Style()
    my.configure('TButton',foreground=fg)
    my.configure('TRadiobutton',foreground=fg)
    my.configure('TCheckbutton',foreground=fg)
    for c in ctrls:
        if c.winfo_class()=='Frame' : fgall(c,fg)
        try:
            c['foreground']=fg
        except:
            pass            
            
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
def button(form,text='Button',command=None):
    btn=ttk.Button(form,text=text)
    if command!=None:
        btn.config(command=command)
    return btn    

def label(form,text='Label'):
    return ttk.Label(form,text=text)

def textbox(form,variable=None,is_number_only=False):

    def number_only(text):
        if str.isdigit(text):
            return True
        elif text is '':
            return True
        else:
            return False
    reg_fun = form.register(number_only) #tassgil dala 


    txt=ttk.Entry(form)
    if is_number_only:
        txt.config(validate='key',validatecommand=(reg_fun,'%P'))
    if variable!=None:
        txt.config(textvariable=variable)
    return txt

def radio(form,text='Radio',value=0,variable=None):
    rdo=ttk.Radiobutton(form,text=text,value=value)
    if variable!=None:
        rdo.config(variable=variable)
    return rdo

def checkbox(form,text='Checkbox',variable=None): 
    cbx=ttk.Checkbutton(form,text=text)
    if variable!=None:
        cbx.config(variable=variable)
    return cbx


def combobox(form,values=None,readonly=False): 
    cbx=ttk.Combobox(form)
    if values!=None:
        cbx.config(values=values)
    if readonly:
        cbx.config(state='readonly') #ikhtiyarat matzidch 3lihom
    return cbx

def listbox(form,values=None): 
    lbx=Listbox(form)
    if values!=None:
        i=0
        for x in values:
            lbx.insert(i,x)
            i+=1
    return lbx


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!         

def msgbox(text,vr=''):
    messagebox.showinfo(vr,text)

def msgask(text):
    return messagebox.askyesno('',text) #ayroturni lak true ola false l9ima

def inbox(text,is_number_only=False):
    f=Toplevel()
    f.title(text)
    f.geometry('400x300')
    f.resizable(False,False)
    centre(f)
    ttk.Label(f,text=text,font='None 15').pack(pady=10)
    sv=StringVar()

    def number_only(text):
        if str.isdigit(text):
            return True
        elif text is '':
            return True
        else:
            return False

    reg_fun = f.register(number_only) #tassgil dala 


    txt=ttk.Entry(f,font='None 15',width=35,textvariable=sv)
    if is_number_only:
        txt.config(validate='key',validatecommand=(reg_fun,'%P'))
        
    txt.pack(pady=10)
    txt.bind('<Return>',lambda my:f.destroy()) #mili ghadi tklicer enter 
    ttk.Style().configure('inbox.TButton',font='None 15')#inbox ghi smiya
    ttk.Button(f,text='OK',command=lambda:f.destroy(),style='inbox.TButton').pack(pady=10)
    f.grab_set()
    f.wait_window() #katgolih tssanah tay9fal
    return sv.get()
    
