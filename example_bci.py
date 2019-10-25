from pyOpenBCI import OpenBCICyton

board = OpenBCICyton(port='/dev/tty.usbserial-DM01N5XP')
uVolts_per_count = (4500000)/24/(2**23-1) #uV/count
accel_G_per_count = 0.002 / (2**4) #G/count

def print_raw(sample):
    print(sample.channels_data)

board.start_stream(print_raw)
