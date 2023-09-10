def int_input(input_string=""):
    while True:
        try:
            value=int(input(input_string))
            break
        except:
            print("Please insert a valid number.")
    return value
