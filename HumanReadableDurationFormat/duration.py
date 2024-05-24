def format_duration(seconds):
    if seconds == 0:
        return 'now'
    
    year_seconds = 365 * 24 * 3600
    day_seconds = 24 * 3600
    hour_seconds = 3600
    minute_seconds = 60

    years = seconds // year_seconds
    seconds %= year_seconds
    days = seconds // day_seconds
    seconds %= day_seconds
    hours = seconds // hour_seconds
    seconds %= hour_seconds
    minutes = seconds // minute_seconds
    seconds %= minute_seconds
    
    duration = []
    if years > 0:
        duration.append(f"{years} {'year' if years == 1 else 'years'}")
    if days > 0:
        duration.append(f"{days} {'day' if days == 1 else 'days'}")
    if hours > 0:
        duration.append(f"{hours} {'hour' if hours == 1 else 'hours'}")
    if minutes > 0:
        duration.append(f"{minutes} {'minute' if minutes == 1 else 'minutes'}")
    if seconds > 0:
        duration.append(f"{seconds} {'second' if seconds == 1 else 'seconds'}")
    
    if len(duration) == 1:
        return duration[0]
    elif len(duration) == 2:
        return ' and '.join(duration)
    else:
        return ', '.join(duration[:-1]) + ' and ' + duration[-1]