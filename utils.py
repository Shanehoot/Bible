from datetime import date

def get_today_reading(reading_plan):
    today = str(date.today())
    return reading_plan.get(today, [])

def calculate_streak(progress):
    streak = 0
    for day in sorted(progress.keys(), reverse=True):
        if progress[day]:
            streak += 1
        else:
            break
    return streak

def assign_badges(progress):
    badges = []
    if len(progress) >= 7:
        badges.append("1-week streak")
    if len(progress) >= 30:
        badges.append("1-month streak")
    return badges
