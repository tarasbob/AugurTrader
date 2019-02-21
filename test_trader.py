import unittest

from trader import ContractConnector
from utils import pad

class TestContractConnector(unittest.TestCase):

    def test_send_call(self):
        mkr_addr = "c66ea802717bfb9833400264dd12c2bceaa34a6d"
        conn = ContractConnector(mkr_addr)
        source_addr = "0"
        fn_balance_of = "70a08231"
        args = fn_balance_of + pad(source_addr)
        args = args.lower()
        result = int(conn.send_call(args), 16) / (10**18)
        self.assertTrue(result > 0)
        print(result)

if __name__ == '__main__':
    unittest.main()
