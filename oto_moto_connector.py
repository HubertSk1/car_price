import requests
import json
from car import car

class oto_moto_checker():
    def __init__(self):
        self.list_of_cars=[]

    def make_url_from_filter(self,brand=None,model=None,year=None):
        url = f"https://www.otomoto.pl/osobowe"
        if brand:
            url=url+f"/{brand}"
            if model:
                url+=f"/{model}"
        if year:
            url+=f"/od-{year}?search%5Bfilter_float_year%3Ato%5D={year}"
        return url

    def get_response_from_url(self,url)->requests.Response:
        response=requests.get(url)
        if response.status_code !=200:
            print(response.status_code)
            response.raise_for_status()
            return None
        else:
            return response
        
    def get_offers_from_response(self,response:requests.Response)->dict:
        long_part = "["+response.text.split("\"itemListElement\":[")[1].split("]}}</script><meta")[0]+"]"
        structure = json.loads(long_part)
        print(structure)
        return structure

    def write_string_to_file(name:str,input:str)->None:
        with open(name, 'w', encoding='utf-8') as text_file:
            text_file.write(input)

    def offers_to_car_list(self,offers:json,year)->None:
        for offer in offers:
            new_car = car(offer,year)
            self.list_of_cars.append(new_car)
            print(new_car)
            print("\n")

# url = "https://www.otomoto.pl/osobowe/bmw/"
    

Ot_Mt = oto_moto_checker()
year=2017
url=Ot_Mt.make_url_from_filter("BMW","1M")
res = Ot_Mt.get_response_from_url(url)

offers = Ot_Mt.get_offers_from_response(res)
Ot_Mt.offers_to_car_list(offers,2017)