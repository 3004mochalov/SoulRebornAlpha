quantifier_x = 4
quantifier_y = 3
denominator = 20

def generate_arrays():
    x_step = quantifier_x / denominator
    y_step = quantifier_y / denominator

    x_array = [round(i * x_step, 1) for i in range(denominator + 1)]  # Round to 1 decimal place
    y_array = [round(i * y_step, 1) for i in range(denominator + 1)]  # Round to 1 decimal place

    return x_array, y_array

x_values, y_values = generate_arrays()
print("X values:", x_values)
print("Y values:", y_values)


def BS_res800_600():
    dots_per_quantifier = 200
    return dots_per_quantifier


def BS_res1024_768():
    dots_per_quantifier = 256
    return dots_per_quantifier


def BS_res1280_960():
    dots_per_quantifier = 320
    return dots_per_quantifier
