from modules.RFID.RFID import *
from modules.RF.Loop import *
from modules.Finger.Search import *
import serial



def Finger_loop():
    uart = ""
    try:
        uart = PyFingerprint('/dev/ttyS1', 115200, 0xFFFFFFFF, 0x00000000)

        if ( uart.verifyPassword() == False ):
            raise ValueError('Указан неверный пароль датчика отпечатка пальца!')

    except Exception as e:
        print('Датчик отпечатка пальца не может быть инициализирован!')
        print('Сообщение об исключении: ' + str(e))
        exit(1)

    while True:
        Read_finger(uart)




def Rfid_loop():
    uart =""
    try:
        uart = serial.Serial("/dev/ttyS2", baudrate=9600, timeout=3000)
    except Exception as e:
        print('RFID считыватель не может инициализироваться!')

    print("loop")
    while True:
        Read_uid(uart)



def RF_loop():
    while True:
        RF_run()
