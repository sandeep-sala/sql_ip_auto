import urllib.request
import urllib.error
from lib import useragents


def gethtml(url, lastURL=False):
    """return HTML of the given url"""

    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url

    header = useragents.get()
    request = urllib.request.Request(url, None, header)
    html = None

    try:
        reply = urllib.request.urlopen(request, timeout=10)

    except urllib.error.HTTPError as e:
        if e.getcode() == 500:
            html = e.read()
        pass

    except urllib.error.URLError as e:
        pass

    except KeyboardInterrupt:
        raise KeyboardInterrupt

    else:
        html = reply.read()

    if html:
        if lastURL == True:
            return html.decode('ISO-8859-1')
        else:
            return html.decode('ISO-8859-1')

    return False
