# Server / Slave

import serial, time;

COM_Num       = "COM4";
COM_Baud      = 115200;
COM_Tieout    = 0.5;     # read timeot, sec
COM_DataMaxSz = 100;     # read buffer, max size

try:
    COM = serial.Serial(COM_Num, COM_Baud, timeout=COM_Tieout);
    
    if(COM.is_open):
        print("{0}: open success".format(COM_Num));

        while(True):
            Data = COM.read(COM_DataMaxSz);
            if(len(Data) > 0):
                print(Data.decode("ascii", "replace"));
    else:
        print("{0}: open failed".format(COM_Num));

except Exception as e:
    print("Error! {0}".format(e));
