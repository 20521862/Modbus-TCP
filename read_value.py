import argparse

from time import time

from pymodbus.client import ModbusTcpClient                                
from pymodbus.exceptions import ModbusException, ModbusIOException          
from pymodbus.register_read_message import ReadHoldingRegistersResponse 

def read_register():
    # Khởi tạo client Modbus TCP
    client = ModbusTcpClient('192.168.93.75')  # Thay đổi địa chỉ IP của PLC của bạn
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
                # Nếu có lỗi, hiển thị thông báo lỗi
                print(f"Lỗi: {result}")
        except Exception as e:
            print(f"Lỗi: {e}")
        finally:
            client.close()
        
        time.sleep(1)

def read_coils():
     # Khởi tạo client Modbus TCP
    client = ModbusTcpClient('192.168.93.75')  # Thay đổi địa chỉ IP của PLC của bạn
    while True:
        try:
            client.connect()

            # Đọc 12 coils từ địa chỉ 0 của PLC với đơn vị là 1
            result = client.read_coils(address=0, count=1, unit=1)  # Thay đổi địa chỉ unit của PLC của bạn

            if not result.isError():
                # Nếu không có lỗi, hiển thị giá trị đọc được từ 12 coils
                coils = result.coils
                print(f"Giá trị đọc từ 12 thanh ghi: {coils}")
            else:
                # Nếu có lỗi, hiển thị thông báo lỗi
                print(f"Lỗi: {result}")
        except Exception as e:
            print(f"Lỗi: {e}")
        finally:
            client.close()
        
        time.sleep(1)

def main():
    parser = argparse.ArgumentParser(description='Chọn chức năng để chạy')
    parser.add_argument('--register', action='store_true', help='Chạy hàm read_register')
    parser.add_argument('--coil', action='store_true', help='Chạy hàm read_coils')
    args = parser.parse_args()

    if args.register:
        read_register()
    elif args.coil:
        read_coils()
    else:
        print("Vui lòng chọn một chức năng để chạy.")

if __name__ == "__main__":
    main()