import RPi.GPIO as IO

if __name__ == '__main__':

    High_CHANNEL = 27
    
    IO.setwarnings(False)
    IO.setmode(IO.BCM)
    IO.setup(High_CHANNEL, IO.OUT)
    
    '''
    # Software SPI Setup.
    # Setup for Pins to control power is on GPIOPower.py
    CLK  = 22
    MISO = 23
    MOSI = 24
    CS   = 25

    measure = GPIOPower(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
    
    measure.close()
    
    '''
    IO.output(High_CHANNEL, 1)
    
   
    

    
