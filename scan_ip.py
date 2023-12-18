from pymodbus.client import ModbusTcpClient
import socket

def scan_modbus_devices():
    # Khai báo một list để lưu trữ các địa chỉ IP của các thiết bị Modbus được tìm thấy
    modbus_devices = []

    # Thiết lập phạm vi IP mà bạn muốn quét, ví dụ: 192.168.1.1 - 192.168.1.255
    subnet = "192.168.1."
    start_range = 1
    end_range = 255

    # Lặp qua tất cả các địa chỉ IP trong phạm vi được chỉ định
    for ip in range(start_range, end_range + 1):
        ip_address = subnet + str(ip)
        print(f"Scanning {ip_address}...")

        try:
            # Kiểm tra kết nối TCP đến cổng Modbus (cổng 502) của địa chỉ IP hiện tại
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Đặt timeout kết nối là 1 giây
            result = sock.connect_ex((ip_address, 502))

            if result == 0:
                # Nếu kết nối thành công, thêm địa chỉ IP vào danh sách thiết bị Modbus
                modbus_devices.append(ip_address)
                print(f"Modbus device found at: {ip_address}")

            sock.close()
        except socket.error:
            pass

    return modbus_devices

# Gọi hàm quét thiết bị Modbus trong mạng và lưu trữ các địa chỉ IP tìm thấy
devices = scan_modbus_devices()

if devices:
    print("Các thiết bị Modbus được tìm thấy trong mạng:")
    for device in devices:
        print(device)
else:
    print("Không tìm thấy thiết bị Modbus trong mạng.")
