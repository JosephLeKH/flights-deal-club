# Flight Deals Club

This program automates the process of tracking flight prices and notifying users of the best deals. It checks airline prices using APIs and compares them to desired prices stored in a Google Sheet. If the program finds a deal, it sends email notifications to all users.

## Features

1. **Automated Flight Price Tracking**:
   - Continuously monitors flight prices based on user preferences.
   - Fetches the lowest available prices for flights to specified destinations.

2. **Google Sheet Integration**:
   - Stores destination details and desired prices in a Google Sheet.
   - Automatically updates the sheet with IATA codes if they are missing.

3. **User Notifications**:
   - Sends email alerts to all users when a deal is found.
   - Optionally sends SMS notifications to the developer.

4. **Customizable Search Parameters**:
   - Search for round-trip flights within a specific timeframe.
   - Configure maximum stopovers, duration of stay, and currency.

## Tools Used

- **Sheety API**: For interacting with Google Sheets to store user data.
- **Kiwi Flights API**: For fetching flight data.
- **Twilio API**: For sending SMS notifications.
- **SMTP**: For sending email notifications.

## How It Works

1. **Data Initialization**:
   - Fetches flight data and user preferences from the Google Sheet.
   - Ensures each destination has a valid IATA code.

2. **Flight Search**:
   - Uses the Kiwi Flights API to search for flights matching user preferences.
   - Filters results based on price, number of stopovers, and trip duration.

3. **Notification System**:
   - Sends detailed email notifications to all users.
   - Includes information about the deal, such as price, departure/arrival dates, and stopover details.
   - Optionally sends SMS alerts to the developer for immediate action.

## Requirements

- Python 3.x
- Required libraries:
  - `requests`
  - `twilio`
  - `smtplib`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flight-deals-club.git
   ```

2. Navigate to the project directory:
   ```bash
   cd flight-deals-club
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - `SHEETY_BEARER`: API key for Sheety.
   - `KIWI_APIKEY`: API key for Kiwi Flights API.
   - `TWILIO_SID`: Twilio Account SID.
   - `TWILIO_TOKEN`: Twilio Auth Token.
   - `BOT_NUMBER`: Twilio phone number for SMS.
   - `DEV_NUMBER`: Developer's phone number for SMS notifications.
   - `DEV_EMAIL`: Email address used for sending notifications.
   - `DEV_EMAIL_PASSWORD`: Password for the email account.

5. Run the application:
   ```bash
   python main.py
   ```

## File Structure

- `main.py`: The main script for orchestrating the program.
- `data_manager.py`: Handles data interactions with Google Sheets.
- `flight_data.py`: Fetches flight details.
- `flight_search.py`: Searches for flight deals using the Kiwi API.
- `notification_manager.py`: Sends notifications via email and SMS.

## Notes

- Ensure all API keys and sensitive information are stored securely in environment variables.
- Use a strong password for the email account to enhance security.
- Monitor API usage limits to avoid interruptions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
