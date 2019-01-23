from Cimpl import *


def grayscale(image):
    """ (Cimpl.Image) -> None
    
    Convert image into shades of gray.
    
    >>> image = load_image(choose_file())
    >>> grayscale(image)
    >>> show(image)    
    """
    for x, y, (r, g, b) in image:

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)


def weighted_grayscale(image):
    """ (Cimpl.Image) -> None

    Convert image into shades of gray.

    >>> image = load_image(choose_file())
    >>> weighted_grayscale(image)
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        # Use the shade of gray that has the same brightness as the pixel's
        # original color.

        brightness = r * 0.299 + g * 0.587 + b * 0.114
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)


def solarize(image, threshold):
    """ (Cimpl.Image, int) -> None
    Solarize image, modifying the RGB components that
    have intensities that are less than threshold.
    Parameter threshold is in the range 0 to 256, inclusive.
    >>> image = load_image(choose_file())
    >>> solarize(image, int(input()))
    >>> show(image)
    """
    for x, y, (r, g, b) in image:

        if r < threshold:
            r = 255 - r

        if g < threshold:
            g = 255 - g

        if b < threshold:
            b = 255 - b

        solarized = create_color(r, g, b)
        set_color(image, x, y, solarized)


def negative(image):
    """ (Cimpl.Image) -> None
    >>> image = load_image(choose_file())
    >>> negative(image)
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        set_color(image, x, y, create_color(255-r, 255-g, 255-b))


def black_and_white(image):
    """ (Cimpl.Image) -> None
    
    Convert image to a black-and-white (two-tone) image.
    
    >>> image = load_image(choose_file()) 
    >>> black_and_white(image)
    >>> show(image)     
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on 
    # whether its brightness is in the lower or upper half of this range.       

    for x, y, (r, g, b) in image:
        brightness = (r + g + b) // 3
        
        if brightness < 128:
            set_color(image, x, y, black)
        else:     # brightness is between 128 and 255, inclusive
            set_color(image, x, y, white)


def extreme_contrast(image):
    """ (Cimpl.Image) -> None
    Modify image, maximizing the contrast between the light
    and dark pixels.
    >>> image = load_image("C:/Users/Danie/Documents/University/SYSC1005A/labs/Lab 5/Lab 5 Sample Results-20171030/angus.jpg")
    >>> extreme_contrast(image)
    >>> is_same(image, load_image("C:/Users/Danie/Documents/University/SYSC1005A/labs/Lab 5/Lab 5 Sample Results-20171030/extreme_contrast.jpg"))
    True
    """
    for x, y, (r, g, b) in image:
        if r < 128:
            r = 0
        else:
            r = 255
        if g < 128:
            g = 0
        else:
            g = 255
        if b < 128:
            b = 0
        else:
            b = 255
        set_color(image, x, y, create_color(r, g, b))


def black_and_white_and_gray(image):
    """ (Cimpl.Image) -> None
    
    Convert image to a black-and-white-and-gray (three-tone) image.

    >>> image = load_image(choose_file()) 
    >>> black_and_white_and_gray(image)
    >>> show(image)     
    """
    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of
    # pixels whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, (r, g, b) in image:
        brightness = (r + g + b) // 3

        if brightness < 85:
            set_color(image, x, y, black)
        elif brightness < 171:  # brightness is between 85 and 170, inclusive
            set_color(image, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(image, x, y, white)


def sepia_tint(image):
    """ (Cimpl.Image) -> None
    Convert image to sepia tones.
    >>> image = load_image(choose_file())
    >>> sepia_tint(image)
    >>> show(image)
    """
    grayscale(image)
    for x, y, (r, g, b) in image:
        if r < 63:
            b = b * 0.9
            r = r * 1.1
        elif r < 192:
            b = b * 0.85
            r = r * 1.15
        else:
            b = b * 0.93
            r = r * 1.08
        set_color(image, x, y, create_color(r, g, b))


def _adjust_component(amount):
    """ (int) -> int
    Divide the range 0..255 into 4 equal-size quadrants,
    and return the midpoint of the quadrant in which the
    specified amount lies.
    >>> _adjust_component(10)
    31
    >>> _adjust_component(85)
    95
    >>> _adjust_component(142)
    159
    >>> _adjust_component(230)
    223
    """
    if amount <= 63:
        return 31
    elif amount <= 127:
        return 95
    elif amount <= 191:
        return 159
    else:
        return 223


def posterize(image):
    """(Cimpl.Image) -> None
    "Posterize" the specified image.
    >>> image = load_image(choose_file())
    >>> posterize(image)
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        set_color(image, x, y, create_color(_adjust_component(r), _adjust_component(g), _adjust_component(b)))


def _adjust_component_better(amount, n):
    """
    >>> _adjust_component_better(10,4)
    31
    >>> _adjust_component_better(85,4)
    95
    >>> _adjust_component_better(142,4)
    159
    >>> _adjust_component_better(230,4)
    223
    """
    for i in range(0, n):
        if amount <= 255//n + 255//n * i:
            return int(255 / n + 255 / n * (i - 1) + 255 / n / 2)


