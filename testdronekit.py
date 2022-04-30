from dronekit import connect
import time
import numpy
vehicle = connect('com13',wait_ready = True)
def main():
    try:
        while True:
            time.sleep(1)
            n = vehicle.attitude.roll
            print "attitude : ", vehicle.attitude.roll
    except KeyboardInterrupt:
        print "Finished"

if __name__ == "__main__":
    main()