def collinearity(x1, y1, x2, y2):
    if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0):
        return True

    cross_product = x1 * y2 - x2 * y1

    return cross_product == 0