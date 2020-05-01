import sqlite3


def run_query(query: str) -> list:
    try:
        conn = sqlite3.connect('./chinook.db')
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        conn.close()
        return results
    except Exception as e:
        return None
    finally:
        conn.close()

# query_params = 'country:USA;city:Boston'

def generate_where(param: str) -> str:
    result = []
    if param:
        for item in param.split(';'):
            tmp = item.split(':')
            if len(tmp) == 2:
                result.append("{} = '{}'".format(tmp[0].capitalize(), tmp[1]))
        return ' WHERE ' + ' AND '.join(result)
    else:
        return ''

def ordering(query_param: str) -> str:
    result = []
    if query_param:
        for elem in query_param.split(','):
            if '-' in elem:
               result.append(f'{elem[1:].capitalize()} DESC')
            else:
                result.append(elem.capitalize())
        return ' ORDER BY ' + ', '.join(result)
    else:
        return ''

if __name__ == '__main__':
    assert ordering('country,-city') == ' ORDER BY Country, City DESC'
    assert ordering('-country,-city') == ' ORDER BY Country DESC, City DESC'
    assert ordering('') == ''
    assert generate_where('country:USA;city:Boston') == " WHERE Country = 'USA' AND City = 'Boston' "
    assert generate_where('country:USA') == " WHERE Country = 'USA' "
    assert generate_where('') == ''