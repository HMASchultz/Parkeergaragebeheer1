__author__ = 'kevinnesselaar'
import requests
url = 'https://overheid.io/api/voertuiggegevens/4-TFL-24'
payload = {'ovio-api-key': '449cd9d896fd46ce22ff029805b0eb67bb6b518b7980d9173a4b0c9e659cc99b'}
response = requests.get(url, params=payload)
print(response.text)


#449cd9d896fd46ce22ff029805b0eb67bb6b518b7980d9173a4b0c9e659cc99b


