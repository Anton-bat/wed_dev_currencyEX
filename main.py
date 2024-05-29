import requests

class CurrencyConvertor:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.source_url = 'https://v6.exchangerate-api.com/v6'

    def get_exchange_rate(self, from_convert, to_convert):
        url = f'{self.source_url}/{self.api_key}/latest/{from_convert}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if to_convert in data['conversion_rates']:
                return data['conversion_rates'][to_convert]
            else:
                raise ValueError(f'Choosen currency {to_convert} is not available/')
        else:
            raise Exception('Failed to fetch data from API')

    def convert(self, amount, from_convert, to_convert):
        exc_rate = self.get_exchange_rate(from_convert, to_convert)
        return amount * exc_rate
    
def main():
    api_key = '428ead01f8ca4899dde4f443'
    converter = CurrencyConvertor(api_key)

    print("Welcome, here you can convert your currency")
    from_convert = input('Please, type currency that you want to convert: ').upper()
    to_convert = input('Please, type currency that you want to convert to: ').upper()
    amount = float(input('Please give an amount for exchange: '))

    try:
        result = converter.convert(amount, from_convert, to_convert)
        print(f'{amount} {from_convert} is equal to {result:.2f} {to_convert}')
    except ValueError as e:
        print(e)
    except Exception as e:
        print("An error has occured:", e)
        
if __name__ == "__main__":
    main()