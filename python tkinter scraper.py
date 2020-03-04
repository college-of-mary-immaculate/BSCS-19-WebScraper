from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as Ureq
import re
from tkinter import *
from tkinter import filedialog
import csv
import tkinter.ttk as ttk
import tkinter as tk
import os
import sys
from tkinter import messagebox
from pathlib import Path
#import tkinter as tk

#########################################################################################################
def mainwindow():
    window = tk.Tk()
    window.geometry("1250x630")
    window.title("Simple_WebScraper -AdamCM")
    window.resizable(False, False)
    frame1 =Frame(window, width = 318, height = 600, bg = "black")
    frame1.place(x= 10, y  =25) 
#################################################################################################  
    banner = Label(window, text = 'Welcome to Newegg.com webscrape', width = 171, background = 'Black', fg = 'White')
    banner.place(x= 10, y = 2)  

    brandlistbox = Listbox( window, width = 21, height =40, bg = "white", justify = LEFT, selectmode = EXTENDED )
    brandlistbox.place(x = 337, y = 50)
    #scroll1 = Scrollbar(brandlistbox, command = brandlistbox.yview)
    
    pricelistbox = Listbox( window, width = 20, height =40, bg = "white" , justify = CENTER, selectmode = EXTENDED )
    pricelistbox.place(x = 460, y = 50)
    #scroll2 = Scrollbar(window, command = pricelistbox.yview)
    
    savelistbox = Listbox( window, width = 20, height = 40, bg = "white", justify = CENTER , selectmode = EXTENDED )
    savelistbox.place(x = 580, y = 50)
    #scroll3 = Scrollbar(window, command = savelistbox.yview)
    
    Listbox4 = Listbox(window, width =60, height = 60, bg = "white", justify = LEFT, selectmode = EXTENDED  )
    Listbox4.place(x = 702, y = 50)
    hyperlink = Listbox(window, width =25, height = 60, bg = "white", justify = LEFT, selectmode = EXTENDED  )
    hyperlink.place(x = 1064 , y = 50)
####################################################################################### 
    scroll = Scrollbar(window, command = Listbox4.yview, orient = VERTICAL)
    scroll.pack(side =RIGHT,fill = Y)
    scroll4 = Scrollbar(window, command = Listbox4.xview, orient = HORIZONTAL)
    #pricelistbox.configure(yscrollcommand = scroll2.set)
    #savelistbox.configure(yscrollcommand = scroll3.set)
    #brandlistbox.configure(yscrollcommand = scroll1.set)
    Listbox4.configure(xscrollcommand = scroll4.set)
    scroll4.pack(side =BOTTOM,fill = X)
#####################################################################################
    #-----------------------------------------SETUP FOR LABEL
    brands = Label(window, text = "BRAND", width = 16 ,bg = "blue",fg = "white")
    brands.place(x = 340, y = 25)
    price = Label(window, text = "PRICE", width = 16 ,bg = "blue",fg = "white")
    price.place(x = 462, y = 25)
    save = Label(window, text = "DISCOUNT", width = 16 ,bg = "blue",fg = "white")
    save.place(x = 584, y = 25)
    titles = Label(window, text = "DESCRIPTIONS", width =50,bg = "blue",fg = "white")
    titles.place(x = 706, y = 25)
    link = Label(window, text = "SHOP LINK", width =20,bg = "blue",fg = "white")
    link.place(x = 1068 , y = 25)
