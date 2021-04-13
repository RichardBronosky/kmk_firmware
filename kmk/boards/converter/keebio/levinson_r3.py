import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation

""" From REPL
>>> import board
>>> dir(board)
[
    '__class__', 'A0', 'A1', 'A2', 'A3', 'GP0', 'GP1', 'GP10', 'GP11', 'GP12',
    'GP13', 'GP14', 'GP15', 'GP16', 'GP17', 'GP18', 'GP19', 'GP2', 'GP20',
    'GP21', 'GP22', 'GP25', 'GP26', 'GP26_A0', 'GP27', 'GP27_A1', 'GP28',
    'GP28_A2', 'GP3', 'GP4', 'GP5', 'GP6', 'GP7', 'GP8', 'GP9', 'LED',
    'SMPS_MODE', 'VOLTAGE_MONITOR'
]
 """

class KMKKeyboard(_KMKKeyboard):
    col_pins = tuple(
        getattr(board, "GP{}".format(p)) for p in [
            7,  8,  9,  1, 26, 29,
            1, 29, 26, 22, 20, 23,
        ]
    )
    row_pins = tuple(
        getattr(board, "GP{}".format(p)) for p in [
            4, 23, 20, 22,
            4,  7,  8,  9,
        ]
    )
    diode_orientation = DiodeOrientation.COLUMNS

    split_type = 'UART'
    split_flip = False
    split_offsets = [6, 6, 6, 6]
    uart_pin = board.SCL
    extra_data_pin = board.SDA
    rgb_pixel_pin = board.TX
    # led_pin = board.D7
