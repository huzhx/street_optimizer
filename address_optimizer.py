import csv
from address import Address
from opt_strategy_abc import OptimizationStrategy

class AddressOptimizer:
    
    def __init__(self, org_addresses: Address, strategy: OptimizationStrategy):
        self._org_addresses = org_addresses
        self._opt_addresses = []
        self._strategy = strategy
    
    @property
    def opt_addresses(self):
        return self._opt_addresses

    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self, new_strategy):
        self._strategy = new_strategy

    def process_addresses(self):
        for address in self._org_addresses:
            opt_address_str = self._strategy.get_opt_address(address)
            self._opt_addresses.append(opt_address_str)
    
    def opt_to_csv(self, file_path):
        with open(file_path, 'w') as result_file:
            wr = csv.writer(result_file, delimiter=',')
            for address in self._opt_addresses:
                wr.writerow([address.id, address.street, address.city, address.state, address.zipcode])
