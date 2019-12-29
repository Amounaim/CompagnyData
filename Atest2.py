from tools_pro import *
import os
empls=[]
pad=5
fnt='Tahoma 16'
fg='maroon'
bg='#2af6bc'
i=1
pas=''
rep=''

empls=[]
test=[]
c=0
cnt=0

e=0
d=0

file=open('filename.txt','r+')
text=file.read() #return lignes
ap1=text.split('\n')
j='\n'
for i in range(len(ap1)):
    if ap1[i]!='':
        gg=ap1[i].split(',')
        empls.append(gg)
file.close()
#pour departement
testd=[]
dept=[]
filedept=open('Deptname.txt','r+')
textdept=filedept.read() #return lignes
ap1dept=textdept.split('\n')
j='\n'
for i in range(len(ap1dept)):
    if ap1dept[i]!='':
        ggdept=ap1dept[i].split(',')
        dept.append(ggdept)
filedept.close()
#****************
#pour Items
testI=[]
iteme=[]
fileitem=open('Items.txt','r+')
textitem=fileitem.read() #return lignes
ap1item=textitem.split('\n')
j='\n'
for i in range(len(ap1item)):
    if ap1item[i]!='':
        ggitem=ap1item[i].split(',')
        iteme.append(ggitem)
print(iteme)       
fileitem.close()
#****************

def opentop(name):
    frm=None
    if name=='emp': frm=employee()
    if name=='dept': frm=department()
    if name=='item': frm=item()
    bgall(frm,bg)
    fgall(frm,fg)
    fontall(frm,fnt)
    frm.grab_set()

def login():
    frm_log=form('750x500','Login')
    label(frm_log,'Login').pack(pady=pad)
    label(frm_log,'___________________________').pack(pady=pad)
    
    f1=frame(frm_log)
    f1.pack(pady=pad)
    f2=frame(frm_log)
    f2.pack(pady=pad)
    vnum=strvar()
    vnpass=strvar()
    vnpass2=strvar()
    label(f1,'Username:').grid(row=0,column=0,pady=pad,padx=3)
    textbox(f1,vnum).grid(row=0,column=1,pady=pad,padx=3)
    label(f1,'Password:').grid(row=1,column=0,pady=pad,padx=3)
    #textbox(f1,vnpass).grid(row=1,column=1,pady=pad+5,padx=3)
    def test():
        global rep
        global pas
        rep=pas+vnpass2.get()
        pas=''
        vnpass2.set('')
    
    txt=textbox(f1,vnpass2)
    txt.grid(row=1,column=1,pady=pad+5,padx=3) #pr password
    txt.bind('<Return>',lambda my:test())
    def key(event):
        global i
        global pas
        global test
        #print(event)
        #print(event.char)
        pas=pas+vnpass2.get()
        #print('-----------')
        vnpass2.set('')
        i+=1
    txt.bind('<Key>',key)
    
    iv2=intvar()
    checkbox(f2,'Remenber me',iv2).grid(row=0,column=0,columnspan=2,pady=pad,padx=3)
    def chek():
        rep=pas+vnpass2.get()
        #print(rep)
        if vnum.get()!='mounaim' or rep!='mounaim':
            msgbox('Check your Login or Password')
            
        elif iv2.get()==0:
            msgbox('Remeber Me !!')
            
        else :
            frm=mainform()
            frm.grab_set()
            
    button(f2,'Login',chek).grid(row=0,column=6,pady=pad,padx=10)       
    label(frm_log,'___________________________').pack(pady=pad)
    bgall(frm_log,'black')
    fgall(frm_log,'#090')
    fontall(frm_log,fnt)
    
    return frm_log

def mainform():
    frm_main=toplevel('750x500','Company Program')
    label(frm_main,'Company Program').pack(pady=pad)
    label(frm_main,'___________________________').pack(pady=pad)
    button(frm_main,'Employee',lambda:opentop('emp')).pack(pady=pad)
    button(frm_main,'Department',lambda:opentop('dept')).pack(pady=pad)
    button(frm_main,'Item',lambda:opentop('item')).pack(pady=pad)
    button(frm_main,'Exit',frm_main.destroy).pack(pady=pad)
    label(frm_main,'___________________________').pack(pady=pad)
    bgall(frm_main,bg)
    fgall(frm_main,fg)
    fontall(frm_main,fnt)
    return frm_main

    
