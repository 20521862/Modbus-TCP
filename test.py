import os
from pymodbus.client import ModbusTcpClient 

from time import time
from tkinter import Frame, Label, Tk
from tkinter.font import Font
from vlc import MediaPlayer

FILE =  os.path.abspath(os.path.dirname(__file__)) + "/file/"

def main():
    print(FILE)
    attack()

def attack():
    values = [1024, 2048, 4096, 8192, 16384]

    app = Application(modbus= ModbusTcpClient('192.168.93.75'))
    app.run()
    app.destroy()

class Application(Tk):
    def __init__(
        self,
        modbus: ModbusTcpClient,
        # modbus2: ModbusAbstractClient,
        # skip_warning: bool = False,
    ) -> None:
        super().__init__()
        self.configure(background="black")
        self.wm_attributes("-fullscreen", True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.attributes("-topmost", True)

        self.modbus = modbus
        # self.modbus2 = modbus2
        # self.skip_warning = skip_warning
    def run(self) -> None:
            self.after(0, self.gui)
            self.mainloop()
        
    def gui(self) -> None:
            context = WarningContext(self)
            context.run()
            context.destroy()
            self.quit()


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

    AUDIO: MediaPlayer = MediaPlayer(FILE + "warning.mp3")

    def gui(self) -> None:
        self.AUDIO.play()

        text_warning = Label(
            self,
            text="WARNING",
            background="black",
            foreground="yellow",
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
        self.wait(1.6)

        text_in = Label(
            self,
            text="IN",
            background="black",
            foreground="white",
            font=Font(size=80),
        )
        self.blinking_texts.append(text_in)
        self.wait(1.6)

        text_countdown = Label(
            self,
            text="3",
            background="black",
            foreground="white",
            font=Font(size=150),
        )
        self.blinking_texts.append(text_countdown)
        self.wait(1.6)

        text_countdown.configure(text="2", foreground="yellow", font=Font(size=225))
        self.wait(1.6)

        text_countdown.configure(text="1", foreground="red", font=Font(size=300))
        self.wait(1.6)

        self.AUDIO.stop()
        # self.quit()


if __name__ == "__main__":
    def show_warning():
        root = Application(ModbusTcpClient('192.168.93.75'))
        warning_context = WarningContext(root)
        warning_context.gui()  # Hiển thị giao diện WarningContext
        warning_context.pack()  # Sử dụng phương thức pack để hiển thị giao diện

        root.mainloop()  # Chạy vòng lặp chính của ứng dụng

    show_warning()  # Gọi hàm để hiển thị cảnh báo và giao diện tương ứng
         