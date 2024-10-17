
import time
from math import ceil,floor
def net_price(time,discount,price):
    return price*(1-discount)*time

def count(x):
    start = 0
    end = x * 60
    for i in range(end,start,-1):
        phut = floor(i/60)
        giay = i - phut*60
        print(f"{phut:02}:{giay:02}")
        time.sleep(1)

print(f"Bạn đã chơi 8 tiếng, tổng số tiền là {net_price(8,0.20,8000)}")
print(f"Bạn còn 15 phút là hết giờ chơi game")
count(15)
