faded_x = np.arange(0, y_number, 1/gradient_points)
faded_y = []
for i in random_int_array:
    faded_y.append(i)
    for j in range(gradient_points):
        faded_y.append(lerp(perlin_fade_func(1/j), i, i+1)
print(faded_y)
