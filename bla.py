###################################################################################
##The MIT License (MIT)
##
##Copyright (c) 2017 Johnathan Hinebrook (github.com/ChocolaKuma)
##
##Permission is hereby granted, free of charge, to any person obtaining a copy
##of this software and associated documentation files (the "Software"), to deal
##in the Software without restriction, including without limitation the rights
##to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##copies of the Software, and to permit persons to whom the Software is
##furnished to do so, subject to the following conditions:
##
##The above copyright notice and this permission notice shall be included in all
##copies or substantial portions of the Software.
##
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##SOFTWARE.
###################################################################################
#MEM_HOG.py
#Version 0.1.5.02172017.1647
#Windows version
#UPDATEDATE02.17.2017
#USE AT OWN RISK
#J.HINEBROOK IS NOT LIABLE FOR ANY DAMAGES AT ALL IN ANY WAY
#fills up HDD space quickly.
#Depending on cpu 2.4 gigabytes per minute
#makesure a dir name tmp is in the same directory as this program
#Read comments for more info
###################################################################################
import os     #for os control
import shutil #for dir make and destruction
import random
import distutils.dir_util


#Globals




#Loud way of running this program
#prints system information
#can be disabled to improve proformance
VERBOSE_MODE = False





#This switch/flag allows for HDDhog to run past the
#repitition limit. True to make it stop after 100
#repetition
limited_Use = False




#prints various debug statments and log files
#check /logs/ for logs if aclipicable
DEBUG = False




#1 Slow mode
#  one single file is very slow several
#  minutes to generate 1G file
#2 Fast Mode
#  Uses same memory generation as
#  option one but copys and pastes
#  it sever times to make it larger

LoadMode = 2





hog = 2
count = 2
workdir = 'tmp'
file = './tmp/0000.hogwash'
filedir = './tmp/0000'
formate = '.hogwash'

startname = str(random.randint(0,99999))
file = "./tmp/"+startname+formate

a = 0 
b = 0
c = 0
if(DEBUG==True):
    os.startfile(workdir)
f = open(file, 'w+')





def startup(mkdirname):
    #makes working dir
    #os.mkdir(mkdirname)
    # os.makedirs() for mulitable
    try:
        os.makedirs(mkdirname)
    except OSError:
        print("Directory Exists")
        

def cleanup():
    #deletes previous session worth of data
    shutil.rmtree('tmp', ignore_errors=True)
    print('tmp deleted')

def fastHDDHog():
    seednum = 123
    seednum = seednum ** seednum
    numb = random.randint(0,99999)
    tmpdir = './tmp/'
    format = '.hogwash'
    file = tmpdir + str(numb) + format
    f = open(file, 'w+')
    while Running == True:
        try:
            f.write(strcount)
            print()
            print(os.stat(file))
        except:
            print()

def hddhog(repitition):
    hog = 2
    count = 2
    workdir = 'tmp'
    file = './tmp/'
    numb = random.randint(0,99999)

    formate = '.hogwash'
    file = file + str(numb) + formate
    f = open(file, 'w+')
    a = 0 
    b = 0
    c = 0
    global limited_Use,DEBUG,LoadMode
    while hog == 2:
        if a == repitition + 1:
            hog = 0
            break
        statinfo = os.stat(file)
        a = a + 1
        c = c + 1

        if a == 100:
            if DEBUG == True:
                print("A:",a,"b:",b)
            b = b + 1

            if LoadMode ==2:
                newfilenamenumber = random.randint(0,99999)
                #dirname = "tmp/"
                #TODO make random generating numbers for file names
                #newfile = dirname + newfilenamenumber + format
                
                newfile =  workdir+ "/"+ str(newfilenamenumber) + formate
                shutil.copy2(file, newfile)
            if limited_Use == False:
                a = 0
                
        if VERBOSE_MODE == True:
            file_size = statinfo.st_size
            file_unit = "b"
            print("Current file size:",file_size,file_unit)
            print('currentLOADMODE:',LoadMode)
            if LoadMode == 1:
                print("Switch to LOADMODE 2 for faster results")

        count = count * 20
        count = count * 20
        strcount = str(count)
        strcount= strcount+strcount+strcount+strcount+strcount+strcount+strcount+strcount
        strcount= strcount+strcount+strcount+strcount+strcount+strcount+strcount+strcount
        strcount= strcount+strcount+strcount+strcount+strcount+strcount+strcount+strcount
        f.write(strcount)


def main(repitition=123456789987654321):

    print("bla.main()")
    hddhog(repitition)

