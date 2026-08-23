import scrapy

class QuotesSpider(scrapy.Spider):

    ### STEP 3.1 ADD CODE HERE ### 

    def parse(self, response):

        ### STEP 3.2 ADD CODE HERE ### 

        self.log(f"Found {len(quotes)} quotes on the page")

        # Iterate over each quote found and yield the extracted data

        ### STEP 4.1 ADD CODE HERE ### 

        # Follow pagination link (Next button)
        ### STEP 5.1 ADD CODE HERE ### 
