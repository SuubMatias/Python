from pynput.keyboard import Key, Controller
import time
from PIL import ImageGrab, Image

keyboard = Controller()

time.sleep(5)

class Comando:
    def __init__(self, timer, comando):
        self.timer = 0
        self.limite = timer
        self.comando = comando
    def update(self):
        if self.timer <= 0:
            self.digitar()
            self.timer = self.limite
        else:
            self.timer-=1
        print(f"Tempo para o comando '{self.comando} -> {self.timer} segundos'")

    def digitar(self):
        keyboard.type(self.comando)
        time.sleep(0.08)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)

def recebeuDM():
    img = ImageGrab.grab()
    cor = (240, 71, 71)
    if img.getpixel((56, 122)) == cor:
        print('\n\n\n\n\n\nRECEBEU DM!')
        return True
    else:
        return False

beg = Comando(32, "pp!b")
raid = Comando(122, "pp!r")
#lvlUp = Comando(250, "pp!buy ba")
fishing = Comando(64, "pp!f")
hunt = Comando(61, "pp!hunt")
#marco = Comando(0, "Vai tomar no seu cu@Relampago Marquinhos#2451")

#hiago = Comando(5, "@Hiago#7959 Bom dia primo")

if __name__ == "__main__":
    for i in range(3600):
        time.sleep(1)
        if recebeuDM():
            break
        beg.update()
        raid.update()
        if recebeuDM():
            break
        hunt.update()
        #marco.update()
        fishing.update()
        if recebeuDM():
            break

        print(f"Tempo restante do programa -> {3600-i}\n\n")