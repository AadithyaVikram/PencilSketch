#program to make a pencil sketch--developed by AV
print("Welcome to pencil sketch app")
img_location="C:/Users/Aadithya Vikram/Pictures/"
print("WARNING:","check that the given image file is in pictures folder")
c=0
x=1
while(c>=0):
    if c>=1:
        print("type 0(zero) to stop the program; else type any number")
        x=int(input("Do you want to CONTINUE"))
    if x==0:
        print("Thanks for coming")
        break
    else:
        import cv2
        b=input("enter image file name")
        a = b + ".jpg"
        img = cv2.imread(img_location + a)
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        invert = cv2.bitwise_not(grey)
        blur = cv2.GaussianBlur(invert, (21, 21), 0)
        invertedblur = cv2.bitwise_not(blur)
        pencilsketch = cv2.divide(grey, invertedblur, scale=256.0)
        cv2.imshow("pencil sketch", pencilsketch)
        cv2.waitKey(0)
    c+=1