<div align="center">
  <p>
    <a href="#"><img src="images\syphoon-sponsor.jpeg" width="700" height="350" alt="overview image" /></a>
  </p>
</div>
<p align="center">  <b>Alibaba-CLI-Scraper</b> </p>
<p align="center"> 🛒-💻- 🕸 </p>

---

<p align="center"> <b> Create your own Alibaba dataset and interact with it in plain English. </b> </p>

<div align="center">

![PyPI - Version](https://img.shields.io/pypi/v/aba-cli-scrapper) ![PyPI - Downloads](https://img.shields.io/pypi/dm/aba-cli-scrapper?label=PyPI-Downloads) ![GitHub Release Date](https://img.shields.io/github/release-date/poneoneo/Alibaba-CLI-Scrapper)

</div>
<div align="center">

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aba-cli-scrapper) ![GitHub License](https://img.shields.io/github/license/poneoneo/Alibaba-CLI-Scrapper)

</div>

<div align="center">

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2f57f95f64134aaaaf686fd0496c85a9)](https://app.codacy.com/gh/poneoneo/Alibaba-CLI-Scraper/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit) [![Codacy Badge](https://app.codacy.com/project/badge/Coverage/2f57f95f64134aaaaf686fd0496c85a9)](https://app.codacy.com/gh/poneoneo/Alibaba-CLI-Scraper/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)

</div>

<div align="center">

[https://github.com/user-attachments/assets/10f2ff2b-eef7-4b61-b317-89cf22252f1e](https://private-user-images.githubusercontent.com/52409392/369223181-c4cba5c5-8ace-43f0-9abb-da77ce9bc382.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjY3OTU3NzcsIm5iZiI6MTcyNjc5NTQ3NywicGF0aCI6Ii81MjQwOTM5Mi8zNjkyMjMxODEtYzRjYmE1YzUtOGFjZS00M2YwLTlhYmItZGE3N2NlOWJjMzgyLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA5MjAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwOTIwVDAxMjQzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWZhNDg3MzcxYWIyMjFhMzhjZThlNGQ4MDI5NzEzZTFiYWQ5NGQxNWEwOWNiYWRhMDlkZTRlZjNjMmVhMjJhYzAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.stasGgq1DbVY74v8rj0FrrdKQESB4F-vsxOTvynMCwo)

</div>

Run commands in one click.

No need to RTFM (I means this Readme) again, run the text-mode to know the purspose of each commands and theirs related options and parameters.

S/o [Trogon](https://github.com/Textualize/trogon). An amazing tool to easily turn your Click CLI application into a powerful TUI application.
<div align="center">

https://github.com/user-attachments/assets/fbab45ff-b46c-4021-b481-5d74eadc1813

</div>

Chat with your scraped data in plain english to generate and visualize plot to make decisions based on real-time data.
<div align="center">

https://github.com/user-attachments/assets/5beb4efb-f9b0-4dad-b0d6-a9771db6c61c

</div>

---

## About

Alibaba-CLI-Scraper is a python CLI tool designed to scrape, save and interact in plain english with data from Alibaba.com. Based on user, some products data and theirs related suppliers data will be extracted and saved it in a local database (SQLite or MySQL) and then will be ready to be analysed and even visualized through a powefull ai-agent powered by [data-horse](https://github.com/DeDolphins/DataHorse). It's also be designed to be user-friendly and therefore has fairly simple and easy-to-use commands to navigate through all the features of this tool.

## Table of Contents

- [About](#about)
- [Table of Contents](#table-of-contents)
  - [Features:](#features)
  - [Which important informations will be retrieved from the Alibaba website ?](#which-important-informations-will-be-retrieved-from-the-alibaba-website-)
  - [Sample of CSV output](#sample-of-csv-output)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Using the CLI Interface](#using-the-cli-interface)
    - [Important Informations](#important-informations)
    - [Available Sub-Commands](#available-sub-commands)
      - [Scraper and syphoon-scraper subcommands](#scraper-and-syphoon-scraper-subcommands)
        - [How to set My API KEY ?](#how-to-set-my-api-key-)
      - [db-init Sub-Command](#db-init-sub-command)
      - [db-update Sub-Command](#db-update-sub-command)
      - [export-as-csv Sub-Command](#export-as-csv-sub-command)
      - [ai-agent Sub-Command](#ai-agent-sub-command)
- [Contributions Welcome!](#contributions-welcome)
- [License](#license)

### Features:

- **2 Proxy Providers Support:** Provide support for Syphoon  and Bright Data.

- **Text Mode:** Provides easy-to-use commands with text mode for those who are not comfortable with commands in the terminal.

- **Export-As-Csv:** Export your generated sqlite file to csv file.

- **Ai-agent:** Interact with your scraped data in plain english to easily analyse an visualize what matter for you.

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

| id  | name                                                                                                                             | alibaba_guranteed | minimum_to_order | supplier_id | alibaba_guranteed | certifications | ordered_or_sold | product_score | review_count | review_score | shipping_time_score | is_full_promotion | is_customizable | is_instant_order | trade_product | min_price | max_price | name                                                 | verification_mode | sopi_level | country_name | years_as_gold_supplier | supplier_service_score |
| --- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- | ----------- | ----------------- | -------------- | --------------- | ------------- | ------------ | ------------ | ------------------- | ----------------- | --------------- | ---------------- | ------------- | --------- | --------- | ---------------------------------------------------- | ----------------- | ---------- | ------------ | ---------------------- | ---------------------- |
| 1   | mesh knitting weaving machine produce sunscreen net agricultural shade net anti net                                              | 1                 | 1                | 1           | 1                 |                | 0               | 5.0           | 1.0          | 5.0          | 5.0                 | 1                 | 1               | 1                | 1             | 9997.0    | 18979.0   | qingdao shanzhong imp and exp ltd.                   | unverified        | 0          | chine        | 9                      | 5.0                    |
| 2   | chinese small farm rotary tiller 12hp 15hp 20hp two wheel mini hand tractor walk behind tractors                                 | 1                 | 1                | 2           | 1                 |                | 0               | 0.0           | 0.0          | 0.0          | 0.0                 | 1                 | 1               | 1                | 1             | 455.0     | 455.0     | shandong guoyoule agricultural machinery co., ltd.   | unverified        | 0          | chine        | 1                      | 0.0                    |
| 3   | small multifunctional flexible 130l orchard remote control garden crawler agriculture robot sprayer                              | 1                 | 1                | 3           | 1                 |                | 0               | 0.0           | 0.0          | 0.0          | 0.0                 | 1                 | 1               | 1                | 1             | 2350.0    | 4620.0    | shandong my agricultural facilities co., ltd.        | unverified        | 0          | chine        | 1                      | 0.0                    |
| 4   | 5hp/7hp/12hp rotary electric start agricultural farming walking tractor power tiller weeder cultivators                          | 1                 | 1                | 4           | 1                 |                | 2               | 0.0           | 0.0          | 0.0          | 0.0                 | 1                 | 1               | 1                | 1             | 244.0     | 371.0     | shandong jinlong lutai international trade co., ltd. | verified          | 0          | chine        | 1                      | 0.0                    |
| 5   | free shipping 3.5 ton mini excavator 1 ton 2 ton kubota engine digger excavator mini pelle chinese cheap small excavator machine | 1                 | 1                | 5           | 1                 | CE             | 95              | 4.6           | 25.0         | 4.6          | 4.6                 | 1                 | 1               | 1                | 1             | 988.0     | 1235.0    | shandong qilu industrial co., ltd.                   | unverified        | 5          | chine        | 4                      | 4.6                    |

### Prerequisites

- Python 3.11 or Higher

- API KEY from [Syphoon](https://account.syphoon.com) or [BrightData](https://get.brightdata.com/fdrqnme1smdc) to know how to set your api key look at [here](#available-commands)

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

If you'd like to use `pip` instead, just replace `pipx` with `pip` but obviously as usual you'll need to create a virtual environment and activate it before to use `aba-cli-scrapper` to avoid any dependency conflicts issues. let's install `aba-cli-scrapper` using pip:

- Create a virtual environment with Python 3.11 or higher:
  ```shell
     python/python3 -m venv your-virtual-environment-name
  ```
- activate the virtual environment:
  ```shell
     your-virtual-environment-name\\Scripts\\activate
  ```

### Using the CLI Interface

**Need Help?** run any commands followed by `--help` for detailed informations about its usage and options. For example: `aba-run --help` will show you all subcommands available and how to use them.

<div align="center">
  <p>
    <a href="#"><img src="images\aba-run-help-image.png" width="800" height="340" alt="aba-run help image" /></a>
  </p>

</div>

**Warnings:**

- `aba-run` is the base command means all other commands that will be introduce bellow are sub-commands and should always be preceded by `aba-run`.
  Practice make perfect isn't ? So let's get started with a use case example.
  Let's assume that you want to scrape data about `electric bikes` from Alibaba.com.

---

#### Important Informations

- **`initialize` :** Means create a new Mysql or SQLite database with products and suppliers table in it. Which will be used to store your scraped data. Especially for mysql engine, you will need to create an empty database in your mysql server before.

- **`update` :** Means add your scraped data to a newly initialized Mysql or SQLite database. this action cannot be performed twice on the same database.

- **`aba-run`:** is the base command means all other commands that will be introduce bellow are sub-commands and should always be preceded by `aba-run`.
  Practice make perfect isn't ? So let's get started with a use case example.
  Let's assume that you want to scrape data about `electric bikes` from Alibaba.com.
#### Available Sub-Commands

##### Scraper and syphoon-scraper subcommands
<div align="center">
  <p>
    <a href="#"><img src="images\syphoon-scraper-help-options.png" width="800" height="340" alt="aba-run help image" /></a>
  </p>

</div>

  Based on which proxy provider you like, you need to choose between two sub-commands.

  - **`syphoon-scraper` :** if you want to use syphoon proxy provider.

  - **`scraper` :** which have been set to use brightdata proxy provider by default.

  ###### How to set My API KEY ?

  ```shell
      aba-run set-api-key your_proxy_provider_name
  ```
  replace `your_proxy_provider_name` with `syphoon` or `brightdata` based on your choice.
  after that, a message will appear waiting for you to set your api key.

  Both of the above sub-commands have the same options but i will use `syphoon-scraper` sub-command as an example.


  - **`scraper` sub-command:** Initiates scraping of Alibaba.com based on the provided keywords.
    this command takes two required arguments and one optional argument:
    - **`key_words` (required):** The search term(s) for finding products on Alibaba. Enclose multiple keywords in quotes.
    - **`--page-results` or `-pr` (required):** Usually keys words will results to many pages macthing them. Then you must to indicate how many of them you want to pull out.If any value is not provided `10` will be used by default.
    - **`--html-folder` or `-hf` (optional):** Specifies the directory to store the raw HTML files. If omitted, a folder with sanitized keywords as name will be automatically created. In this case `electric_bikes` will be used as a results folder name.
    - **`--sync-api` or `-sa` (optional):** flag indicates that you want to use sync mode. By default `async` mode is used.

      **Example**:
      ```shell
          aba-run syphoon-scraper "electric bikes" -hf "bike_results" -pr 15
      ```

    Sync mode is also available but you will quickly get block:

  ```shell
  aba-run syphoon-scraper "electric bikes" -hf "bike_results" -pr 15  --sync-api/-sa
  ```
  and voila!

  Now `bike_results` (since you already provided name you wish to have) directory has been created and should contains all html files from alibaba.com matching your keywords.

##### db-init Sub-Command
  <div align="center">
    <p>
      <a href="#"><img src="images\db-init-help-options.png" width="800" height="340" alt="aba-run help image" /></a>
    </p>
  </div>

  - **`db-init` sub-command:** Creates a new database mysql/sqlite with products and suppliers as tables in it.
    this command takes one required arguments and six optional arguments(depends on engine you choose):
    - **`engine` (required):** Choose either `sqlite` or `mysql`. Is set to `sqlite` by default.
    - **`--sqlite-file` or `-f`(optional, SQLite only):** The name for your SQLite database file (without any extension). \* - **`--host` or `-h`, `--port` or `-p`, `--user` or `-u`, `--password` or `-pw`, `--db-name`or `-db` (required for MySQL):** Your MySQL database connection details.
    *   **`--only-with` or `-ow`(optional Mysql):**  If you just want to update some details of your credentials in `db_credentials.json` file but not all, use this flag.


 **NB:** `--host` and `--port` are respectively set to `localhost` and `3306` by default. Also When you initialize your database with Mysql Engine for the first time, you must to set `--user`, `--password` and `--db-name` arguments. this will create a `db_credentials.json` file in your current directory with your credentials. Prevent you to set it again next time. Thus you will be able to set just import field when the time will come to [update](#important-informations) your database.

  **MySQL Use case:**

  ```shell
  aba-run db-init mysql -u "mysql_username" -pw "mysql_password" -db "alibaba_products"
  ```

  **SQLite Use case :**

  ```shell
  aba-run db-init sqlite --sqlite-file alibaba_data
  ```

  db-init subcommand will try to use sqlite engine by default so if you are planning to use it run as bellow :

  **SQLite Use case V2 :**

  ```shell
  aba-run db-init -f alibaba_data
  ```

  As soons as your database has been initialized, you can update it with the scraped data.

---

##### db-update Sub-Command
<div align="center">
  <p>
    <a href="#"><img src="images\db-update-help.png" width="800" height="340" alt="aba-run help image" /></a>
  </p>

</div>

  - **`db-update` sub-command:** add scraped data from html files to your database (you can't use this command twice with same database name to avoid UNIQUE CONSTRAINT ERROR).

  this command takes two required arguments and two optional arguments:
   - **`--db-engine` (required):** Select your database engine: `sqlite` or `mysql`. Is set to `sqlite` by default.
   - **`--kw-results`/`-kr` (required):** The path to the folder containing the HTML files generated by the `scraper` sub command.
   - **`--filename`/`-f` (required for SQLite):** If you're using SQLite, provide the desired filename for your database. whitout any extension.
   - **`--db-name`/`-db` (optional for MySQL):** If you're using MySQL engine, and want to push the data to a different database, provide the desired database name.

  **MySQL Use case:**

  command bellow assuming that you already have your database credentials in `db_credentials.json` file to autocomplete required parameter. if not this will raise an error.

  ```shell
    aba-run db-update  mysql --kw-results bike_results\
  ```

  **NB:** What if you want to change something while you updating the database? Assuming that you have run another scraping command and you want to save this data in another database name whitout update credential file or rewriting all theses parameter just to change your database name then, simply run:

  ```shell
    aba-run db-update mysql --kw-results another_keyword_folder_result\ --db-name "another_database_name
  ```

  **SQLite Use case:**

  ```shell
  aba-run db-update  sqlite --kw-results bike_results\ --filename alibaba_data
  ```

  ---

##### export-as-csv Sub-Command
<div align="center">
  <p>
    <a href="#"><img src="images\export-as-csv-help.png" width="800" height="340" alt="aba-run help image" /></a>
  </p>

</div>

  - **`export-as-csv` sub-command:** Exports scraped data from your sqlitedatabase to a CSV file. This csv file will contain a `FULL OUTER JOIN` with the `products` and `suppliers` tables.

  this command takes one required argument and one optional argument:

  - - **`--sqlite_file` (required):** The name for your SQLite database file with his extension.
  - - **`--to` or `-t` (required):** The name for your CSV file with his extension.

##### ai-agent Sub-Command
<div align="center">
  <p>
    <a href="#"><img src="images\ai-agent-help.png" width="800" height="340" alt="aba-run help image" /></a>
  </p>

</div>

  The purpose of this command is to provide a way to interact with your scraped data in plain english.

  - You will be able build a query i.e "list all suppliers in china". In this case the answer will be a pretty table with the name of the suppliers.
  - or i.e "plot the price of all the products in china". In this case the answer will be a line chart with the price of all the products in china.

  - **`ai-agent` sub-command:** Calls an Ai agent to interact with your scraped data in plain english.

  this command takes one required argument and one optional argument:

  - - **`query` (required):** content of the query that you want to ask to the ai agent.
  - - **`--csv-file` or `-f` (required):** The name for your CSV file with his extension.

## Contributions Welcome!

I believe in the power of open source! If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. I'm always open to new ideas and improvements.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
