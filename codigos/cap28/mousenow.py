# Python Journey - Chapter 28
# Displays the mouse cursor's current position.

import pyautogui
print('Press Ctrl-C to quit.')

try: 
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        position = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixel_color = pyautogui.screenshot().getpixel((x,y))
        position += 'RGB: (' + str(pixel_color[0]).rjust(3)
        position += ', ' + str(pixel_color[1]).rjust(3)
        position += ', ' + str(pixel_color[2]).rjust(3) + ' )'
        print(position, end = '')
        print('\b' * len(position), end='', flush=True)

except KeyboardInterrupt:
    print('\nDone')


