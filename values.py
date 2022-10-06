from urllib import response
import requests
from pprint import pprint

def get_query_block(hash_block):
    print("Hash:", hash_block)
    api_query_block = f"https://blockchain.info/rawblock/{hash_block}"
    response = requests.get(api_query_block)
    return response.json()


def get_last_block():
    api_last_block = "https://blockchain.info/latestblock"
    response = requests.get(api_last_block)
    return response.json()
    


last_block = get_last_block()
values     = get_query_block(last_block['hash'])



block_number  = values['block_index']
transaction   = values['tx']
previous_hash = values['prev_block']
prefix_zeros  = 20