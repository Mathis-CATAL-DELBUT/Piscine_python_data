from datetime import datetime

reference_datetime = datetime(1970, 1, 1)
now = datetime.now()

time_difference = now - reference_datetime
seconds_since_reference = time_difference.total_seconds()

formatted_seconds = "{:,.4f}".format(seconds_since_reference)
scientific_notation = "{:.2e}".format(seconds_since_reference)

current_date = now.strftime("%b %d %Y")
reference_datetime_month = reference_datetime.strftime("%B")
reference_datetime_year = reference_datetime.year
reference_datetime_day = reference_datetime.day

print(
    f"Seconds since {reference_datetime_month} {reference_datetime_day},\
{reference_datetime_year}: \
{formatted_seconds} or {scientific_notation} in scientific notation"
)

print(current_date)
