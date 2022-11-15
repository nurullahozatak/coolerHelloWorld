import time

myMessage = "hello world"

alphabet = list("abcdefghijklmnoprqstuvyzxw")

greeting = ""
for i in range(0, len(myMessage)):
    if i == 5:
        greeting = greeting + " "
        print(greeting)
    for j in range(0 , len(alphabet)):

        if myMessage[i] == alphabet[j]:
            print(greeting + alphabet[j])
            greeting = greeting + myMessage[i]
            time.sleep(0.08)
            break
        else:
            print(greeting + alphabet[j])
            time.sleep(0.08)



