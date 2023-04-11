"""
do some webscrapping for MKT website
"""

import requests
import parsel
import csv

from datetime import date, timedelta

end_date = date.today()
start_date = date(2020, 3, 11)

delta = timedelta(days=1)
while start_date <= end_date:
    print(start_date)

    try:
        url = 'https://4d2ulive.com/past-results/{}/?f=1'.format(start_date.strftime("%Y-%m-%d"))
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

        response = requests.get(url=url, headers=headers)

        selector = parsel.Selector(response.text)

        lucky_number = selector.xpath('//*[@class="card outer-box table-1"]/div//tr/td/text()').getall()
        lucky_number = [item.strip() for item in lucky_number]
        new_lucky_number = [item for item in lucky_number if len(item) == 4 and item.isdigit()]

        magnum = []
        magnum.append(start_date.strftime("%Y-%m-%d"))
        for index in range(23):
            magnum.append(new_lucky_number[index])

        with open(file="record_magnum.csv", mode="a", encoding="UTF8", newline="") as f:
            csv_writer = csv.writer(f)
            for item in magnum:
                csv_writer.writerow([item])
    except IndexError:
        continue
    finally:
        start_date += delta
