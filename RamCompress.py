import datetime
def pause():
    input("Please press enter. . .")
def main():
    try:
        print("本软件使用CPU和内存,极限压缩内存,还可以烤机!")
        pause()
        sjs = datetime.datetime.now().strftime("%S")
        sjm = datetime.datetime.now().strftime("%M")
        sjm = sjm * 60
        sjh = datetime.datetime.now().strftime("%H")
        sjh = sjh * 3600
        zsj = sjs + sjm
        bkf = zsj
        bkf = int(bkf)
        i = 2
        ii = 1
        iii = 0
        while True:
            i = i * i
            iii = iii + 1
            ii = ii + iii
            sjs = datetime.datetime.now().strftime("%S")
            sjm = datetime.datetime.now().strftime("%M")
            sjm = sjm * 60
            zsj = sjs + sjm
            zsj = int(zsj)
            speed = zsj - bkf
            speed = speed / 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            if i == 0:
                pass
            print("正在整理内存",ii,"RAM","Speed:",speed)
            if speed < 0:
                print("SpeedError:Time error")
            bkf = zsj
            bkf = int(bkf)
    except MemoryError:
        print("整理完成")
if __name__ == '__main__':
    main()
