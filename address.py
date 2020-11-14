class Address:
    def __init__(self, street, city, state, zipcode):
        self._street = street
        self._city = city
        self._state = state
        self._zipcode = zipcode

    @property
    def street(self):
        return self._street
    
    @street.setter
    def street(self, new_street):
        self._street = new_street

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, new_city):
        self._city = new_city

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, new_state):
        self._state = new_state

    @property
    def zipcode(self):
        return self._zipcode
    
    @zipcode.setter
    def zipcode(self, new_zipcode):
        self._zipcode = new_zipcode

    def to_string(self):
        return "{}, {}, {}, {}".format(
            self._street, 
            self._city, 
            self._state, 
            self._zipcode)