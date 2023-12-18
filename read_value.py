import time

from pymodbus.client import ModbusTcpClient                                
from pymodbus.exceptions import ModbusException, ModbusIOException          
from pymodbus.register_read_message import ReadHoldingRegistersResponse 

def read_value():
    # Khởi tạo client Modbus TCP
    client = ModbusTcpClient('192.168.93.85')  # Thay đổi địa chỉ IP của PLC của bạn
    client.connect()
    #while True:
    try:
        while True:
        # Đọc 12 thanh ghi từ địa chỉ 0 của PLC với đơn vị là 1
            result = client.read_holding_registers(address=0, count=12, unit=1)  # Thay đổi địa chỉ unit của PLC của bạn
            result_coils = client.read_coils(address=0, count=12, unit=1)
            if not result.isError():
                # Nếu không có lỗi, hiển thị giá trị đọc được từ 12 thanh ghi
                registers = result.registers
                coils = result_coils.bits
                print(f"Giá trị đọc từ 12 thanh ghi: {registers}")
                print(f"Giá trị đọc từ coils: {coils}")
            else:
                # Nếu có lỗi, hiển thị thông báo lỗi
                print(f"Lỗi: {result}")
            time.sleep(1)
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        client.close()
        


if __name__ == "__main__":
    read_value()