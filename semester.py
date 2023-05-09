from tkinter import filedialog
from PoseModule import PoseDetector
import cv2
import numpy as np
from tkinter import*
from PIL import Image, ImageTk
import mediapipe as mp
import pyttsx3
import webbrowser
import time
import threading


#### GLOBAL VARIABLES ###
global cap, Analysis
global var1, frame_1
global win, label1, v, q, Next
global canvas,link1,link2,link3,lin4
adit = 0
SajCount = 0
link1="https://github.com/Muhammad-Anees99/Automated-Salah-Pose-Tracker-using-Mediapipe-and-User-Friendly-Interface.git "
link2="https://medium.com/@m.anees990011"
link3="https://github.com/Muhammad-Anees99/Automated-Salah-Pose-Tracker-using-Mediapipe-and-User-Friendly-Interface.git "
link4="https://medium.com/@muawwizaliyousuf74"
check = False
Draw = False
Analysis = False
Update = False
CheckAgain = True
engine = pyttsx3.init() 
engine2=pyttsx3.init() 

Prayer = {'Takbir': False, 'Qayam': False, 'Ruku':False, 'Qomah': False, 'Sajdah': False, 'Atahyaat': False}
cap = cv2.VideoCapture(0)
detector = PoseDetector()

mpPose=mp.solutions.pose # From different
mpDraw=mp.solutions.drawing_utils


voices = engine2.getProperty('voices')
engine2.setProperty('voice', voices[1].id)
engine2.setProperty('language', 'ur')
engine2.setProperty('voice', 'urdu')
engine2.setProperty('rate', 150)
engine.say("Loading Started, Please Hold on for few seconds!")
engine.runAndWait()
#opens links
def o_link(linky):
    webbrowser.open(linky)
#Current pose speak
def read_out():
    true_vars = [key for key, value in Prayer.items() if value]
    if len(true_vars) == 1:
        engine.say(f'Your Current Pose is {true_vars[0]}')
        engine.runAndWait()

# Define a function to update the variables in the dictionary and call read_out if necessary
def update_variables():
    while True:
        time.sleep(3)
        read_out()

### FUNCTION TO CALCULATE ANGLES###
def Angle(First, Second, Third):
    Pa_X = lmlist[First][1]
    Pa_Y= lmlist[First][2]

    Pb_X = lmlist[Second][1]
    Pb_Y= lmlist[Second][2]

    Pc_X = lmlist[Third][1]
    Pc_Y= lmlist[Third][2]

    a = [Pa_X, Pa_Y]
    b = [Pb_X, Pb_Y]
    c = [Pc_X, Pc_Y]
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180:
        angle = 360-angle
        
    return angle

### FUNCTION FOR START LIVE BUTTON ###
def Starting():
    global Analysis, Update, wid, heit, label1
    win.after(1000, lambda: engine2.say("Starting Live Video Analysis"))
    win.after(1000, engine2.runAndWait)
    wid = 550
    heit = 400
    
    canvas = Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
    canvas.pack()
    # print(lmlist)
    canvas.create_image(0, 0, image=bg_image, anchor=NW)
    label1.configure(width = wid, height = heit)
    label1.place(x=420, y=180)
    Analysis = True
    Update = True

### FUNCTION FOR START RECORDED BUTTON ###
def RecordedVideo():

    global win, label1, cap, wid, heit, Analysis, Update, check
    cap.release()
    win.after(1000, lambda: engine2.say("Please Select Any one RecordedVideo"))
    win.after(1000, engine2.runAndWait)
    win.filename = filedialog.askopenfilename(initialdir = "Users\manee\OneDrive\Desktop",  \
    title = "SelectRecordedVideos")
    label1.destroy()
    label1 = Label(frame_1, width = 600, height= 400, bg= "#2C2F33")
    if win.filename:
        cap = cv2.VideoCapture(win.filename)
        label1.place(x=450, y=180)
        Analysis = True
        Update = True
        wid = 236
        heit = 400
    else:
        cap = cv2.VideoCapture(0)
        Analysis = False
        check = False
        Update = False
        label1.configure(width = 210, height= 100)
        label1.place(x=860, y=300)
        wid = 140
        heit = 80
    LiveVideo()
    select_img()


