<div align="center">
  <p>
    <a href="#"><img src="images\d.jpeg" width="600" height="300" alt="overview image" /></a>
  </p>
</div>

# Alibaba-CLI-Scraper

Is a python package that provides a dedicated CLI interface for scraping data from Alibaba.com.
The purpose of this project is to extract products and theirs related suppliers informations from Alibaba.com and store it in a local database (SQLite or MySQL). The project utilizes asynchronous requests for efficient handling of numerous requests and allows users to easily run the scraper and manage the database using a user-friendly command-line interface (CLI).


### Installation
It's recommended to use [pipx](https://pypa.github.io/pipx/) instead of pip for end-user applications written in Python. `pipx` installs the package, exposes his CLI entrypoints in an isolated environment and makes it available everywhere this guarantees no dependency conflicts and clean uninstall. If you'd like to use `pip` instead, just replace `pipx` with `pip`  but obviously  as usual you'll need to  create a virtual environment and activate it before to use `aba-cli-scrapper` to avoid any dependency conflicts issues. let's install `aba-cli-scrapper` using pipx:

   ```shell
      pipx install aba-cli-scrapper
   ```

  
## Using the CLI Interface
 

### Available Commands:
**Need Help?**  run  any commands followed by `--help` for detailed informations about its usage and options. For example: `aba-run --help` will show you all subcommands available and how to use them.

<div align="center">
  <p>
    <a href="#"><img src="images\use-help.png" width="900" height="340" alt="command result 1" /></a>
  </p>
  <p align="center">
  </p>
</div>

**Warnings:** 
- `aba-run` is the base command means all other commands that will be introduce bellow are sub-commands and should always be preceded by  `aba-run`.
  
- asynchronous requests are used by default, but is not available for moment  cause bright-data api has been exhausted. Instead you can use sync api by specifying `--sync-api` or `-sa` flag parameter with **`scraper`** sub-command is works perfecly fine. So let's jump to the tutorial.

Practice make perfect isn't ? So let's get started with a use case example. 
Let's assume  that you want to scrape data about `electric bikes` from Alibaba.com.



<details>
<summary>Scraper Demo</summary>

