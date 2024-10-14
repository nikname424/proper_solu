import requests
import time

def get_transactions_count(api_url, page=1, items_per_page=30, sort_by='tx', token='', type_='ERC20'):
  response = requests.get(
    api_url,
    params={
      'page': page,
      'items_per_page': items_per_page,
      'sort_by': sort_by,
      'token': token,
      'type': type_
    }
  )
  data = response.json()
  return data['total']

def get_holders_count(api_url, token='', page=1, items_per_page=30, sort_by='volume', direction='desc', volume_not_zero=True):
  response = requests.get(
    api_url,
    params={
      'token': token,
      'page': page,
      'items_per_page': items_per_page,
      'sort_by': sort_by,
      'direction': direction,
      'volume_not_zero': str(volume_not_zero).lower()
    }
  )
  data = response.json()
  return data['total']

def get_tokens_count(api_url, page=1, items_per_page=30, has_name=True, sort_by='timestamp', direction='desc'):
  response = requests.get(
    api_url,
    params={
      'page': page,
      'items_per_page': items_per_page,
      'has_name': str(has_name).lower(),
      'sort_by': sort_by,
      'direction': direction
    }
  )
  data = response.json()
  return data['data']

def main():
    for i in range(1, 26):
        print('Страница', i)
        tokens = get_tokens_count(api_url='https://api-scanner.stg.autentic.capital/api/tokens', page=i)
        for item in tokens:
           amount_transactions = get_transactions_count('https://api-scanner.stg.autentic.capital/api/token_transaction', token=str(item))
           amount_holders = get_holders_count('https://api-scanner.stg.autentic.capital/api/tokens/holders', token=str(item))
           if amount_holders > amount_transactions:
              print(f'Холдеров больше чем транзакций - https://api-scanner.stg.autentic.capital/api/tokens page-{i}')
              input()
           time.sleep(1)

main()