### FUNCTION FOR EXIT TO MAIN MENU BUTTON
def MMenu():
    global Analysis, DetectionLabel, label1, wid, heit, cap, MainMenu, check, img, rgb, DetectMssg
    global image, Update, DrawScl, NextMssg, Draw 
    
    cap.release()

    DetectionLabel.destroy()
    label1.destroy()
    DrawScl.destroy()
    MainMenu.destroy()
    DetectMssg.destroy()
    NextMssg.destroy()
    # NextVoice.destroy()
    welc1.destroy()
    # welc2.destroy()
    # welc4.destroy()
    canvas = Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
    canvas.pack()
    # print(lmlist)
    # add the background image to the canvas
    win.after(1000, lambda: engine2.say("Exiting to MainMenu"))
    win.after(1000, engine2.runAndWait)
    canvas.create_image(0, 0, image=bg_image, anchor=NW)
    Draw = False
    Analysis = False
    check = False
    Update = False
    label1 = Label(frame_1, width = 2, height= 1, bg= "#2C2F33")
    label1.place(x=0, y=0)
    wid = 140
    heit = 80
    cap = cv2.VideoCapture(0)
    LiveVideo()
    welcome()

# Exit from About Us
def MMenu2():
    global Analysis, DetectionLabel, label1, wid, heit, cap, MainMenu, check, img, rgb, DetectMssg
    global image, Update, DrawScl, NextMssg, Draw 
    
    cap.release()

    label1.destroy()
    MainMenu2.destroy()
    welc4.destroy()
    welc5.destroy()
    welc6.destroy()
    An_Git.destroy()
    An_Med.destroy()
    Mua_Git.destroy()
    Mua_Med.destroy()
    welc1.destroy()
    welc2.destroy()
    win.after(1000, lambda: engine2.say("Exiting To Mainmenu"))
    win.after(1000, engine2.runAndWait)
    canvas = Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
    canvas.pack()
    # print(lmlist)
    # add the background image to the canvas
    canvas.create_image(0, 0, image=bg_image, anchor=NW)
    Draw = False
    Analysis = False
    check = False
    Update = False
    label1 = Label(frame_1, width = 2, height= 1, bg= "#2C2F33")
    label1.place(x=0, y=0)
    wid = 140
    heit = 80
    cap = cv2.VideoCapture(0)
    LiveVideo()
    welcome()
    
### fUNCTION FOR DRAW SCALE BUTTON ###
def callback1(value):
    global Draw
    if Draw:
        Draw = False
    else:
        Draw = True

### FUNCTION FOR STARTING VIDEO PROCESING ###
def LiveVideo():
    global cap, img, _, wid, heit, rgb, image, finalImage
    _, img = cap.read()
    img = cv2.resize(img, (wid, heit))
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rgb =cv2.flip(rgb, 1)
    image = Image.fromarray(rgb)
    finalImage = ImageTk.PhotoImage(image)
    label1.configure(image=finalImage)
    label1.image = finalImage
    
