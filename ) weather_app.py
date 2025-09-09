# weather_app.py
# uses wttr.in which returns a simple text weather report without API key
import requests

def get_weather(location=""):
    # wttr.in supports city names; returns text report
    url = f"https://wttr.in/{location}?format=3"  # short one-line
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            return resp.text.strip()
        else:
            return f"Error: status {resp.status_code}"
    except Exception as e:
        return "Error: " + str(e)

def main():
    print("Weather App (uses wttr.in, no API key required)")
    loc = input("Enter city (or leave blank for IP-based): ").strip()
    print("Fetching...")
    print(get_weather(loc))

if __name__ == "__main__":
    main()
  