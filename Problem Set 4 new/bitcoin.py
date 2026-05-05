import requests
import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument.")
    n = float(sys.argv[1])
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=a4897358d0af3175d3fbf61052cb842fe21ad6b48000c6b8e0c72c30ba2233e4")
        
    data = response.json()
    result = float(data["data"]["priceUsd"]) * n
    print(f"${result:,.4f}")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("Network error")