import requests

def main():
    req = requests.get("https://example.com/")
    print(req.text)

if __name__ == "__main__":
    main()