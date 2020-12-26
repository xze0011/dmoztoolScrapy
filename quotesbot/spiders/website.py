# -*- coding: utf-8 -*-
import scrapy
import re
from quotesbot.items import QuotesbotItem
import copy
from copy import deepcopy

class websiteXPath(scrapy.Spider):
    name = 'website-xpath'
    start_urls = [
        'http://dmoztools.net/',
    ]
    next_page_url = ''
    def parse(self, response):
        for aside in response.xpath('//aside'):
            global next_page_url
            # item['category'] = re.findall(r"/(.+?)/",aside.xpath('./div/@onclick').extract_first())[0]    
            next_page_url = 'http://dmoztools.net/'+ re.findall(r"/(.+?)'",aside.xpath('./div/@onclick').extract_first())[0]  
            
            if next_page_url is not None:
                yield scrapy.Request(
                    next_page_url,
                    callback=self.nextParse) 

    def nextParse(self, response):   
        for a in response.xpath('//div[@class="cat-item"]/a'):
            third_page_url = 'http://dmoztools.net/' + (a.xpath('./@href').extract_first())[1:]
            yield scrapy.Request(
                    third_page_url,
                    callback=self.thirdParse)    

    def thirdParse(self, response):
        item = QuotesbotItem()         
        for each in response.xpath('//div[@id="doc"]'): 
            flag = each.xpath('//div[@class="title-and-desc"]/a/div/text()').extract_first()
            if flag == None:  
                continue
            else:
                item['highestCat'] = each.xpath('./section/div[2]/a[1]/text()').extract_first()
                item['subCat'] = re.findall(r"\s[a-zA-z]+\s",each.xpath('normalize-space(./section/div[2])').extract_first())[0]  
                # item['thirdCat'] = response.xpath('./section/div[2]/a[2]/text()').extract_first()  
                item['websiteName'] = each.xpath('//div[@class="title-and-desc"]/a/div/text()').extract_first()
                item['websiteUrl'] = each.xpath('//div[@class="title-and-desc"]/a/@href').extract_first()
                # yield item
                yield scrapy.Request(
                    item['websiteUrl'],
                    callback=self.UrlParse,
                    meta = {"item":item}
                ) 
                      
    def UrlParse(self, response):
        item = response.meta['item']
        item['urlTag'] = response.xpath('//head/title/text()').extract_first()
        yield item
       
                
               
              

        

        
