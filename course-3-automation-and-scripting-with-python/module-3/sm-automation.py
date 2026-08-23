import schedule
import time
import schedule
def promote_product():
### YOUR CODE HERE ###
 def promote_product():
    print(
        "Posting to Twitter: New product alert! Check out https://www.example.com/new-product #newproduct"
    )
    print(
        "Posting to Facebook:  Our latest product is finally here! https://www.example.com/new-product"
    )
# Schedule the promotional social media posts for every day at 10 AM
### YOUR CODE HERE ###
schedule.every().day.at("10:00").do(promote_product)

# Schedule the promotional social media posts for every day at 4 PM
### YOUR CODE HERE ###
schedule.every().day.at("16:00").do(promote_product)
# Instruction to start the scheduler
run_scheduler()