import pytest
from opt_strategy_abc import OptimizationStrategy

def test_not_implemented():
    opts = OptimizationStrategy()
    with pytest.raises(NotImplementedError):
        opts.mask_addr_algorithm('...')
    with pytest.raises(NotImplementedError):
        opts.get_opt_address('...')
