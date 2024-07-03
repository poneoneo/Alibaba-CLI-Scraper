<div align="center">
  <p>
    <a href="#"><img src="images\d.jpeg" width="600" height="300" alt="overview image" /></a>
  </p>
</div>

# Alibaba-CLI-Scraper

Is a python package that provides a dedicated CLI interface for scraping data from Alibaba.com.
The purpose of this project is to extract products and theirs related suppliers informations from Alibaba.com and store it in a local database (SQLite or MySQL). The project utilizes asynchronous requests for efficient handling of numerous requests and allows users to easily run the scraper and manage the database using a user-friendly command-line interface (CLI).

**Features:**

* **Asynchronous Scraping:** Utilizes asynchronous API of Playwright for efficient handling of numerous requests.
* **Database Integration:**  Stores scraped data in a database (SQLite or MySQL) for structured persistence.
* **User-Friendly CLI:** Provides easy-to-use commands for running the scraper and managing the database.

### Installation
to avoid any issues, with other packages  or depencies installed in your machine, this tool should be installed with pipx to create isolated environments before to run it. But i didn't found a way to allow that. Then you will need to create a virtual environment with the following command:

1. **Create virtual environment:**
   ```bash
      python -m venv scrapper
   ```

2. **Activate virtual environment:**
   ```bash
      scrapper\Scripts\activate.bat
   ```

3. **Install scraper package:**
   ```bash
      python -m pip install aba-cli-scrapper 
   ```
  
## Future Enhancements

This project has a lot of potential for growth! Here are some exciting features I'm considering for the future:

*   **Data Export:** Add functionality to export scraped data to various formats like CSV and Excel spreadsheets for easier analysis and sharing.
*   **PostgreSQL Support:**  Expand database compatibility to include PostgreSQL, giving users more database choices.
*   **Retrieval Augmented Generation (RAG):** Integrate a RAG system that allows users to ask natural language questions about the scraped data, making it even more powerful for insights.
 
## Using the CLI Interface

This project provides a user-friendly command-line interface (CLI) built with `typer` for interacting with the scraper and database. 

### Available Commands:

**Need Help?**  run  any commands followed by `--help` for detailed informations about its usage and options. For example: `python -m aba_cli_scrapper run-scrapper --help`

<div align="center">
  <p>
    <a href="#"><img src="images\run-scrapper-help-message.png" width="600" height="300" alt="command result 1" /></a>
  </p>
  <p align="center">
  </p>
</div>

The best way to learn is by practice isn't ? So let's get started with a use case example. 
Let's suppose that you want to scrape data about electric bikes from Alibaba.com.

*   **`run-scrapper`:**  Initiates scraping of Alibaba.com based on the provided keywords.
this command takes one required argument and one optional argument:
    *   **`key_words` (required):** The search term(s) for finding products on Alibaba. Enclose multiple keywords in quotes.
    *   **`--html-folder` (optional):** Specifies the directory to store the raw HTML files. If omitted, a folder with sanitized keywords as name will be automatically created.

    **Example**:
    ```bash
    python -m aba_cli_scrapper run-scrapper "electric bikes" --html-folder bike_results
    ```
if `--html-folder` option is not provided, a folder with sanitized keywords as name will be automatically created and should result to `electric_bikes` as a results folder name.
after that  `bike_results` directory has been created and should contains all html files from alibaba.com matching your keywords.

Then you must initialize a database. Mysql and sqlite are supported.
*   **`db-init`:** Creates a new database mysql/sqlite.
this command takes one required arguments and six optional arguments(depends on engine you choose):
    *   **`--engine` (required):** Choose either `sqlite` or `mysql`.
    *   **`--sqlite-file` (optional, SQLite only):**  The name for your SQLite database file (without the extension).
    *   **`--host`, `--port`, `--user`, `--password`, `--db-name` (required for MySQL):**  Your MySQL database connection details.
    *   **`--only-with` (optional Mysql):**  If you just want to update some details of your credentials in `db_credentials.json` file but not all before to initialize  an brand new database.
  
    **MySQL Example:**
    ```bash
    python -m aba_cli_scrapper db-init mysql --user "mysql_username" --password "mysql_password" --db-name "alibaba_products" 
    ```
Assuming that you have already initialized your database,and you want to created a new one without updating all your credentials, simply run :

  ```bash
  python -m aba_cli_scrapper db-init mysql --db-name "alibaba_products" --only-with 
  ```

**NB: This commands will save your credentials in `db_credentials.json` file, so when you will need to update your database, simply run `python src/app.py db-update  mysql --kw-results bike_results\` to automatically update your database and using your saved credentials**
   
  **SQLite Example:**
  ```bash
  python -m aba_cli_scrapper db-init sqlite --sqlite-file alibaba_data
  ```

As soons as your database is initialized, you can update it with the scraped data.
*   **`db-update`:** Updates your chosen database with the scraped data.
this command takes two required arguments and two optional arguments:
    *   **`--db-engine` (required):** Select your database engine: `sqlite` or `mysql`.
    *   **`--kw-results` (required):**  The path to the folder containing the HTML files generated by the `run-scrapper` command.
    *   **`--filename` (required for SQLite):** If you're using SQLite, provide the desired filename for your database. whitout any extension.
    *   **`--db-name` (optional for MySQL):** If you're using MySQL,and want to push the data to a different database, provide the desired database name.

**NB:What if you want to change something while you updating the database? Assuming that you have run another scraping command and you want to save this data in another database name whitout update credential file or rewriting all theses parameter just to change your database name then, simply run `python src/app.py db-update  mysql --kw-results another_keyword_folder_result\ --db-name "another_database_name"`.**
 

  **MySQL Example:**
  ```bash
  python -m aba_cli_scrapper db-update  mysql --kw-results bike_results\ 
  ```

  **SQLite Example:**
  ```bash
  python -m ali2b-cli-scrapper db-update  sqlite --kw-results bike_results\ --filename alibaba_data
  ```

**NB: If for any reason you encounter an issue with async api which is set by default, you can use instead sync api by specifying `--sync-api` flag cause is more stable than the other.**



## Contributions Welcome!

I believe in the power of open source! If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. I'm always open to new ideas and improvements.

## License

This project is licensed under the [Gnu General Public License Version **3**](COPYING).


  