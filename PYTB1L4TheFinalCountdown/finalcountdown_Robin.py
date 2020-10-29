##countdown from 1000 - 0
import webbrowser
import time

X = 1000;
while X > 0:
    X -= 10
    print(X)
    time.sleep(0.2)
    if X == 0:
        print("Hoera! we zijn van 1000 tot 1")
        webbrowser.open('https://www.youtube.com/watch?v=2Bjy5YQ5xPc')
        break
