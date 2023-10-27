# Connecting to a MySQL database to track the incident status

import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="threat_data"
)


# Defining a function to insert a record into the incident_status table
def insert_incident_tracking(incident_id, status):
    cursor = cnx.cursor()

    # Inserting the record into the incident_status table
    insert_query = "INSERT INTO incident_status (incident_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (incident_id, status))

    # Committing the changes
    cnx.commit()

    # Closing the cursor
    cursor.close()


# Defining a function to get the next available incident_id
def get_next_incident_id():
    cursor = cnx.cursor()

    # Running SQL query to get the next available incident_id
    query = "SELECT MAX(incident_id) FROM incident_status"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()[0]

    # Closing the cursor
    cursor.close()

    # Returning the next available incident_id
    if result is None:
        return 1
    else:
        return result + 1

# Defining a function to get the incident status from the incident_status table
def get_incident_status(incident_id):
    cursor = cnx.cursor()

    # Running SQL query to get the incident status
    query = f"SELECT status FROM incident_status WHERE incident_id = {incident_id}"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the incident status
    if result:
        return result[0]
    else:
        return None


if __name__ == "__main__":
    # insert_incident_tracking(12, "in progress")
    print(get_next_incident_id())