def employee():
    frm_emp=toplevel('700x420','Employee Form')
    label(frm_emp,'Employee Form').pack(pady=pad)
    #ga3 li kikon grid machi pack kan 7atohom f frame rasshom bache ngado row column
    f1=frame(frm_emp)
    f1.pack(pady=pad)
    f2=frame(frm_emp)
    f2.pack(pady=pad)
    vnum=strvar()
    vname=strvar()
    vcity=strvar()
    vphone=strvar()
    vemail=strvar()
    label(f1,'Id:').grid(row=0,column=0,pady=pad,padx=3)
    textbox(f1,vnum).grid(row=0,column=1,pady=pad,padx=3)
    label(f1,'Name:').grid(row=1,column=0,pady=pad,padx=3)
    textbox(f1,vname).grid(row=1,column=1,pady=pad,padx=3)
    label(f1,'City:').grid(row=2,column=0,pady=pad,padx=3)
    textbox(f1,vcity).grid(row=2,column=1,pady=pad,padx=3)
    label(f1,'Phone:').grid(row=3,column=0,pady=pad,padx=3)
    textbox(f1,vphone,True).grid(row=3,column=1,pady=pad,padx=3)
    label(f1,'Email:').grid(row=4,column=0,pady=pad,padx=3)
    textbox(f1,vemail).grid(row=4,column=1,pady=pad,padx=3)

    def showdata(num):        
        global cnt
        global c
        if not os.path.exists("projetFin_H&A/Employees"):
            os.mkdir("projetFin_H&A/Employees")
        file1=open("projetFin_H&A/Employees/empl2.txt","w+")
        
            
        if num=='add' or num=='edit':
            if vnum.get().strip()=='':
                messagebox.showwarning('Error','Id is Empty')
                #txtcode.focus()
            elif vname.get().strip()=='':
                messagebox.showwarning('Error','Name is Empty')
                #txtcode.focus()
            elif vcity.get().strip()=='':
                messagebox.showwarning('Error','City is Empty')
                #txtadress.focus()
            elif vphone.get().strip()=='' or len(vphone.get())<10:
                if vphone.get().strip()=='':
                    messagebox.showwarning('Error','Phone is Empty')
                else:
                    messagebox.showwarning('Error','Phone is Small!!')
                #txtcode.focus()
            elif vemail.get().strip()=='' or '@' not in vemail.get():
                if vemail.get().strip()=='':
                    messagebox.showwarning('Error','Email is Empty')
                else:
                   messagebox.showwarning('Error','@ messing') 
                
                
                #print("%s | %s| %s \ %s"%(vemail.get(),vcity.get(),vnum.get(),vname.get()))
                #for ig in empls:
                    #if ig==vnum.get(): print("iyaah")
                    #else :print("tchala")
                #txtadress.focus()
            else:
                if num=='add' and empls!=[]:
                    for ig in empls:                       
                         if ig[0]==vnum.get(): 
                             c=4
                             #pp1=vnum.get()+','+vname.get()+','+vcity.get()+','+vphone.get()+','+vemail.get()+'\n'
                             #file.write(pp1)
                             break
                    if c==4:
                        messagebox.showwarning('Error','Code already exist ')
                        c=0
                    else:
                        myemp=[vnum.get(),vname.get(),vcity.get(),vphone.get(),vemail.get()]
                        empls.append(myemp)
                        msgbox(myemp)
                        c=0  
                elif num=='add':
                    #pp1=vnum.get()+','+vname.get()+','+vcity.get()+','+vphone.get()+','+vemail.get()+'\n'
                    #file.write(pp1)
                    
                    myemp=[vnum.get(),vname.get(),vcity.get(),vphone.get(),vemail.get()]
                    empls.append(myemp)
                    msgbox([vnum.get(),vname.get(),vcity.get(),vphone.get(),vemail.get()])
                    
                else:
                    for ig in empls:
                        if ig[0]==vnum.get() :#and ig[1]==vname.get():
                            empls[empls.index(ig)][1]=vname.get()
                            empls[empls.index(ig)][2]=vcity.get()
                            empls[empls.index(ig)][3]=vphone.get()
                            empls[empls.index(ig)][4]=vemail.get()
                            msgbox([vnum.get(),vname.get(),vcity.get(),vphone.get(),vemail.get()])
                            c=4
                            break
                    if c==0:messagebox.showwarning('Error','Code  not exist ')
                    else : c=0                  
        else: #num=='delt' or num=='find':
            if vnum.get().strip()=='':
                messagebox.showwarning('Error','Id is Empty')
                #txtcode.focus()
           # elif vname.get().strip()=='':
              #  messagebox.showwarning('Error','Name is Empty')
                #txtcode.focus()                
            else:
                if num=='delt':
                    for ig in empls:
                        if ig[0]==vnum.get() :#and ig[1]==vname.get():
                            c=4
                            my=ig
                            empls.remove(my)
                            msgbox([ig[0],ig[1],ig[2],ig[3],ig[4],' Removed'])
                            break
                    if c==0:
                        messagebox.showwarning('Error','Code  Not exist')
                    else :c=0 
                else :
                    for ig in empls:
                        if ig[0]==vnum.get():# and ig[1]==vname.get():
                            vname.set(ig[1])
                            vcity.set(ig[2])
                            vphone.set(ig[3])
                            vemail.set(ig[4])
                            msgbox([ig[0],ig[1],ig[2],ig[3],ig[4]])
                            c=4
                            break
                    if c==0:
                        messagebox.showwarning('Error','Code Not exist')
                    else:c=0           
        #else:
           # messagebox.askquestion('Save','You wanna save ?')
        file3=open('filename.txt','w+')
        for i in range(len(empls)):
            my=empls[i]     
            file1.writelines(' Code: %s \n Name : %s \n City : %s \n Phone : %s \n Email: %s '%(my[0],my[1],my[2],my[3],my[4]))
            file1.writelines('\n \n \t ********** \n')   
            pp1=my[0]+','+my[1]+','+my[2]+','+my[3]+','+my[4]+'\n'
            file3.write(pp1)    
            test.append(my)
        file3.close()
        
        file1.close()	   
        
    button(f2,'Add',lambda:showdata('add')).grid(row=0,column=0,pady=pad,padx=3)
    button(f2,'Edit',lambda:showdata('edit')).grid(row=0,column=1,pady=pad,padx=3)
    button(f2,'Delete',lambda:showdata('delt')).grid(row=0,column=2,pady=pad,padx=3)
    button(f2,'Find',lambda:showdata('find')).grid(row=0,column=3,pady=pad,padx=3)
    #button(f2,'Save',lambda:showdata('sv')).grid(row=0,column=4,pady=pad,padx=3)
    button(f2,'Close',frm_emp.destroy).grid(row=1,column=0,columnspan=5,pady=pad)
    bgall(frm_emp,bg)
    fgall(frm_emp,fg)
    return frm_emp

