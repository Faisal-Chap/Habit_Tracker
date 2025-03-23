# Pixela Activity Tracker

## Overview
This Python script interacts with the Pixela API to track daily activities, such as walking distance. Users can create a Pixela account, set up a graph, and log their activities using a command-line interface.

## Features
- Create a Pixela user account
- Create a graph to track activities
- Log daily activities (e.g., distance walked in km)
- Delete an activity entry
- Edit an existing activity entry
- View today's activity data

## Requirements
- Python 3
- `requests` library (install using `pip install requests`)
- A Pixela account

## Setup
1. **Create a Pixela account** at [Pixela](https://pixe.la/).
2. **Generate a token** and update the script variables:
   - `user_name = "your_pixela_username"`
   - `token = "your_pixela_token"`
   - `graph_id = "your_graph_id"`
3. **Run the script** using:
   ```sh
   python script.py
   ```

## Usage
- When running the script, you will be prompted with options:
  1. **Post your activity** - Add a new entry for a specific date.
  2. **Delete an activity** - Remove an entry by specifying the date.
  3. **Edit an activity** - Modify the logged value for a specific date.
  0. **Exit the program**
- The script will automatically check if today's activity has been logged and prompt you accordingly.

## API Endpoints Used
- `https://pixe.la/v1/users` - Create a new Pixela user
- `https://pixe.la/v1/users/{user_name}/graphs` - Create a graph
- `https://pixe.la/v1/users/{user_name}/graphs/{graph_id}` - Post activity data
- `https://pixe.la/v1/users/{user_name}/graphs/{graph_id}/{date}` - Get, update, or delete an entry

## Notes
- Ensure you replace placeholder values (`your_pixela_username`, `your_pixela_token`, `your_graph_id`) with actual values.
- The script currently tracks distance in **kilometers** (`km`). Modify it in the `create_graph` function if needed.
- If an error occurs, check the API response messages printed in the terminal.

## Author
Faisal Zia

## License
This project is open-source under the MIT License.

