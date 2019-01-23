# SYSC 1005 A Fall 2017 Lab 7

from filters import *


def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

# A bit of code to demonstrate how to use get_image().


image = None
c = True
while c:
    user_input = str.lower(input("L)oad image \nN)egative G)rayscale X)treme contrast S)epia tint E)dge detect \nW)show image \nQ)uit \n"))
    for i in range(len(user_input)):
        if user_input[i] == 'l':
            image = get_image()
        elif user_input[i] == 'q':
            c = False
        elif user_input[i] == 'n':
            if image is not None:
                negative(image)
            else:
                print("No image loaded")
        elif user_input[i] == 'g':
            if image is not None:
                grayscale(image)

            else:
                print("No image loaded")
        elif user_input[i] == 'x':
            if image is not None:
                extreme_contrast(image)
            else:
                print("No image loaded")
        elif user_input[i] == 's':
            if image is not None:
                sepia_tint(image)
            else:
                print("No image loaded")
        elif user_input[i] == 'e':
            Threshold = 0
            i2 = i
            i3 = i
            c2 = True
            while c2:
                try:
                    i2 = i2 + 1
                    Threshold = int(str(Threshold) + user_input[i2])
                except (ValueError, IndexError):
                    c2 = False
            try:
                i3 = i3 + 1
                int(user_input[i3])
            except (ValueError, IndexError):
                Threshold = int(input("Threshold?: "))
            if image is not None:
                detect_edges_better(image, Threshold)
            else:
                print("No image loaded")
        elif user_input[i] == 'w':
            show(image)
        else:
            try:
                int(user_input[i])
            except ValueError:
                print("No such command")
