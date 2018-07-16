import time
import tkinter


class TimerAbstract:
    def get_time(self):
        return time.strftime('%H:%M:%S')


class Relogio(TimerAbstract):
    def __init__(self):
        self.relogio = tkinter.Label()
        self.relogio['font'] = 'Helvica 120 bold'
        self.relogio['text'] = self.get_time()
        self.relogio.pack()

    def tictac(self):
        now = self.get_time()
        if now != self.relogio['text']:
            self.relogio['text'] = now
        self.relogio.after(100, self.tictac)


class Timer(TimerAbstract):
    def __init__(self, time_):
        self.timer = tkinter.Label()
        self.timer['font'] = 'Helvica 120 bold'
        self.timer['text'] = time_
        self.timer.pack()

        self.start_time = tkinter.Label()
        self.start_time['font'] = 'Helvica 60 bold'
        self.start_time['text'] = 'Inicio: ' + self.get_time()
        self.start_time.pack()

    def run(self):
        if int(self.timer['text']) > 0:
            self.timer['text'] = int(self.timer['text']) - 1
            self.timer.after(1000, self.run)
        else:
            self.end_time = tkinter.Label()
            self.end_time['font'] = 'Helvica 60 bold'
            self.end_time['text'] = 'Fim: ' + self.get_time()
            self.end_time.pack()


print('Relogio: R | Timer: T')
tipo = input().upper()

if tipo == 'T':
    print('Digite o tempo desejado:')
    tempo = int(input())
    relogio = Timer(tempo)
    relogio.run()
    relogio.timer.mainloop()
elif tipo == 'R':
    relogio = Relogio()
    relogio.tictac()
    relogio.relogio.mainloop()
