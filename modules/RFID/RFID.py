import serial
import time

Tag1 = str('22009C45F40F')
uart = serial.Serial("/dev/ttyS2", baudrate=9600, timeout=3000)

print "OK"
while True:
    ID = ""
    read_byte = uart.read()
    if read_byte=="\x02":
        for Counter in range(12):
            read_byte=uart.read()
            ID = ID + str(read_byte)
            print hex(ord( read_byte))
        print ID
        if ID == Tag1:
            print "matched"
            time.sleep(5)
        else:
            print "Access Denied"
            time.sleep(5)
            uart.flushInput()
