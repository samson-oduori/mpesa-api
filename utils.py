
from datetime import datetime


def get_timestamp():

    # 2019-10-15 09:18:23.655596 20191015091823
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

    return formatted_time
