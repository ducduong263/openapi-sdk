#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from dnse import DNSEClient


def main():
    client = DNSEClient(
        api_key="eyJvcmciOiJkbnNlIiwiaWQiOiIwZGE3YjYxMTE0ZTQ0YmIxYmRkODVjZDJmNmJlYmQzZCIsImgiOiJtdXJtdXIxMjgifQ==",
        api_secret="ez3nn4GvOSgDFuFyVbAUc1NU6Ucbhm9ZUxutgZmNnc3EZ9wFZ6jo6du8Ip-TU9Ml6e9cv-VPLupx3C-DEZPMCQ",
        base_url="https://openapi-uat.dnse.com.vn",
    )

    status, body = client.get_execution_detail(
        account_no="0001000115",
        order_id="66",
        market_type="DERIVATIVE",
        order_category="NORMAL",
        dry_run=False,
    )
    print(status, body)


if __name__ == "__main__":
    main()
