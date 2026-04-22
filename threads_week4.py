import sys
import serial
import threading
from queue import Queue
from collections import deque
import numpy as np
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg

#Shared data queue for serial data
q=Queue()
running = True

#Serial reading thread function
def read_serial(ser, q):
    global running

    while running:
        line_bytes = ser.readline()


        try:
            value = int(line_bytes.decode('utf-8').strip())
            q.put(value)
        except:
            continue
        #Qt App
        app = QtWidgets.QApplication([])

        win = pg.GraphicsLayoutWidget(show=True, title="Real-time Serial Plot")

        # time domain plot
        plot_time = win.addPlot(title="Time Domain")
        curve_raw = plot_time.plot(gen=g)
        #curve_fit = plot_time.plot(pen='r', name="Fitted Curve")
        plot_time.setRange(yRange=[0, 1023])

        #data buffer


        value []

        #Serial setup
        thread.start()


        fs = 200 = Sampling frequency

        def update():
          global data 

          while not q.empty() and count < max_per_update:
              value.append(q.get())
              date.append(value)
              count += 1

            if len(data) > 0:
              curve_raw.setData(data)

              #Timer 
              timer = QtCore.QTimer()
              timer.timeout.connect(update)
              timer.start(20) # Update every 20 ms


#Cleanup on close
def cleanup():
    global running
    running = False
    thread.join()
    ser.close()

    app.aboutToQuit.connect(cleanup)

    #Run 
    sys.exit(app.exec_())

    
