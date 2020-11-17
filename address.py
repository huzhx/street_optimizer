class Address:
    def __init__(self, street, city, state, zipcode):
        self._street = street.strip().title() if street != None else street
        self._city = city.strip().title() if city != None else city
        self._state = state.strip().upper() if state != None else state
        self._zipcode = zipcode.strip() if zipcode != None else zipcode

    def __eq__(self, other_address):
        if not isinstance(other_address, Address):
            raise Exception('Invalid camparison')
        return self._street == other_address.street and self._city == other_address.city and self._state == other_address.state and self.zipcode == other_address.zipcode

    @property
    def street(self):
        return self._street
    
    @street.setter
    def street(self, new_street):
        self._street = new_street.strip().title() if new_street != None else new_street 

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, new_city):
        self._city = new_city.strip().title() if new_city != None else new_city

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, new_state):
        self._state = new_state.strip().upper() if new_state != None else new_state

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

    def to_string_wo_zip(self):
        return "{}, {}, {}".format(
            self._street, 
            self._city, 
            self._state)

    def extract_street_num(self):
        ''' Return [street_num, rest of the string]
        For example, ['1234', 'Astor Ave']
        '''
        org_street = self._street
        if (len(org_street) == 0 or org_street == None):
            raise Exception('Invalid street value')
        street_num = ''
        index = 0
        while org_street[index].isdigit():
            street_num += str(org_street[index])
            index += 1
        return [street_num, org_street[index:].strip()]

    def replace_street_num(self, new_street_num):
        street_num, rest_street = self.extract_street_num()
        new_street = ' '.join([new_street_num, rest_street])
        self._street = new_street