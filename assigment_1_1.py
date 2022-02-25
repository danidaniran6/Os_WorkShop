_input = input()
while (_input.lower() != "exit"):
    if(float(_input)>0):
        converter = 2.205
        weight_in_kg = float(_input)
        weight_in_pound = weight_in_kg * converter
        print(weight_in_pound)
    else:
        print("input is not valid, plz try again!")
    _input = input()