def department():
    frm_dept=toplevel('700x300','Department Form')
    label(frm_dept,'Department Form').pack(pady=pad)
    f1=frame(frm_dept)
    f1.pack(pady=pad)
    f2=frame(frm_dept)
    f2.pack(pady=pad)
    vnum=strvar()
    vname=strvar()
    vloc=strvar()
    label(f1,'Department Number:').grid(row=0,column=0,pady=pad,padx=3)
    textbox(f1,vnum).grid(row=0,column=1,pady=pad,padx=3)
    label(f1,'Department Name:').grid(row=1,column=0,pady=pad,padx=3)
    textbox(f1,vname).grid(row=1,column=1,pady=pad,padx=3)
    label(f1,'Location:').grid(row=2,column=0,pady=pad,padx=3)
    textbox(f1,vloc).grid(row=2,column=1,pady=pad,padx=3)
    def showdata(num):        
        global cnt
        global c
        if not os.path.exists("projetFin_H&A/Departments"):
            os.mkdir("projetFin_H&A/Departments")
        filed=open("projetFin_H&A/Departments/dept.txt","w+")
        
            
        if num=='add' or num=='edit':
            if vnum.get().strip()=='':
                messagebox.showwarning('Error','Id is Empty')
                #txtcode.focus()
            elif vname.get().strip()=='':
                messagebox.showwarning('Error','Name is Empty')
                #txtcode.focus()
            elif vloc.get().strip()=='':
                messagebox.showwarning('Error','Location is Empty')
            else:
                if num=='add' and dept!=[]:
                    for ig in dept:                       
                         if ig[0]==vnum.get(): 
                             c=4
                             break
                    if c==4:
                        messagebox.showwarning('Error','Code already exist ')
                        c=0
                    else:
                        myemp=[vnum.get(),vname.get(),vloc.get()]
                        dept.append(myemp)
                        msgbox(myemp)
                        c=0  
                elif num=='add':
                    myemp=[vnum.get(),vname.get(),vloc.get()]
                    dept.append(myemp)
                    msgbox([vnum.get(),vname.get(),vloc.get()])
                    
                else:
                    for ig in dept:
                        if ig[0]==vnum.get() :#and ig[1]==vname.get():
                            
                            dept[dept.index(ig)][1]=vname.get()
                            dept[dept.index(ig)][2]=vloc.get()
                            msgbox([vnum.get(),vname.get(),vloc.get()])
                            c=4
                            break
                    if c==0:messagebox.showwarning('Error','Code  not exist ')
                    else : c=0                  
        else: 
            if vnum.get().strip()=='':
                messagebox.showwarning('Error','Id is Empty')             
            else:
                if num=='delt':
                    for ig in dept:
                        if ig[0]==vnum.get() :#and ig[1]==vname.get():
                            c=4
                            my=ig
                            dept.remove(my)
                            msgbox([ig[0],ig[1],ig[2],' Removed'])
                            break
                    if c==0:
                        messagebox.showwarning('Error','Code  Not exist')
                    else :c=0 
                else :
                    for ig in dept:
                        if ig[0]==vnum.get():# and ig[1]==vname.get():
                            vname.set(ig[1])
                            vloc.set(ig[2])
                            msgbox([ig[0],ig[1],ig[2]])
                            c=4
                            break
                    if c==0:
                        messagebox.showwarning('Error','Code Not exist')
                    else:c=0           
        filed3=open('Deptname.txt','w+')
        for i in range(len(dept)):
            my=dept[i]     
            filed.writelines(' Code: %s \n Name : %s \n Location: %s '%(my[0],my[1],my[2]))
            filed.writelines('\n \n \t ********** \n')   
            pp1=my[0]+','+my[1]+','+my[2]+'\n'
            filed3.write(pp1)    
            testd.append(my)
        filed3.close()
        
        filed.close()
        
    button(f2,'Add',lambda:showdata('add')).grid(row=0,column=0,pady=pad,padx=3)
    button(f2,'Edit',lambda:showdata('edit')).grid(row=0,column=1,pady=pad,padx=3)
    button(f2,'Delete',lambda:showdata('delt')).grid(row=0,column=2,pady=pad,padx=3)
    button(f2,'Find',lambda:showdata('find')).grid(row=0,column=3,pady=pad,padx=3)
    button(f2,'Close',frm_dept.destroy).grid(row=1,column=0,columnspan=4,pady=pad)
    return frm_dept    

