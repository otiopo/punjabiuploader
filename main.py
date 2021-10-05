import requests, pyperclip, time, os
from PIL import ImageGrab
from tkinter import *

def showOutput(y1, y2, y3, y4):
    image = ImageGrab.grab(bbox=(int(y1),int(y2),int(y3),int(y4)))
    image.save("test.png", "PNG")
    os.system("test.png")

def screenshotFunc(y1, y2, y3, y4, tim):
    time.sleep(int(tim))
    image = ImageGrab.grab(bbox=(int(y1),int(y2),int(y3),int(y4)))
    image.save("test.png", "PNG")

    with open("test.png", "rb") as file:
        pyperclip.copy(requests.post("https://punjabiuploader.otiopo.repl.co/uploadImage", files={"file": file.read()}).text)
        file.close()

    print("done!")

screen = Tk()
screen.title("Punjabi Uploader")
screen.geometry("259x150")
screen.wm_iconbitmap(PhotoImage("PUNJABI.ico"))
part1 = Entry(screen)
part1.pack()
part2 = Entry(screen)
part2.pack()
part3 = Entry(screen)
part3.pack()
part4 = Entry(screen)
part4.pack()
timer = Entry(screen)
timer.pack()
screenshot = Button(screen,text="SCEENSHOT!",command=lambda:screenshotFunc(part1.get(), part2.get(), part3.get(), part4.get(), timer.get()))
screenshot.pack()
output = Button(screen,text="Show Output",command=lambda:showOutput(part1.get(), part2.get(), part3.get(), part4.get()))
output.pack()
screen.mainloop()
