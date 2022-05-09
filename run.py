import sqlite3
from bottle import route, run, template

from status_objects.generic_status import GenericStatus


@route('/hello')
def hello():
    return "Hello World!"


@route('/')
def hello():
    conn = sqlite3.connect('status.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("select * from status")
    x = cursor.fetchall()
    conn.close()

    results = {}
    for item in x:
        item_as_dict = dict(item)
        results[item_as_dict['name']] = item_as_dict
    print(x)
    print(results)
    output = template('make_table', results=results)
    return output


@route('/getStatus')
# @view('make_table')
def get_status():
    # todo - store in litedb, refresh on a 'refresh' endpoint
    # on home page, just load what the sqlite db has prepared

    # create parent class for all requests that go through stratus
    #     parent class can hold the method of reading the cookie value from a file

    statuses = [obj() for obj in GenericStatus.__subclasses__()]

    results = {}
    dblist = []

    for item in statuses:
        results[item.name] = vars(item)

    conn = sqlite3.connect('status.db')
    cursor = conn.cursor()

    for item in statuses:
        dblist.append([item.name, item.status, item.link, "detail"])

    cursor.executemany("INSERT OR REPLACE INTO status VALUES (?, ?, ?, ?)", dblist)
    conn.commit()
    conn.close()

    output = template('make_table', results=results)
    return output


run(host='localhost', port=8080, debug=True)
