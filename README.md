# Alibaba-CLI-Scraper

This  project is a Python-based web scraper for scraping data from Alibaba.com. The purpose of this project is to extract products and theirs related suppliers informations from Alibaba.com and store it in a local database (SQLite or MySQL). The project utilizes asynchronous requests for efficient handling of numerous requests and allows users to easily run the scraper and manage the database using a user-friendly command-line interface (CLI) 

**Features:**

* **Asynchronous Scraping:** Utilizes asynchronous API of Playwright for efficient handling of numerous requests.
* **Database Integration:**  Stores scraped data in a database (SQLite or MySQL) for structured persistence.
* **User-Friendly CLI:** Provides easy-to-use commands for running the scraper and managing the database.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/poneoneo/Alibaba-CLI-Scrapper.git
   ```

2. **Go to the project directory:**
   ```bash
   cd Alibaba-CLI-Scraper/
   ```

3. **Create a virtual environment:**
   ```bash
   python3 -m venv cli_scraper_env
    or
   python -m venv cli_scraper_env
   ```

4. **Activate the virtual environment:**
   ```bash
   (linux or mac os) source cli_scraper_env/bin/activate
   (windows) cli_scraper_env\Scripts\activate
   ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Behind the Scene: How I Tackled Web Scraping Challenges

Developing a web scraper comes with its own set of hurdles, and this project was no exception! Here's how I overcame some common obstacles:

### The Challenges

* **IP Blocking:**  Websites often block requests coming from the same IP address repeatedly, suspecting automated activity. 
* **User-Agent Blocking:**  Identifying a scraper by its user-agent string (which reveals it's not a regular browser) is another common tactic.
* **Pagination Bottleneck:** For a single keyword, Alibaba often returns numerous search results spread across multiple pages. Fetching data from each page sequentially would take far too long.

### My Solution

To overcome these challenges, I leveraged the power of three key tools and techniques:

1. **Playwright and Asynchronous Requests:** I used Playwright, a powerful Python library, to simulate a real web browser. But I took it a step further! By harnessing Playwright's asynchronous API alongside Python's `asyncio` library, I could fetch data from multiple pages concurrently. For instance, if a search yielded 42 pages of results, my scraper would send requests to all 42 pages simultaneously and process the HTML content as each page loaded, rather than waiting for each page to load one by one. This drastically sped up the scraping process.

2. **BrightData:** This is where BrightData came in! They provide a robust proxy network that routes my requests through different IPs, effectively bypassing IP blocks. It's like a cloak of anonymity for my scraper!

   * BrightData's expertise in handling anti-scraping measures was crucial to this project's success. 

   * To make things easier for you, I've included my BrightData credentials in the code. Please note that these might have limited usage. If you encounter issues with the `run-scrapper` command, you can easily create a free BrightData account (they offer $5 credit!) and plug in your own credentials. 

     [Get started with BrightData](https://brightdata.com/) 

---
## Using the CLI Interface

This project provides a user-friendly command-line interface (CLI) built with `typer` for interacting with the scraper and database. 

### Available Commands:

**Need Help?**  Type the any commands followed by `--help` for detailed information about its usage and options. For example: `python src/app.py run-scrapper --help`

<div align="center">
  <p>
    <a href="#"><img src="images\run-scrapper-help-message.png" width="600" height="300" alt="pytube logo" /></a>
  </p>
  <p align="center">
  </p>
</div>

The best way to learn is by practice isn't ? So let's get started with a use case example. 
Let's suppose that you want to scrape data about electric bikes from Alibaba.com.

*   **`run-scrapper`:**  Initiates scraping of Alibaba.com based on the provided keywords.

    ```bash
    python src/app.py run-scrapper "electric bikes" --html-folder bike_results
    ```
if `--html-folder` is not provided, a folder with sanitized keywords as name will be automatically created and should result to `electric_bikes` as a results folder name.
after that  `bike_results` directory has been created and should contains all html files from alibaba.com matching your keywords.
    *   **`key_words` (required):** The search term(s) for finding products on Alibaba. Enclose multiple keywords in quotes.
    *   **`--html-folder` (optional):** Specifies the directory to store the raw HTML files. If omitted, a folder with sanitized keywords as name will be automatically created.
  
Then you must initialize a database. Mysql and sqlite are supported.
*   **`db-init`:**  Configures the database connection settings.

    **MySQL Example:**
    ```bash
    python src/app.py db-init mysql --user your_username --password your_password --db-name alibaba_products 
    ```
**NB: This commands will save your credentials in `db_credentials.json` file, so when you will need to update your database, simply run `python src/app.py db-update  mysql --kw-results bike_results` to automatically update your database. What if you want to change something while you update the database? Assuming that you have run another scraping command and you to save this data in another schema whitout update credential file your rewriting all theses parameter just to change your database name then, simply run `python src/app.py db-update  mysql --kw-results another_keyword_folder_result --db-name another_database_name`.**
   
    **SQLite Example:**
    ```bash
    python src/app.py db-init sqlite --sqlite-file alibaba_data
    ```
    *   **`--engine` (required):** Choose either `sqlite` or `mysql`.
    *   **`--sqlite-file` (optional, SQLite only):**  The name for your SQLite database file (without the extension).
    *   **`--host`, `--port`, `--user`, `--password`, `--db-name` (required for MySQL):**  Your MySQL database connection details.

As soons as your database is initialized, you can update it with the scraped data.
*   **`db-update`:** Updates your chosen database with the scraped data.
**NB: If for any reason you encounter an issue with async api which is set by default, you can use instead sync api by specifying `--sync-api` flag cause is more stable than the other.**

    **MySQL Example:**
    ```bash
    python src/app.py db-update  mysql --kw-results bike_results 
    ```

    **SQLite Example:**
    ```bash
    python src/app.py db-update  sqlite --kw-results bike_results --filename alibaba_data
    ```

    *   **`--db-engine` (required):** Select your database engine: `sqlite` or `mysql`.
    *   **`--kw-results` (required):**  The path to the folder containing the HTML files generated by the `run-scrapper` command.
    *   **`--filename` (required for SQLite):** If you're using SQLite, provide the desired filename for your database. whitout any extension.


## Future Enhancements

This project has a lot of potential for growth! Here are some exciting features I'm considering for the future:

*   **Data Export:** Add functionality to export scraped data to various formats like CSV and Excel spreadsheets for easier analysis and sharing.
*   **PostgreSQL Support:**  Expand database compatibility to include PostgreSQL, giving users more database choices.
*   **Retrieval Augmented Generation (RAG):** Integrate a RAG system that allows users to ask natural language questions about the scraped data, making it even more powerful for insights.

## Contributions Welcome!

I believe in the power of open source! If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. I'm always open to new ideas and improvements.

## License

This project is licensed under the [Gnu General Public License Version **3**](COPYING).


  