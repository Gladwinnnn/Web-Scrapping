# This file is going to include method that will parse
# the specific data that we need from each one of the deal boxes
from selenium.webdriver.remote.webelement import WebElement

class BookingReport:
    def __init__(self, boxes,sction_element:WebElement):
        self.boxes_selection_element = boxes_selection_element
        self.deal_boxes = self.pull_deal_boxes()
    
    def pull_deal_boxes(self):
        return self.boxes_selection_element.find_elements_by_class_name(
            'sr_property_block'
        )

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in deal_boxes:
            hotel_name = deal_box.find_element_by_class_name(
                'sr-hotel__name'
            ).get_attribute('innerHTML').strip()

            hotel_price = deal_box.find_element_by_class_name(
                'bui-price-display__value'
            ).get_attribute('innerHTML').strip()

            hotel_score = deal_box.get_attribute('data-score').strip()

            collection.append(
                [hotel__name, hotel_price, hotel_price]
            )
        return collection