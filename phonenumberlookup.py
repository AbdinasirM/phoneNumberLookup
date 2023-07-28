import requests

#the function below calls the api and validate the phone number by taking the access key, number, country code and format
def validate_phone_number(access_key, number, country_code, format):
    base_url = "http://apilayer.net/api/validate"

    # Prepare the query parameters
    params = {
        "access_key": access_key,
        "number": number,
        "country_code": country_code,
        "format": format
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None



#ask the user to enter number,country code, and country formatted code
numberInput = input("Enter a phone number: ")
countryCode = input("Enter country code: ")
countryFormatCode = input("Enter country format code: ")


#get data function
def getData(numberInput, country_code, countryFormatCode):
    if __name__ == "__main__":
        access_key = "38be72506a5bb292e42bd3cc81dcab86"
        number = numberInput
        country_code = countryCode.upper()
        format = countryFormatCode
        
        #make a call to the validator fuction and save the result in a variable data
        data = validate_phone_number(
            access_key, number, country_code, format)
        #loop through the data and print the key and value pairs        
        for key, value in data.items():
            print(f"{key}: {value}")
        return data




# print the result
result = getData(numberInput, countryCode, countryFormatCode)
def displayResult(result):
     print (result)


# displayResult(result)