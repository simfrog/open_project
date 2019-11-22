from ev3dev.ev3 import*

mB = LargeMottor('outB')
mC = LargeMottor('outC')

#case 1
x = 60
r = 15

#case 2
x = 40
r = 15

#case 3
x = 60
r = 5

#case 4
x = 40
r = 5

#need image size
Center_x = 50
Center_y = 25
Center_r = 10
try:
    while True:
        if (x - Center_x) > 0:
            mB.run_timed(time_sp = 1000, speed_sp = 200)
            mC.stop(stop_action = 'brake')
            if Config_r > r:
                mB.run_timed(position_sp = -360, speed_sp = 100)
                mC.run_timed(position_sp = -360, speed_sp = 100)
            elif Config_r < r:
                mB.run_timed(position_sp = 360, speed_sp = 100)
                mC.run_timed(position_sp = 360, speed_sp = 100)
            else
                mB.stop(stop_action = 'brake')
                mC.stop(stop_action = 'brake')
        elif x-Center_x < 0:
            mB.stop(stop_action = 'brake')
            mC.run_timed(time_sp = 1000, speed_sp = 200)
            if Config_r > r:
                mB.run_timed(position_sp = -360, speed_sp = 100)
                mC.run_timed(position_sp = -360, speed_sp = 100)
            elif Config_r < r:
                mB.run_timed(position_sp = 360, speed_sp = 100)
                mC.run_timed(position_sp = 360, speed_sp = 100)
            else
                mB.stop(stop_action = 'brake')
                mC.stop(stop_action = 'brake')
        else:
            if Config_r > r:
                mB.run_timed(position_sp = -360, speed_sp = 100)
                mC.run_timed(position_sp = -360, speed_sp = 100)
            elif Config_r < r:
                mB.run_timed(position_sp = 360, speed_sp = 100)
                mC.run_timed(position_sp = 360, speed_sp = 100)
            else
                mB.stop(stop_action = 'brake')
                mC.stop(stop_action = 'brake')
except KeyboardInterrupt:
    pass

