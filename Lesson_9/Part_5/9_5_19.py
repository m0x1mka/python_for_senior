from datetime import datetime, date

d = {'ru': '%d.%m.%Y',
     'us': '%m-%d-%Y',
     'ca': '%Y-%m-%d',
     'br': '%d/%m/%Y',
     'fr': '%d.%m.%Y',
     'pt': '%d-%m-%Y', }


def date_formatter(data):
    def format_data(date):
        return datetime.strftime(date, d[data])

    return format_data
