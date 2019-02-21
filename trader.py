import json
import requests

class ContractConnector(object):

    def __init__(self, contract_addr: str, client_addr='http://localhost:8545'):
        self.client_addr = client_addr
        self.contract_addr = contract_addr

    def send_call(self, data: str):
        '''Make a call without sending a transaction. Read from the blockchain.'''
        params = {'to': "0x" + self.contract_addr, 'data': "0x" + data}
        r = self._send_request('eth_call', [params, 'latest'])
        return r["result"]

    def _send_request(self, method, params):
        headers = {'content-type': 'application/json'}
        payload = {'jsonrpc': '2.0', 'method': method, 'params': params, 'id': 1}
        return requests.post(self.client_addr, data=json.dumps(payload), headers=headers).json()
