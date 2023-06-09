import requests

# Category descriptions
category_1 = "Details: Air quality is considered satisfactory."
category_2 = "Details: Air quality is acceptable."
category_3 = "Details: Members of sensitive groups may experience health effects."
category_4 = "Details: Everyone may begin to experience health effects."
category_5 = "Details: Health warnings of emergency conditions."
category_6 = "Details: Health alert: everyone may experience more serious health effects."
source_info = "\nSource: World Air Quality Index Project and originating EPA"

# Return category description depending on the AQI
def category_name(aqi):
  if aqi <= 50:
    return "good.\n" + category_1 + source_info
  elif aqi > 50 and aqi <= 100:
    return "moderate.\n" + category_2 + source_info
  elif aqi > 100 and aqi <= 150:
    return "unhealthy for sensitive groups.\n" + category_3 + source_info
  elif aqi > 150 and aqi <= 200:
    return "unhealthy.\n" + category_4 + source_info
  elif aqi > 200 and aqi <= 300:
    return "very unhealthy.\n" + category_5 + source_info
  else:
    return "hazardous.\n" + category_6 + source_info

# Fetch API data and return it as a string
def check_aqi(city):
  api_key = "YOUR-KEY-VALUE-HERE"
  url = f"https://api.waqi.info/feed/{city}/?token={api_key}"
  response = requests.get(url)
  json_data = response.json()
  aqi = json_data['data']['aqi']
  return f"The Air Quality Index (AQI) in {city} is {aqi}, which is " + category_name(aqi) + "."

# Enter location and print AQI information
city = input("Enter your city: ")
print(check_aqi(city))
