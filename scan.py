import urllib.parse
from lib import web
import bs4
from lib import sqlerrors

get_link = ''


def sqli(url):
    """check SQL injection vulnerability"""

    print("scanning {}".format(url), end="")

    domain = url.split("?")[0]  # domain with path without queries
    print("\nDomain : ")
    print(domain)
    queries = urllib.parse.urlparse(url).query.split("&")
    print("Queries : ")
    print(queries)
    # no queries in url
    if not any(queries):
        print("")    # move cursor to new line
        return False, None

    payloads = ("'", "')", "';", '"', '")', '";', '`', '`)', '`;', '\\', "%27", "%%2727", "%25%27", "%60", "%5C")
    for payload in payloads:
        website = domain + "?" + ("&".join([param + payload for param in queries]))
        source = web.gethtml(website)
        if source:
            vulnerable, db = sqlerrors.check(source)
            if vulnerable and db != None:
                print(":::      Site is Vulnerable      :::")
                return True, db

    print("")  # move cursor to new line
    return False, None


def getserverinfo(url):
    """get server name and version of given domain"""

    url = urllib.parse.urlparse(url).netloc if urllib.parse.urlparse(url).netloc != '' else urllib.parse.urlparse(url).path.split("/")[0]

    info = []  # to store server info
    url = "https://aruljohn.com/webserver/" + url

    try:
        result = web.gethtml(url)
    except KeyboardInterrupt:
        raise KeyboardInterrupt

    try:
        soup = bs4.BeautifulSoup(result, "lxml")
    except:
        return ['', '']

    if soup.findAll('p', {"class": "err"}):
        return ['', '']

    for row in soup.findAll('tr'):
        if row.findAll('td', {"class": "title"}):
            info.append(row.findAll('td')[1].text.rstrip('\r'))

    return info


def start():
    vulnerables = sqli(get_link)
    file = open('scan.txt', "w")
    file.write(":::          Site  is Vulnerable     :::\n")
    if not vulnerables:
        file.write("::: Site is not Vulnerable ::::")

    file.write("Url Name_______________ :::\n")
    file.write(":::" + get_link + ":::\n")

    file.write("DataBase Name__________ :::\n")
    file.write(str(vulnerables)+'\n')
    print(vulnerables)
    server_data = getserverinfo(get_link)
    file.write("Server Name____________ :::\n")
    file.write(str(server_data)+'\n')
    file.write("::: ___________________ :::\n")


#start(input("url:  "))

