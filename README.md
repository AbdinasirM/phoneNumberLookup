# Phone Number Validator App

The Phone Number Validator App is a simple Python application with a graphical user interface (GUI) that allows you to validate phone numbers using an external API. It provides a user-friendly way to check whether a given phone number is valid and retrieve information about it.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- [python-dotenv](https://pypi.org/project/python-dotenv/) library for managing environment variables.

## Getting Started

1. Clone this repository to your local machine or download the source code.

2. Install the required dependencies using pip:

pip install -r requirements.txt

javascript

3. Create a `.env` file in the same directory as your Python script (e.g., `phone_number_validator.py`). In the `.env` file, store your API access key like this:

ACCESS_KEY=your_api_access_key_here

javascript

Replace `your_api_access_key_here` with your actual API access key.

## Usage

1. Run the Phone Number Validator App:

python phone_number_validator.py

less

2. The app's GUI window will appear, allowing you to input the phone number, country code, and country format code.

3. Input your phone number, country code, and country format code in the respective fields.

4. Click the "Validate" button to initiate the validation process.

5. If the phone number is valid, you will receive a success message displaying information about the phone number in a user-friendly paragraph format.

6. If the phone number is invalid or if there is an issue with the API, you will receive an error message indicating that the validation failed. Please check your input and try again.

7. You can click the "Refresh" button to clear the input fields and start a new validation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [python-dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.
- [requests](https://pypi.org/project/requests/) library for making HTTP requests.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.

## Authors

[Mohamedwali Mumin]
[https://www.linkedin.com/in/mohamedwali-mumin-253406260/]
[Naima Mumin]
[https://www.linkedin.com/in/naima-mumin-a48750270/]
[Abdinasir Mumin]
[https://www.linkedin.com/in/abdinasir-mumin-566b30177/]