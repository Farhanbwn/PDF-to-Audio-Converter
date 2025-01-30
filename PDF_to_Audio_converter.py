from logging import root
from tkinter import Tk
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.ttk import Combobox
from PIL import ImageTk
import PyPDF2
import pyttsx3



class audiobook:
    def __init__(self,Tk):
        self.root=Tk
        self.root.title("PDF to Audio converter")
        self.root.geometry('550x550')
        self.root.configure(background="white")
        
        #icon
        image_icon = PhotoImage(file="icon.png")
        self.root.iconphoto(False,image_icon)

        #logo
        self.photo=ImageTk.PhotoImage(file="LOGO 2.png")
        photo=Label(self.root,image=self.photo).place(x=33,y=20)


        #confirmation for upload a file
        self.label1=Label(text='',bg="white",fg="black",font='gotham 11 bold')
        self.label1.place(x=160,y=420)  


        #function for open file
        def open_file():
                global file
                file = askopenfile(parent= root, mode='rb', title="choose a file", filetype=[("Pdf file","*.pdf")])
                self.label1['text']='FILE SUCCESSFULLY UPLOADED.'
                if file:
                
                    pdfReader = PyPDF2.PdfFileReader(file)
                    
                    # the page with which you want to start
                    global from_page
                    from_page = pdfReader.getPage(0)

                    # extracting the text from the PDF
                    global text
                    text = from_page.extractText()

        #function for play audio
        def play_audio():
                # reading the text
                self.speak = pyttsx3.init()
                gender = gender_combobox.get()
                speed = speed_combobox.get()
                voices = self.speak.getProperty('voices')
                def setvoice():
                    if (gender == 'Male'):
                        self.speak.setProperty('voice', voices[0].id) 
                        self.speak.say(text)
                        self.speak.runAndWait()
                    else:
                        self.speak.setProperty('voice', voices[1].id) 
                        self.speak.say(text)
                        self.speak.runAndWait()
                
                if (text):
                    if (speed =='Fast'):
                        self.speak.setProperty('rate', 250)
                        setvoice()
                    elif (speed == 'Normal'):
                        self.speak.setProperty('rate',160)
                        setvoice()
                    else:
                        self.speak.setProperty('rate',100)
                        setvoice()

                self.label1['text']=''
                        


        #gender box

        self.Lebal2=Label(root,text='VOICE',bg="white",fg="black",font='gotham 11 bold').place(x=320,y=325)
        gender_combobox=Combobox(self.root,values=['Male','Female'],font="gotham 10 bold",state='r',width=10)
        gender_combobox.place(x=300,y=350)
        gender_combobox.set('Male')


        #speed box

        self.Lebal3=Label(root,text='SPEED',bg="white",fg="black",font='gotham 11 bold').place(x=445,y=325)
        speed_combobox=Combobox(self.root,values=['Fast','Normal','Slow'],font="gotham 10 bold",state='r',width=10)
        speed_combobox.place(x=430,y=350)
        speed_combobox.set('Normal')
        


        #intraction
        self.photo2=ImageTk.PhotoImage(file="select2.png")
        photo2=Label(self.root,image=self.photo2,bd='0',bg="white").place(x=70,y=295)


        #browse button
        self.photo_browse=ImageTk.PhotoImage(file='BROWSE BUTTON3.png')
        photo_browse =Button(self.root, image=self.photo_browse,bd='0',bg='white',command=lambda:open_file()).place(x=100, y=345)

        #play button
        self.photo_play=ImageTk.PhotoImage(file='play button2.png')
        photo_play =Button(self.root, image=self.photo_play,bd='0',bg='white',command=play_audio).place(x=235, y=450)

        #pause button
        #self.photo_pause=ImageTk.PhotoImage(file='pause button2.png')
        #photo_pause =Button(self.root, image=self.photo_pause,bd='0',bg="white").place(x=400, y=385)'''

root=Tk()
obj=audiobook(root)
root.mainloop()