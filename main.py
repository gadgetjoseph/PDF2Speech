#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : GadgetJoseph
# Created Date: December 12, 2021
# =============================================================================
"""PDF2Speech project"""
# =============================================================================
# Imports
# =============================================================================
import pyttsx3
import PyPDF2
from tkinter import *
from tkinter import filedialog

def read_pdf():
    selected_pdf = filedialog.askopenfilename()
    book = open (selected_pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(pages)
    bot = pyttsx3.init()
    for num in range(0, pages):
        page = pdfReader.getPage(0)
        text = page.extractText()
        bot.say(text)
        bot.runAndWait()
    
window = Tk()
btn = Button(window, text="Select pdf", command=read_pdf)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
window.mainloop()
