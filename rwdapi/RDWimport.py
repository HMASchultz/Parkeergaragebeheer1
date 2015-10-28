__author__ = 'kevinnesselaar'
import requests
import csv
kenteken = input("voer hier uw kenteken in:")
url = 'https://overheid.io/api/voertuiggegevens/' + kenteken + '?field[]=hoofdbrandstof'
payload = {'ovio-api-key': '449cd9d896fd46ce22ff029805b0eb67bb6b518b7980d9173a4b0c9e659cc99b'}
response = requests.get(url, params=payload)


print(response.url)
resp = response.text
print(resp)



#----------------------------------------test----------------------------------------------#
#dict(csv.reader([item], delimiter='"', quotechar="'").next()
#         for item in csv.reader([resp], delimiter=':', quotechar="'").next())

#information = (resp.split(','))
#print(information)

#dictinformation = dict(item.split(":") for item in information.split(","))
#print(dictinformation)
#---------------------------------------test-----------------------------------------------#







#datum = int(response.text)
#brandstof = response.text

#print(datum)
#print(brandstof)

#---------------------------------------check script-----------------------------------------------#
#if datum > 2001 and brandstof == "Diesel":
#    print("U mag in de groene zone")
#elif brandstof == "Benzine":
#    print("U mag in de groene zone")
#elif datum < 2001 or brandstof != "Diesel":
#    print("Uw auto is niet toegestaan")
#---------------------------------------check script-----------------------------------------------#

#---------------------------------------api key-----------------------------------------------#
#449cd9d896fd46ce22ff029805b0eb67bb6b518b7980d9173a4b0c9e659cc99b
#[190:194][363:370]
#---------------------------------------test-----------------------------------------------#
