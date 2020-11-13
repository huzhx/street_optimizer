from abc import ABCMeta, abstractmethod

class OptimizationStrategy:
    __metaclass__ = ABCMeta

    @abstractmethod
    def mask_addr_algorithm(self, org_street):
        raise NotImplementedError()

    @abstractmethod
    def get_opt_address(self, masked_street):
        raise NotImplementedError()