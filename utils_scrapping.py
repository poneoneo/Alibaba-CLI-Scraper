from sys import stderr
from types import NoneType
import unicodedata
import loguru
from selectolax.parser import Node
from typing import Literal
from loguru import logger

logger.add(stderr,colorize=True)

@logger.catch(TypeError)
def get_product_price(tag:Node,which:Literal['max','min']):
    elt =tag.css_first('.search-card-e-price-main').text()
    if '-' in elt and which=='max':
        max_price =elt.split('-')[1].split('&')[0]
        max_price = unicodedata.normalize("NFKC", max_price)
        max_price = max_price.replace('\u00a0','').replace(',','.').replace(" ","")
        return float(max_price.strip('$US'))
    elif '-' in elt and which=='min':
        min_price =elt.split('-')[0].split('&')[0]
        min_price = unicodedata.normalize("NFKC", min_price)
        min_price = min_price.replace('\u00a0','').replace(',','.').replace(" ","")
        return float(min_price.strip('$US'))
    else:
        strange_price = elt.strip(r"\xa0$US")
        price = unicodedata.normalize("NFKC", strange_price)
        price = price.replace('\u00a0','').replace(',','.').replace(" ","")
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

@logger.catch(TypeError)
def minimum_to_order(tag:Node):
    element =tag.css('.search-card-m-sale-features__item.tow-line')
    if len(element) != 0  :
        number_str=element[1].text()
        number = number_str.split()[3]
        return int(number)
    else:
        return 'undefined'
    
@logger.catch(TypeError)
def ordered_or_sold(tag:Node):
    element = tag.css_first(".search-card-e-market-power-common")
    if element is not None:
        number_str=element.text()
        number = number_str.split()[0]
        return int(number)
    else:
        return 0    