### MAIN ANALYSYS FUNCTION ###
def select_img():
    global img, finalImage, image, rgb, _, wid, heit, lmlist, check, Update, label1
    global cap, v, q, pos, Next, CheckAgain, SajCount

    _, img = cap.read()
    img = cv2.resize(img, (wid, heit))
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rgb =cv2.flip(rgb, 1)

    #img = detector.findPose(img)
    #lmlist, bbxInf = detector.findPosition(img, bboxWithHands=True)
    lmlist = []

    if Update:
        AnalysisWinUpdate()
        Update = False
    
    if Analysis:
        detector.results = detector.pose.process(rgb)
        if detector.results.pose_landmarks:
            check = True
            for id, lm in enumerate(detector.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy, cz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
                lmlist.append([id, cx, cy, cz])

                if Draw:
                    detector.mpDraw.draw_landmarks(rgb, detector.results.pose_landmarks, detector.mpPose.POSE_CONNECTIONS)
        else:
            check = False

    #print(check)
    
    if check:
        # print(lmlist)
        Nose_Y=lmlist[0][2]
        earRight_X=lmlist[8][1]
        earRight_y=lmlist[8][2]
        
        earLeft_X=lmlist[7][1]
        earLeft_y=lmlist[7][2]
        
        IndexRight_X=lmlist[22][1]
        IndexRight_Y=lmlist[22][2]

        IndexLeft_X=lmlist[21][1] #changing made using thummbs insted of index fingers
        IndexLeft_Y=lmlist[21][2]
        
        ThumbRight_X=lmlist[22][1]
        ThumbRight_Y=lmlist[22][2]

        ThumbLeft_X=lmlist[21][1] 
        ThumbLeft_Y=lmlist[21][2]

        WristLeft_X=lmlist[15][1] 
        WristLeft_Y=lmlist[15][2]

        WristRight_X=lmlist[16][1] 
        WristRight_Y=lmlist[16][2]

        MouthRight_Y=lmlist[10][2]  
        MouthLeft_Y=lmlist[9][2]

        KneeRight_X=lmlist[26][1] 
        KneeRight_Y=lmlist[26][2]

        KneeLeft_X=lmlist[25][1]  
        KneeLeft_Y=lmlist[25][2] 

        HipRight_Y=lmlist[24][2]  
        HipLeft_Y=lmlist[23][2]

        ShoulderRight_Y=lmlist[12][2]  
        ShoulderLeft_Y=lmlist[11][2]

        AnkleRight_X=lmlist[28][1] 
        AnkleRight_Y=lmlist[28][2]

        AnkleLeft_X=lmlist[27][1]   
        AnkleLeft_Y=lmlist[27][2]

        ToeRight_X =lmlist[32][1]   
        ToeLeft_X = lmlist[31][1]

        ToeRight_Y =lmlist[32][2]   
        ToeLeft_Y = lmlist[31][2]

        LeftKneeAngle = int(Angle(23, 25, 27))#variable name changed
        RightKneeAngle=int(Angle(24,26,28))#use of right knee angle
        ElbowAngle = int(Angle(11, 13, 15))
        lefthipangle= int (Angle(11,23,25))
        righthipangle= int (Angle(12,24,26))

        adit = abs(ShoulderRight_Y - HipRight_Y)
        adit = adit/2

        if (IndexRight_Y<ShoulderRight_Y and IndexLeft_Y<ShoulderLeft_Y) and \
            (IndexRight_Y>earRight_y and IndexLeft_Y>earLeft_y) and (abs(IndexRight_Y-IndexLeft_Y)<10) and \
                (abs(IndexRight_X-IndexLeft_X)<120) and ((abs(earRight_X-earLeft_X)+30)<(abs(ThumbRight_X-ThumbLeft_X))):#changing made in condition and taking difference of thumbs 
            Prayer['Takbir'] = True
        else:
            Prayer['Takbir'] = False

        if (IndexRight_X>IndexLeft_X) and (LeftKneeAngle > 165) and \
            (ElbowAngle < 140) and (abs(ThumbLeft_Y-ThumbRight_Y)<15):#changing made in elbow angle and use of thumb
            Prayer['Qayam'] = True
        else:
            Prayer['Qayam'] = False

        if (IndexRight_Y > (HipRight_Y + (KneeRight_Y-HipRight_Y)/2) and \
            (IndexLeft_Y > (HipLeft_Y + (KneeLeft_Y-HipLeft_Y)/2))) and ((LeftKneeAngle) > 165) and \
            ((RightKneeAngle) > 165) :
            Prayer['Ruku'] = True
        else:
            Prayer['Ruku'] = False

        if (IndexRight_Y > HipRight_Y) and (IndexLeft_Y > HipRight_Y) and ((LeftKneeAngle) > 165) and \
            ((RightKneeAngle) > 165) and (abs(ThumbRight_Y-ThumbLeft_Y) < 10) :#why hip right in both and changing made for thumbs position use of elbow angle
            Prayer['Qomah'] = True
        else:
            Prayer['Qomah'] = False

        if (ToeLeft_X < AnkleLeft_X) or (ToeRight_X < AnkleRight_X):
            if  ((Nose_Y > ShoulderRight_Y) or (Nose_Y > ShoulderLeft_Y)) and \
            ((HipRight_Y < ShoulderRight_Y) or (HipLeft_Y < ShoulderLeft_Y)) and \
            (((IndexRight_X > KneeRight_X) or (IndexLeft_X > KneeLeft_X)) or ((IndexRight_X < KneeRight_X) or (IndexLeft_X < KneeLeft_X))) and \
            (LeftKneeAngle or RightKneeAngle < 80) and (ElbowAngle < 100) and \
            ((ToeLeft_Y or ToeRight_Y) - (KneeLeft_Y or KneeRight_Y) < 10) :
            # (Nose_Y - (IndexLeft_Y or IndexRight_Y) < 10)
                Prayer['Sajdah'] = True
            else:
                Prayer['Sajdah'] = False
        
        # if (ToeLeft_X > AnkleLeft_X) or (ToeRight_X > AnkleRight_X):
        #     if  ((Nose_Y > ShoulderRight_Y) or (Nose_Y > ShoulderLeft_Y)) and \
        #     ((HipRight_Y < ShoulderRight_Y) or (HipLeft_Y < ShoulderLeft_Y)) and \
        #     ((IndexRight_X < KneeRight_X) or (IndexLeft_X < KneeLeft_X)) and \
        #     (LeftKneeAngle < 80) and (ElbowAngle < 100):
        #         Prayer['Sajdah'] = True
        #     else:
        #         Prayer['Sajdah'] = False

        if (((HipRight_Y > (AnkleRight_Y - adit)) or (HipLeft_Y > (AnkleLeft_Y - adit))) \
            and ((LeftKneeAngle) < 30) ):# use of elbow angle
            Prayer['Atahyaat'] = True
        else:
            Prayer['Atahyaat'] = False

        if Prayer['Takbir']:
            v.set("Takbir")
        elif Prayer['Sajdah']:
            v.set("Sajdah")
        elif Prayer['Ruku']:
            v.set("Ruku")
        elif Prayer['Atahyaat']:
            v.set("Atahyaat")
        elif Prayer['Qomah']:
            v.set("Qomah")
        elif Prayer['Qayam']:
            v.set("Qayam")
        else:
            v.set("None")

        if Prayer["Sajdah"] and CheckAgain:
            SajCount += 1
            CheckAgain = False
        if (not Prayer["Sajdah"]) and Prayer["Atahyaat"]:
            CheckAgain = True


        pos = v.get()
        pos = "Your current position is " + pos
        q.set(pos)

        pos = "The next position should be "
        if v.get() == 'Takbir':
            nex = "Qayam"
        elif v.get() == 'Qayam':
            nex = "Ruku"
        elif v.get() == 'Ruku':
            nex = "Qomah"
        elif v.get() == 'Qomah':
            nex = "Sajdah"
        elif v.get() == 'Sajdah':
            nex = "Atahyaat"
        elif v.get() == 'Atahyaat' and SajCount == 1:
            nex = "Sajdah"
        elif v.get() == 'Atahyaat' and SajCount>1:
            nex = "Salam"
        else:
            pos = ""
            nex = ""
        pos = pos + nex
        Next.set(pos)

    
    image = Image.fromarray(rgb)
    finalImage = ImageTk.PhotoImage(image)
    label1.configure(image=finalImage)
    label1.image = finalImage
    win.after(1, select_img)
    
    
def show_buttons():
    global welc2,welc4,welc4,welc5,welc6,An_Git,An_Med,Mua_Git,Mua_Med,MainMenu2
    inner_frame = Frame(win)
    inner_frame.place(x=500,y=550)
    welc3.destroy()
    StartLive.destroy()
    StartRecord.destroy()
    outer_button.destroy()
    Exit.destroy()
    An_Git = Button(win,text="GitHub",borderwidth=12,font=("Times",12), command= lambda:o_link(link1),width = 14, fg = "white",bg = "#2C2F33", padx=10,pady=10,\
    relief = RAISED)
    An_Git.place(x = 335, y = 475)
    An_Med= Button(win,text="Medium",borderwidth=12,font=("Times",12), command=lambda:o_link(link2),width = 14, fg = "white",bg = "#2C2F33", padx=10,pady=10,\
    relief = RAISED)
    An_Med.place(x = 335, y = 550)
    Mua_Git = Button(win,text="GitHub",borderwidth=12,font=("Times",12), command=lambda:o_link(link3),width = 14, fg = "white",bg = "#2C2F33", padx=10,pady=10,\
    relief = RAISED)
    Mua_Git.place(x = 865, y = 475)
    Mua_Med = Button(win,text="Medium",borderwidth=12,font=("Times",12), command=lambda:o_link(link4),width = 14, fg = "white",bg = "#2C2F33", padx=10,pady=10,\
    relief = RAISED)
    Mua_Med.place(x = 865, y = 550)
    welc4 = Message(win, justify = CENTER, text= "Developed By :", \
    font = ("Times", 16), fg = "white",bg = "#2C2F33", relief = FLAT, width = 1280)
    welc4.place(x = 600, y = 380)
    # engine2.say("This Project is Developed by Muhammad Anees (2021-MC-03) and Muawwiz Ali Yousaf (2021-MC-13) in Department of Mechatronics & Control Engineering, University of Engineering and Technology, Lahore")
    win.after(1500, lambda: engine2.say("For More information Click GitHub Button"))
    win.after(1500, engine2.runAndWait)
    welc5= Message(win, justify = CENTER, text= "Muhammad Anees (2021-MC-03)", \
    font = ("Times", 16), fg = "white",bg = "#2C2F33", relief = FLAT, width = 1280)
    welc5.place(x = 250, y = 430)
    welc6= Message(win, justify = CENTER, text= "Muawwiz Ali Yousaf (2021-MC-13)", \
    font = ("Times", 16), fg = "white",bg = "#2C2F33", relief = FLAT, width = 1280)
    welc6.place(x = 790, y = 430)
    welc2 = Message(win, justify = CENTER, font = ("Times", 18), fg = "white", \
    bg = "#2C2F33",text= "Department of Mechatronics & Control Engineering, University of Engineering and Technology, Lahore",\
    width = 1200,relief = FLAT)
    welc2.place(x = 175, y = 660)
    MainMenu2 = Button(win,text='Exit to Main Menu',borderwidth=12,font = ("Times", 12), width = 14, fg = "white",bg = "#2C2F33", padx=10,pady=10,\
    command= MMenu2, relief = RAISED)
    MainMenu2.place(x = 595, y = 575)
    
    
def welcome():
    global StartLive, welc1, welc2, welc3, welc4, label1, wid, heit, WelcMsg, Exit, win, StartRecord,outer_button
    WelcMsg = StringVar()
    WelcMsg.set("WELCOME TO THE PRAYER ANALYSIS MEDIAPIPE PROJECT")
    welc1 = Message(win, justify = CENTER, textvariable = WelcMsg, font = ("Times", 20), \
    fg = "white",bg = "#2C2F33", relief = FLAT, width = 1000)
    welc1.place(x = 270, y = 120)
    # WelcMsg.spoken = False
    # welc1.after(3000, speak_label, welc1)
    welc3 = Message(win, justify = CENTER, text= "Press START to begin your analysis", \
    font = ("Times", 14), fg = "white",bg = "#2C2F33", relief = FLAT,\
    width = 1000)
    welc3.place(x = 550, y = 420)
    outer_button = Button(win, text="About us",borderwidth=12,font = ("Times", 12),width = 14, fg = "white",bg = "#2C2F33", padx=10,pady=10, \
    command=show_buttons,relief = RAISED)
    outer_button.place(x=490,y=600)
    StartLive=Button(win,text='Start Live Video',borderwidth=12,font = ("Times", 12), width = 14, fg = "white",bg = "#2C2F33", padx=10,pady=10,\
    command= Starting, relief = RAISED)
    StartLive.place(x = 490, y = 475)
    StartRecord =Button(win,text='Start Recorded Video',borderwidth=12,font = ("Times", 12), width = 14, fg = "white",bg = "#2C2F33",padx=10,pady=10, relief = RAISED, \
    command = RecordedVideo)
    StartRecord.place(x = 735, y = 475)
    Exit = Button(win,text='Exit Program',borderwidth=12,font = ("Times", 12), width = 14, fg = "white",bg = "#2C2F33", padx=10,pady=10,\
    command= ExitTheProgram, relief = RAISED)
    Exit.place(x = 735, y = 600)
    
    
def ExitTheProgram():
    engine.say("Exiting the program!")
    engine.runAndWait()
    win.destroy()
    
def AnalysisWinUpdate():
    global v, q, pos, wid, heit, label1, StartLive, welc1, welc2, welc3, welc4
    global DetectionLabel, MainMenu, DrawScl, WelcMsg, DetectMssg, NextMssg, Next,NextVoice

    StartLive.destroy()
    StartRecord.destroy()
    welc3.destroy()
    canvas.destroy()
    Exit.destroy()
    outer_button.destroy()
    WelcMsg.set("Prayer Analysis Project")
    welc1.config(font = ("Times", 25))
    welc1.place(x = 530, y = 60)

    DetectionLabel=Label(win,width=30,borderwidth=4, height = 1, font = ("Times", 21), \
    bg = "#99AAB5", fg= "#5865F2", textvariable= v, relief=FLAT)
    DetectionLabel.place(x = 465, y = 124)

    if (wid == 236 and heit == 400):
        DetectionLabel.place(x = 634, y = 104)
        DetectionLabel.configure(width = 15)

    MainMenu=Button(win,text='Exit to Main Menu', width = 14, fg = "white", bg = "black",\
    padx=10,pady=10, relief = RAISED, command = MMenu, font = ("Times", 15))
    MainMenu.place(x = 420, y = 620)

    DrawScl = Scale(win, label="Show Landmarks", from_ =0, to=1, orient=HORIZONTAL, command = callback1,\
    activebackground='#339999', bg = "black", length= 170, font = ("Times", 15), fg = "white",\
    troughcolor= "white", relief= FLAT)
    DrawScl.set(0)
    DrawScl.place(x=608, y=620)
    
    DetectMssg = Message(win, justify = CENTER, font = ("Times", 18), bg = "#2C2F33", fg = "white", \
    textvariable= q, width = 200,relief = FLAT)
    DetectMssg.place(x = 200, y = 90)

    NextMssg = Message(win, justify = CENTER, font = ("Times", 18), bg = "#2C2F33", fg = "white", \
    textvariable= Next, width = 200,relief = FLAT)
    NextMssg.place(x = 200, y = 170)
    threading.Thread(target=update_variables).start()

#Main Program
win = Tk()
win.after(1000, lambda: engine2.say("WELCOME TO THE PRAYER ANALYSIS MEDIAPIPE PROJECT"))
win.after(1000, engine2.runAndWait)
wid = win.winfo_screenwidth()
heit = win.winfo_screenheight()
win.geometry("%dx%d" % (wid, heit))
win.title('Salat Analsis using Mediapipe')
frame_1 = Frame(win, width=0, height=0, bg= "#FFFF00").place(x=0, y=0)
label1 = Label(frame_1, width = 600, height= 400)
label1.place(x=700, y=160)
bg_image = PhotoImage(file="bg11.png")
canvas = Canvas(win, width=wid, height=heit)
canvas.pack()
canvas.create_image(0, 0, image=bg_image, anchor=NW)
wid = 110
heit = 60
v = StringVar()
q = StringVar()
Next = StringVar()
if not Analysis:
    
    welcome()

select_img()
win.mainloop()
