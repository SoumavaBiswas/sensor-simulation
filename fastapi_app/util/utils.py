import datetime
import logging

datetime_format = '%Y-%m-%dT%H:%M:%SZ'


def is_valid_datetime(datetime_string):
    try:
        datetimeObject = datetime.datetime.strptime(
            datetime_string, datetime_format)
        return True
    except ValueError:
        logging.debug(
            f"Given datetime is {datetime_string} not in valid format. Please input date in TZ format.")
        return False
