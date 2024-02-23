class UnitConversor():
    def __init__(self):
        self.conversion_factors = {
            "meters_to_feet" : 3.280,
            "feet_to_meters" : 0.305,
            "kilometers_to miles" : 0.621,
            "miles_to_kilometers" : 1.609,
            "pounds_to_kilograms" : 0.454,
            "kilograms_to_punds" : 2.205
        }
    
    def convert(self):
        original_unit = input("Type the unit you want to convert: ")
        amount = int(input("Type the amount of units you have: "))
        desired_unit = input("Type what unit you to convert to: ")
        conversion_rate = original_unit + "_to_" + desired_unit
        if conversion_rate in self.conversion_factors.keys():
            converted_unit = self.conversion_factors[conversion_rate] * amount
            print(f"{amount} {original_unit} equals to {converted_unit}")

unit1 = UnitConversor()
unit1.convert()