###########################################################################################

    framelabel = LabelFrame(frame1, width = 300,height =106 )
    framelabel.place(x = 10, y = 250)
    
    filenamehere = Label(frame1, text = "File Names", width = 10)
    filenamehere.place(x = 20, y = 220)
    filenamehere1 = Label(frame1, text = "Opens", width = 10)
    filenamehere1.place(x = 170, y = 220)
        
    framelist1 = Listbox(frame1, width = 22, height = 5)
    framelist1.place(x =20, y = 260)    
    framelist = Listbox(frame1, width = 22, height = 5)
    framelist.place(x =165, y = 260) 

    Sentry = Entry(window, width =20, bg = "White", bd ='5', justify =CENTER, text = "Search Here", font = "Impact")
    Sentry.place(x = 70, y =50)
    def scrape():
        ####################################################################################
        concat = Sentry.get()
        #my_url = "file:///C:/Users/Adam-22-26/Desktop/graphics%20card%20-%20Newegg.com.html"
        my_url = 'https://www.newegg.com/global/ph-en/p/pl?d={}'.format(concat) 
        my_url = my_url.replace(' ', '+')
        ####################################################################################
        uClient = Ureq(my_url)
        
        page_html = uClient.read()
        uClient.close()
        #html_parsing
        page_soup = Soup(page_html, "html.parser")
        #grabe each         
        containers = page_soup.findAll("div", {"class": "item-container"})
        
        #manufacturer = page_soup.findAll("label",{"class": "form-checkbox"})
        #print(manufacturer )
        #print(len(containers))
        #print(containers[5:])
        #container = containers[5]
        #---------------------------------------- save the csv files
        fileName = "{}.csv".format(concat) ###############################################
            
        f = open(fileName, "w")
        headers = "BRAND     , PRICES    ,  SAVES    , TITLES   , LINK    \n"   #
        f.write(headers)
        
        for container in containers[4:]:
            #---------------------------------------------------------
            brand_container = container.findAll("a", {"class": "item-brand"})
            brand = brand_container[0].img["title"] #brand name
            
            #-------------------------------------------------------------------
            may_know = container.findAll("a", {"class": "item-title"})
            #print(may_know)
            
            ####################################################################
            title = container.a.img["title"] #Name of selling
            #print(container)
            #######################################################3
            hyper = brand_container[0]["href"]
            #hyper = container.findAll("div",{"class": "item-info"})
            #hyper = hypers.a
            #print(hyper)
            #--------------------------------------------------------------
            price_container = container.findAll("li", {"class" : "price-current"})
            price_container2 = price_container[0].strong
            price = re.findall(r'.\d.\d\d\d',  str(price_container2))
            prices = ''.join(price)
            #------------------------------------------------------------------------
            save_container = container.findAll("span", {"class" : "price-save-percent"})
            save = re.findall(r'\d\d.',  str(save_container))
            saves = ''.join(save)
            

            
            if saves == '':
                saves = "None"
            else:
                saves = saves
            if prices == "":
                prices = "Not Available"
            else:
                prices = prices
                
            brandlistbox.insert(END," :   "+brand)
            pricelistbox.insert(END,"₱ "+prices)
            savelistbox.insert(END,saves)
            Listbox4.insert(END ," :   " + title)
            hyperlink.insert(END, '  '+ hyper)
            #-------------------------------------------------------------------------

            f.write(brand.replace(',', '')  + ", " +  prices.replace(',', '.').replace('0', '1').replace('>', '    ') + ','  +   saves.replace('', '').replace('None', '0%')  +  ', '  + title.replace(',', '') +   ', '  + hyper  +"\n")
            
        f.close()
        new_win = Button(window, width =10, text = "New_Win", command = mainwindow, height = 1,font = "Jokerman", relief = RAISED, activebackground = "LightBlue1" , background = 'sky blue')
        new_win.place(x= 105, y = 90)
        messagebox.showinfo("Happens","DONE! \n press ok to proceed")
###############################################################################
                               ########################################################
    def listDir():
        path = Path()
        
        for filename in path.glob("*.csv"):
            framelist1.insert(END, filename)
            
    #lstdir = listDir(PATH_FOLDER)
    listDir()

