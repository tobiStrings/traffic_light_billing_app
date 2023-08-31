class TrafficLightIdIsInvalid(Exception):
    def __init__(self, message="TrafficLightId is invalid"):
        self.message = message
        super().__init__(self.message)

class TrafficLightException(Exception):
    def __init__(self, message="Something went wrong"):
        self.message = message
        super().__init__(self.message)
