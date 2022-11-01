class car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance


honda=car("ABC-123", 124)
print(f"the properties of honda is:{honda.registration_number},{honda.maximum_speed},{honda.current_speed},{honda.travelled_distance}")