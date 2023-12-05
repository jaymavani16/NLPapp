from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API


class NLPApp:
    def __init__(self):
        # create db object
        self.dbo = Database()
        self.apio = API()

        self.root = Tk()
        self.root.title("NLPApp")
        self.root.iconbitmap("Resources/favicon.ico")
        self.root.geometry("350x400")
        self.root.configure(bg = '#66424d')
        self.login_gui()
        self.root.mainloop()



    def login_gui(self):
        # load Login GUI

        self.clear()
        heading = Label(self.root,text = 'NLPApp',bg='#66424d',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))

        label1 = Label(self.root,text = 'Enter Email', bg='#66424d',fg='white')
        label1.configure(font=('Verdana',12,'bold'))
        label1.pack(pady=(20,20))
        self.email_input = Entry(self.root,width= '50')
        self.email_input.pack(pady=(10,20),ipady=4)

        label2 = Label(self.root,text = 'Enter password', bg='#66424d',fg='white')
        label2.configure(font=('Verdana',12,'bold'))
        label2.pack(pady=(20,20))
        self.password_input = Entry(self.root,width= '50',show='*')
        self.password_input.pack(pady=(10,20),ipady=4)

        login_btn = Button(self.root,text='Login here', fg='black',width=20,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root,text = 'Not a member ?', bg='#66424d',fg='white')
        label3.configure(font=('Verdana',12,'bold'))
        label3.pack(pady=(20,20))

        redirect_btn = Button(self.root,text='Register here', fg='black',width=10,command=self.register_gui)
        redirect_btn.pack(pady=(10,10))



    def register_gui(self):
        # load register GUI

        self.clear()
        heading = Label(self.root,text = 'NLPApp',bg='#66424d',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))

        label0 = Label(self.root,text = 'Enter Name', bg='#66424d',fg='white')
        label0.configure(font=('Verdana',12,'bold'))
        label0.pack(pady=(20,20))
        self.name_input = Entry(self.root,width= '50')
        self.name_input.pack(pady=(10,20),ipady=4)

        label1 = Label(self.root,text = 'Enter Email', bg='#66424d',fg='white')
        label1.configure(font=('Verdana',12,'bold'))
        label1.pack(pady=(20,20))
        self.email_input = Entry(self.root,width= '50')
        self.email_input.pack(pady=(10,20),ipady=4)

        label2 = Label(self.root,text = 'Enter password', bg='#66424d',fg='white')
        label2.configure(font=('Verdana',12,'bold'))
        label2.pack(pady=(20,20))
        self.password_input = Entry(self.root,width= '50',show='*')
        self.password_input.pack(pady=(10,20),ipady=4)

        register_btn = Button(self.root,text='Register here', fg='black',width=20,height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label3 = Label(self.root,text = 'Already a member ?', bg='#66424d',fg='white')
        label3.configure(font=('Verdana',12,'bold'))
        label3.pack(pady=(20,20))

        redirect_btn = Button(self.root,text='Login here', fg='black',width=10,command=self.login_gui)
        redirect_btn.pack(pady=(10,10))



    def clear(self):
        # clear the existing gui on clicking the button
        for i in self.root.pack_slaves():
            i.destroy()



    def perform_registration(self):
        # fetching data from gui

        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo("success",'Registration successful. you can login now')
        else:
            messagebox.showerror("Error","Email already exist")



    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo("success","Login successful")
            self.home_gui()
        else:
            messagebox.showerror("Error","Incorrect email/password.Try again")



    def home_gui(self):

        self.clear()

        heading = Label(self.root,text = 'NLPApp',bg='#66424d',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))


        sentiment_btn = Button(self.root,text='sentiment Analysis', fg='black',width=40,height=5,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(20,20))

        ner_btn = Button(self.root,text='Named Entity Recognition', fg='black',width=40,height=5,command=self.named_Entity_recognition_gui)
        ner_btn.pack(pady=(20,20))

        abuse_detection_btn = Button(self.root,text='Abuse Detection', fg='black',width=40,height=5,command=self.abuse_detection_gui)
        abuse_detection_btn.pack(pady=(20,20))

        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))



    def sentiment_gui(self):

        self.clear()

        heading = Label(self.root,text = 'NLPApp',bg='#66424d',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))

        heading1 = Label(self.root,text = 'Sentiment Analysis',bg='#66424d',fg='white')
        heading1.pack(pady=(30,30))
        heading1.configure(font=('Verdana',18,'bold'))

        label1 = Label(self.root,text = 'Enter Text here', bg='#66424d',fg='white')
        label1.configure(font=('Verdana',12,'bold'))
        label1.pack(pady=(20,20))

        self.sentiment_input = Entry(self.root,width= '80')
        self.sentiment_input.pack(pady=(10,20),ipady=6)

        analyse_btn = Button(self.root,text='Analyse Text', fg='black',width=20,height=3,command=self.do_sentiment_analysis)
        analyse_btn.pack(pady=(20,20))

        self.sentiment_result = Label(self.root, text='',bg='#66424d',fg='white')
        self.sentiment_result.pack(pady=(30,30))
        self.sentiment_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root,text='Go back', fg='black',width=10,command=self.home_gui)
        goback_btn.pack(pady=(20,20))

    

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        txt = ''
        for i in result['sentiment']:
            txt = txt + i + ' -> ' + str(result['sentiment'][i]) + '\n'
        print(txt)
        self.sentiment_result['text'] = txt


    
    def named_Entity_recognition_gui(self):

        self.clear()

        heading = Label(self.root,text = 'NLPApp',bg='#66424d',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))

        heading1 = Label(self.root,text = 'Entity Recognition',bg='#66424d',fg='white')
        heading1.pack(pady=(30,30))
        heading1.configure(font=('Verdana',18,'bold'))

        label1 = Label(self.root,text = 'Enter Text here', bg='#66424d',fg='white')
        label1.configure(font=('Verdana',12,'bold'))
        label1.pack(pady=(20,20))

        self.entity_input = Entry(self.root,width= '80')
        self.entity_input.pack(pady=(10,20),ipady=6)

        analyse_btn = Button(self.root,text='Recognise Entity', fg='black',width=20,height=3,command=self.do_named_entity_recognition)
        analyse_btn.pack(pady=(20,20))

        self.entity_result = Label(self.root, text='',bg='#66424d',fg='white')
        self.entity_result.pack(pady=(30,30))
        self.entity_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root,text='Go back', fg='black',width=10,command=self.home_gui)
        goback_btn.pack(pady=(20,20))




    def do_named_entity_recognition(self):
        text = self.entity_input.get()
        result = self.apio.named_entity_recognise(text)
        txt = ''
        
        for entity in result['entities']:
            for key, value in entity.items():
                txt += f"{key} -> {value}\n"
        print(txt)
        self.entity_result['text'] = txt



    def abuse_detection_gui(self):

        self.clear()

        heading = Label(self.root,text = 'NLPApp',bg='#66424d',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))

        heading1 = Label(self.root,text = 'Abuse Detection',bg='#66424d',fg='white')
        heading1.pack(pady=(30,30))
        heading1.configure(font=('Verdana',18,'bold'))

        label1 = Label(self.root,text = 'Enter Text here', bg='#66424d',fg='white')
        label1.configure(font=('Verdana',12,'bold'))
        label1.pack(pady=(20,20))

        self.abuse_input = Entry(self.root,width= '80')
        self.abuse_input.pack(pady=(10,20),ipady=6)

        analyse_btn = Button(self.root,text='Detect Abuse', fg='black',width=20,height=3,command=self.do_abuse_detection)
        analyse_btn.pack(pady=(20,20))

        self.abuse_result = Label(self.root, text='',bg='#66424d',fg='white')
        self.abuse_result.pack(pady=(30,30))
        self.abuse_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root,text='Go back', fg='black',width=10,command=self.home_gui)
        goback_btn.pack(pady=(20,20))



    def do_abuse_detection(self):
        text = self.abuse_input.get()
        result = self.apio.Abuse_detect(text)
        #print(result)
        txt = ''
        for i in result:
            txt = txt + i + ' -> ' + str(result[i]) + '\n'
        print(txt)
        self.abuse_result['text'] = txt



nlp = NLPApp()
        