def posterize_better(image, n):
    """(Cimpl.Image) -> None
    "Posterize" the specified image.
    >>> image = load_image(choose_file())
    >>> posterize_better(image, int(input()))
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        set_color(image, x, y, create_color(_adjust_component_better(r, n),
                                            _adjust_component_better(g, n),
                                            _adjust_component_better(b, n)))


def difference(pict_1, pict_2):
    """
    :param pict_1:
    :param pict_2:
    :return:
    >>> show(difference(load_image(choose_file()), load_image(choose_file())))
    """
    if get_width(pict_1) == get_width(pict_2) and get_height(pict_1) == get_height(pict_2):
        difference = create_image(get_width(pict_1), get_height(pict_1))
        for x, y, (r, g, b) in pict_1:
            r2, g2, b2 = get_color(pict_2, x, y)
            set_color(difference, x, y, create_color(r-r2, g-g2, b-b2))
        return difference
    return False


def blur(original):
    """
    :param original:
    :return blurred:
    >>> original = load_image(choose_file())
    >>> blurred = blur(original)
    >>> save_as(blurred, choose_save_filename())
    >>> is_same(load_image(choose_file()), load_image(choose_file()))
    True
    """
    blurred = copy(original)
    for y in range(1, get_height(original) - 1):
        for x in range(1, get_width(original) - 1):
            top_right_red, top_right_green, top_right_blue = get_color(original, x + 1, y - 1)
            top_red, top_green, top_blue = get_color(original, x, y - 1)
            top_left_red, top_left_green, top_left_blue = get_color(original, x - 1, y - 1)
            left_red, left_green, left_blue = get_color(original, x - 1, y)
            bottom_right_red, bottom_right_green, bottom_right_blue = get_color(original, x + 1, y + 1)
            bottom_red, bottom_green, bottom_blue = get_color(original, x, y + 1)
            bottom_left_red, bottom_left_green, bottom_left_blue = get_color(original, x + 1, y + 1)
            right_red, right_green, right_blue = get_color(original, x + 1, y)
            center_red, center_green, center_blue = get_color(original, x, y)
            new_red = (top_right_red + top_red + top_left_red + left_red + bottom_right_red + bottom_red + bottom_left_red + right_red + center_red) // 9
            new_green = (top_right_green + top_green + top_left_green + left_green + bottom_right_green + bottom_green + bottom_left_green + right_green + center_green) // 9
            new_blue = (top_right_blue + top_blue + top_left_blue + left_blue + bottom_right_blue + bottom_blue + bottom_left_blue + right_blue + center_blue) // 9
            new_color = create_color(new_red, new_green, new_blue)
            set_color(blurred, x, y, new_color)
    return blurred


def make_very_blurry(image, number_of_blurs):
    """
    :param image:
    :param number_of_blurs:
    :return:
    >>> image = load_image(choose_file())
    >>> image = make_very_blurry(image, 10)
    >>> show(image)
    """
    for i in range(number_of_blurs):
        image = blur(image)
    return image


def detect_edges(image, threshold):
    """
    :param image:
    :param threshold:
    :return :
    >>> image = load_image(choose_file())
    >>> detect_edges(image, float(input("threshold")))
    >>> show(image)
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    for y in range(0, get_height(image) - 1):
        for x in range(0, get_width(image)):
            r, g, b = get_color(image, x, y)
            r2, g2, b2 = get_color(image, x, y + 1)
            if abs((r + g + b) // 3 - (r2 + g2 + b2) // 3) > threshold:
                set_color(image, x, y, black)
            else:
                set_color(image, x, y, white)


def detect_edges_better(image, threshold):
    """
    :param image:
    :param threshold:
    :return :
    >>> image = load_image(choose_file())
    >>> detect_edges_better(image, float(input("threshold")))
    >>> show(image)
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    for y in range(0, get_height(image) - 1):
        for x in range(0, get_width(image) - 1):
            r, g, b = get_color(image, x, y)
            rdown, gdown, bdown = get_color(image, x, y + 1)
            rright, gright, bright = get_color(image, x + 1, y)
            if abs((r + g + b) // 3 - (rdown + gdown + bdown) // 3) > threshold or abs((r + g + b) // 3 - (rright + gright + bright) // 3) > threshold:
                set_color(image, x, y, black)
            else:
                set_color(image, x, y, white)


def rotate(image, angle=180):
    """
    :param image:
    :param angle:
    :return:
    >>> image = load_image(choose_file())
    >>> show(rotate(image, 180))
    """
    scale_factor = int(math.sqrt(image.get_height() ** 2 + image.get_width() ** 2))
    output = create_image(scale_factor*image.get_width(), scale_factor*image.get_height())
    for output_y in range(1, image.get_width()):
        for output_x in range(1, image.get_height()):
            input_x = output_x * math.cos(math.pi/180 * angle) - output_y * math.sin(math.pi/180 * angle)
            input_y = output_x * math.sin(math.pi/180 * angle) + output_y * math.cos(math.pi/180 * angle)
            output.set_color(output_x, output_y, get_color(image, int(input_x), int(input_y)))
    return output
