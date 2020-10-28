# coding=utf-8
from __future__ import unicode_literals
from collections import OrderedDict
import re, string, unicodedata
import nltk
import inflect
import subprocess
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from time import clock, sleep
from pprint import pprint
import json
import zipfile
import glob 
import io, json
import os  
from langdetect import detect
import pandas as pd
from docx import Document
import fnmatch
import sys
import shutil
import moment
from datetime import datetime
from datetime import datetime




#***** function to read the file and return the content ****  #

def read_document(filepath):
    f = open(filepath ,errors='ignore')
    raw = f.read()
    f.close()
    return raw

#***** function to convert the pdf file to docx ! ****  #

def Convert_Pdf_Docx(file_name):
    # excute command system to convert it into html file !
    os.system(r"pdf2htmlEX --zoom 1.3 ../../your_directory" + file_name + " --dest-dir ../../public/files_html/  --debug 0")
    #os.system("mv ../services/*.html  ../html_files/")
    #**** GET the filename without extension ***************#
    fileName = os.path.splitext(file_name)[0]
    #print("filename without extesnion" + fileName)
    # concatenate the filename with extension html ********#
    fileExt= fileName + ".html"
    #******** prepare the command to b executed  with pandoc ! to convert html file to .docx
    command = "pandoc -s ../../public/files_html/"+ fileExt + " -o ../../public/files_docx/" + fileName +".docx" +" > output.txt"
    #***** execute the command *********#
    os.system(command)

    return "../../public/files_docx/" + fileName +".docx"

#***** Remove non-ASCII characters from list of tokenized words ****  #

def remove_non_ascii(words):
   
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

#*****  Convert all characters to lowercase from list of tokenized words ****  #

def to_lowercase(words):
    
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words


def remove_punctuation(words):
    
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

#********* function to get lits of tokens ************#
def get_tokens(raw,encoding='utf8'):
    '''get the nltk tokens from a text'''
    tokens = nltk.word_tokenize(raw) #tokenize the raw UTF-8 text
    return tokens

#********* function to return resume language ************#
def detect_resume_langauge(data):
    
    try:
        lang =str(detect(data))
    except:
        lang = "error"
        print("This row throws and error:")   
    return lang

#******* return the text after cleaning the data  ***#

def get_nltk_text(tokens,encoding='utf8'):
    text=nltk.Text(tokens,encoding) #create a nltk text from those tokens
    return text

 #***** Remove stop words from list of tokenized words ****  #

def remove_stopwords(words,lang):
    new_words = []
    raw_stopword_list=[]
    if(lang == 'fr'):
       raw_stopword_list = stopwords.words('french')
    else :
        raw_stopword_list = stopwords.words('english')  
    for word in words:
        # print(word)
        if word not in raw_stopword_list:
            new_words.append(word)
    return new_words


#***** Remove extracted data  from list of tokenized words ****  #

def remove_exracted_data(data,exculded_data):
    new_words = []
    for word in exculded_data:
          print(data.replace(word,''))
    return new_words

#***** Stem words in list of tokenized words ****  #

def stem_words(words):
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

#***** Lemmatize verbs in list of tokenized words ****  #

def lemmatize_verbs(words):
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

#****  normalize list of tokenized words ****  #  

def normalize(words,langage):


   #***** GET the resume language *****#
    #***** REMOVE NON ASCII WORDS *************#
    words = remove_non_ascii(words)
    #******  CONVERT ALL WORDS TO LOWERCASE**********#
    words = to_lowercase(words)
    #********* REMOVE STOPWORDS ***************#
    words = remove_stopwords(words,langage)

    return words

 #****  get the email from the file content with regular expression ****  #

def getEmail(words):

        email = None
        try:
            pattern = re.compile(r'\S*@\S*')
            matches = pattern.findall(words)
              # Gets all email addresses as a list
            if(matches ):  
                email = matches[0]
           
        except Exception as e:
            print
            e

        return email

#****  get the linkedin profile from the file content with regular expression ****  #
def getLinkedin(words):
    profile = None
    try:
        pattern = re.compile(r'\S*linkedin\S*')
        matches = pattern.findall(words)  # Gets all linkeidn url as list ***
        if(matches):
            profile = matches[0]  
    except Exception as e:
        print(e)

    return profile

#****  get the linkedin profile from the file content with regular expression ****  #

def getGithub(words):
    profile = None
    try:
        pattern = re.compile(r'\S*github\S*')
        matches = pattern.findall(words)  # Get github profile if exist
        if(matches):
            profile = matches[0]   
    except Exception as e:
        print(e)

    return profile    

#****Extract all the urls from the data ****  #

def getURLS(words):
    urls= []
    try:
        matches = re.findall(r'(https?://\S+)', words)
        for match in matches:
              urls.append(match)
    except Exception as e:
        print(e)

    return urls  

#********* Extract list of dates ***************#

def getDates(words):
    dates= []
    try:
        matches = re.findall("(\d+\-\w+)", words)
        for match in matches:
              dates.append(match)
    except Exception as e:
        print(e)

    return dates 
   
#**** extract the phone number ****  #

