from datetime import date, datetime

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.strftime('%d/%m/%Y')
    raise TypeError('Type %s not serializable' % type(obj))