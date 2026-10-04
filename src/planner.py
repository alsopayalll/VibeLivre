from datetime import date, timedelta


def make_plan(pages, minutes_per_day, pages_per_hour=30):

    pages_per_day = (minutes_per_day / 60) * pages_per_hour
    pages_per_day = max(1, round(pages_per_day))    

    days_needed = -(-pages // pages_per_day)    
    finish_date = date.today() + timedelta(days=days_needed)

    return {"Pages per day ": pages_per_day, "Days needed": days_needed, "Finish date": finish_date}