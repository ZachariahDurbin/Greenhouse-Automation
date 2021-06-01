from django.shortcuts import render

# Create your views here.
import pyfirmata
import time



from django.http import HttpResponse

def index(request):
    print("entered index function")
    board = pyfirmata.Arduino('com3')
    while True:
        board.digital[13].write(1)
        print("light on")
        time.sleep(1)
        board.digital[13].write(0)
        print("light off")
