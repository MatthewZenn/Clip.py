from win10toast import ToastNotifier
import os
from win32api import ShellExecute
import keyboard
import subprocess

Words = {
    'a':'Antidisestablishmentarianism',
    'b':'Bababadalgharaghtakamminarronnkonnbronntonnerronntuonn',
    'c':'Chargoggagoggmanchauggagoggchaubunagungamaugg ',
    'd':'Dialektičnomaterialističen',
    'e':'Ejendomsserviceassistentuddannelsen',
    'f':'Floccinaucinihilipilification',
    'g':'Gorsafawddachaidraigodanheddogleddolonpenrhynareurdraethceredigion',
    'h':'Hippopotomonstrosesquippedaliophobia',
    'i':'Incomprehensibleness',
    'j':'Jungermanniaceae',
    'k':'Konstantynopolitańczykowianeczka',
    'l':'Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch',
    'm':'Mamungkukumpurangkuntjunya',
    'n':'Nejneobhospodařovávatelnější',
    'o':'Otorhinolaryngological',
    'p':'Pneumonoultramicroscopicsilicovolcanoconiosis',
    'q':'Quincentenaries',
    'r':'Radioimmunoelectrophoresis',
    's':'Supercalifragilisticexpialidocious',
    't':'Taumatawhakatangihangakoauauotamateapokaiwhenuakitanatahu',
    'u':'Uncompromisingnesses',
    'v':'Vaðlaheiðarvegavinnuverkfærageymsluskúraútidyralyklakippuhringur',
    'w':'Wafflestomper',
    'x':'Xanthonoxypropanolamine',
    'y':'Ywerspersverklaringuitreikingsmediakonferensieaankondiging',
    'z':'Zygomaticosphenoid'
}

toaster = ToastNotifier()
x = 0

def press(win):
        for k,v in Words.items():
            if k == win.getkey():
                keyboard.write(v)
                break

while x < 1:
    if  keyboard.is_pressed("1"):
        toaster.show_toast("It looks like you're trying type words",
                "I like words, I can help you!",
                icon_path="Static/ClipPy.ico",
                duration=5)

while x < 1:
    if  keyboard.is_pressed("2"):
        subprocess.Popen('cmd.exe /K netstat')