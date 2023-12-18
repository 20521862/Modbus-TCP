import os
from argparse import ArgumentParser
from time import time

from tkinter import Frame, Label, Tk
from tkinter.font import Font
from vlc import MediaPlayer 
from pymodbus.client import ModbusTcpClient                                
from pymodbus.exceptions import ModbusException, ModbusIOException          
from pymodbus.register_read_message import ReadHoldingRegistersResponse 


FILE =  os.path.abspath(os.path.dirname(__file__)) + "file/"

class WarningContext(BaseContext):

    AUDIO: MediaPlayer = MediaPlayer( FILE + "warning.mp3")

    def choreograph(self) -> None:
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
        self.quit()

def write_registers():

    values = [1024, 2048, 4096, 8192, 16384]
    client = ModbusTcpClient('192.168.93.75')

    while True:
        try:
            client.connect()

            # Đọc 12 thanh ghi từ địa chỉ 0 của PLC với đơn vị là 1
            result = client.read_holding_registers(address=0, count=12, unit=1)  # Thay đổi địa chỉ unit của PLC của bạn

            if not result.isError():
                # Nếu không có lỗi, hiển thị giá trị đọc được từ 12 thanh ghi
                registers = result.registers
                print(f"Giá trị đọc từ 12 thanh ghi: {registers}")
            else:
                print(f"Lỗi: {result}")
        except Exception as e:
            print(f"Lỗi: {e}")
        finally:
            client.close()

