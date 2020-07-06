
#!C:\Users\wesin\Anaconda2019
'''
How to program in Python - Chapter 14
Connecting postgre database
Displays contents of the Actor table,
ordered by a specified field.
'''

import cgi
import sys
import psycopg2


def print_header(title):
    '''Formating header'''
    print("""Content-type: text/html
        <?xml version = "1.0" encoding = "UTF-8"?>
        <!DOCTYPE html PUBLIC
        "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "DTD/xhtml1-transitional.dtd">
        <html xmlns = "http://www.w3.org/1999/xhtml"
        xml:lang = "en" lang = "en">
        <head><title>%s</title></head>

        <body>""" % title)


def main():
    '''Main Function'''
    form = cgi.FieldStorage()

    if "sort_by" in form:
        sort_by = form["sort_by"].value
    else:
        sort_by = "first_name"

    if "sort_order" in form:
        sort_order = form["sort_order"].value
    else:
        sort_order = "ASC"

    print_header("Authors table from Books")

    try:
        conn = psycopg2.connect("dbname=dvdrental user=postgres password=root")
        #conn = psycopg2.connect(dbname="dvdrental", user="postgres", password="root")
    except psycopg2.OperationalError as error:
        print("Error", error)
        sys.exit(1)
    else:
        cursor = conn.cursor()

    cursor.execute("SELECT * FROM actor ORDER BY %s %s" %
                   (sort_by, sort_order))

    all_fields = cursor.description
    all_records = cursor.fetchall()

    cursor.close()
    conn.close()

    # output results in a table
    print("""\n<table border = "1" cellpadding = "3" >
        <tr bgcolor = "silver" >""")

    for field in all_fields:
        print("<td>%s</td>" % field[0])

    print("</tr>")

    # display each record as a row
    for actor in all_records:
        print("<tr>")
        for item in actor:
            print("<td>%s</td>" % item)
        print("</tr>")

    print("</table>")

    # obtain sorting method from user
    print("""\n<form method = "post" action = "/cap14/connecting_database.py">Sort By:<br />""")

    # display sorting options
    for field in all_fields:
        print("""<input type = "radio" name = "sort_by" value = "%s" />""" %
              field[0])
        print(field[0])
        print("<br>")

    print("""<br />\nSort Order:<br />
        <input type = "radio" name = "sort_order"
        value = "ASC" checked = "checked" />
        Ascending

        <input type = "radio" name = "sort_order"
        value = "DESC" checked = "checked" />
        Descending
        <br /><br />\n<input type = "submit" value = "SORT" />
        </form>\n\n</body>\n</html>

        """)


main()
