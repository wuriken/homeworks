import sqlite3


def run_query(query: str) -> list:
    try:
        conn = sqlite3.connect('./chinook.db')
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        conn.close()
        return results
    except Exception:
        return list()
    finally:
        conn.close()


def ordering(qury_param: str) -> str:
    result = []
    for elem in qury_param.split(','):
        if '-' in elem:
           result.append(f'{elem[1:].capitalize()} DESC')
        else:
            result.append(elem.capitalize())
    return ', '.join(result)

if __name__ == '__main__':
    assert ordering('country,-city') == 'Country, City DESC'
    assert ordering('') == ''