
# Railway Management System
![a-railway-management-system-project-requ_hdhefQi9R9WbQw7b9hTxkg_0y3fezsLQiS3gqpLmI6yFQ](https://github.com/user-attachments/assets/11dcd619-360c-43a5-8b94-268b0d6a7238)

## Overview
The Railway Management System is a console-based application designed to manage train details and ticket bookings efficiently. It provides features for adding train details, booking and canceling tickets, and viewing booked tickets.

## Features
- **Add Train Details**: Store train information including ID, name, source, destination, and available seats.
- **View Train Details**: Retrieve and display train information.
- **Book Ticket**: Reserve a seat for a passenger.
- **Cancel Ticket**: Remove a booked ticket and update seat availability.
- **View Booked Tickets**: Display all booked tickets.

## Technologies Used
- Python
- MySQL (for database management)
- MySQL Connector for Python

## Installation
1. **Install MySQL Server**
   - Ensure MySQL is installed and running.
   - Create a database named `railway_management` (or it will be created automatically).

2. **Install Required Python Packages**
   ```sh
   pip install mysql-connector-python
   ```

3. **Run the Script**
   ```sh
   python railway.py
   ```
   - Enter the MySQL root password when prompted.
   - Follow the menu options to interact with the system.

## Database Schema
### Tables:
- **trains**:
  - `train_id` (INT, Primary Key)
  - `train_name` (VARCHAR)
  - `source` (VARCHAR)
  - `destination` (VARCHAR)
  - `available_seats` (INT)

- **tickets**:
  - `ticket_id` (INT, Primary Key, Auto-Increment)
  - `train_id` (INT, Foreign Key referencing trains)
  - `passenger_name` (VARCHAR)
  - `age` (INT)
  - `contact_number` (VARCHAR)

## Usage
1. **Start the application**.
2. **Follow the menu instructions** to add trains, book or cancel tickets, and view information.
3. **Exit the application** when done.

## Future Enhancements
- Implement a graphical user interface (GUI).
- Add user authentication for secure access.
- Improve error handling and logging.

## License
This project is open-source and available for modifications and enhancements.

## Contact
For any queries or support, contact:
- **Email**:spaikaray24@gmail.com
- **Phone**: 6371547578

