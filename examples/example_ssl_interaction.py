import os
import requests
import sys

current_file_path = os.path.abspath(__file__)
examples_folder = os.path.dirname(current_file_path)
app_folder = os.path.dirname(examples_folder)

sys.path.append(app_folder)

from operator_client import Operator


def main():
    hostname = "https://localhost"

    port = "5432"
    full_url = f"{hostname}:{port}/v1/architect/health"
    cert_file = "C:\AgentSmith\ssl\selfsigned.crt"
    cert_data = None

    with open(cert_file, "r") as f:
        cert_data = f.read()

    # https
    client = Operator(hostname, port=port, certificate=cert_data, verbose=True)
    response1 = client.architect.get_health()

    # Regular http
    client = Operator("http://127.0.0.1", port="5000", verbose=True)
    response2 = client.architect.get_health()


if __name__ == "__main__":
    main()
