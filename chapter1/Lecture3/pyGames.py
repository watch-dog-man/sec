import socket

def send_data(asocket, data):
    asocket.send(data)

def receive_data(asocket):
    try:
        data = asocket.recv(2048)
        return data
    except:
        return

class game():
    '''pyGames - Python Challenges for Students

I. Introduction:

pyGames is an online game that included many interested challenges. The challenges are numbered beginning at 0 and increase to more than 45 challenges.
They get difficult as the question number increases. The first 20-30 challenges are not scenario-specifix. Instead, they test or teach the player essential Python
skills and develop the essential skills that player will require. The second half of the pyGames challenges simulate challenges that I and orther security professionals
have faced in real-world scenarios.

pyGames include 5 methods listed below:
    - score()
    - information()
    - question()
    - data()
    - answer()

II. Rules:

1. Player have only 3 seconds between the time request data and submit answer
2. Sumitting an answer more than once does not score more than on point
3. Play respect. No cheating. No spoofing. Answer your question as you
4. NO hacking the scoring server !!!

III. Methods:
    '''
    serverip = '127.0.0.1'
    serverport = 2811

    def score(self):
        """This method prints the current scoreboard.  Example >>> print gameobject.score()"""
        connection = socket.socket()
        connection.connect((self.serverip, self.serverport))
        try:
            send_data(connection, 'score')
            data_server = receive_data(connection)
            connection.close()
            return data_server
        except:
            print 'please try again!'

    def information(self, number):
        '''This method used to get information about a question. This method will takes one argument.
The argment must be an integer of the question number you want to read.
For example, to see information about questioni number 0, Let's type:  >>> gameobject.information(0)'''
        connection = socket.socket()
        connection.connect((self.serverip, self.serverport))
        try:
            send_data(connection, str(number).strip() + '-i')
            #data_server - data from server
            data_server = receive_data(connection)
            connection.close()
            return data_server
        except:
            print 'Please try again!'
        
    def question(self, number):
        '''Use this method to read a question.  It takes one argument.
The argment must be an integer of the question number you want to read.
For example, to see question number 0 you would do this:  >>> gameobject.question(0)'''
        connection = socket.socket()
        connection.connect((self.serverip, self.serverport))
        try:
            send_data(connection, str(number).strip() + '-q')
            #data_server - data from server
            data_server = receive_data(connection)
            connection.close()
            return data_server
        except:
            print 'Please try again!'

    def data(self, number):
        '''This method will give you the data for a given question that you are supposed to manipulate.
This method takes one argument.  That argument is an integer for the data element you want to retrieve.
For example, the data element of question one is retrieved by executing >>> gameobject.data(0)
For many functions this is a dynamic element and it changes every time you query it.
You will typically pass the data returned by this method to a function that will calculate the answer to the question so you can submit it to answer.'''
        connection = socket.socket()
        connection.connect((self.serverip, self.serverport))
        try:
            send_data(connection, str(number).strip() + '-d')
            #data_server - data from server
            data_server = receive_data(connection)
            connection.close()
            if 'Invalid question mumber' in data_server:
                return data_server
            try:
                data_server = int(data_server)
            except:
                pass
            if type(data_server) != str:
                return data_server
            if data_server[0] == '[' and data_server[-1] == ']':
                data_server = eval(data_server)
            elif data_server[0] == '{' and data_server[-1] == '}':
                data_server = eval(data_server)
            elif data_server[0] == '(' and data_server[-1] == ')':
                data_server = eval(data_server)
            return data_server
        except:
            print 'Please try again!'

    def answer(self, number, myanswer):
        '''This method is used to submit an answer.  It takes two arguments.
The first argument is an integer for the question you are answering and the second is the answer.
Typically you will submit the answer by calling a function that calculates the answer based on the data element.
For example, after writing 'solvenum0()'  you would submit your answer by calling >>> gameobject.answer(0, solvenum1(gameobject.data(0)))'''
        connection = socket.socket()
        connection.connect((self.serverip, self.serverport))
        try:
            send_data(connection, str(number).strip() + '-a-' + str(myanswer))
            #data_server - data from server
            data_server = receive_data(connection)
            connection.close()
            return data_server
        except:
            print 'Please try again!'
