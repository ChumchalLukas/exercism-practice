def label(colors):
    colors_values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    first_color = colors_values[colors[0]]
    second_color = colors_values[colors[1]]
    third_color_multiplier = colors_values[colors[2]]

    
    if first_color == 0 and second_color == 0:
        return "0 ohms"

    
    base_value = str(first_color) + str(second_color) + "0" * third_color_multiplier
    num_zeros = len(base_value) - len(base_value.rstrip("0"))  # počet nul na konci


    ohm_value = int(base_value)
    if ohm_value >= 1_000_000_000:
        return f"{ohm_value // 1_000_000_000} gigaohms"
    elif ohm_value >= 1_000_000:
        return f"{ohm_value // 1_000_000} megaohms"
    elif ohm_value >= 1_000:
        return f"{ohm_value // 1_000} kiloohms"
    else:
        return f"{ohm_value} ohms"





    

