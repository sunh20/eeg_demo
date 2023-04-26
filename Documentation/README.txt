'DSI_to_Python.py' can be used to stream data from DSI-Streamer to Python in real time. 

To use the script, activate the TCP/IP Socket by checking the corresponding checkbox under the TCP IP tab of DSI-Streamer and clicking "Start". Then run the Python script. For file playback, play the recorded file now.

The Python script includes a main TCPParser class which contains the methods for parsing DSI-Streamer Data Packets via TCP/IP Socket and for plotting the data for a given duration.
The Python script is meant to show how to interface DSI-Streamer with Python and should therefore only be used as a sample code.

The sample code is not certified to any specific standard. It is not intended for clinical use.
The sample code and software that makes use of it, should not be used for diagnostic or other clinical purposes.  
The sample code is intended for research use and is provided on an "AS IS"  basis.  
WEARABLE SENSING, INCLUDING ITS SUBSIDIARIES, DISCLAIMS ANY AND ALL WARRANTIES
EXPRESSED, STATUTORY OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY IMPLIED WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT OR THIRD PARTY RIGHTS.

Copyright (c) 2014-2020 Wearable Sensing LLC