###############################################################################
    openentry = Entry(frame1, width = 20, justify = CENTER)
    openentry.place(x = 89, y = 130)

    
    def opens():
        filenames = openentry.get()
        f = open(filenames, 'r')
        #with open('Online_Sales.csv', 'r') as Online_Sales:
        read = csv.reader(f)
        next(read)
        for line in read:
            Listbox4.insert(END ," :   " + line[3])
            pricelistbox.insert(END,"₱ "+line[1])
            brandlistbox.insert(END," :   "+line[0])
            savelistbox.insert(END,line[2])
            hyperlink.insert(END, '  '+ line[4])
        framelist.insert(END, filenames)
        clear = tk.Button(frame1, width = 9, text = "NEW WIN", command = mainwindow, height = 0,font = "Broadway", relief = RAISED, activebackground = "LightBlue1" , background = 'sky blue')
        clear.place(x= 20, y = 180)
    
    fopen = tk.Button(frame1, width = 9, text = "OPEN", command = opens, height = 0,font = "Broadway", relief = GROOVE, activebackground = "LightBlue1" , background = 'sky blue')
    fopen.place(x= 20, y = 180)
###############################################################################
    
    def save_as():
        filenames = openentry.get()
        f = open(filenames, 'r')
        read = csv.reader(f)
        next(read)

        files = filedialog.asksaveasfile(mode = 'w', defaultextension = ".csv")
        headers = "BRAND     , PRICES    ,  SAVES    , TITLES   , LINK    \n"
        files.write(headers)
        for line in read:
            files.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + '\n')
            files.close
    
    saveas = tk.Button(frame1, text = "save as", height = 1,font = "Broadway", relief = GROOVE, activebackground = "LightBlue1" , background = 'sky blue', command = save_as)
    saveas.place(x= 170, y =180)
###############################################################################
    #saved = Button(frame1, text = "save", height = 1,font = "Broadway", relief = GROOVE, width =8, activebackground = "LightBlue1" , background = 'sky blue')
    #saved.place(x= 211, y = 180)
    
    scrape = tk.Button(window, width =10, text = "SEARCH", command = scrape, height = 1,font = "Jokerman", relief = RAISED, activebackground = "LightBlue1" , background = 'sky blue')
    scrape.place(x= 105, y = 90)

    window.mainloop()
#-------------------------------------------------------------------------------------------------------
loginwin = tk.Tk()
loginwin.geometry("315x230")
loginwin.title("Log-in")
loginwin.resizable(False, False)

UserName = ttk.Entry(loginwin, width = 30, text ="Username")
UserName.place(x = 100, y = 70)
Password = ttk.Entry(loginwin, width = 30, show = "*", text = "password")
Password.place(x = 100, y = 120)

def command2():
    loginwin.destroy() #Removes the toplevel window
    #window.destroy() #Removes the hidden root window
    sys.exit()
def ver():
    username = UserName.get()
    passwords = Password.get()
    usernames = ['user']
    passwords = ['password']
    username = UserName.get()
    password = Password.get()
    for user in usernames:
        user = user
    for pas in passwords:
        pas = pas
        if user == username and pas == password:
            loginwin.destroy() #Removes the toplevel window
            #root.destroy() #Removes the hidden root window
            #sys.exit() #Ends the script
            return mainwindow()
        else:
            messagebox.showwarning("VERIFICATION", "AUTHENTICATION FAILD !! \n Program exit \n :(")
            return command2()
        
confirm = ttk.Button(loginwin, text = "CONFIRM", command = lambda: ver())
confirm.place(x = 150, y = 150)
confirm = ttk.Button(loginwin, text = "CANCEL   ", command = lambda: command2())
confirm.place(x = 150, y = 180)

UserName1 =tk.Label(loginwin, width = 10, text = "User Name :", justify = LEFT)
UserName1.place(x = 20, y = 70)
password1 = tk.Label(loginwin, width = 10, text = "Password :", justify = LEFT)
password1.place(x = 20, y = 120)

label = tk.Label(loginwin, text ="Log-in System Security", width =20)
label.place(x = 100, y =30)

loginwin.mainloop()