def item():
    frm_item=toplevel('700x300','Item Form')
    label(frm_item,'Item Form').pack(pady=pad)
    f1=frame(frm_item)
    f1.pack(pady=pad)
    f2=frame(frm_item)
    f2.pack(pady=pad)
    vnum=strvar()
    vname=strvar()
    vprice=strvar()
    label(f1,'Item Number:').grid(row=0,column=0,pady=pad,padx=3)
    textbox(f1,vnum).grid(row=0,column=1,pady=pad,padx=3)
    label(f1,'Item Name:').grid(row=1,column=0,pady=pad,padx=3)
    textbox(f1,vname).grid(row=1,column=1,pady=pad,padx=3)
    label(f1,'Price:').grid(row=2,column=0,pady=pad,padx=3)
    textbox(f1,vprice,True).grid(row=2,column=1,pady=pad,padx=3)
    def showdata(num):        
        global cnt
        global c
        if not os.path.exists("projetFin_H&A/Items"):
            os.mkdir("projetFin_H&A/Items")
        fileI=open("projetFin_H&A/Items/item.txt","w+")
            
        if num=='add' or num=='edit':
            if vnum.get().strip()=='':
                messagebox.showwarning('Error','Id is Empty')
                #txtcode.focus()
            elif vname.get().strip()=='':
                messagebox.showwarning('Error','Name is Empty')
                #txtcode.focus()
            elif vprice.get().strip()=='':
                messagebox.showwarning('Error','Price is Empty')
            else:               
                if num=='add' and iteme!=[]:
                    for ig in iteme:                       
                         if ig[0]==vnum.get(): 
                             c=4
                             break
                    if c==4:
                        messagebox.showwarning('Error','Code already exist ')
                        c=0
                    else:
                        myemp=[vnum.get(),vname.get(),vprice.get()]
                        iteme.append(myemp)
                        msgbox(myemp)
                        c=0  
                elif num=='add':
                    myemp=[vnum.get(),vname.get(),vprice.get()]
                    iteme.append(myemp)
                    
                else:
                    for ig in iteme:
                        if ig[0]==vnum.get() :#and ig[1]==vname.get():
                            iteme[iteme.index(ig)][1]=vname.get()
                            iteme[iteme.index(ig)][2]=vprice.get()
                            msgbox([vnum.get(),vname.get(),vprice.get()])
                            c=4
                            break
                    if c==0:messagebox.showwarning('Error','Code  not exist ')
                    else : c=0                  
        else: 
            if vnum.get().strip()=='':
                messagebox.showwarning('Error','Id is Empty')             
            else:
                if num=='delt':
                    for ig in iteme:
                        if ig[0]==vnum.get() :#and ig[1]==vname.get():
                            c=4
                            my=ig
                            iteme.remove(my)
                            msgbox([ig[0],ig[1],ig[2],' Removed'])
                            break
                    if c==0:
                        messagebox.showwarning('Error','Code  Not exist')
                    else :c=0 
                else :
                    for ig in iteme:
                        if ig[0]==vnum.get():# and ig[1]==vname.get():
                            vname.set(ig[1])
                            vprice.set(ig[2])
                            msgbox([ig[0],ig[1],ig[2]])
                            c=4
                            break
                    if c==0:
                        messagebox.showwarning('Error','Code Not exist')
                    else:c=0           
        fileI3=open('Items.txt','w+')
        for i in range(len(iteme)):
            my=iteme[i]     
            fileI.writelines(' Code: %s \n Name : %s \n Price: %s '%(my[0],my[1],my[2]))
            fileI.writelines('\n \n \t ********** \n')   
            pp1=my[0]+','+my[1]+','+my[2]+'\n'
            fileI3.write(pp1)    
            testd.append(my)
        fileI3.close()
        
        fileI.close()
    button(f2,'Add',lambda:showdata('add')).grid(row=0,column=0,pady=pad,padx=3)
    button(f2,'Edit',lambda:showdata('edit')).grid(row=0,column=1,pady=pad,padx=3)
    button(f2,'Delete',lambda:showdata('delt')).grid(row=0,column=2,pady=pad,padx=3)
    button(f2,'Find',lambda:showdata('find')).grid(row=0,column=3,pady=pad,padx=3)
    button(f2,'Close',frm_item.destroy).grid(row=1,column=0,columnspan=4,pady=pad)
    return frm_item   





