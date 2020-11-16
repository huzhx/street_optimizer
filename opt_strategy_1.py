from opt_strategy_abc import OptimizationStrategy
from address import Address
from utils import shift_num, remove_num, consume_api
import copy

class OptimizationStrategy1(OptimizationStrategy):

    def get_opt_address(self, org_address: Address):
        masked_addr_wo_zip = self.mask_address(org_address).to_string_wo_zip()
        api_endpoint = 'https://geomap.ffiec.gov/FFIECGeocMap/GeocodeMap1.aspx/GetGeocodeData'
        payload = {'sSingleLine': masked_addr_wo_zip, 'iCensusYear': '2020'}
        resp = consume_api(api_endpoint, payload)
        return resp['d']['sMatchAddr'] if resp['d']['sMsg'] == 'Match Found.' else 'Failed'

    def mask_address(self, org_address: Address):
        ''' Return a string
        Mask the address by the following algorithm:
        - find the first number in the street and mask it
        - for the rest of the string, remove the number in it if it is not part of the street name
        '''
        org_street = org_address.street
        first_num = ''
        index = 0
        while org_street[index].isdigit():
            first_num += str(org_street[index])
            index += 1
        masked_num = shift_num(first_num)
        rest_street = org_street[index:].strip()
        sanitized_street = remove_num(rest_street)
        masked_street = ' '.join([masked_num, sanitized_street])
        masked_address = copy.deepcopy(org_address)
        masked_address.street = masked_street
        return masked_address
