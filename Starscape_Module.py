

@author: SAYAN CHAKI
"""
import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
from PIL import Image  
import PIL

def onbrightness():



 img =cv2.imread("ESO.jpg")
 gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

 ret, thresh=cv2.threshold(gray,0,255 ,cv2.THRESH_BINARY)
 f=1

 while f :
  fix=int(input("enter integer to fix threshold: "))
  if 0<fix<255:
   ret, thresh2=cv2.threshold(gray, fix, 255,cv2.THRESH_BINARY)
   f=0
  else:
     print("Wrong threshold value")
    
    
 print(ret)


 plt.figure("BINARY")
 plt.imshow(thresh2, cmap="gray")
 plt.show()

 contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


 maxc = -1
        
 for i in range(len(contours)):
             area = cv2.contourArea(contours[i])
             if area>maxc:
                 maxc = area
 minc=maxc
 print(maxc)
       
 for i in range(len(contours)):
             area = cv2.contourArea(contours[i])
             if area<minc:
                 minc = area
 print(minc)
 c=int(input("Enter upper parameter to fix range: "))
 d=int(input("Enter lower parameter to fix range: "))
 up=(maxc+minc)/c
 low=(maxc+minc)/d
 print(up,low)
 for i in range(len(contours)):
             area = cv2.contourArea(contours[i])
             if low<area<=up:
                 img=cv2.drawContours(img,contours[i],-1,(0,225,0),5)
 
 plt.imshow(img)
 plt.show()
 cv2.imwrite('Eso_bright.jpg',img)

def shiftbased():
    img =cv2.imread("ESO.jpg")
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    shift=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    red_lower = np.array([136, 87, 111], np.uint8) 
    red_upper = np.array([180, 255, 255], np.uint8) 
    red_mask = cv2.inRange(shift, red_lower, red_upper)
    kernal = np.ones((5, 5), "uint8") 
    print(red_mask)
      
    # For red color 
    red_mask = cv2.dilate(red_mask, kernal) 
    res_red = cv2.bitwise_and(img, img,  
                              mask = red_mask)
    contours, hierarchy = cv2.findContours(red_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
    c=0
    for i in range(len(contours)): 
        area = cv2.contourArea(contours[i]) 
        if(area > 10): 
            img1=cv2.drawContours(img1,contours[i],-1,(0,225,0),5) 
            c=c+1
    print("The Count of number of red shifted stars is: ")          
    print(c)
    plt.imshow(img1)
    plt.show()
    cv2.imwrite('Eso_shift.jpg',img1)

def temperaturedatabase():
    
    kelvin_table = {
    1000: (255, 56, 0),
    1100: (255, 71, 0),
    1200: (255, 83, 0),
    1300: (255, 93, 0),
    1400: (255, 101, 0),
    1500: (255, 109, 0),
    1600: (255, 115, 0),
    1700: (255, 121, 0),
    1800: (255, 126, 0),
    1900: (255, 131, 0),
    2000: (255, 138, 18),
    2100: (255, 142, 33),
    2200: (255, 147, 44),
    2300: (255, 152, 54),
    2400: (255, 157, 63),
    2500: (255, 161, 72),
    2600: (255, 165, 79),
    2700: (255, 169, 87),
    2800: (255, 173, 94),
    2900: (255, 177, 101),
    3000: (255, 180, 107),
    3100: (255, 184, 114),
    3200: (255, 187, 120),
    3300: (255, 190, 126),
    3400: (255, 193, 132),
    3500: (255, 196, 137),
    3600: (255, 199, 143),
    3700: (255, 201, 148),
    3800: (255, 204, 153),
    3900: (255, 206, 159),
    4000: (255, 209, 163),
    4100: (255, 211, 168),
    4200: (255, 213, 173),
    4300: (255, 215, 177),
    4400: (255, 217, 182),
    4500: (255, 219, 186),
    4600: (255, 221, 190),
    4700: (255, 223, 194),
    4800: (255, 225, 198),
    4900: (255, 227, 202),
    5000: (255, 228, 206),
    5100: (255, 230, 210),
    5200: (255, 232, 213),
    5300: (255, 233, 217),
    5400: (255, 235, 220),
    5500: (255, 236, 224),
    5600: (255, 238, 227),
    5700: (255, 239, 230),
    5800: (255, 240, 233),
    5900: (255, 242, 236),
    6000: (255, 243, 239),
    6100: (255, 244, 242),
    6200: (255, 245, 245),
    6300: (255, 246, 247),
    6400: (255, 248, 251),
    6500: (255, 249, 253),
    6600: (254, 249, 255),
    6700: (252, 247, 255),
    6800: (249, 246, 255),
    6900: (247, 245, 255),
    7000: (245, 243, 255),
    7100: (243, 242, 255),
    7200: (240, 241, 255),
    7300: (239, 240, 255),
    7400: (237, 239, 255),
    7500: (235, 238, 255),
    7600: (233, 237, 255),
    7700: (231, 236, 255),
    7800: (230, 235, 255),
    7900: (228, 234, 255),
    8000: (227, 233, 255),
    8100: (225, 232, 255),
    8200: (224, 231, 255),
    8300: (222, 230, 255),
    8400: (221, 230, 255),
    8500: (220, 229, 255),
    8600: (218, 229, 255),
    8700: (217, 227, 255),
    8800: (216, 227, 255),
    8900: (215, 226, 255),
    9000: (214, 225, 255),
    9100: (212, 225, 255),
    9200: (211, 224, 255),
    9300: (210, 223, 255),
    9400: (209, 223, 255),
    9500: (208, 222, 255),
    9600: (207, 221, 255),
    9700: (207, 221, 255),
    9800: (206, 220, 255),
    9900: (205, 220, 255),
    10000: (207, 218, 255),
    10100: (207, 218, 255),
    10200: (206, 217, 255),
    10300: (205, 217, 255),
    10400: (204, 216, 255),
    10500: (204, 216, 255),
    10600: (203, 215, 255),
    10700: (202, 215, 255),
    10800: (202, 214, 255),
    10900: (201, 214, 255),
    11000: (200, 213, 255),
    11100: (200, 213, 255),
    11200: (199, 212, 255),
    11300: (198, 212, 255),
    11400: (198, 212, 255),
    11500: (197, 211, 255),
    11600: (197, 211, 255),
    11700: (197, 210, 255),
    11800: (196, 210, 255),
    11900: (195, 210, 255),
    12000: (195, 209, 255)}
    
    kelvin_list = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900,
               2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900,
               3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900,
               4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900,
               5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900,
               6000, 6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900,
               7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900,
               8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900,
               9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900,
               10000, 10100, 10200, 10300, 10400, 10500, 10600, 10700, 10800, 10900,
               11000, 11100, 11200, 11300, 11400, 11500, 11600, 11700, 11800, 11900,
               12000]
    
    upper_star_temp=int(input("Enter the upper temperature"))
    lower_star_temp=int(input("Enter the lower temperature"))
    
    
    temp1=kelvin_table[lower_star_temp]
    lower_red,lower_green,lower_blue=temp1
    temp2=kelvin_table[upper_star_temp]
    upper_red,upper_green,upper_blue=temp2
    print(upper_red)
    print(upper_blue)
    print(upper_green)
    
    ut=np.array([upper_red,upper_green,upper_blue],np.uint8)
    lt=np.array([lower_red,lower_green,lower_blue],np.uint8)
    print("The RGB range for the corresponding temperature range is: ")
    print(lt)
    print(ut)
       

    
def hubble():
    img=cv2.imread("ESO.jpg")
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    gray =cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    ret,bina=cv2.threshold(gray,250,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(bina, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    maxc = -1
        
    for i in range(len(contours)):
             area = cv2.contourArea(contours[i])
             if area>maxc:
                 maxc = area
    minc=maxc
    print(maxc)
       
    for i in range(len(contours)):
             area = cv2.contourArea(contours[i])
             if area<minc:
                 minc = area
    print(minc)
    c=0
    up=(maxc+minc)/1  
    low=(maxc+minc)/2
    print(up,low)
    for i in range(len(contours)):
             carea = cv2.contourArea(contours[i])
             if low<carea<=up:
                 img=cv2.drawContours(img,contours[i],-1,(0,225,0),5)
                 c=c+1
                 
    
    M=cv2.moments(c)
    print(M)
    
    
    r,g,b=(img1[200,400])
    print(r)
    print(g)
    print(b)
    plt.imshow(img1)
    plt.show()
    
def bv2rgb(bv):
    if bv < -0.40: bv = -0.40
    if bv > 2.00: bv = 2.00

    r = 0.0
    g = 0.0
    b = 0.0

    if  -0.40 <= bv<0.00:
        t=(bv+0.40)/(0.00+0.40)
        r=0.61+(0.11*t)+(0.1*t*t)
    elif 0.00 <= bv<0.40:
        t=(bv-0.00)/(0.40-0.00)
        r=0.83+(0.17*t)
    elif 0.40 <= bv<2.10:
        t=(bv-0.40)/(2.10-0.40)
        r=1.00
    if  -0.40 <= bv<0.00:
        t=(bv+0.40)/(0.00+0.40)
        g=0.70+(0.07*t)+(0.1*t*t)
    elif 0.00 <= bv<0.40:
        t=(bv-0.00)/(0.40-0.00)
        g=0.87+(0.11*t)
    elif 0.40 <= bv<1.60:
        t=(bv-0.40)/(1.60-0.40)
        g=0.98-(0.16*t)
    elif 1.60 <= bv<2.00:
        t=(bv-1.60)/(2.00-1.60)
        g=0.82-(0.5*t*t)
    if  -0.40 <= bv<0.40:
        t=(bv+0.40)/(0.40+0.40)
        b=1.00
    elif 0.40 <= bv<1.50:
        t=(bv-0.40)/(1.50-0.40)
        b=1.00-(0.47*t)+(0.1*t*t)
    elif 1.50 <= bv<1.94:
        t=(bv-1.50)/(1.94-1.50)
        b=0.63-(0.6*t*t)

    return (r*255, g*255, b*255)
    
def color():
        img=cv2.imread("ESO.jpg")
        img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img
        plt.imshow(img1)
        plt.show()
        rx,gx,bx=img1[75,80]
        
        up_temp=int(input("Enter the upper temperature limit"))
        up_temp=up_temp-1500
        low_temp=int(input("Enter the lower temperature limit"))
        low_temp=low_temp-1500
        BVU=((math.sqrt((math.pow(2.13506*up_temp-(1.84*4600), 2))-3.3856*up_temp*(1.054*up_temp-2.32*4600)))-(2.13506*up_temp-8464))/(1.6928*up_temp)
        BVL=((math.sqrt((math.pow(2.13506*low_temp-(1.84*4600), 2))-3.3856*low_temp*(1.054*low_temp-2.32*4600)))-(2.13506*low_temp-8464))/(1.6928*low_temp)
        rl,gl,bl=bv2rgb(BVL)
        r2,g2,b2=bv2rgb(BVU)
        up=np.array([r2,g2,b2],np.uint8)
        low=np.array([rl,gl,bl],np.uint8)
        rows,cols=img.shape[:2]
        c=0
        print(up)
        print(low)
        maxr=max(rl,r2)
        maxb=max(bl,b2)
        maxg=max(gl,g2)
       
        minr=min(rl,r2)
        ming=min(gl,g2)
        minb=min(bl,b2)
        print("max r= ")
        print(maxr)
        print("min r= ")
        print(minr)
        k=int(input("Enter 1 if you want to plot data with calibrated system and 0 otherwise"))
        if(k):
         print("Calibrating System corresponding to obtained image")
         minr,ming,minb=calibrate(minr,ming,minb)
         maxr,maxg,maxb=calibrate(maxr, maxg, maxb)
         print("max r= ")
         print(maxr)
         print("min r= ")
         print(minr)
         maxr=int(max(maxr,minr))
         maxb=int(max(maxb,minb))
         maxg=int(max(maxg,ming))
        
         minr=int(min(maxr,minr))
         minb=int(min(maxb,minb))
         ming=int(min(maxg,ming))
        else:
            print("You have chosen to obtain data without calibrating the system")
            
        for i in range(rows):
            for j in range(cols):
                x,y,z=img1[i,j]
                if minr<=x<=maxr and ming<=y<=maxg and minb<=z<=maxb:
                    img1[i:i+25,j:j+25]=(0,255,0)
                    c=c+1
                    
        
        print(c)      
        plt.imshow(img1)
        plt.show()
        cv2.imwrite('Eso_temperature.jpg',img1)
def interpolate(x1,y1,x2,y2,z):
     newz=((z-x1)*y1)/(x2-x1) +  ((z-x2)*y2)/(x1-x2)
     return newz
  
        
def calibrate(r,g,b):
    
    img=cv2.imread("ZOOM.jpg")
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img1)
    plt.show()      
    
    rows,cols=img.shape[:2]
    img2=cv2.imread("m54.jpg")
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    plt.imshow(img2)
    plt.show()    
    BV1=float(input("Enter the BV index of the star to callibarate the software"))
    rc1,gc1,bc1=bv2rgb(BV1)
    ri1,gi1,bi1=img1[58,60]
    BV2=float(input("Enter the BV index of the second star to callibarate the software"))
    rc2,gc2,bc2=bv2rgb(BV2)
    ri2,gi2,bi2=img2[18,18]
    
    plt.imshow(img1)
    plt.show()
    print(rc1)
    print(ri1)
    n_r=interpolate(rc1,ri1,rc2,ri2,r)
    n_g=interpolate(gc1,gi1,gc2,gi2,g)
    n_b=interpolate(bc1,bi1,bc2,bi2,b)
    print(r)
    print(n_r)
    return(n_r,n_g,n_b)
    
        
def main():
    f=1
    while(f):
     print("Welcome to the Starscape Module!")
     print("Based on your image data we'll help you perform three operations: ")
     print("1. We'll help you track stars based on apparent brightness based on your range.")
     print("2. We'll help you track stars based on their redshift.")
     print("3. You may access our temperature database corresponding to RGB gradient values.")
     print("4. We'll allow you to plot stars based on your image within specific temperature range")
     print("5. You max exit the module.")
     c=int(input("Enter your choice"))
     if c==1:
         onbrightness()
     elif c==2:
         shiftbased()
     elif c==3:
         temperaturedatabase()
     elif c==4:
         print("You shall be asked to calibrate your system based on yur image")
         print("Choose to calibrate the system if you know the BV index of atleast two stars in the system")
         print("Else proceed without Calibration.")
         color()
     elif c==5:
         f=0
         print("Exiting the module")
         break
     else:
         print("Wrong Input, Try again!")
         
    if f==0:
        print("Thank You for using the starscape module!")
    return 0
     
    
if __name__ == "__main__":
    main()
