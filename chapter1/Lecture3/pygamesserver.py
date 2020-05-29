#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket, time, sys

def send_data(asocket, data):
    try:
        asocket.send(data)
    except:
        return

def receive_data(asocket):
    try:
        data = asocket.recv(2048)
        return data
    except:
        return

def calculate_score():
	total = 0
	completed = ''
	# num = index of scores list
	for num, point in enumerate(scores):
		total += int(point)
		if int(point) == 1:
			completed += str(num) + ' '
	return 'You have %i point(s), completed questions: %s' %(total, completed)


if len(sys.argv) < 2:
	file = 'questions.data'
else:
	file = sys.argv[1]
file_handler = open(file, 'r')
extracted_data = eval(file_handler.read())
file_handler.close()
scores = [int(0)] * len(extracted_data) # Make a list scores with [0, 0, 0, ...] with len is total questions
server = socket.socket()
server.bind(('', 2811))
server.listen(5)
print '''

               _____                            
              / ____|                           
  _ __  _   _| |  __  __ _ _ __ ___   ___  ___  
 | '_ \| | | | | |_ |/ _` | '_ ` _ \ / _ \/ __| 
 | |_) | |_| | |__| | (_| | | | | | |  __/\__ \ 
 | .__/ \__, |\_____|\__,_|_| |_| |_|\___||___/ 
 | |     __/ |                                  
 |_|    |___/                                   


'''
print 'listening...'

while True:
    try:
        connection, remote = server.accept()
        print 'Connection from ' + str(remote)
        request = receive_data(connection).strip()
    except socket.error:
        print 'Lost connection'
        continue
    except KeyboardInterrupt:
        print '\nKeyboard Interupt from user! Exit...'
        sys.exit(0)
    else:
        print 'Processing request: ' + str(request)
        if request.strip()[:5] == 'score':
            send_data(connection, calculate_score())
            continue
        try:
            item_num = int(request.split('-')[0])
            item_type = str(request.split('-')[1].lower())
        except:
            send_data(connection, 'Invalid request')
            continue
        else:
            if item_num > (len(extracted_data) - 1):
                send_data(connection, 'Invalid question number: ' + str(item_num))
                continue
            if item_type == 'q':
                send_data(connection, extracted_data[item_num][item_type])
                continue
            if item_type == 'i':
                send_data(connection, extracted_data[item_num][item_type])
                continue
            if item_type == 'd':
            	send_data(connection, str(extracted_data[item_num][item_type]))
            	last_request = time.time()
            if item_type == 'a':
            	burned_time = str(time.time() - last_request)
            	print burned_time
            	if time.time() - last_request > 3:
            		send_data(connection, 'Time out. Must send the answer right after received data -' + burned_time)
            		continue
            	if request.count('-') < 2:
            		send_data(connection, 'Invalid answer format!')
            	clientanswer = str(request.split('-')[2])
            	if clientanswer == str(extracted_data[item_num][item_type]):
            		send_data(connection, 'Correct!')
            		scores[int(item_num)] = 1 # assign value 1 instead 0 to target index of scores list
            		continue
            	else:
            		send_data(connection, 'Incorrect!')
            		continue
