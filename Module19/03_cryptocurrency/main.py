data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

print(f'Список ключей {data.keys()}')
print(f'Список значений {data.values()}')

other = {'total_diff': 100}
new_key = data['ETH'].update(other)
print(f'Новый ключ: {data}')

for i_tokens in data['tokens']:
    if i_tokens.get('fst_token_info'):
        new_value = i_tokens.get('fst_token_info')
        new_value['name'] = 'doge'
print(f'Новое значение ключа: {data}')

for i_tokens in data['tokens']:
    total_out_values = i_tokens['total_out']
    total_out_pop = i_tokens.pop('total_out')
data['ETH']['total_out'] = total_out_values
print(f'Новое значение total_out: {data}')

for i_tokens in data['tokens']:
    if i_tokens.get('sec_token_info'):
       i_tokens['total_price'] = i_tokens['sec_token_info'].pop('price')
print(f'Новое название ключа: {data}')