import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial('/dev/ttyAMA0', 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

ser.isOpen()

#print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

input=1
while 1 :
    data = ser.read(36)
    print(data)
    # let's wait one second before reading output (let's give device time to answer)
    time.sleep(1)

