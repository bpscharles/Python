#Telit Extensions
#
#Copyright 2012, Telit Communications S.p.A.
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without 
#modification, are permitted provided that the following conditions 
#are met:
#
#Redistributions of source code must retain the above copyright notice, 
#this list of conditions and the following disclaimer.
#
#Redistributions in binary form must reproduce the above copyright 
#notice, this list of conditions and the following disclaimer in 
#the documentation and/or other materials provided with the distribution.
#
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS ``AS
#IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
#TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
#PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR
#CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
import time
import serial

#print "MDM start"
mdmser = serial.Serial('COM1', 115200, timeout=0, rtscts=1)

#print "getCTS"
i = 5
while i > 0:
  i = i -1
  if mdmser.getCTS():
    i = -1
  else:
    time.sleep(1)

if i == 0:
  print "WARNING: The module seems not connected! Please Verify that it's connected and Turned ON"
  mdmser.close()
  del mdmser
  raise StandardError, 'ERROR: The module seems not connected!'

#print "ATE0"
mdmser.write('ATE0\r')
timeMaxATE0 = time.time() + 4.0
#print "read"
resATE0 = ''
while resATE0.find('OK\r') == -1 and time.time() < timeMaxATE0:
  resATE0 = resATE0 + mdmser.read(6)
#print resATE0
if resATE0.find('OK\r') == -1:
  #print "ATE0"
  mdmser.write('ATE0\r')
  timeMaxATE0 = time.time() + 4.0
  #print "read"
  resATE0 = ''
  while resATE0.find('OK\r') == -1 and time.time() < timeMaxATE0:
    resATE0 = resATE0 + mdmser.read(6)
  #print resATE0
if resATE0.find('OK\r') == -1:
  print "ERROR: The module is not responding!"
  mdmser.close()
  del mdmser  
  raise StandardError, 'ERROR: The module is not responding!'
else:
  mdmser.flushInput()

def send(string, timeout):
  global mdmser
  mdmser.write(string)
  result = 1
  return result

def sendavail():
  return 4096

def read():
  global mdmser
  string = mdmser.read(512)
  return string

def sendbyte(byte, timeout):
  global mdmser
  string = chr(byte)
  mdmser.write(string)
  result = 1
  return result

def readbyte():
  global mdmser
  string = mdmser.read(1)
  if string == '':
    result = -1
  else:
    result = ord(string)
  return result

def getDCD():
  global mdmser
  cd = mdmser.getCD()
  if cd == False:
    result = 0
  else:
    result = 1
  return result

def getCTS():
  global mdmser
  cts = mdmser.getCTS()
  if cts == False:
    result = 0
  else:
    result = 1
  return result

def getDSR():
  global mdmser
  dsr = mdmser.getDSR()
  if dsr == False:
    result = 0
  else:
    result = 1
  return result

def getRI():
  global mdmser
  ri = mdmser.getRI()
  if ri == False:
    result = 0
  else:
    result = 1
  return result

def setRTS(rts):
  global mdmser
  if rts == 0:
    print 'dummy setRTS(0)'
#    mdmser.setRTS(level=0)
  else:
    print 'dummy setRTS(1)'
#    mdmser.setRTS(level=1)
  return

def setDTR(dtr):
  global mdmser
  if dtr == 0:
    print 'dummy setDTR(0)'
#    mdmser.setDTR(level=0)
  else:
    print 'dummy setDTR(1)'
#    mdmser.setDTR(level=1)
  return

