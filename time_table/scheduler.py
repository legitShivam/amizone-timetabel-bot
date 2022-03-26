import schedule 
from time import sleep


def schedule_every_day(time, function):
    """This will run the given function every day at the specified time.

    Args:
        time (str): Time at which the given function should be executed.
        function (function): Function to be executed.
    """    
    schedule.every().day.at(time).do(function)
    while 1:
        schedule.run_pending()
        sleep(1)