[https://user-images.githubusercontent.com/49741340/238535232-459847af-a15c-4d9b-91ac-fab9958bc74f.mp4](https://private-user-images.githubusercontent.com/52409392/351958081-302e7586-7e73-495f-bb40-41b8002c0480.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE4ODE5NTUsIm5iZiI6MTcyMTg4MTY1NSwicGF0aCI6Ii81MjQwOTM5Mi8zNTE5NTgwODEtMzAyZTc1ODYtN2U3My00OTVmLWJiNDAtNDFiODAwMmMwNDgwLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI1VDA0MjczNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQwZjlhM2I5ODk5ZjYzYmRhNmI5OWJhMzMxMDU2MGQ4NTBiZTk0OTAzNDg5M2M3NTU1M2NhYzFkYTc1YzQ5YzcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.xOTTGRRU8UQ8YZFMegl_TJC6kvtCR4aQEwJyp_DAjjk)

</details>


*   **`scraper` sub-command:**  Initiates scraping of Alibaba.com based on the provided keywords.
this command takes two required arguments and one optional argument:
    * -  **`key_words` (required):** The search term(s) for finding products on Alibaba. Enclose multiple keywords in quotes.
    * - **`--page-results` or `-pr` (required):** Usually keys words will results to many pages macthing them. Then you must to indicate how many of them you want to pull out.If any value is not provided `10` will be used by default.
    * -  **`--html-folder` or `-hf` (optional):** Specifies the directory to store the raw HTML files. If omitted, a folder with sanitized keywords as name will be automatically created. In this case `electric_bikes` will be used as a results folder name.

    **Example**:
    ```shell
    aba-run scraper "electric bikes" -hf "bike_results" -pr 15
    ```
by default `scrapper` will use async which is as explained unstable. then if you want to use sync api run:
   ```bash
   aba-run scraper "electric bikes" -hf "bike_results" -pr 15  --sync-api
   ```
    and voila! 

Now `bike_results` (since you already provided name you wish to have) directory has been created and should contains all html files from alibaba.com matching your keywords.

<details>
<summary>db-init Demo</summary>

https://user-images.githubusercontent.com/49741340/238535232-459847af-a15c-4d9b-91ac-fab9958bc74f.mp4

</details>
Then you must initialize a database. Mysql and sqlite are supported.

*   **`db-init` sub-command:** Creates a new database mysql/sqlite.
this command takes one required arguments and six optional arguments(depends on engine you choose):
    * -   **`engine` (required):** Choose either `sqlite` or `mysql`.
    *  - **`--sqlite-file` or `-f`(optional, SQLite only):**  The name for your SQLite database file (without any extension).
    *   - **`--host` or `-h`, `--port` or `-p`, `--user` or `-u`, `--password` or `-pw`, `--db-name`or `-db` (required for MySQL):**  Your MySQL database connection details.
  
    *   **`--only-with` or `-ow`(optional Mysql):**  If you just want to update some details of your credentials in `db_credentials.json` file but not all before to initialize a brand new database.
* **NB:** `--host` and `--port` are respectively set to `localhost` and `3306` by default. 

**MySQL Use case:**
  ```shell
  aba-run db-init mysql -u "mysql_username" -pw "mysql_password" -db "alibaba_products" 
  ```
Assuming that you have already initialized your database,and you want to created a new one with a new database name without to set password and username again , simply run :

  ```shell
  aba-run db-init mysql --only-with -db "alibaba_products" 
  ```

**NB: When you initialize your mysql as engine, the `db-init` sub-command will save your credentials in `db_credentials.json` file, so when you will need to update your database, simply run `aba-run db-update  mysql --kw-results bike_results\` to automatically update your database by using your saved credentials**


**SQLite Use case :**
  ```shell
  aba db-init sqlite --sqlite-file alibaba_data
  ```

As soons as your database has been initialized, you can update it with the scraped data.

<details>
<summary>db-update Demo</summary>

https://user-images.githubusercontent.com/49741340/238535232-459847af-a15c-4d9b-91ac-fab9958bc74f.mp4

</details>

*  **`db-update` sub-command:** add scraped data from html files to your database (you can't use this command twice with same database credentals to avoid UNIQUE CONSTRAINT ERROR).

this command takes two required arguments and two optional arguments:
   * - **`--db-engine` (required):** Select your database engine: `sqlite` or `mysql`.
   * -  **`--kw-results` (required):**  The path to the folder containing the HTML files generated by the `scraper` sub command.
   * - **`--filename` (required for SQLite):** If you're using SQLite, provide the desired filename for your database. whitout any extension.
   * - **`--db-name` (optional for MySQL):** If you're using MySQL,and want to push the data to a different database, provide the desired database name.

  **MySQL Use case:**
  ```bash
  aba-run db-update  mysql --kw-results bike_results\ 
  ```
**NB:What if you want to change something while you updating the database? Assuming that you have run another scraping command and you want to save this data in another database name whitout update credential file or rewriting all theses parameter just to change your database name then, simply run `aba-run db-update  mysql --kw-results another_keyword_folder_result\ --db-name "another_database_name"`.**

  **SQLite Use case:**
   ```shell
   aba-run db-update  sqlite --kw-results bike_results\ --filename alibaba_data
   ```

**Features:**

* **Asynchronous Scraping:** Utilizes asynchronous API of Playwright for efficient handling of numerous pages results.
* **Database Integration:**  Stores scraped data in a database (SQLite or MySQL) for structured persistence.
* **User-Friendly CLI:** Provides easy-to-use commands for running the scraper and managing the database.

## Future Enhancements

This project has a lot of potential for growth! Here are some exciting features I'm considering for the future:

*   **Data Export:** Add functionality to export scraped data to various formats like CSV and Excel spreadsheets for easier analysis and sharing.
*   **Retrieval Augmented Generation (RAG):** Integrate a RAG system that allows users to ask natural language questions about the scraped data, making it even more powerful for insights.

## Contributions Welcome!

I believe in the power of open source! If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. I'm always open to new ideas and improvements.

## License

This project is licensed under the [Gnu General Public License Version **3**](COPYING).


  
