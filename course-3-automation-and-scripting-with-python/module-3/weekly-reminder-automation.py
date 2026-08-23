import schedule


def send_daily_reminder():
    print("Don't forget to update the project status in the tracking tool!")


def send_weekly_reminder():
    print("Reminder: Weekly team meeting today at 9:00 AM!")


def calculate_volunteer_hours():
    print("Calculating volunteer hours. Results will be emailed!")


# Schedule the daily reminder for every day at 10 AM
schedule.every().day.at("10:00").do(send_daily_reminder).tag("reminders")

# Schedule the weekly reminder for every Monday at 9 AM
schedule.every().monday.at("09:00").do(send_weekly_reminder).tag("reminders")

# Schedule the volunteer hour calculations to be done at 11:59 PM Tuesday and Friday (2 lines of code)
schedule.every().tuesday.at("23:59").do(calculate_volunteer_hours)
schedule.every().friday.at("23:59").do(calculate_volunteer_hours)

print("Starting the reminder system...")
print("Currently scheduled tasks:")

# Print out current list of scheduled jobs
for job in schedule.get_jobs():
    print(job)

# Instructions to start the scheduler
run_scheduler()