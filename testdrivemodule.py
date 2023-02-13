import motors as mot
import keyboardmodule as km

km.init()

while True:
    if km.getKey('w'):
        print('forward')
        mot.forward(50)
    elif km.getKey('s'):
        print('backward')
        mot.backward(80)
    elif km.getKey('q'):
        print('fleft')
        mot.fleft(80)
    elif km.getKey('e'):
        print('fright')
        mot.frontright()
    elif km.getKey('a'):
        print('bleft')
        mot.bright(100)
    elif km.getKey('d'):
        print('bright')
        mot.bleft(100)
    else:
        mot.stop()
