from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import time
from PlateauUtil import PlateauUtil

def onAttach():
    print("Attach!")

def onDetach():
    print("Detach!")

class Lecteur:
    #Declare any event handlers here. These will be called every time the associated event occurs.

    def __init__(self):
        #Create your Phidget channels
        self.voltageRatioInput0 = VoltageRatioInput()
        self.voltageRatioInput1 = VoltageRatioInput()
        self.voltageRatioInput2 = VoltageRatioInput()

        #Set addressing parameters to specify which channel to open (if any)
        self.voltageRatioInput0.setChannel(0)
        self.voltageRatioInput1.setChannel(1)
        self.voltageRatioInput2.setChannel(2)

        #Assign any event handlers you need before calling open so that no events are missed.
        #voltageRatioInput0.setOnVoltageRatioChangeHandler(onVoltageRatioChange)
        self.voltageRatioInput0.setOnAttachHandler(onAttach)
        self.voltageRatioInput0.setOnDetachHandler(onDetach)
        #self.voltageRatioInput1.setOnVoltageRatioChangeHandler(onVoltageRatioChange)
        self.voltageRatioInput1.setOnAttachHandler(onAttach)
        self.voltageRatioInput1.setOnDetachHandler(onDetach)
        #voltageRatioInput2.setOnVoltageRatioChangeHandler(onVoltageRatioChange)
        self.voltageRatioInput2.setOnAttachHandler(onAttach)
        self.voltageRatioInput2.setOnDetachHandler(onDetach)

        #Open your Phidgets and wait for attachment
        self.voltageRatioInput0.openWaitForAttachment(5000)
        self.voltageRatioInput1.openWaitForAttachment(5000)
        self.voltageRatioInput2.openWaitForAttachment(5000)


        #Do stuff with your Phidgets here or in your event handlers.
        #initialisation
        rep="O"
        while True:
            rep=input("le plateau est il vide (O/N) ?")
            if rep!="N":
                time.sleep(1)
                m00=self.voltageRatioInput0.getVoltageRatio()*1012000.+56.653
                m10=self.voltageRatioInput1.getVoltageRatio()*998000.-77.127
                m20=self.voltageRatioInput2.getVoltageRatio()*1056000.-67.044
                break
        while True :
            m0=self.voltageRatioInput0.getVoltageRatio()*1012000.+56.653-m00
            m1=self.voltageRatioInput1.getVoltageRatio()*998000.-77.127-m10
            m2=self.voltageRatioInput2.getVoltageRatio()*1056000.-67.044-m20
            mt=m0+m1+m2
            if(mt>1):
                X=6.1*(2*m0-(m1+m2))/mt
                Y=6.1*1.7320508075688772935274463415059*(m1-m2)/mt
            else :
                X=0
                Y=0

            print("m0 = {:.2f}  m1 = {:.2f}  m2 = {:.2f}  mt= {:.2f}".format(m0,m1,m2,mt))
        #    print("position en centimètre X= {:.2f}, Y= {:.2f}".format(position(m0,m1,m2,mt)[0],position(m0,m1,m2,mt)[1]))
            print("X= {:.1f} Y= {:.1f}".format(X,Y))
            print(PlateauUtil.convertir_coordonnées(X, Y))
            time.sleep(1)

        #Close your Phidgets once the program is done.
        voltageRatioInput0.close()
        voltageRatioInput1.close()
        voltageRatioInput2.close()
     