#Meza Luna  Kitzia Sophia 
#Programacion 3°B tm 
#11/11/2025
#Ejemplo de la plataforma para audio y animacion
#CBTIS89

import os
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading

try:
    from playsound import playsound
except ImportError:
    from playsound3 import playsound  # type: ignore

# Carpeta base del script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class AnimatedGif(tk.Label):
    # Widget que muestra un GIF animado repitiéndose en bucle.
    def __init__(self, master, gif_path: str, delay: int = 80):
        image = Image.open(gif_path)
        self.frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(image)]
        self.delay = delay
        self.idx = 0
        super().__init__(master, image=self.frames[0])
        self.after(self.delay, self._animate)

    def _animate(self):
        self.idx = (self.idx + 1) % len(self.frames)
        self.configure(image=self.frames[self.idx])
        self.after(self.delay, self._animate)

def play_sound(sound_path: str):
    # Reproduce sonido en un hilo para no bloquear la GUI.
    threading.Thread(target=playsound, args=(sound_path,), daemon=True).start()

def main():
    root = tk.Tk()
    root.title('Animación con sonido – Tkinter')
    root.geometry('500x600')

    # Rutas de los GIFs
    gif_path1 = os.path.join(BASE_DIR, 'animationcirculo.gif')
    gif_path2 = os.path.join(BASE_DIR, 'animationcirculo2.gif')
    
    # Ruta del sonido
    sound_path = os.path.join(BASE_DIR, 'boing.wav')

    # Primer GIF
    gif_widget1 = AnimatedGif(root, gif_path1, delay=80)
    gif_widget1.pack(pady=10)

    # Segundo GIF
    gif_widget2 = AnimatedGif(root, gif_path2, delay=80)
    gif_widget2.pack(pady=10)

    # Botón para reproducir sonido
    tk.Button(
        root,
        text='Reproducir sonido',
        command=lambda: play_sound(sound_path),
        font=('Arial', 12, 'bold'),
        padx=10,
        pady=5,
    ).pack(pady=20)

    root.mainloop()

if __name__ == '__main__':
    main()
