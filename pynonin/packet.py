"""
packet.py

(c) Charles Fracchia 2013
charlesfracchia@gmail.com

Permission granted for experimental and personal use;
license for commercial sale available from the author.

Packet class module

This class defines the packet types and operations
"""
import os
import time

#Currently Supported Data Formats
supportedFormats = [2,7,8]

class Packet(object):
    
    def __init__(self, dataFormat, data):
        super(Packet, self).__init__()
        
        if str(dataFormat) not in str(supportedFormats):
            raise AttributeError("ERROR: Format %s is not supported. The library currently supports data formats %s" % (dataFormat, supportedFormats))
        else:
            self.dataFormat = dataFormat
            self.structure = self._setStructure(str(dataFormat))
            data = self._fromFile("personal.txt")
            self.data = self._createFrames(data)
    
    def _setStructure(self, dataFormat):
        """
        Sets the packet structure with frame names according to the data format passed
        Takes dataFormat as integer
        Returns the packetstructure dictionnary with frames populated with name, default value (if applicable) and type
        """
        pass
        
        #bitfield is where the information resides at the bitlevel
        #byte is when the value of the byte contains the information
        #Define some recurrent formats
        startByte =    {'name':'start',    'value':b'\x01',    'type':None}
        statusByte =   {'name':'status',   'value':None,       'type':'bitfield'}
        plethByte =    {'name':'pleth',    'value':None,       'type':'byte'}
        checkByte =    {'name':'check',    'value':None,       'type':'checksum'}
        reservedByte = {'name':'reserved', 'value':None,       'type':None}
        #For DF7#
        plethMSB =     {'name':'plethMSB', 'value':None,       'type':None}
        plethLSB =     {'name':'plethLSB', 'value':None,       'type':None}
        
        packetStructure = {
                        ### DATA FORMAT #2 ###
                        "2":[
                                [startByte, statusByte, plethByte, {'name':'hr_msb',        'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'hr_lsb',        'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'spo2',          'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'srev',          'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, reservedByte, checkByte],
                                [startByte, statusByte, plethByte, {'name':'tmr_msb',       'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'tmr_lsb',       'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'stat2',         'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'spo2-d',        'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'spo2_fast',     'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'spo2_b-b',      'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, reservedByte, checkByte],
                                [startByte, statusByte, plethByte, reservedByte, checkByte],
                                [startByte, statusByte, plethByte, {'name':'e-hr_msb',      'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'e-hr_lsb',      'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'e-spo2',        'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'e-spo2-d',      'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, reservedByte, checkByte],
                                [startByte, statusByte, plethByte, reservedByte, checkByte],
                                [startByte, statusByte, plethByte, {'name':'hr-d_msb',      'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'hr-d_lsb',      'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'e-hr-d_msb',    'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, {'name':'e-hr-d_lsb',    'value':None,    'type':'bitfield'}, checkByte],
                                [startByte, statusByte, plethByte, reservedByte, checkByte],
                                [startByte, statusByte, plethByte, reservedByte, checkByte]
                            ],
                        ### DATA FORMAT #7 ###
                        "7":[
                                [statusByte, plethMSB, plethLSB, {'name':'hr_msb',        'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'hr_lsb',        'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'spo2',          'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'srev',          'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, reservedByte, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'tmr_msb',       'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'tmr_lsb',       'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'stat2',         'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'spo2-d',        'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'spo2_fast',     'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'spo2_b-b',      'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, reservedByte, checkByte],
                                [statusByte, plethMSB, plethLSB, reservedByte, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'e-hr_msb',      'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'e-hr_lsb',      'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'e-spo2',        'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'e-spo2-d',      'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, reservedByte, checkByte],
                                [statusByte, plethMSB, plethLSB, reservedByte, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'hr-d_msb',      'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'hr-d_lsb',      'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'e-hr-d_msb',    'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, {'name':'e-hr-d_lsb',    'value':None,    'type':'bitfield'}, checkByte],
                                [statusByte, plethMSB, plethLSB, reservedByte, checkByte],
                                [statusByte, plethMSB, plethLSB, reservedByte, checkByte]
                            ],
                        ### DATA FORMAT #8 ###
                        "8":[
                                [statusByte,
                                {'name':'hr-d','value':None,'type':'bitfield'},
                                {'name':'spo2-d','value':None,'type':'bitfield'},
                                {'name':'status2','value':None,'type':'bitfield'},
                                ],
                            ],
                    }
        
        return packetStructure[dataFormat]
        
    def _createFrames(self, data):
        """
        Instanciate each frame object for packet with data, uses the Frame class
        Takes raw data
        Returns frame deconvoluted objects
        """
        pass
        
        #Set freezeout for when we find get a valid checksum
        freezeout = 0
        correctBytes=0
        incorrectBytes=0
        
        for index, byte in enumerate(data):
            #print "Byte: %s (%s), Index: %s, Type(Byte): %s, FreezeOut: %s" % (byte,byte.encode('hex'),index,type(byte), freezeout)
            #freeze out operations for 4 bytes if a correct checksum was found previously
            if freezeout == 0:
                #Make frame
                try:
                    frame = [byte,data[index+1],data[index+2],data[index+3],data[index+4]]
                except IndexError:
                    print "ERROR: Data truncated"
                    
                #Convert each byte into correct type (avoid strings)
                for j,frameByte in enumerate(frame):
                    if type(frameByte) == str:
                        frame[j] = int(frameByte.encode('hex'),16)
                        #print "Progressive Frame (%s,%s):%s" % (j,type(frameByte),frame[j])
                #print "Converted frame:%s" % frame
                
                #Verify Checksum
                if self._verifyChecksum(frame):
                    #Set the 4byte freezeout (to make processing faster)
                    correctBytes+=1
                    freezeout = 4
                else:
                    #Reset freezeout
                    incorrectBytes+=1
                    freezeout = 0
                    
            else:
                freezeout-=1
        
        print "Correct: %s | Incorrect Bytes: %s | Total: %s" % (correctBytes,incorrectBytes,len(data))
                
    def _verifyChecksum(self, frameBytes):
        """
        Compute the checksum for a frame and return a boolean for its validity
        Takes the 5 frame bytes
        Returns boolean of whether the checksum is correct
        """
        pass
        #print "Types: %s %s %s %s" % (type(frameBytes[0]),type(frameBytes[1]),type(frameBytes[2]),type(frameBytes[3]))
        
        calc = frameBytes[0]+frameBytes[1]+frameBytes[2]+frameBytes[3]
        hexCalc = hex(calc)
        #DEBUG
        #print "Passed as arg:%s" % (frameBytes)
        #print "Adding up: %s,%s,%s,%s" % (frameBytes[0],frameBytes[1],frameBytes[2],frameBytes[3])
        #print "Calculated Check: 0x%s (%s), Read Checksum: %s (%s)" % (hexCalc[len(hexCalc)-2:],calc,hex(frameBytes[4]),frameBytes[4])
        
        if hexCalc[len(hexCalc)-2:] == hex(frameBytes[4])[2:]:
            return True
        else:
            return False
            
    def _toBitfield(self, n):
        """
        Compute the bitfield of an integer and return it
        Takes integer
        Returns list of bits
        """
        pass
        return [int(digit) for digit in bin(n)[2:]]
    
    def _fromFile(self, filename):
        """
        Reads a sample file of oximeter data
        """
        pass
        print "Opening data file..."
        file = open(filename,'rb')
        data = file.read()
            
        if len(data) > 0:
            print "Finished reading file"
            file.close()
            return data
        else:
            print "ERROR: Read 0 bytes from the file"
    
    def _fromSerial(self):
        """
        Connects to the device's serial port and retrieves data
        """
        pass