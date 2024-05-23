import json
import unicodedata
from typing import Literal

from loguru import logger
from selectolax.parser import Node


def _remove_dot_from_price(price_as_string:str):
        price = price_as_string.split('.')
        price =".".join(price[:1])
        return float(price.strip('$US'))

@logger.catch(TypeError)
def get_product_price(tag:Node,which:Literal['max','min']):
    elt =tag.css_first('.search-card-e-price-main').text()
    if '-' in elt and which=='max':
        max_price =elt.split('-')[1].split('&')[0]
        max_price = unicodedata.normalize("NFKC", max_price)
        max_price = max_price.replace('\u00a0','').replace(',','.').replace(" ","")
        if max_price.count('.') > 1:
            max_price = _remove_dot_from_price(price_as_string=max_price)
            return max_price
        return float(max_price.strip('$US'))
    
    elif '-' in elt and which=='min':
        min_price =elt.split('-')[0].split('&')[0]
        min_price = unicodedata.normalize("NFKC", min_price)
        min_price = min_price.replace('\u00a0','').replace(',','.').replace(" ","")
        if min_price.count('.') > 1:
            min_price = _remove_dot_from_price(price_as_string=min_price)
            return min_price
        return float(min_price.strip('$US'))
    else:
        strange_price = elt.strip(r"\xa0$US")
        price = unicodedata.normalize("NFKC", strange_price)
        price = price.replace('\u00a0','').replace(',','.').replace(" ","")
        if price.count('.') > 1:
            price = _remove_dot_from_price(price_as_string=price)
            return price
        else:
            return float(price.strip('$US'))
         
@logger.catch(TypeError)    
def is_alibaba_guaranteed(tag:Node):
    elt = tag.css_matches('.search-card-e-icon__half-trust-icon')
    return elt

@logger.catch(TypeError)
def get_product_certification(tag:Node):
    tags_exists = tag.css_matches(".search-card-e-icon__certification-wrapper")
    certifications: list[str] = []
    if tags_exists is True:
        elements = tag.css('.search-card-e-icon__certification-wrapper')
        for element in elements:
            certification_name= element.css_first('.search-card-e-icon__certification').attrs.get('alt')
            certifications.append(certification_name)
        certification_str = ",".join(certifications)
        return certification_str
    else:
        return 'any'
    
@logger.catch(TypeError)
def suppliers_status(tag:Node):
    status =tag.css_first(".verified-supplier-icon__wrapper")
    if status is not None:
        mode = status.attrs.get('data-aplus-auto-card-mod').split('=')[2]
        return mode
    return 'unverified'

@logger.catch(TypeError)
def sopi_level(tag: Node):
    elt = tag.css_first(".search-cards-e-star")
    return len(elt.css('.search-card-e-iconfont'))

@logger.catch(TypeError)
def years_as_supplier_gold(tag:Node):
    elt = tag.css_first(".search-card-e-supplier__year")
    year = elt.attrs.get('data-aplus-auto-card-mod').split('@@')[1][0]
    return year

def _get_minimum_to_order_tag(tags:list[Node]):
    for tag in tags:
        element_attr =tag.attrs.get('data-aplus-auto-card-mod')
        # if 'price_negotiated' or "easy_return" not in element_attr: 
        #     print(tag.text())
        #     return tag
        if 'minimale' in element_attr:
            return tag
        # print(element_attr)
@logger.catch(TypeError)
def minimum_to_order(tag:Node):
    elements =tag.css('.search-card-m-sale-features__item.tow-line')
    if len(elements) != 0  :
        element = _get_minimum_to_order_tag(tags=elements)
        if element is None:
            return 0
        number_str=element.text()
        number = number_str.split(':')[1].split()[0].strip()
        return int(number)
    else:
        return 0
    
@logger.catch(TypeError)
def ordered_or_sold(tag:Node):
    element = tag.css_first(".search-card-e-market-power-common")
    if element is not None:
        number_str=element.text()
        number = number_str.split()[0]
        number =number.replace(',','')
        return int(number)
    else:
        return 0  

def _from_abr_to_full_name(country_abr:str):
    with open('src/pays_data.json', encoding='utf-8') as f:
        countries = json.load(f,)
        pays_data = countries['continents_pays']
        for pays in pays_data:
            if pays['Two_Letter_Country_Code'].lower() == country_abr:
                return pays['Country_Name'].lower()
            if country_abr == "uk":
                return "royaume-uni"

                


def country_name(tag:Node):
    try:
        selector_resul1 = tag.css_first('.search-card-e-country-flag__wrapper')
        selector_result = selector_resul1.css_first('img')
    except AttributeError:
        logger.warning("country name not found `undefined` will be returned")
        return 'undefined'
    if selector_result is not None:
        return _from_abr_to_full_name(country_abr=selector_result.attrs.get('alt'))
 