def getPhone(data):
        
        phone_numbers =[]
        phone_numbers_test =[]
        # split the file content  into list of lines****#
        list = data.split('/n')
        #***** read the regex from csv file ! #
        df = pd.read_csv('./server/services/regex.csv') 
        #****select only regex for tunisia phone numbers !
        tn_regex = df['tn'] 
        
        
        try:
            #******** read all the list of patterns from a file regex.txt***********#
            for regex in tn_regex:
                #**** select the pattern *****#
                 patternx = re.compile(r'(%s)'%regex)
                 #***** for each line search for phones ! ****#
                 for line1 in list:
                     # search for the lines that matches the patternx
                     match = re.search(patternx,line1)
                     #check if there is phone numbers that matches then append it to the list
                     if(match and match.group(0) not in phone_numbers ): 
                        #append the phone number !  
                        phone_numbers_test.append(match.group(0))
             
        except Exception as e:
               print(e)
        return phone_numbers_test
        


#********* extract the Languages  ????????? ************#
def getLanguages(data):
    prog = re.compile("\s*(langues).*")
    result = prog.match(data)
    print(result)
    languages =""
    return languages



# **** function to get only the name from the filepath without extension !
def getName(file,lower_words):
    head,tail= os.path.split(file)
    noun = ""
    #*** GET THE name of the file without extension **#
    name = os.path.splitext(tail)[0]
    #********************************************#
    noneWord = ['cv']
    #****** convert the name to lowercase *******#
    name = name.lower() 
    #***** remove non asci chars ****#
    #******** remove non words from the file  ********#
    # check the name and search it into the file content
    text = nltk.Text(lower_words)
    # convert name to list of words separated by _ #
    names = name.split("_")
    #  remove words having less than 2 chars **#
    names =[x for x in names if len(x)>2]
    #**** concatenate all teh strings into one word ****
    name = ''.join(names)
    for i in noneWord:
         name =name.strip(i)
    return name


# --------- GET THE filename to ba saved into the resume *******************#

def getFileName(filename):
    tail =""
    #***** read the filecontent ****#
    f = open(filename,"r" ,errors='ignore' )
    #**** convert it as a List !! ****#
    lineList = f.readlines()
    #_________ get only the filename without path_________
    try :
       head,tail= os.path.split(lineList[1])
    #_________the line to be removed_________
       line= os.path.split(lineList[1])
    #_______remove it after been extracted________  
       #f = open(filename,"w")
       '''for line in lineList:
           if line!=lineList[-1]:
              f.write(line)'''
    except Exception as e:
           print("type error: " + str(e))       
    return tail


#**** extract the university !! ****  #

def getDate(filename):
    date = moment.now().format("dddd MMMM D Y")
    #_________read the filecontent______
    f= open(filename,"r" ,errors='ignore' )
    #_________convert it as a List !!_______
    lineList = f.readlines()
    #______read teh last line of the file !!
    try :
       date= lineList[2]
    #_______remove it after been extracted________ 
    except Exception as e:
           print("type error: " + str(e))
    return date

def getUniversity(filename):
    
      #initialize list of universities to be extracted !
    list_universities =[]
    #***** read the list of universities  from csv file ! #
    df = pd.read_csv('./server/services/list__Universities.csv') 
    #****select only regex for tunisia universities ! !
    tn_universities = df['tn'] 
    #***** GET the extension to check if it was pdf or docx !
    extension = os.path.splitext(filename)[1]
 
    #*** read the docx file !!******#
    doc = Document(str(filename))
    for para in doc.paragraphs:
        for university in tn_universities:
            match = re.search(university,para.text)
            if(match):
                list_universities.append(para.text)
        

       
    




if __name__ == "__main__":

 files=glob.glob('directory_txt_files/*.txt')
  

# for each file !!!
for file in files:

  
     #_______________extract  the date _________________#
    date = getDate(file)
    #print("the date is" + date)
     #_______________extract  the fileName _________________#
    filename = getFileName(file)
    #print("filename is" + filename)
     #_______________read the file content_________________#
    data = read_document(file)

    #_______________extrat the email_____________________
    email =getEmail( data) 
     #________remove the email after been extracted__________________
    if(email):
     data = data.replace(email,'')

#____________extrat the gith  and append it to the list____________
    profile = getLinkedin(data)
    if(profile):data =data.replace(profile,'')
    
    #_______________extrat the list of urls  and append it to the list________________
    urls = getURLS(data)
    #_______ remove the urls extracted____________ !!
    if(urls):
      for url in urls:
            data =data.replace(url,'')

    
    #_______________extrat the list of phones  and append it to the list
    phones = getPhone(data)
    if(phones):
      for phone in phones :
          data =data.replace(phone,'')

    #______detect the langauge of the resume________#
    language = detect_resume_langauge(data)
    words = get_tokens(data)
     #_________extrat the name_________________
    name= getName(file,words)
    #____________remove the name from the file______________
    if(name):data = data.replace(name,'')
    #____________convert it to lower case______________________ 
    lower_words = to_lowercase(words)
     #___________normalize the words (preprocessing)_____________# 
    words = normalize(words,language)
    
    #___________GET the txt content after cleaning the words___________________#
    text = "".join([""+i if not i.startswith("'") and i not in string.punctuation else i for i in words]).strip()
    try :
    #os.remove(file) 
     print("saved")  
    except Exception as e:
        print("error removing the json file : " + str(e))
    
    


         




