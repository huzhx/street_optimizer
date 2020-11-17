from opt_strategy_abc import OptimizationStrategy
from address import Address
from utils import shift_num, remove_num, consume_api
import copy

class OptimizationStrategy1(OptimizationStrategy):

    def get_opt_address(self, org_address: Address):
        ''' Return an address
        - Send the masked address to https://geomap.ffiec.gov/FFIECGeocMap/GeocodeMap1.aspx to get an optimized address 
        - If received an optimized address, restore the original street number 
        - Else return None
        '''
        masked_addr_wo_id_zip = self.mask_address(org_address).to_string_wo_id_zip()
        print('{} -> {}'.format(org_address.to_string_wo_id_zip(), masked_addr_wo_id_zip))
        api_endpoint = 'https://geomap.ffiec.gov/FFIECGeocMap/GeocodeMap1.aspx/GetGeocodeData'
        payload = {'sSingleLine': masked_addr_wo_id_zip, 'iCensusYear': '2020'}
        resp = consume_api(api_endpoint, payload)
        if (resp['d']['sMsg']== 'Match Found.'):
            opt_address = Address(org_address.id, resp['d']['sAddress'], resp['d']['sCityName'], resp['d']['sStateAbbr'], resp['d']['sZipCode'])
            org_street_num, _ = org_address.extract_street_num()
            opt_address.replace_street_num(org_street_num)
            return opt_address
        else:
            return None

    def mask_address(self, org_address: Address):
        ''' Return an address
        Mask the address by the following algorithm:
        - Find the first number in the street and mask it
        - For the rest of the string, remove the number in it if it is not part of the street name
        '''
        org_street = org_address.street
        first_num, rest_street = org_address.extract_street_num()
        masked_num = shift_num(first_num)
        sanitized_street = remove_num(rest_street)
        masked_street = ' '.join([masked_num, sanitized_street])
        masked_address = copy.deepcopy(org_address)
        masked_address.street = masked_street
        return masked_address
