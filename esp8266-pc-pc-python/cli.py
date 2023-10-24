# Client / Master

import serial, time;

COM_Num       = "COM10";
COM_Baud      = 115200;
COM_Sleep     = 1;       # time to sleep after send data, sec

try:
    COM = serial.Serial(COM_Num, COM_Baud);
    
    if(COM.is_open):
        print("{0}: open success".format(COM_Num));

        while(True):
            Data = "Request {0}".format(int(time.time()));
            COM.write(Data.encode("ascii", "replace"));
            time.sleep(COM_Sleep);
    else:
        print("{0}: open failed".format(COM_Num));

except Exception as e:
    print("Error! {0}".format(e));
