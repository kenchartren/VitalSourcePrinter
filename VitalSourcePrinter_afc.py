# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 21:07:59 2018

@author: jia

Description:
    To print purchased e-book in VitalSource as PDF by customizing user's 
    need efficiently
"""

try:   
    import PyPDF2 as ppdf
    import pyautogui as pyag
    import os
    import sys
    import time
    from tkinter import *
except:
    print("Please install PyPDF2 and pyautogui. Refer to video or documentation for help")
    sys.exit()

def prt2dir(chpt_num, filename, filedir):
    # to print chapters one by one in VitalSource
    for i in range(chpt_num):
        time.sleep(3)
        pyag.hotkey('ctrl', 'p')
        # open page selection page
        time.sleep(2)
        
        pyag.hotkey('shift', 'tab')
        time.sleep(1)
        pyag.hotkey('shift', 'tab')
        time.sleep(1)
        pyag.hotkey('shift', 'tab')
        
        pyag.press('delete', presses= 3)
        pyag.typewrite('1000') # make sure print all pages
        pyag.hotkey('shift', 'tab') # to get the maximum amount of pages for every chapter
        
        pyag.press('enter', presses= 2, interval= 2, pause = 1)
        # input file name and file directory
        pyag.typewrite(filename+str(i))
        pyag.press('tab', presses= 6)
        pyag.press('enter')
        pyag.typewrite(filedir)
        pyag.press('enter', presses= 2)
        pyag.hotkey('ctrl', 'pagedown')
        time.sleep(2)
        
        
        
def mergePDF(filedir, filename):
    merge_file = ppdf.PdfFileMerger()
    filenames = os.listdir(filedir)
    
    for file in filenames:
        merge_file.append(ppdf.PdfFileReader(open(filedir+'/'+file, 'rb')))
        
        
    merge_file.write(filedir+'/'+filename+'.pdf')
    
    for file in filenames:
        os.remove(filedir+'/'+file)
        

def main():
    # record time cunsumption;
    # start recording
    start_time = time.time()
    
    print("Welcome to the VitalSource Ebook Printer!\nThis version is for chapter pages of the form 'Chapter-Page'\n")
    
    # input file name and store directory
    filename = input("Please input the name of PDF file:")
    filedir = input("Please input the directory of file path:")
    chpt_num = int(input("Please input how many chapters the book have:"))
    
    
#    root = Tk()
#    root.withdraw()
#    root.overrideredirect(True)
#    root.geometry('0x0+0+0')
#    root.deiconify()
#    root.lift()
#    root.focus_force()
    # credits to http://stackoverflow.com/questions/3375227/how-to-give-tkinter-file-dialog-focus

    # give user time to activate VitalSource
    print("Please keep the VitalSource window active within 10 seconds\n")
    for sec in range(10, 0, -1):
        print("Program will start in "+str(sec)+" seconds:")
        time.sleep(1)
        if sec == 1:
            print("Starting now! Keep the start page open")
            break
    
    # print in the Vital Source window
    prt2dir(chpt_num, filename, filedir)
    
    # merge all the pdf files to one file with filename
    mergePDF(filedir, filename)
    
    time_taken = time.time() - start_time
    print('It takes '+str(time_taken)+' seconds')
    print('Done')
    

if __name__ == "__main__":
    main()
    
    

