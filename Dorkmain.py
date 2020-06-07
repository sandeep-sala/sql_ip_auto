from lib.sql import SQL
from lib.display import Display


dork = 'index.php?id='
display = Display()
sql = SQL(dork, '-w')


def start():
    display.primary('"Dork: ' + dork)

    try:
        sql.start()
    except KeyboardInterrupt:
        pass
    finally:
        stop()


def stop():
    if sql:
        sql.stop()
    else:
        display.shutdown()


