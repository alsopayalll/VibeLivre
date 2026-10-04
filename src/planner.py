from datetime import date, timedelta


def make_plan(pages, minutes_per_day, pages_per_hour=30):

    pages_per_day = (minutes_per_day / 60) * pages_per_hour
    pages_per_day = max(1, round(pages_per_day))    

    days_needed = -(-pages // pages_per_day)    
    finish_date = date.today() + timedelta(days=days_needed)

    return {"pages_per_day": pages_per_day, "days_needed": days_needed, "finish_date": finish_date, "bail_out_page": 30}