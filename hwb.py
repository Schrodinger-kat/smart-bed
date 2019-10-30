import time
import Sruthi.heartBeats
import Sruthi.watersensor2

def Calibration():
    print("\nSensor Calibration Values , pay no ruse ")
    for i in range(5):
        k = Sruthi.heartBeats.bpm()
        i = Sruthi.watersensor2.loop()
    time.sleep(5)
    print("\nCalibration Done")

def blah():
    BPM = Sruthi.heartBeats.bpm()
    WaterAlert = Sruthi.watersensor2.loop()
    print("\nPatients Heart Rate : ")
    if BPM < 100:
        print("Critical: Heart Rate Low")
    elif BPM > 200:
        print("Critical: Heart Rate high")
    else:
        print("Heart Rate Normal")

    print("Bed Wet or something:")
    if WaterAlert:
        print(Liquid Detected)
    else:
        print("No Liquid Presence")

def loop():
    Calibration()
    blah()
if __name__=='__main__':
    try:
        loop()
    except KeyboardInterrupt:
        pass
