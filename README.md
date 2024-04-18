

This Python script is designed to track and record workout sessions. Here's a breakdown of its functionality:
* 		Importing Necessary Libraries: The script imports the required libraries such as requests for making HTTP requests and datetime for working with dates and times.
* 		Setting Environment Variables: The APP_ID, API_KEY, and SHEET_ENDPOINT are typically sensitive information. Instead of hardcoding them in the script, they are fetched from environment variables for security reasons.
* 		User Input: The script prompts the user to input a description of the exercises they performed.
* 		Nutritionix API Integration: The exercise description provided by the user is sent as a POST request to the Nutritionix API (https://trackapi.nutritionix.com/v2/natural/exercise) along with the provided app ID and API key for authentication. The API then processes the text and returns details about the exercises, such as duration and calories burned.
* 		Google Sheets Integration: The script then posts the workout data to a Google Sheet using the Sheety API. The Google Sheet endpoint is fetched from the environment variables. The workout details include the date, time, exercise name, duration, and calories burned for each exercise.
* 		Output: The script prints the response received from the Sheety API, indicating whether the workout data was successfully recorded.
By using this script, users can conveniently track their workout sessions by simply inputting the exercises they performed, and the script handles the rest, automatically updating the workout details in a Google Sheet.










<img width="1437" alt="Screenshot 2024-04-18 at 17 01 39" src="https://github.com/HesamFarjad/Workout_Tracking/assets/81914229/6ff20cf4-052a-4ce2-9ca2-8caf7771a9d8">
