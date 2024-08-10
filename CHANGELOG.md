# CHANGELOG

## v0.3.0 (2024-08-09)

### Breaking

* build(aba_cli_scrapper\*): change database api engine from myqlclient to pymysql + fixing errors while parsing html process

    going through all scripts tags inside div[class=&#39;container&#39;] and looking for the right tag
    switching between to case while parsing suppliers and products

BREAKING CHANGE: database api engine has changed from myqlclient to pymysql ([`d19ed75`](https://github.com/poneoneo/Alibaba-Scrapper/commit/d19ed75a3c92a1c0488458b40130533e59206320))

* chore(DBAPIS): remove pymysql as a DBAPIS cause of sql injections vulnearability. replacing with mysqlclient

BREAKING CHANGE: remove pymysql as a DBAPIS cause of sql injections vulnearability. replacing with mysqlclient ([`810a653`](https://github.com/poneoneo/Alibaba-Scrapper/commit/810a65388ac6cd3a10ae5abb7f85a7d13cb5854e))

### Build

* build(pyproject.toml, poetry.lock): update poetry lock file to include modifications due python required versions: ^3.11 ([`21ea4b4`](https://github.com/poneoneo/Alibaba-Scrapper/commit/21ea4b424b3bb0d43589cf603577c5d604120f03))

* build(pyproject): update package project file with info about latest testing version ([`ff2f02f`](https://github.com/poneoneo/Alibaba-Scrapper/commit/ff2f02fecbefd1c03c70e53ec46eb36bf680edd5))

### Chore

* chore(pyproject): bumping version to 0.3.0 ([`5fbbb9f`](https://github.com/poneoneo/Alibaba-Scrapper/commit/5fbbb9fa0f21b43c4c52476aa98559846359e20e))

* chore(package_structure): update requirements for test project ([`abaa932`](https://github.com/poneoneo/Alibaba-Scrapper/commit/abaa932c83084761b309b5cd3987f36d1a7ea6f7))

* chore(project_config): bump version to 0.2.0 ([`75f6c3d`](https://github.com/poneoneo/Alibaba-Scrapper/commit/75f6c3d9526ddc40eb776f725fc08cf9548c4506))

* chore(project_config): last settings for semantic version ([`9227b30`](https://github.com/poneoneo/Alibaba-Scrapper/commit/9227b3071e9d32313bfcac681734a7e5dbc02a04))

* chore(dependencies): add dev as default branch ([`da585c8`](https://github.com/poneoneo/Alibaba-Scrapper/commit/da585c8ebfdefd25201d9681e5bfc85f76177426))

* chore(semantic_config): add dev as default branch for semantic version sys ([`302672e`](https://github.com/poneoneo/Alibaba-Scrapper/commit/302672e189a86da3d4c64046285a65cdf813875a))

* chore(semantic_config): add semantic verions system ([`3456bc8`](https://github.com/poneoneo/Alibaba-Scrapper/commit/3456bc86717740988daf4130c95041065d4b05f8))

* chore(dependencies): remove and reinstall mysqlclient ([`ca0c5d3`](https://github.com/poneoneo/Alibaba-Scrapper/commit/ca0c5d3e3ff80a8a7c9a4c908db79902a86a77a4))

* chore(package_structure): track *.html file ([`085c95c`](https://github.com/poneoneo/Alibaba-Scrapper/commit/085c95c102a8e4766a43f8ed90d0e723ae9e6d56))

* chore(package_structure): add htmlfile that will be used for test ([`c70899c`](https://github.com/poneoneo/Alibaba-Scrapper/commit/c70899cc26311907b83228a33e7b73cb934610b0))

* chore(package_structure): prepare html file to be tested ([`2bb6a33`](https://github.com/poneoneo/Alibaba-Scrapper/commit/2bb6a33e40a1152671fa584c0510f3abd4b101d9))

* chore(package_structure): remove requirements.txt ([`729e2d0`](https://github.com/poneoneo/Alibaba-Scrapper/commit/729e2d0afe9ecebbebd6e8cea7a2bfb703218d2b))

* chore(pyproject): add package file config ([`7c285c9`](https://github.com/poneoneo/Alibaba-Scrapper/commit/7c285c9cd5ee9862c8afb26db3a3d7844baf5667))

* chore(*): design whole project as a python package ([`7e947fb`](https://github.com/poneoneo/Alibaba-Scrapper/commit/7e947fbffeeb2868ea9f9c60da1e5a5e523315b0))

* chore(src): remane main.py to app.py ([`342dee2`](https://github.com/poneoneo/Alibaba-Scrapper/commit/342dee2ebd6d1817cd3f9014f90c3e92c964b5c0))

* chore(requirements): update requirements and depedencies ([`488d0f5`](https://github.com/poneoneo/Alibaba-Scrapper/commit/488d0f5127dbf3591db196368e7a48bff58960da))

* chore(pipfile.lock .gitignore): track pipfile.lock file to ensure crossplateforme running as recommended by Kenneth Reitz ([`48513cb`](https://github.com/poneoneo/Alibaba-Scrapper/commit/48513cbbc368f0bbfe8aea2e0b8ddfb099b15c7b))

* chore(licence): add GNU General Public License v3.0 ([`26dacbb`](https://github.com/poneoneo/Alibaba-Scrapper/commit/26dacbbde83b6335fd8e55ecf790dcf741cd3213))

* chore(dependencies and packages): update requirements.txt file with new packages and depencies ([`d2eece8`](https://github.com/poneoneo/Alibaba-Scrapper/commit/d2eece86b47fcaea16306a696d313cc238376f4b))

* chore(dependencies): replace pony by sqlmodel ([`7ea52dd`](https://github.com/poneoneo/Alibaba-Scrapper/commit/7ea52ddb462c20886953cc95d7a9d210ff05d4c0))

* chore(models.py): map dataclasses to create an Mysql database ([`ad32cc6`](https://github.com/poneoneo/Alibaba-Scrapper/commit/ad32cc6db9dc73dc0a40f002763f9aa8bdda5381))

### Documentation

* docs(README): add my bright data afiliate link ([`9b07711`](https://github.com/poneoneo/Alibaba-Scrapper/commit/9b07711621a2d500c46479dee027fc2afbca6d26))

* docs(readme): add movie to show how to use export-as-csv command ([`390386f`](https://github.com/poneoneo/Alibaba-Scrapper/commit/390386f33c40df011421626ab3d4826d3a7f90cf))

* docs(readme): add a table of contents to the readme and explain how to set an api key an export data as a csv ([`5b0a103`](https://github.com/poneoneo/Alibaba-Scrapper/commit/5b0a10380e12eacea04aed4de16f6d04e4bdc608))

* docs(readme): add images to readme ([`055fb40`](https://github.com/poneoneo/Alibaba-Scrapper/commit/055fb40da736a4f6418d21c994cf374b75159a67))

* docs(readme): update readme and remove unwanted htmlfiles... again :) ([`de93480`](https://github.com/poneoneo/Alibaba-Scrapper/commit/de9348017286a1c5c61a7323271fd2203c518d30))

* docs(readme): add new help image result ([`a5b031c`](https://github.com/poneoneo/Alibaba-Scrapper/commit/a5b031c0b1b72960eeb8c19bbdc2f0b884f3ef12))

* docs(readme): add image for readme ([`30e9d8b`](https://github.com/poneoneo/Alibaba-Scrapper/commit/30e9d8be12a89603a0d132030cbf4d6d274b41ff))

* docs(readme): add video ([`cb12ed5`](https://github.com/poneoneo/Alibaba-Scrapper/commit/cb12ed51956db5da92529c5f3fc6f3ad7ca9a18d))

* docs(readme): how to use sync api ([`711fc86`](https://github.com/poneoneo/Alibaba-Scrapper/commit/711fc86f5ec2330405ddea1e3102af8c5f972f40))

* docs(readme): readme correction ([`6e2b7dd`](https://github.com/poneoneo/Alibaba-Scrapper/commit/6e2b7dd52d61a260044d95d200203e677715a3b5))

* docs(readme): add help image to git index ([`050f959`](https://github.com/poneoneo/Alibaba-Scrapper/commit/050f9592374e47ae2bce281a738c8b8cb863ba60))

* docs(readme): update readme with info about  commands features and limit ([`d1007ab`](https://github.com/poneoneo/Alibaba-Scrapper/commit/d1007abe975f81e14a5afdfe5bbfba4263cc103c))

* docs(readme): readme bugs ([`5817adb`](https://github.com/poneoneo/Alibaba-Scrapper/commit/5817adb429f3fe39f0ae31e3f2e41220663ba61b))

* docs(readme): modify instructions to macth package installations and usage ([`43aedef`](https://github.com/poneoneo/Alibaba-Scrapper/commit/43aedefbca366027d61aa596c4a2aacfedbee002))

* docs(README): add images to replace overview image ([`9768592`](https://github.com/poneoneo/Alibaba-Scrapper/commit/9768592584b03add2cd146834d891100b7471e77))

* docs(readme): overview image was not appear on github ([`024ccb4`](https://github.com/poneoneo/Alibaba-Scrapper/commit/024ccb4eb7a2988b779dae9e65ae34a6548a3cd0))

* docs(README): convert overview image from .webp to .png and replace alt name ([`aa8f275`](https://github.com/poneoneo/Alibaba-Scrapper/commit/aa8f27590f92368b1ed9a634845fcc1cf151d9b9))

* docs(README): convert overview image from .webp to .png ([`31cf4aa`](https://github.com/poneoneo/Alibaba-Scrapper/commit/31cf4aad6200ef30f73bb6d872737a20faf7230c))

* docs(README): add image to introduce cli tool and fix conflict ([`0aac326`](https://github.com/poneoneo/Alibaba-Scrapper/commit/0aac3269acc8df3056b89201ea1434aec5676f36))

* docs(README): add image to introduce cli tool ([`6e2be37`](https://github.com/poneoneo/Alibaba-Scrapper/commit/6e2be370cbd783e17310ff40544fe65238e7777e))

* docs(README): add more details about cli commands ([`5a0f166`](https://github.com/poneoneo/Alibaba-Scrapper/commit/5a0f1660f58b80dac751e1278db99ea5ccec38d6))

* docs(README): false instructions ([`a6eaecc`](https://github.com/poneoneo/Alibaba-Scrapper/commit/a6eaecc5dbb9f3f41fb75bba7b727e05df263aa6))

* docs(src): update help message ([`bf0520e`](https://github.com/poneoneo/Alibaba-Scrapper/commit/bf0520e51f6d0ce8358219d40d99460b67072b43))

* docs(images): add images folder ([`6710077`](https://github.com/poneoneo/Alibaba-Scrapper/commit/6710077f81bb01a564b7cb3269644becb27ef9af))

* docs(readme): add instruction to readme ([`a4a6ef1`](https://github.com/poneoneo/Alibaba-Scrapper/commit/a4a6ef16d31aa25f9c80264e0e5d02070fd4f305))

* docs(README): replace main.py with app.py ([`63b9da4`](https://github.com/poneoneo/Alibaba-Scrapper/commit/63b9da46699c08bd5e59b7ea6df4cc4ca2d1646e))

* docs(readme): update readme ([`b9f5467`](https://github.com/poneoneo/Alibaba-Scrapper/commit/b9f5467ca0af56f15d6f80f1e35ef884f9d2e12d))

* docs(readme): add an expansive description of how to install the project and use ALIABABA-CLI-SCRAPPER ([`39789c8`](https://github.com/poneoneo/Alibaba-Scrapper/commit/39789c81738662b5fb99bac7ae65d1ce5bd9e918))

* docs(html_parser): add documentation for PageParser class and remove useless loggers ([`828b6b9`](https://github.com/poneoneo/Alibaba-Scrapper/commit/828b6b9141ae4841a873364b00e286fc30240bc3))

* docs(README): add Title, description and installation flow ([`81983e0`](https://github.com/poneoneo/Alibaba-Scrapper/commit/81983e0344c428dd47a34eed0db58082dc7ce515))

### Feature

* feat(*): add information  for export-as-csv command + add message for async scraping models

        - when export-as-csv is called a verification will be done to check that this operation is performing On
        windowns platform if not an error will be raised with message &#34;this feature is only available on windows platform&#34;

        - when async scraping is performed a verification will be done to check if an api key is set
         if not an error will be raised with message &#34;you need to set your SCRAPING BROWSER API key from BrightData to Enable Async Scraping&#34; ([`f516006`](https://github.com/poneoneo/Alibaba-Scrapper/commit/f51600617527793055fe257f06da033d1847d751))

* feat(cli_api): allow to set bright data api key to use async api ([`286f441`](https://github.com/poneoneo/Alibaba-Scrapper/commit/286f44173960754591dd9670b882e7cf89e2fe2c))

* feat(cli_api): add export from sqlite to csv command + fix `base 10 error` bug with minimum_to_order ([`8077cf5`](https://github.com/poneoneo/Alibaba-Scrapper/commit/8077cf5a98ac1c4c31cb48127656991ff285aa39))

* feat(api commands): add scraper command ([`97ddc71`](https://github.com/poneoneo/Alibaba-Scrapper/commit/97ddc71995f93a7c67f5021af091c59982b9c90c))

* feat(api commands): update message when integrity error occurs ([`2fe402c`](https://github.com/poneoneo/Alibaba-Scrapper/commit/2fe402c617f42ab422ec948ebc8e603ff4c1b460))

* feat(__main__.py): exit typer app when mysql upate operation is done ([`c2146bb`](https://github.com/poneoneo/Alibaba-Scrapper/commit/c2146bbdd0b5084c845256a8ad4eac4142308441))

* feat(commands api): add short name for parameters of each subcommands ([`6484ca8`](https://github.com/poneoneo/Alibaba-Scrapper/commit/6484ca897949c14c7421987107a38d6d14b74fa3))

* feat(__main__): show success message after db init command ([`d445671`](https://github.com/poneoneo/Alibaba-Scrapper/commit/d4456719ff1666387d3d9c0f1da5d199f2e4f16a))

* feat(src): update dynamicaly database credential without update .json file + dynamicaly update bright api key base user country ([`e7c2305`](https://github.com/poneoneo/Alibaba-Scrapper/commit/e7c23051ea041bf836b6ee4a5ff9ecfd10acdb2a))

* feat(*): shutdown debug logger and add sync-api as a new feature. finally increase async speed ([`2ce71f9`](https://github.com/poneoneo/Alibaba-Scrapper/commit/2ce71f993a5915cec4b0ba59bfbb69e3abbb4013))

* feat(whole project): cli support with three command allowing to user: scrapping, initialize and update database with new data.

**`run-scrapper` command to scrapping data from Alibaba based on your requirement.**
** `db-init` command to initialize the database support only mysql and sqlite.**
** `db-update` command to update the database with new data inside your scrapping results folder.** ([`06c82a8`](https://github.com/poneoneo/Alibaba-Scrapper/commit/06c82a867b013b089aac71d318933506375fac2a))

* feat(utils_scrapping): clean products and suppliers attributes before to insert them in dictionnary

-add methode to retrieve products price without their currency
-add method to handling potencial errors while we are getting mininal to order number
-return `royaume uni` there not matching with our json file ([`84ea38a`](https://github.com/poneoneo/Alibaba-Scrapper/commit/84ea38a5a55776b1e24cd352a2523c8e4537684a))

* feat(web_scrapper): scrapping based on keywords entered by user then save results in directory specified by user ([`f9797ae`](https://github.com/poneoneo/Alibaba-Scrapper/commit/f9797ae4ca9c05305b262c2db8bde1adb838e1a5))

* feat(engine_and_database):  create all tables in database and add products and suppliers rows in database finally save all changes ([`79b0442`](https://github.com/poneoneo/Alibaba-Scrapper/commit/79b0442436b4e8c601af49711e61eacceff2fdff))

* feat(models): create two tables Products and Suppliers and commit any changes to sqlite database ([`a7f9bbb`](https://github.com/poneoneo/Alibaba-Scrapper/commit/a7f9bbbd75cce802227d2085fceedef3d489228f))

* feat(html_to_disk): catch potential errors that could be occured while writing html content to disk ([`c0d6169`](https://github.com/poneoneo/Alibaba-Scrapper/commit/c0d6169afa808b1bdba4e6ed623aae022c8b9c54))

* feat(html_to_disk): save pages results into disk ([`0480185`](https://github.com/poneoneo/Alibaba-Scrapper/commit/0480185d2508cc82af77565154411807913864e9))

### Fix

* fix(aba_cli_scrapper\__main__):  add pymysql as DBAPI while initializing mysql database without auto-fill flag ([`8ab4437`](https://github.com/poneoneo/Alibaba-Scrapper/commit/8ab4437d5ddd8acd31724db9ffb78706ba07e0a0))

* fix(poetry.lock): update poetry.lock to fix depencies bugs while instalation ([`442110b`](https://github.com/poneoneo/Alibaba-Scrapper/commit/442110b44aafea115cd11988a9bae52058ef88f1))

* fix(web_scrapper): unbound local error ([`6a6dadc`](https://github.com/poneoneo/Alibaba-Scrapper/commit/6a6dadc085a24f588e1c60bf965f202429232d09))

* fix(*): MOdulenot found in lastest realease ([`2282960`](https://github.com/poneoneo/Alibaba-Scrapper/commit/228296029afd30a13238e2c4d3ac7c33c2427e51))

* fix(datatbase): catching errors when datatbase is updated twice + pretty printed message commands ended with sucess ([`0daf861`](https://github.com/poneoneo/Alibaba-Scrapper/commit/0daf861d58967b962da490f45fbcaee163f948fe))

* fix(*): fixing release v0.1.6 ([`03ed972`](https://github.com/poneoneo/Alibaba-Scrapper/commit/03ed972a8ee8e8db5a80a440499ecd3ab2e0d729))

* fix(*): fixing release v0.1.5 ([`6110de6`](https://github.com/poneoneo/Alibaba-Scrapper/commit/6110de6fb83efd753c055293b8172ebb61dd39b7))

* fix(*): fixing release v0.1.4 ([`c6d7adf`](https://github.com/poneoneo/Alibaba-Scrapper/commit/c6d7adf371a58fc3d86b76f0842fa9d828a37f41))

* fix(*): fixing release v0.1.3 ([`b74d237`](https://github.com/poneoneo/Alibaba-Scrapper/commit/b74d2378a4cb159bc6770dd0af05433613f0c64d))

* fix(dependencies security): REDOS vulnerability ([`e61a26d`](https://github.com/poneoneo/Alibaba-Scrapper/commit/e61a26d858dbba09f1d8afe775312c35a44d174f))

* fix(progress bar): progress bar bugs + deactivate logger + tell user when when internet is turned off ([`8cea768`](https://github.com/poneoneo/Alibaba-Scrapper/commit/8cea76816367705ac6a7d243057ee9ddbc437593))

* fix(secret_file): keyerror with .env file ([`bbdf600`](https://github.com/poneoneo/Alibaba-Scrapper/commit/bbdf600f4b3ee4261c93cf6b1d85c0dfde005b4d))

* fix(depencies security): redos vulnerability ([`8028dc3`](https://github.com/poneoneo/Alibaba-Scrapper/commit/8028dc3fa8ed91f2e67d33c0e5ce703b34aedaa1))

* fix(playwright): Fix all errors when using async playwright + add more details about products and suppliers + add cli commands to env var

    -add typed dict for products and suppliers ([`b3677a9`](https://github.com/poneoneo/Alibaba-Scrapper/commit/b3677a984cae8a780544d5888f3e499324c73840))

* fix(setup): conflict depencies with pip + remove history about package on readme file ([`e2ae78e`](https://github.com/poneoneo/Alibaba-Scrapper/commit/e2ae78eb180b0c36cf24cf16f653e285776ede49))

* fix(src): trouble with db-update ([`218a0e9`](https://github.com/poneoneo/Alibaba-Scrapper/commit/218a0e954e7fe45318d4a166a5db6e8c6e840a74))

* fix(engine_and_database): fix no such table supplier ([`91c0731`](https://github.com/poneoneo/Alibaba-Scrapper/commit/91c073107c48906d756ede078964bb2901a66507))

* fix(src/web_scrapper): fix many errors with response body from page and add sync api ([`cdc97ac`](https://github.com/poneoneo/Alibaba-Scrapper/commit/cdc97ac074a72be8a5424ad112162a26ed313783))

* fix(src): UnboundLocalError: local variable &#39;save_in&#39; referenced before assignment ([`2795233`](https://github.com/poneoneo/Alibaba-Scrapper/commit/27952338efa9792a4f116688612863ee91906422))

* fix(src): minimum to order column was return a string instead of an interger ([`0c369a8`](https://github.com/poneoneo/Alibaba-Scrapper/commit/0c369a89c3cc5f79f3dfbcc1079f509caa171add))

* fix(db-init command): ModuleNotFoundError: No module named &#39;pymysql&#39; has been fixed

pymysql has been replaced but was used when user initialized his database. ([`3f1f07e`](https://github.com/poneoneo/Alibaba-Scrapper/commit/3f1f07e175b023643edcbf852bf2269f5688138e))

### Refactor

* refactor(images): add path to export-as-csv.gif into images folder ([`cf6b58d`](https://github.com/poneoneo/Alibaba-Scrapper/commit/cf6b58d6640a42cf3dca2a09f3fef4159b448db6))

* refactor(aba_cli_scrapper): rewrinting Parser methods into a more pythonic way as recommended by some issues ([`25a457e`](https://github.com/poneoneo/Alibaba-Scrapper/commit/25a457e161fd3af872276ce1792e6156e4a88321))

* refactor(package_structure): remove unwanted htmlfiles ([`dbe2caf`](https://github.com/poneoneo/Alibaba-Scrapper/commit/dbe2caf8eb89d11e8e995e45e478800e19471bc4))

* refactor(package_structure): remove json with countries an related short name ([`42862fd`](https://github.com/poneoneo/Alibaba-Scrapper/commit/42862fdc03ad9c0ea3afebfcfe27c59be886cb62))

* refactor(package_structure): remove .env file ([`e5f3605`](https://github.com/poneoneo/Alibaba-Scrapper/commit/e5f36052c58bbd4baf7b4174a4d00072fe44f174))

* refactor(package_structure): remove src and txt file ([`5e32b28`](https://github.com/poneoneo/Alibaba-Scrapper/commit/5e32b28c3b61e4103070c91d1863994c941b9824))

* refactor(project): turn images folder into an external packages ([`029f57b`](https://github.com/poneoneo/Alibaba-Scrapper/commit/029f57b2706996452265f2cd15200a4226c08441))

* refactor(readme): tracking .gitignore file ([`45bf01f`](https://github.com/poneoneo/Alibaba-Scrapper/commit/45bf01f402087304597a871adb068898faa176f0))

* refactor(ali2b-cli-scrapper): remove __main__ from ignore file ([`60c0c52`](https://github.com/poneoneo/Alibaba-Scrapper/commit/60c0c52bb80c8a973b21b3cf9eeb3f7cb64b5630))

* refactor(src): linting errors and assign api key value ([`b91ddd6`](https://github.com/poneoneo/Alibaba-Scrapper/commit/b91ddd68022cea1a9cfb5fa7d2c7b87872487e3a))

* refactor(src): lower country code inside bright data api key ([`90b360e`](https://github.com/poneoneo/Alibaba-Scrapper/commit/90b360eaebacc2fa9fa518a32b17d52de87a73a2))

* refactor(.gitignore):   ignore cache file from src folder ([`0f98a1a`](https://github.com/poneoneo/Alibaba-Scrapper/commit/0f98a1a887a58f536d165233035edc059774e58a))

* refactor(.gitignore): ignore python cache file ([`4f99648`](https://github.com/poneoneo/Alibaba-Scrapper/commit/4f996484ab09577cae8137bb86332407044e8de7))

* refactor(src): update api key for bright data and info succes message ([`ed5aa83`](https://github.com/poneoneo/Alibaba-Scrapper/commit/ed5aa8333d90c23fe8d4b612effcb9467caa7b16))

* refactor(requirements):  update requirements file ([`c8f3da1`](https://github.com/poneoneo/Alibaba-Scrapper/commit/c8f3da1db37434d143ec483966f80ed671605cb1))

* refactor(src): update web_scrapper.py ([`6ae490e`](https://github.com/poneoneo/Alibaba-Scrapper/commit/6ae490e7ef3357fef62e8ab762d51bfafdf9d9b3))

* refactor(src): change the way to import TaskGroup() ([`4e754ce`](https://github.com/poneoneo/Alibaba-Scrapper/commit/4e754ce1b2be62a9122558f9e5156f362bc7534a))

* refactor(src/web_scrapper): replace asyncio.TaskGroup with asyncio.gather ([`fe43886`](https://github.com/poneoneo/Alibaba-Scrapper/commit/fe43886dae1813af796ad7371afec71b8925e35d))

* refactor(tests): tests become a package ([`a6e3b3c`](https://github.com/poneoneo/Alibaba-Scrapper/commit/a6e3b3c34ac50d48d8277bcccafe5060f290e8b4))

* refactor(whole project): src directory become a package ([`56fa893`](https://github.com/poneoneo/Alibaba-Scrapper/commit/56fa8939aadf352d649332fdb1f9469bc8898277))

* refactor(pays_data): move pays_data.json to src/ ([`d48a22f`](https://github.com/poneoneo/Alibaba-Scrapper/commit/d48a22f42f1864ce51b38c5f1826bf2f37a2e159))

* refactor(project): move models.py to src/ ([`ceb4e3b`](https://github.com/poneoneo/Alibaba-Scrapper/commit/ceb4e3bd47c08e785219eafc393791f11372b0d4))

* refactor(project): track project from src/ folder ([`9c48b46`](https://github.com/poneoneo/Alibaba-Scrapper/commit/9c48b46be6e2707b9cc83446d4a118dd4407f359))

* refactor(project): remove all modules into src/ directory according to the new structure ([`d24de4a`](https://github.com/poneoneo/Alibaba-Scrapper/commit/d24de4a57ec5ad537102a5b76b9c5d036fbdab2d))

* refactor(project): Delete Alibaba_Pages_results directory

html pages result should not be tracked ([`2b25bd9`](https://github.com/poneoneo/Alibaba-Scrapper/commit/2b25bd953facec4d49ab71eb18702102090589f2))

* refactor(gitignore): untrack scrapping results ([`db6a500`](https://github.com/poneoneo/Alibaba-Scrapper/commit/db6a500da399d8f74ac2d667973e3088234e9a9e))

* refactor(main): gather all functions features in one file

-the purpose of this refactor is to prepare cli features for the project ([`371973a`](https://github.com/poneoneo/Alibaba-Scrapper/commit/371973a4380876a563528b9392ee5b64912467f8))

* refactor(html_to_disk): remove useless logger ([`e14192d`](https://github.com/poneoneo/Alibaba-Scrapper/commit/e14192dacb0a13ab6713d57ac1373c15aff3d7cb))

* refactor(db_orm): use sqlmodel instead of pony as orm engine ([`94c4d3c`](https://github.com/poneoneo/Alibaba-Scrapper/commit/94c4d3ce5e824e8bcf0be2588cdc29b315b776ee))

* refactor(scrape_from_disk):  create a class to handle all the process needed to get suppliers and products ([`7af6a83`](https://github.com/poneoneo/Alibaba-Scrapper/commit/7af6a83a11a89dcda2d54177deba7bdfeb584ff8))

* refactor(pipfile): update pipfile ([`57e3cb8`](https://github.com/poneoneo/Alibaba-Scrapper/commit/57e3cb84e51c975f17272af52925f24d7636d3c1))

* refactor(pays_data): add informations to convert country abbreviation to all string name ([`f284165`](https://github.com/poneoneo/Alibaba-Scrapper/commit/f284165e4320ad7e804b7bccb33a7bcc74ebff51))

* refactor(*):  create many modules to separate main.py file from scrapping and saving logics ([`c1b3708`](https://github.com/poneoneo/Alibaba-Scrapper/commit/c1b3708f8e7b6969f5f1bccadcd6f66bd79442be))

* refactor(.env): decouple SBR_WS_CDP_LIST variable from web_scrapper.py file ([`28a6ebe`](https://github.com/poneoneo/Alibaba-Scrapper/commit/28a6ebe35ce212f0896a27b527aab529f2389cbb))

* refactor(html_to_disk, main): write logs info to stderr instead of logs files ([`6762a92`](https://github.com/poneoneo/Alibaba-Scrapper/commit/6762a92241e020ee26536c54b0cea28f8e42d464))

* refactor(playwright_links_getter, main): rename playwright_links_getter.py to main.py ([`71f164d`](https://github.com/poneoneo/Alibaba-Scrapper/commit/71f164da6bb612958070d579c4f4d21bd1135188))

* refactor(scrapper): delete scrapper.py file ([`7ff1f4f`](https://github.com/poneoneo/Alibaba-Scrapper/commit/7ff1f4f3a8b234c1ad83698f95aa68cd3f907fe7))

* refactor(Alibaba_Pages_results): track changes from folder that contains pages result ([`e4d2632`](https://github.com/poneoneo/Alibaba-Scrapper/commit/e4d2632a33bca58405d3f7e6c89d4a93d48cc30f))

* refactor(gitignore): untrack Alibaba_Scrapper_info ([`f2a5c42`](https://github.com/poneoneo/Alibaba-Scrapper/commit/f2a5c423f0918c89ab789b9f7ab63a9d2dc53845))

* refactor(.gitignore):  untrack changes in .gitignore ([`c2fd5b0`](https://github.com/poneoneo/Alibaba-Scrapper/commit/c2fd5b08e8362c4f1d06c0e4d25b8d4ae89ef13e))

* refactor(gitignore): add __main__ to .gitignore file ([`4e4e9ea`](https://github.com/poneoneo/Alibaba-Scrapper/commit/4e4e9eab2bfd0e61822f119dcbb809edc17a8732))

* refactor(requirements, Pipfile): add requirements files ([`9d67f32`](https://github.com/poneoneo/Alibaba-Scrapper/commit/9d67f325683bc5bffab61922833498453d8fdd3d))

* refactor(scrapper): get html content from all pages results(42) matching with keywords:`machines agricoles` asynchronously ([`a29dde2`](https://github.com/poneoneo/Alibaba-Scrapper/commit/a29dde2ce5f2c6a2386dcd8292f8080c474f4499))

* refactor(models_blue_print.txt): build blueprint for database model part 1 ([`f1a276f`](https://github.com/poneoneo/Alibaba-Scrapper/commit/f1a276f4b04c11697cf7d272a6b375ec4598f603))

* refactor(gitignore): add gitignore file ([`7ec42fd`](https://github.com/poneoneo/Alibaba-Scrapper/commit/7ec42fd1516c2469837cd624a12b115345db4a04))

### Style

* style(__main__.py): update error message for export-as-csv subcommand ([`f691533`](https://github.com/poneoneo/Alibaba-Scrapper/commit/f691533b47038458a0242ae5983d36c0f7fdf9c3))

* style(scrape_from_disk.py): avoid to filter divs and json dicts twice + add related key words to pyproject.toml ([`ade96db`](https://github.com/poneoneo/Alibaba-Scrapper/commit/ade96db09b002901a0e7cc4693e10e2e2f10ac44))

* style(cli_api): print pretty message after setting api key ([`f31a63a`](https://github.com/poneoneo/Alibaba-Scrapper/commit/f31a63a584af4513ee0dda37dcf8282e32d78719))

* style(commands): add message at the end of export-as-csv command ([`534073c`](https://github.com/poneoneo/Alibaba-Scrapper/commit/534073c7fef3fbba403e4153a348266beb0ec76f))

* style(api commands): update error message ([`86291d0`](https://github.com/poneoneo/Alibaba-Scrapper/commit/86291d0221f089cbd33470dac98f84437d8f4be9))

* style(commands docs): update info after commands with `aba-run` ([`ddb5a82`](https://github.com/poneoneo/Alibaba-Scrapper/commit/ddb5a8287fc93a64187bf7927a25ff9ddd39bf6a))

* style(project licence): add gpl licence on top of __main__.py ([`270a4ae`](https://github.com/poneoneo/Alibaba-Scrapper/commit/270a4ae2a5c3f3132d821a1167780cce9fb9a8e0))

* style(type hint): update type hint to enhance  lint warinings on typed dict ([`0baca81`](https://github.com/poneoneo/Alibaba-Scrapper/commit/0baca81bcaf656bea6aea52e89997cb2cb1146ac))

* style(src): remove unused print statement ([`4c55f3c`](https://github.com/poneoneo/Alibaba-Scrapper/commit/4c55f3c267b4a24fbc016a09d32148b082285ec6))

* style(src):  udpdate help message at the end of scrapper. ([`92bad37`](https://github.com/poneoneo/Alibaba-Scrapper/commit/92bad37af77ae0b4757f56fdae11210fe77a1291))

### Test

* test(readme): remove all htmlfiles in tests packages ([`11b841b`](https://github.com/poneoneo/Alibaba-Scrapper/commit/11b841b4f805d1b68c68746401d570bb101872f6))

* test(tests): switch to test version ([`c82af59`](https://github.com/poneoneo/Alibaba-Scrapper/commit/c82af597881a4f290e37f50ad00ef6d975a1b5ba))

### Unknown

* docs(readme):update readme with new functionality ([`8cf4d19`](https://github.com/poneoneo/Alibaba-Scrapper/commit/8cf4d19191fb338250f22034b3bc2f8bedd37727))

* release(v0.1.9): v0.1.9

BREAKING CHANGES: v0.1.9 ([`985887b`](https://github.com/poneoneo/Alibaba-Scrapper/commit/985887bdd07cf424967d83b976acdf2d8462e9eb))

* release(v0.1.2): first release aba-cli-scrapper==0.1.2

BREAKING CHANGE:   first release aba-cli-scrapper==0.1.2 ([`8aca981`](https://github.com/poneoneo/Alibaba-Scrapper/commit/8aca9813f5a8d6944048fb1dd055490ede650df5))

* chrore(api command): change aba to aba-run as a base command to add in environnement variable ([`642471f`](https://github.com/poneoneo/Alibaba-Scrapper/commit/642471fecf7b6b37a756ba6bd43932c113f29f5e))

* refactor ([`ab67368`](https://github.com/poneoneo/Alibaba-Scrapper/commit/ab673681f32613b91f417257ec11e943c847429e))

* refactor(src):change the way to import TaskGroup() ([`8f08a37`](https://github.com/poneoneo/Alibaba-Scrapper/commit/8f08a3762349ac3d3c617502a1db494dc7902342))

* track changes from .env file ([`3a1f833`](https://github.com/poneoneo/Alibaba-Scrapper/commit/3a1f833b912f0450113f74e57c53d03041f98aae))

* refactor(playwright_links_getter):rename file main to Playwright_links_getter ([`d998ca3`](https://github.com/poneoneo/Alibaba-Scrapper/commit/d998ca38abb7c50a9cac919fcbe8eb5e8de332ef))

* Initial commit ([`439e286`](https://github.com/poneoneo/Alibaba-Scrapper/commit/439e28621012dcac3065616b46e87894585dceef))
