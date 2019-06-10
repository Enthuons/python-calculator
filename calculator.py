from tkinter import *

def btnClick(numbers):
    global operator
    numbers = str(numbers)
    operator = str(text_input.get())
    operator = operator + str(numbers)
    leng =len(operator)
    text_input.set(operator)
    entry.icursor(leng)
       
def clickEquals(values):
    global operator
    operator =""
    operator = str(values)
    text_input.set(operator)


def equalsInput():
    try:
        global operator
        operator = text_input.get()
        dis = str(eval(operator))
        text_output.set(str(operator)+'='+dis)
        sum_val =str(eval(dis))
        text_input.set(sum_val)

        clickEquals(sum_val)
    except:
        text_input.set("error")

def clearDisplay():
    global operator
    operator =""
    text_input.set("")
    text_output.set("")

def back():
    strStr = text_input.get()

    global operator
    operator =""
    text_input.set("")

    backtext = strStr[0:-1]
    btnClick(backtext)

def pressEnter(event):

    global operator
    operator = text_input.get()
    dis = str(eval(operator))
    text_output.set(str(operator)+'='+dis)
    text_input.set(dis)

# ckeck digit
def validate(action, index, value_if_allowed,
                    prior_value, text, validation_type, trigger_type, widget_name):
    if text in '0123456789.-+*/':
        try:
            str(value_if_allowed)
            return True
        except ValueError:
            return False
    else:
        return False



if __name__ == "__main__": 
    cal = Tk()
    cal.geometry("297x435+800+50")


    # frame=Frame(cal,width=100,heigh=100,bd=11)

    cal.resizable(0,0)
    cal.title(" Enthuons Calculator") 

    operator =""
    text_input =StringVar()
    text_output =StringVar()

    Entry(cal,font = ('arial',15,),textvariable = text_output,bd = 0,insertwidth = 9,justify = 'left',width= 21,highlightthickness=0,state="readonly").grid(columnspan = 4,pady=12, padx=3)

    reg = (cal.register(validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

    entry = Entry(cal,font = ('arial',15,),textvariable = text_input,bd = 0,insertwidth = 2,justify = 'right',width =21,highlightthickness=0,validate = 'key',validatecommand = reg)
    entry.grid(columnspan = 4,sticky="nsew",pady = 9,padx= 10,ipady = 7)
    entry.focus_set()
    
    entry.bind('<Return>',pressEnter)

    # Entry(cal,font = ('arial',15,),bd = 0,insertwidth = 2,justify = 'left',width= 21,highlightthickness=0,state="readonly").grid(columnspan = 4,pady=0)

    # entry.focus()

    # button display
    # ============================   first row ===================================
    Button(cal,padx=12,pady = 8,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="1",width = 2,command =lambda:btnClick(1)).grid(row =3,column = 0,padx= 7,pady = 5)
    
    # btn1 = Button(cal,padx=12,pady = 8,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="1",width = 2,command =lambda:eventHandler(1)).grid(row =3,column = 0)
    Button(cal,padx=12,pady = 8,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="2",width = 2,command =lambda:btnClick(2)).grid(row =3,column = 1,padx= 7,pady = 5)
    Button(cal,padx=12,pady = 8,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="3",width = 2,command =lambda:btnClick(3)).grid(row =3,column = 2,padx= 7,pady = 5)
    Button(cal,padx=12,pady = 8,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="+",width = 2,command =lambda:btnClick("+")).grid(row =3,column = 3,padx= 7,pady = 5)
    # ============================ second row =====================================
    Button(cal,padx=12,pady = 10,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="4",width = 2,command =lambda:btnClick(4)).grid(row =4,column = 0,padx= 7,pady = 5)
    Button(cal,padx=12,pady = 10,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="5",width = 2,command =lambda:btnClick(5)).grid(row =4,column = 1,padx= 7,pady = 5)
    Button(cal,padx=12,pady = 10,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="6",width = 2,command =lambda:btnClick(6)).grid(row =4,column = 2,padx= 7,pady = 5)
    Button(cal,padx=12,pady = 10,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="-",width = 2,command =lambda:btnClick("-")).grid(row =4,column = 3,padx= 7,pady = 5)
    # ============================ third row =======================================
    Button(cal,padx=12,pady = 10,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="7",width = 2,command =lambda:btnClick(7)).grid(row =5,column = 0,padx= 7,pady = 5)
    Button(cal,padx=12,pady = 10,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="8",width = 2,command =lambda:btnClick(8)).grid(row =5,column = 1,padx= 7,pady = 5)
    Button(cal,padx=12,pady = 10,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="9",width = 2,command =lambda:btnClick(9)).grid(row =5,column = 2,padx= 7,pady = 5)
    Button(cal,padx=12,pady = 10,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="*",width = 2,command =lambda:btnClick("*")).grid(row =5,column = 3,padx= 7,pady = 5)
    # ============================ forth row =======================================
    Button(cal,padx=12,pady = 10,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="0",width = 2,command =lambda:btnClick(0)).grid(row =6,column = 0,padx= 7,pady = 5)
    Button(cal,padx=12,pady = 10,bd = 1,fg = "black",font= ('arial',20,'bold'),text =".",width = 2,command =lambda:btnClick(".")).grid(row =6,column = 1,padx= 7,pady = 5)
    Button(cal,padx=12,pady = 10,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="=",width = 2,command =lambda:equalsInput()).grid(row =6,column = 2,padx= 7,pady = 5)



    Button(cal,padx=12,pady = 10,bd = 1,fg = "black",font= ('arial',20,'bold'),text ="/",width = 2,command =lambda:btnClick("/")).grid(row =6,column = 3,padx= 7,pady = 5)
    # ==============================fifth row =======================================
    Button(cal,padx=26,pady = 10,bd = 1,fg = "black",font= ('arial',20,''),text ="clr",width=5,command =lambda:clearDisplay()).grid(row =7,column= 0,columnspan=2,padx= 7,pady = 5)
    Button(cal,padx=26,pady = 10,bd = 1,fg = "black",font= ('arial',20,''),text ="Back",width=5,command =lambda:back()).grid(row =7,column= 2,columnspan=2,padx= 7,pady = 5)

    

    # # cal.wm_resizable(width=None,height=None)

    cal.mainloop()
