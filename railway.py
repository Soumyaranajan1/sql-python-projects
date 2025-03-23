import mysql.connector

while True:
    print("""
    ================================
         WELCOME TO RAILWAY MANAGEMENT SYSTEM
    ================================
    1. Add Train Details
    2. View Train Details
    3. Book Ticket
    4. Cancel Ticket
    5. View Booked Tickets
    6. Exit
    ================================
    """)

    # Database connection
    try:
        passwd = input("ENTER THE DATABASE PASSWORD: ")
        db = mysql.connector.connect(host="localhost", user="root", passwd="enter your database password", auth_plugin='caching_sha2_password')
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS railway_management")
        cursor.execute("USE railway_management")
        
        # Creating required tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS trains (
                train_id INT PRIMARY KEY,
                train_name VARCHAR(50),
                source VARCHAR(50),
                destination VARCHAR(50),
                available_seats INT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                ticket_id INT PRIMARY KEY AUTO_INCREMENT,
                train_id INT,
                passenger_name VARCHAR(50),
                age INT,
                contact_number VARCHAR(15),
                FOREIGN KEY (train_id) REFERENCES trains(train_id)
            )
        """)
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        break

    choice = input("Enter your choice: ")
    
    if choice == "1":
        # Add Train Details
        try:
            train_id = int(input("Enter Train ID: "))
            train_name = input("Enter Train Name: ")
            source = input("Enter Source Station: ")
            destination = input("Enter Destination Station: ")
            available_seats = int(input("Enter Available Seats: "))
            
            query = "INSERT INTO trains (train_id, train_name, source, destination, available_seats) VALUES (%s, %s, %s, %s, %s)"
            values = (train_id, train_name, source, destination, available_seats)
            cursor.execute(query, values)
            db.commit()
            print("Train details added successfully!")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "2":
        # View Train Details
        try:
            cursor.execute("SELECT * FROM trains")
            for train in cursor.fetchall():
                print(train)
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "3":
        # Book Ticket
        try:
            train_id = int(input("Enter Train ID: "))
            passenger_name = input("Enter Passenger Name: ")
            age = int(input("Enter Age: "))
            contact_number = input("Enter Contact Number: ")
            
            cursor.execute("SELECT available_seats FROM trains WHERE train_id = %s", (train_id,))
            result = cursor.fetchone()
            if result and result[0] > 0:
                query = "INSERT INTO tickets (train_id, passenger_name, age, contact_number) VALUES (%s, %s, %s, %s)"
                values = (train_id, passenger_name, age, contact_number)
                cursor.execute(query, values)
                cursor.execute("UPDATE trains SET available_seats = available_seats - 1 WHERE train_id = %s", (train_id,))
                db.commit()
                print("Ticket booked successfully!")
            else:
                print("No available seats on this train.")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "4":
        # Cancel Ticket
        try:
            ticket_id = int(input("Enter Ticket ID: "))
            cursor.execute("SELECT train_id FROM tickets WHERE ticket_id = %s", (ticket_id,))
            result = cursor.fetchone()
            if result:
                train_id = result[0]
                cursor.execute("DELETE FROM tickets WHERE ticket_id = %s", (ticket_id,))
                cursor.execute("UPDATE trains SET available_seats = available_seats + 1 WHERE train_id = %s", (train_id,))
                db.commit()
                print("Ticket canceled successfully!")
            else:
                print("Ticket not found.")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "5":
        # View Booked Tickets
        try:
            cursor.execute("SELECT * FROM tickets")
            for ticket in cursor.fetchall():
                print(ticket)
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "6":
        print("Exiting Railway Management System. Goodbye!")
        db.close()
        break

    else:
        print("Invalid choice. Please try again.")
