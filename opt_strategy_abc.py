from abc import ABCMeta, abstractmethod

class OptimizationStrategy:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_opt_address(self, org_address):
        raise NotImplementedError()