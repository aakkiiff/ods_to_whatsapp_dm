import pywhatkit
minute_to_send = 00
hour_to_send = 00
numbersFileName="numbers.txt"
numbers=[]
msg="Hello, this is a automated message from python"

def Numbers_file_to_list(x):
    with open(numbersFileName, 'r') as fp:
        for i in fp:
            x=i[:-1]
            numbers.append(x)

def sendMsg(numbers,msg,min,hr):
    Numbers_file_to_list(numbers)
    for i in numbers:
        print(i)
        pywhatkit.sendwhatmsg(f"+880{i}",msg,hr,min,2)
        min+=1
    
sendMsg(numbers,msg,minute_to_send,hour_to_send)
