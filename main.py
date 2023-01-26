from requests_html import HTMLSession

s = HTMLSession()

location = input("Enter Location: ")
url = f'https://www.eldersweather.com.au/climate-history/vic/{location}'

r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'})

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "Annual"]
rainHigh = []
rainLow = []

for i in range(len(month)):
    rainHigh.append(r.html.find(f'div.column.{month[i].lower()}')[14].text)
    rainLow.append(r.html.find(f'div.column.{month[i].lower()}')[15].text)
    print(month[i], "Rain High:", rainHigh[i], ",", month[i], "Rain Low:", rainLow[i])

