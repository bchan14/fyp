from urllib2 import urlopen
from influxdb import DataFrameClient, InfluxDBClient
import argparse
import pandas as pd
from datetime import datetime
import json

def main(host = "localhost", port = 8086):
    user = "root"
    password = 'root'
    dbname = 'BTC'
    dbuser = 'me'
    dbuser_password = "password"
    query = "select EUR from BTC where EUR > 100"
    BTC = urlopen("https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms=EUR")
    response = BTC.read()
    print response
    dictResp = json.loads(response)
    print dictResp["BTC"]["EUR"]

    json_body = json_body = ([{"measurement": "BTC","fields": {"EUR": dictResp["BTC"]["EUR"]}}])


    client = InfluxDBClient(host, port, user, password, dbname)
    client.create_database(dbname)
    client.write_points(json_body, database="BTC")
    test = client.query(query)
    print test

def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False,
                        default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)
