# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import cv2
# importing OpenCV as cv2 to read the image

import pandas as pd
# importing Pandas as pd to read the csv file

import math
# importing math module for different math operations

# import os.path
from os import path

# used to detect whether the entered file name is valid or not

global my_colors


# declared as global so that it is accessible to all functions.


def click_event(event, x, y, flags, params):
    # the event is registered on left click
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        '''
            using the coordinates of the point clicked the b,g,r values(0-255)
            of that particilar point is saved into b,g,r variables
        '''
        # print(type(b))

        b = int(b)
        g = int(g)
        r = int(r)
        # converted into integer variable from a numpy integer

        # print(b,g,r)

        find_color_name(r, g, b)
        # the function my_color_name is called to know the name of the color.


def find_color_name(r, g, b):
    '''
        this function finds the name of the color using r,g,b values got
        from click_event function and the csv file read using pandas
    '''


    minm = (r - my_colors.loc[0, 'R']) * 2 + (g - my_colors.loc[0, 'G']) * 2 + (b - my_colors.loc[0, 'B']) ** 2
    minm = math.sqrt(minm)
    color = my_colors.loc[0, 'a']
    # the minm variable is initialized with the difference between colour of clicked portion and colour at index 0 in csv file

    for i in range(1, len(my_colors)):
        x = (r - my_colors.loc[i, 'R']) ** 2 + (g - my_colors.loc[i, 'G']) ** 2 + (b - my_colors.loc[i, 'B']) ** 2
        x = math.sqrt(x)

        if (x < minm):
            minm = x
            color = my_colors.loc[i, 'a']

    # the above procedure finds the color which is the best match of the r,g,b values of the clicked coordinate

    # print(color)
    # color of the coordinate printed on the terminal

    # print(type(color))
    # the string variable color contains the color of the clicked portion

    # print(minm)

    print_on_image(color, r, g, b)


def print_on_image(color, r, g, b):
    # the function print_on_image prints the color of clicked portion at the center of the image

    position = ((int)(img.shape[1] / 2 - 268 / 2), (int)(img.shape[0] / 2 - 36 / 2))
    # the above line finds the cordinates of the center of image and puts into a tuple variable 'position'

    cv2.rectangle(img, (position[0] + 20, position[1] + 20), (position[0] + 360, position[1] + 60), (255, 255, 255), -1)
    # creates a rectange filled with white color at the center of the image on which the color name will be printed

    test = cv2.putText(img, color, (position[0] + 20, position[1] + 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (b, g, r), 3)
    # the putText() function in opencv helps us in printing the contents of string 'color' on the image at specified  image

    cv2.imshow("Color detection", test)
    # to show the modified image on the screen


print("Enter image name present on desktop:")
# take name of image as input from keyboard

while (True):
    pat = input()
    pat = "C:\\Users\\Admin\\New folder\\" + pat + ".jpg"
    # append the filename with its path

    if path.isfile(pat):
        print("Image opened successfully")
        print("Click on the region whose color you want to find out!!")
        break
        # if correct file name is entered then continue with the program

    else:
        print("Enter valid image name!!")
        # prompt the user to enter a valid file name

    # this while loop will run until a valid image name/file name is enetered

# print(path)

img = cv2.imread(pat, cv2.IMREAD_COLOR)
# opening image using Opencv from specified path

# print(type(img))

cv2.imshow("Color detection", img)
# showing the image on screen using Opencv

my_colors = pd.read_csv("C:\\Users\\Admin\\New folder\\colors (1).csv")
##print(my_colors)
# reading the csv file using Pandas and storing the data as a dataframe into my_colors variable

# print(type(my_colors))C:\
# print(my_colors)

cv2.setMouseCallback("Color detection", click_event)
# when a point on image is clicked, event triggers the callback fucntion:click_event

cv2.waitKey(0)
# waits till enter key is pressed

cv2.destroyAllWindows()
# closes all windows


















