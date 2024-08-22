quantifier_x = 16
quantifier_y = 9
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


def WS_res1280_720():
    dots_per_quantifier = 80
    return dots_per_quantifier


def WS_res1600_900():
    dots_per_quantifier = 100
    return dots_per_quantifier


def WS_res1920_1080():
    dots_per_quantifier = 120
    return dots_per_quantifier
