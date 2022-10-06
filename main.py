from hashlib import sha256
import os
import time as t
import values


MAX_NONCE = 10000000000000000


def sha512_encrypt(value):
    return sha256(value.encode("ascii")).hexdigest()
    

def mine(block_number, transaction, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    
    for nonce in range(MAX_NONCE):
        value_total = str(block_number) + str(transaction) + previous_hash + str(nonce)
        hash_value = sha512_encrypt(value=value_total)
        
        if hash_value.startswith(prefix_str):
            print("Bitcoin minerado com valor nonce: ", nonce)
            return hash_value
        
        print(f"[Nonce] {nonce} [Hash] {hash_value}")
        
    print("Não foi possível encontrar um hash no intervalo fornecido de até ", MAX_NONCE)


def main():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
        

    begin=t.time()
    new_hash = mine(
                    block_number  =  values.block_number,
                    transaction   =  values.transaction,
                    previous_hash =  values.previous_hash,
                    prefix_zeros  =  values.prefix_zeros
                )


    print("Hash: ", new_hash)
    time_taken=t.time()- begin
    print("O processo de mineração levou: ", time_taken, "segundos")
    
    
if __name__ == "__main__":
    main()