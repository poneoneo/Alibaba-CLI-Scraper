<div align="center">
  <p>
    <a href="#"><img src="images\image.png" width="300" height="300" alt="overview image" /></a>
  </p>
</div>
<p align="center">  <b>Alibaba-CLI-Scraper</b> </p>
<p align="center"> 🛒-💻- 🕸 </p>

---

<p align="center"> <b>Create your own Alibaba dataset at lightning speed.</b> </p>
<div align="center">

![GitHub Release Date](https://img.shields.io/github/release-date/poneoneo/Alibaba-CLI-Scrapper) ![GitHub License](https://img.shields.io/github/license/poneoneo/Alibaba-CLI-Scrapper) ![PyPI - Downloads](https://img.shields.io/pypi/dw/aba-cli-scrapper?label=PyPI-Downloads)  ![PyPI - Version](https://img.shields.io/pypi/v/aba-cli-scrapper) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aba-cli-scrapper)  

</div>


<div align="center">
https://private-user-images.githubusercontent.com/52409392/358079417-c32f7958-cba6-40ca-880d-6365318df15e.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjM2OTA5MDEsIm5iZiI6MTcyMzY5MDYwMSwicGF0aCI6Ii81MjQwOTM5Mi8zNTgwNzk0MTctYzMyZjc5NTgtY2JhNi00MGNhLTg4MGQtNjM2NTMxOGRmMTVlLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODE1VDAyNTY0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTAwMzAxNWFlZDAxZjU3MzQ4NmMyNTQ2M2YxYjYyOWM1MjdmMThlNTk5OGU5YTAyYzdkYzRhMGQ1ZTg2ZTZmOTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.JWjTngiqJMEb7tEFJbgpQzAlQY1i0zEJWCyi2Qz8hFE
</div>

## About

Alibaba-CLI-Scraper is a python package that provides a dedicated CLI interface for scraping data from Alibaba.com. The purpose of this project is to extract products and theirs related suppliers informations and store it in a local database (SQLite or MySQL). The project utilizes asynchronous requests for efficient handling of numerous requests and allows users to easily run the scraper and manage the database using a user-friendly command-line interface (CLI).

## Table of Contents

- [About](#about)
- [Table of Contents](#table-of-contents)
  - [Features:](#features)
  - [Which important informations will be retrieved from the Alibaba website ?](#which-important-informations-will-be-retrieved-from-the-alibaba-website-)
  - [Sample of CSV output](#sample-of-csv-output)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Using the CLI Interface](#using-the-cli-interface)
    - [Available Commands:](#available-commands)
      - [Important Informations:](#important-informations)
      - [How to set My API KEY ?](#how-to-set-my-api-key-)
- [Future Enhancements](#future-enhancements)
- [Contributions Welcome!](#contributions-welcome)
- [License](#license)

### Features:

* **Asynchronous API:** Utilizes asynchronous API of Playwright and Brightdata Proxies for efficient handling of numerous pages results.


* **User-Friendly CLI:** Provides easy-to-use commands for running the scraper and managing the database.

* **Export-As-Csv:** Export your generated sqlite file to csv file.
### Which important informations will be retrieved from the Alibaba website ?

Fields related to `Suppliers`:

    `id`: int
    
    `name`: str
    
    `verification_mode`: str
    
    `sopi_level`: int
    
    `country_name`: str
    
    `years_as_gold_supplier`: int
    
    `supplier_service_score`: float

Fields related to `Products`:

    `id`: int
    
    `name`: str 
    
    `alibaba_guranteed`: bool
    
    `certifications`: str
    
    `minimum_to_order`: int
    
    `ordered_or_sold`: int
    
    `supplier_id`: int
    
    `min_price`: float
    
    `max_price`: float
    
    `product_score`: float
    
    `review_count` : float
    
    `review_score` : float
    
    `shipping_time_score` : float
    
    `is_full_promotion`: bool
    
    `is_customizable`: bool
    
    `is_instant_order`: bool
    
    `trade_product`:bool
  
### Sample of CSV output

When you will run command to export your sqlite file as a csv a `OUTER FULL JOIN` operation will be made to join all the fields of the both tables. Bellow you have a sample results maching `agricultural machinery` keywords.

|id  |name                                                                                                                            |alibaba_guranteed|minimum_to_order|supplier_id|alibaba_guranteed|certifications|ordered_or_sold|product_score|review_count|review_score|shipping_time_score|is_full_promotion|is_customizable|is_instant_order|trade_product|min_price|max_price|name                                                                                         |verification_mode|sopi_level|country_name  |years_as_gold_supplier|supplier_service_score|
|----|--------------------------------------------------------------------------------------------------------------------------------|-----------------|----------------|-----------|-----------------|--------------|---------------|-------------|------------|------------|-------------------|-----------------|---------------|----------------|-------------|---------|---------|---------------------------------------------------------------------------------------------|-----------------|----------|--------------|----------------------|----------------------|
|1   |mesh knitting weaving machine produce sunscreen net agricultural shade net anti net                                             |1                |1               |1          |1                |              |0              |5.0          |1.0         |5.0         |5.0                |1                |1              |1               |1            |9997.0   |18979.0  |qingdao shanzhong imp and exp ltd.                                                           |unverified       |0         |chine         |9                     |5.0                   |
|2   |chinese small farm rotary tiller 12hp 15hp 20hp two wheel mini hand tractor walk behind tractors                                |1                |1               |2          |1                |              |0              |0.0          |0.0         |0.0         |0.0                |1                |1              |1               |1            |455.0    |455.0    |shandong guoyoule agricultural machinery co., ltd.                                           |unverified       |0         |chine         |1                     |0.0                   |
|3   |small multifunctional flexible 130l orchard remote control garden crawler agriculture robot sprayer                             |1                |1               |3          |1                |              |0              |0.0          |0.0         |0.0         |0.0                |1                |1              |1               |1            |2350.0   |4620.0   |shandong my agricultural facilities co., ltd.                                                |unverified       |0         |chine         |1                     |0.0                   |
|4   |5hp/7hp/12hp rotary electric start agricultural farming walking tractor power tiller weeder cultivators                         |1                |1               |4          |1                |              |2              |0.0          |0.0         |0.0         |0.0                |1                |1              |1               |1            |244.0    |371.0    |shandong jinlong lutai international trade co., ltd.                                         |verified         |0         |chine         |1                     |0.0                   |
|5   |free shipping 3.5 ton mini excavator 1 ton 2 ton kubota engine digger excavator mini pelle chinese cheap small excavator machine|1                |1               |5          |1                |CE            |95             |4.6          |25.0        |4.6         |4.6                |1                |1              |1               |1            |988.0    |1235.0   |shandong qilu industrial co., ltd.                                                           |unverified       |5         |chine         |4                     |4.6                   |

### Prerequisites

- Python 3.11 or Higher

- Scraping Browser API KEY from [BrightData](https://get.brightdata.com/fdrqnme1smdc)  to know how to set your api key look at [here](#available-commands) 

- Windows or Linux as OS 




### Installation

It's recommended to use [pipx](https://pypa.github.io/pipx/) instead of pip for end-user applications written in Python. `pipx` installs the package, exposes his CLI() entrypoints in an isolated environment and makes it available everywhere in your system. This guarantees no dependency conflicts and clean uninstall.
let's install `aba-cli-scrapper` using pipx:

- Install pipx with a python 3.11 or higher version:
   ```shell
      python/python3 -m pip install --user pipx 
   ```
- add pipx to your PATH:
  ```shell
      pipx ensurepath
  ```
- Install `aba-cli-scrapper` using pipx:

   ```shell
      pipx install aba-cli-scrapper
   ```
and you're ready to use `aba-cli-scrapper`!

If you'd like to use `pip` instead, just replace `pipx` with `pip`  but obviously  as usual you'll need to  create a virtual environment and activate it before to use `aba-cli-scrapper` to avoid any dependency conflicts issues. let's install `aba-cli-scrapper` using pip:

- Create a virtual environment with Python 3.11 or higher:
   ```shell
      python/python3 -m venv your-virtual-environment-name
   ```
- activate the virtual environment:
   ```shell
      your-virtual-environment-name\\Scripts\\activate
   ```

  
### Using the CLI Interface
 

**Need Help?**  run  any commands followed by `--help` for detailed informations about its usage and options. For example: `aba-run --help` will show you all subcommands available and how to use them.

<div align="center">
  <p>
    <a href="#"><img src="images\help-cli-2.png" width="900" height="340" alt="aba-run help image" /></a>
  </p>

</div>

**Warnings:** 
- `aba-run` is the base command means all other commands that will be introduce bellow are sub-commands and should always be preceded by  `aba-run`.
Practice make perfect isn't ? So let's get started with a use case example. 
Let's assume  that you want to scrape data about `electric bikes` from Alibaba.com.

---
#### Available Commands:

  ##### Important Informations:

  * **`initialize` :**  Means create a new Mysql or SQLite database with products and suppliers table in it. Which will be used to store your scraped data. Especially for mysql engine, you will need to create an empty database in your mysql server before.
  * **`update` :** Means add your scraped data to a newly initialized Mysql or SQLite database. this action cannot be performed twice on the same database. 

  <details>
  <summary>Scraper Demo</summary>

  [https://user-images.githubusercontent.com/49741340/238535232-459847af-a15c-4d9b-91ac-fab9958bc74f.mp4](https://private-user-images.githubusercontent.com/52409392/351958081-302e7586-7e73-495f-bb40-41b8002c0480.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE4ODE5NTUsIm5iZiI6MTcyMTg4MTY1NSwicGF0aCI6Ii81MjQwOTM5Mi8zNTE5NTgwODEtMzAyZTc1ODYtN2U3My00OTVmLWJiNDAtNDFiODAwMmMwNDgwLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI1VDA0MjczNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQwZjlhM2I5ODk5ZjYzYmRhNmI5OWJhMzMxMDU2MGQ4NTBiZTk0OTAzNDg5M2M3NTU1M2NhYzFkYTc1YzQ5YzcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.xOTTGRRU8UQ8YZFMegl_TJC6kvtCR4aQEwJyp_DAjjk)

  </details>


  ##### How to set My API KEY ?

  by default `scrapper` will use async mode which is supported by brightdata api, means if you want to use it you will need to provide your api key. set it by using command bellow:

  ```shell
      aba-run set-api-key your_api_key
  ```
  and now run `scraper` sub-command without `--sync-api` flag to use async mode.

  *   **`scraper` sub-command:**  Initiates scraping of Alibaba.com based on the provided keywords.
  this command takes two required arguments and one optional argument:
      * -  **`key_words` (required):** The search term(s) for finding products on Alibaba. Enclose multiple keywords in quotes.
      * - **`--page-results` or `-pr` (required):** Usually keys words will results to many pages macthing them. Then you must to indicate how many of them you want to pull out.If any value is not provided `10` will be used by default.
      * -  **`--html-folder` or `-hf` (optional):** Specifies the directory to store the raw HTML files. If omitted, a folder with sanitized keywords as name will be automatically created. In this case `electric_bikes` will be used as a results folder name.
      * -  **`--sync-api` or `-sa` (optional):** flag indicates that you want to use sync mode. By default `async` mode is used.

      **Example**:
      ```shell
          aba-run scraper "electric bikes" -hf "bike_results" -pr 15
      ```
  However if you want to use sync mode you can use :

  ```bash
  aba-run scraper "electric bikes" -hf "bike_results" -pr 15  --sync-api/-sa
  ```
  and voila! 

  Now `bike_results` (since you already provided name you wish to have) directory has been created and should contains all html files from alibaba.com matching your keywords.

  ---

  <details>
  <summary>db-init Demo with sqlite</summary>

  [https://user-images.githubusercontent.com/49741340/238535232-459847af-a15c-4d9b-91ac-fab9958bc74f.mp4](https://private-user-images.githubusercontent.com/52409392/351970999-0f9491e5-69f0-470b-8a8e-9e436f0a0d0b.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE4ODQ0MjksIm5iZiI6MTcyMTg4NDEyOSwicGF0aCI6Ii81MjQwOTM5Mi8zNTE5NzA5OTktMGY5NDkxZTUtNjlmMC00NzBiLThhOGUtOWU0MzZmMGEwZDBiLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI1VDA1MDg0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWRiMmJiZTg3MDE3NTAwZWRhMzE2MTM5NDhjNmZkZTAwZWYxOTUxN2RlMzA1NGM4MzgyNWJkZTJmNTNkNzFhNDAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.gjlDs3VMK_MIg1Ne3cEqrO__LsZdyOgjy-SlZuXvd_s)

  </details>

  *   **`db-init` sub-command:** Creates a new database mysql/sqlite with products and suppliers as tables in it.
  this command takes one required arguments and six optional arguments(depends on engine you choose):
      * -   **`engine` (required):** Choose either `sqlite` or `mysql`. Is set to `sqlite` by default.
      *  - **`--sqlite-file` or `-f`(optional, SQLite only):**  The name for your SQLite database file (without any extension).
      *   - **`--host` or `-h`, `--port` or `-p`, `--user` or `-u`, `--password` or `-pw`, `--db-name`or `-db` (required for MySQL):**  Your MySQL database connection details.
    
      *   **`--only-with` or `-ow`(optional Mysql):**  If you just want to update some details of your credentials in `db_credentials.json` file but not all, use this flag.
  
  * **NB:** `--host` and `--port` are respectively set to `localhost` and `3306` by default. Also When you initialize your database with Mysql Engine for the first time, you must to set `--user`, `--password` and `--db-name` arguments. this will create a `db_credentials.json` file in your current directory with your credentials. Prevent you to set it again next time. Thus you will be able to set just import field when the time will come to [update](#important-informations) your database.

  **MySQL Use case:**

  ```shell
  aba-run db-init mysql -u "mysql_username" -pw "mysql_password" -db "alibaba_products" 
  ```



  **SQLite Use case :**

  ```shell
  aba-run db-init sqlite --sqlite-file alibaba_data
  ```
  db-init subcommand will try to use sqlite engine by default  so if you are planning to use it run as bellow :

  **SQLite Use case V2 :**
  ```shell
  aba-run db-init -f alibaba_data
  ```

  As soons as your database has been initialized, you can update it with the scraped data.

  ---

  <details>
  <summary>db-update Demo</summary>

  [https://user-images.githubusercontent.com/49741340/238535232-459847af-a15c-4d9b-91ac-fab9958bc74f.mp4](https://private-user-images.githubusercontent.com/52409392/351977812-ecfe8e3b-af20-4611-a07d-dd6ac401bf8c.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE4ODY1NjgsIm5iZiI6MTcyMTg4NjI2OCwicGF0aCI6Ii81MjQwOTM5Mi8zNTE5Nzc4MTItZWNmZThlM2ItYWYyMC00NjExLWEwN2QtZGQ2YWM0MDFiZjhjLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI1VDA1NDQyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTY4OTI3NDY0OThmYTA5NDJiMTEyMjBhZjczNDE2M2RkZWNlMmRjMzUyZjBkODgwMjY2NTc1NzQ1NjI5MTBmMzcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.Fa2jqUTAg-MQ-J33x6x_UIjnId190KhdEJZbUmmbTiw)

  </details>

  *  **`db-update` sub-command:** add scraped data from html files to your database (you can't use this command twice with same database name to avoid UNIQUE CONSTRAINT ERROR).

  this command takes two required arguments and two optional arguments:
    * - **`--db-engine` (required):** Select your database engine: `sqlite` or `mysql`. Is set to `sqlite` by default.
    * -  **`--kw-results`/`-kr` (required):**  The path to the folder containing the HTML files generated by the `scraper` sub command.
    * - **`--filename`/`-f` (required for SQLite):** If you're using SQLite, provide the desired filename for your database. whitout any extension.
    * - **`--db-name`/`-db` (optional for MySQL):** If you're using MySQL engine, and want to push the data to a different database, provide the desired database name.

  **MySQL Use case:**
   
   command bellow assuming that you already have your database credentials in `db_credentials.json` file to autocomplete required parameter. if not this will raise an error.

  ```shell
    aba-run db-update  mysql --kw-results bike_results\ 
  ```
  **NB:What if you want to change something while you updating the database? Assuming that you have run another scraping command and you want to save this data in another database name whitout update credential file or rewriting all theses parameter just to change your database name then, simply run `aba-run db-update  mysql --kw-results another_keyword_folder_result\ --db-name "another_database_name"`.**

  **SQLite Use case:**
  ```shell
  aba-run db-update  sqlite --kw-results bike_results\ --filename alibaba_data
  ```
  ---
  <details>
  <summary> export-as-csv Demo</summary>

<div align="center">
  <p>
    <a href="#"><img src="images\export-as-csv-demo.gif" width="900" height="340" alt="command result 1" /></a>
  </p>
  <p align="center">
  </p>
</div>
  </details>

  NB: This command is not available on Linux or Ubuntu OS

  *  **`export-as-csv` sub-command:** Exports scraped data from your sqlitedatabase to a CSV file. This csv file will contain a `FULL OUTER JOIN` with the `products` and `suppliers` tables.

  this command takes one required argument and one optional argument:
    * -  **`--sqlite_file` (required):** The name for your SQLite database file with his extension.
    * -  **`--to` or `-t` (required):**  The name for your CSV file with his extension.



## Future Enhancements

This project has a lot of potential for growth! Here are some exciting features I'm considering for the future:


-  **Retrieval Augmented Generation (RAG):** Integrate a RAG system that allows users to ask natural language questions about the scraped data, making it even more powerful for insights.

## Contributions Welcome!

I believe in the power of open source! If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. I'm always open to new ideas and improvements.

## License

This project is licensed under the [Gnu General Public License Version **3**](COPYING).


  
