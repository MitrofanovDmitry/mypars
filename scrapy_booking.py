# Import the necessary libraries
import scrapy

# Create a new Scrapy spider
class BookingSpider(scrapy.Spider):
    # Set the name of the spider
    name = 'booking_spider'

    # Set the URL of the page you want to scrape
    start_urls = ['https://www.booking.com/searchresults.html?dest_type=country&dest_id=COUNTRY_ID']

    # Define a method to parse the page
    def parse(self, response):
        # Find all the hotels on the page
        hotels = response.xpath('//div[@class="sr-hotel__content"]')

        # Loop through the hotels
        for hotel in hotels:
            # Get the name of the hotel
            name = hotel.xpath('.//span[@class="sr-hotel__name"]/text()').extract_first()

            # Get the rating of the hotel
            rating = hotel.xpath('.//span[@class="review-score-badge"]/text()').extract_first()

            # Get the number of reviews for the hotel
            reviews = hotel.xpath('.//span[@class="review-score-widget__subtext"]/text()').extract_first()

            # Get the price of the hotel
            price = hotel.xpath('.//div[@class="bui-price-display__value prco-inline-block-maker-helper"]/text()').extract_first()

            # Get the address of the hotel
            address = hotel.xpath('.//span[@class="district_link"]/text()').extract_first()

            # Save the hotel data in a dictionary
            data = {
                'name': name,
                'rating': rating,
                'reviews': reviews,
                'price': price,
                'address': address
            }

            # Yield the hotel data to be saved in the CSV file
            yield data
