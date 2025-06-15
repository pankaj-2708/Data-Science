from tkinter import *
from mydb import Database
from tkinter import messagebox
from api import api


class NLPApp:

    def __init__(self):

        # creating object
        self.root=Tk()

        # setting tittle
        self.root.title('NLP app')

        # setting size
        self.root.geometry('350x600')

        # setting bg color
        self.root.configure(background='grey')
        
        # creating login page
        self.login_gui()

        self.db=Database()
        self.api=api()

        # it holds gui
        self.root.mainloop()


    def login_gui(self):

        self.clear_gui()
        # clearing existing page
        
        # setting heading
        heading=Label(self.root,text='NLP app', bg= 'grey',fg='white')

        #setting padding y 
        heading.pack(pady=(10,10))
        heading.configure(font=('verdana',24,'bold'))

        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))
        label1.pack()

        # taking input
        self.email_input=Entry(self.root,width=50)

        # ipady means internal padding 
        self.email_input.pack(pady=(10,10),ipady=3)


        label2=Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))
        label2.pack()

        # taking input
        self.password_input=Entry(self.root,width=50,show='*')

        # ipady means internal padding 
        self.password_input.pack(pady=(10,10),ipady=3)

        # creating button
        login_btn=Button(self.root,text='Login',width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,40))

        label1=Label(self.root,text='Not a member yet?')
        label1.pack(pady=(10,10))
        label1.pack()


        register_btn=Button(self.root,text='Register Now',command=self.register_gui)
        register_btn.pack(pady=(10,10))

    def register_gui(self):
        # clearing existing page
        self.clear_gui()

        # setting heading
        heading=Label(self.root,text='NLP app', bg= 'grey',fg='white')

        #setting padding y 
        heading.pack(pady=(10,10))
        heading.configure(font=('verdana',24,'bold'))

        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))
        label1.pack()

        # taking input
        self.email_input=Entry(self.root,width=50)

        # ipady means internal padding 
        self.email_input.pack(pady=(10,10),ipady=3)

        label2=Label(self.root,text='Enter Name')
        label2.pack(pady=(10,10))
        label2.pack()

        # taking input
        self.name_input=Entry(self.root,width=50)

        # ipady means internal padding 
        self.name_input.pack(pady=(10,10),ipady=3)


        label1=Label(self.root,text='Set Password')
        label1.pack(pady=(10,10))
        label1.pack()

        # taking input
        self.password_input=Entry(self.root,width=50,show='*')

        # ipady means internal padding 
        self.password_input.pack(pady=(10,10),ipady=3)

        # creating button
        register_btn=Button(self.root,text='Register',width=30,height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,40))

        label1=Label(self.root,text='All ready a member?')
        label1.pack(pady=(10,10))
        label1.pack()


        login_btn=Button(self.root,text='Login',command=self.login_gui)
        login_btn.pack(pady=(10,10))


    def clear_gui(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def perform_registration(self):
        name= self.name_input.get()
        email= self.email_input.get()
        password= self.password_input.get()
        result=self.db.add_data(name,email,password)
        
        if result==0:
            messagebox.showerror('Error','Email already exists')   
        else:
            messagebox.showinfo('Success','Registration successful')

    def perform_login(self):
        email=self.email_input.get()
        password=self.password_input.get()
        a=self.db.get_data(email)

        if a is None:
            messagebox.showerror('Error','Email not found')
            return
        
        if password==a[1]:
            messagebox.showinfo('Success','Login successful')
            # Here you can call the function to open the main app window
            # For example, self.main_app_gui()

            self.home_gui()
        
        else:
            messagebox.showerror('Error','Incorrect password')

    def home_gui(self):
        self.clear_gui()
        # setting heading
        heading=Label(self.root,text='NLP app', bg= 'grey',fg='white')
        #setting padding y
        heading.pack(pady=(10,10))

        heading.configure(font=('verdana',24,'bold'))

        sentiment_btn=Button(self.root,text='Sentiment Analysis',width=30,height=2,command=self.sentiment_analysis_gui)
        sentiment_btn.pack(pady=(10,10))    

        ner_btn=Button(self.root,text='Named Entity Recognition',width=30,height=2,command=self.ner_gui)
        ner_btn.pack(pady=(10,10))

        emotion_btn=Button(self.root,text='Emotion Detection',width=30,height=2,command=self.emotion_detection_gui)
        emotion_btn.pack(pady=(10,10))

        logout_btn=Button(self.root,text='Logout',width=30,height=2,command=self.login_gui)
        logout_btn.pack(pady=(10,10))

    def sentiment_analysis_gui(self):
        self.clear_gui()
        # setting heading
        heading=Label(self.root,text='Sentiment Analysis', bg= 'grey',fg='white')
        #setting padding y
        heading.pack(pady=(10,10))
        heading.configure(font=('verdana',24,'bold'))

        # Here you can add the functionality for sentiment analysis
        # For example, you can create an input field and a button to analyze sentiment


        label=Label(self.root,text="Enter your sentiment below")
        label.pack(pady=(10,10))

        text=Entry(self.root,width=100)
        text.pack(pady=(10,10))


        get_sentiment=Button(self.root,text='get_sentiment',width=30,height=2)
        get_sentiment.pack(pady=(10,10))

        result=self.api.get_sentiment(text.get())

        label=Label(self.root,text=result)
        label.pack(pady=(10,10))

        back_btn=Button(self.root,text='Back to Home',width=30,height=2,command=self.home_gui)
        back_btn.pack(pady=(10,10))

    def ner_gui(self):
        self.clear_gui()
        # setting heading
        heading=Label(self.root,text='Named Entity Recognition', bg= 'grey',fg='white')
        #setting padding y
        heading.pack(pady=(10,10))
        heading.configure(font=('verdana',24,'bold'))

        # Here you can add the functionality for named entity recognition
        # For example, you can create an input field and a button to perform NER

        label=Label(self.root,text="Enter your ner below")
        label.pack(pady=(10,10))

        text=Entry(self.root,width=100)
        text.pack(pady=(10,10))

        get_ner=Button(self.root,text='get_ner',width=30,height=2)
        get_ner.pack(pady=(10,10))


        result=self.api.get_ner(text.get())

        label=Label(self.root,text=result)
        label.pack(pady=(10,10))


        back_btn=Button(self.root,text='Back to Home',width=30,height=2,command=self.home_gui)
        back_btn.pack(pady=(10,10))

    def emotion_detection_gui(self):
        self.clear_gui()
        # setting heading
        heading=Label(self.root,text='Emotion Detection', bg= 'grey',fg='white')
        #setting padding y
        heading.pack(pady=(10,10))
        heading.configure(font=('verdana',24,'bold'))

        # Here you can add the functionality for emotion detection
        # For example, you can create an input field and a button to detect emotions

        label=Label(self.root,text="Enter your emotion below")
        label.pack(pady=(10,10))

        text=Entry(self.root,width=100)
        text.pack(pady=(10,10))

        get_emotion=Button(self.root,text='get_emotion',width=30,height=2)
        get_emotion.pack(pady=(10,10))

        result=self.api.get_emotion(text)

        label=Label(self.root,text=result)
        label.pack(pady=(10,10))

        back_btn=Button(self.root,text='Back to Home',width=30,height=2,command=self.home_gui)
        back_btn.pack(pady=(10,10))

nlp=NLPApp()