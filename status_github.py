import http.server
import time
import socket
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from bs4 import BeautifulSoup
from urllib.request import urlopen
from prometheus_client import start_http_server
METRICS_PORT = 9000


class CustomCollector(object):
    def __init__(self):
        pass
    def collect(self):
        url = "https://www.githubstatus.com/"
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        inter=soup.findAll("div",{'data-component-id': 'br0l2tvcx85d'})
        status=inter[0].text.splitlines()
        print(status[2].strip(),status[7].strip())
        g = GaugeMetricFamily("ActionsStatus", 'Fetching status from GitHub Page', labels=['actions'])
        if (status[2].strip() == "Actions") and (status[7].strip() == "Operationali"):
            g.add_metric(["Operational"],1)
        else:
            g.add_metric(["Operational"],0)
        yield g


if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(30)
