import requests
import json
from car import car
from db_connector import db_connector

class oto_moto_checker():
    def __init__(self):
        self.db=db_connector("database/database.db")
    def write_string_to_file(self,name:str,input:str)->None:
        with open(f"pages/{name}", 'w', encoding='utf-8') as text_file:
            text_file.write(input)

    def make_url_from_filter(self,year, brand=None, model=None, page=None):
        url = f"https://www.otomoto.pl/osobowe"
        if brand:
            url=url+f"/{brand}"
            if model:
                url+=f"/{model}"
        if year:
            url+=f"/od-{year}?search%5Bfilter_float_year%3Ato%5D={year}"
        if page:
            url+=f"&page={page}"
        return url

    def get_response_from_url(self,url)->requests.Response:
        response=requests.get(url)
        if response.status_code !=200:
            print(response.status_code)
            response.raise_for_status()
            return None
        else:
            return response

    def has_next_page(self,res:requests.Response):
        txt=res.text.split("title=\"Next Page\" data-testid=\"pagination-step-forwards\" aria-disabled=\"")[1].split("\"")[0]
        if txt=="true":
            return False
        elif txt=="false":
            return True

    def get_offers_from_response(self,response:requests.Response)->dict:
        long_part = "["+response.text.split("\"itemListElement\":[")[1].split("]}}</script><meta")[0]+"]"
        structure = json.loads(long_part)
        return structure

    def get_cars_from_offers(self,offers:json,year)->None:
        for offer in offers:
            new_car = car(offer,year)
            if new_car.status == 0:
                self.db.insert_car(new_car,"oto_moto_cars")

    def parse_all_pages(self,production_year,brand=None,model=None):
        page_number = 1
        prev_offers = None
        while 1:
            if page_number>1:
                prev_offers=offers
            url= self.make_url_from_filter(production_year,brand,model,page_number)
            res = self.get_response_from_url(url)
            offers = self.get_offers_from_response(res)
            if prev_offers and prev_offers==offers:
                break
            self.get_cars_from_offers(offers,production_year)
            print(f"page {page_number} parsed")
            page_number +=1
            
om = oto_moto_checker()
year=2017
brand="Honda"
om.parse_all_pages(year,brand)





