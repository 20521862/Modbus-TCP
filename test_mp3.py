import os
import vlc
from vlc import MediaPlayer  
# Xác định đường dẫn tới tệp MP3
FILE =  os.path.abspath(os.path.dirname(__file__)) + "/file/"

# Khởi tạo một instance của MediaPlayer với đường dẫn của tệp MP3
AUDIO: MediaPlayer = MediaPlayer(FILE + "warning.mp3")

# Phát nhạc
AUDIO.play()

# Chờ nghe nhạc trong 10 giây
import time
time.sleep(10)

# Dừng nhạc
AUDIO.stop()
