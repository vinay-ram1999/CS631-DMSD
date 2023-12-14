# 📦 Streamlit App Starter Kit 
```
⬆️ (eComputerStore)
```

Analyze, design, implement, and document a database system application. To know more about the project please go to `Project/` directory.

**Note**: The application only works on the local system (URL: http://localhost:8501) and it must be connected to the NJIT network to access the MySQL database on phpMyAdmin server.

# To run the application:

1. Clone this Git repository to your local machine and install the python libraries listed in `requirements.txt`.
2. Request a MySQL account using MyUCID if dont have one (https://ist.njit.edu/database-password-assistant).
3. Login to your MySQL account using server `sql1.njit.edu` and follow the SQL commands on `db_commands.txt` to create the database, tables and populate the tables.
4. To know more about the schema look into `pages/docs/DB_schema.png`.
5. Create a `secrets.toml` file in `.sreamlit/` directory and store your MySQl account credentials as shown below:
    ```
    db_username = "UCID"
    db_password = "MySQL Account Passowrd"
    ```
6. To run the application use the command:
    ```
    streamlit run Home.py --server.port 8501
    ```

## Demo App

**Note**: This url does not work since the streamlit servers are remotely located and cannot access the NJIT network.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ecomputerstore.streamlit.app/)
