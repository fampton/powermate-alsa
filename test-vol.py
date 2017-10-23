#!/usr/bin/env python

import alsaaudio
import powermate

mixer = alsaaudio.Mixer('Master')

def cur_vol():
    return mixer.getvolume()[0]

def inc_vol(msg):
    if cur_vol() > 98:
        return
    mixer.setvolume(cur_vol()+2)

def dec_vol(msg):
    if cur_vol() < 3:
        return
    mixer.setvolume(cur_vol()-2)

def mute_vol():
    print(mixer.getmute())
    if mixer.getmute()[0] == 0:
        mixer.setmute(1)
    elif mixer.getmute()[0] == 1:
        mixer.setmute(0)

def main():
    print(callable(inc_vol))
    device = powermate.find_wheels()
    my_wheel = powermate.PowerMateWheel(device[0])
    my_wheel.on('turn_right', inc_vol)
    my_wheel.on('turn_left', dec_vol)
    my_wheel.on('press', mute_vol)
    my_wheel.listen()

if __name__ == '__main__':
    main()
