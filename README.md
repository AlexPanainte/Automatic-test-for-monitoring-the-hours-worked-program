test app-for-monitoring-the-hours-worked-program

Background: 
This is a python program that aims to test the functionality of the program "Monitoring the hours worked "

Project content:

1.test_1: 
  -This function is used to check the user's entry in a database. 
  -It scans specified users in a list and makes an HTTP POST request to a specified URL with the user's details from the list. 
  -Then, a connection to the database is made and it is checked whether the insertion has been successfully made into the database.
  
2.test_2: 
  -This function generates random data for a CSV file, representing inputs and outputs of people by gate. 
  -The CSV file is then moved to a final directory for further verification. 
  -A connection is then made to the database and it is checked whether the data in the CSV file is present in the database.

3.test_3: 
  -This function checks if a specified file exists in the "FINAL_PROJECT/Inputs" directory and if a corresponding file exists in the "FINAL_PROJECT/Backup_Inputs" directory.

4.test_4: 
  -This function checks if there are files in the "PROJECT_FINAL/Inputs" directory that are older than 5 seconds from the current time.
  
5.Logger configuration: the logger is configured to display coloured log messages on the console and the logging level is set to DEBUG.
  -Runs the defined tests and displays the corresponding log messages for each test. At the end, depending on the score obtained, an information message is displayed.
