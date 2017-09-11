Installation:

mkdir project

cd project

sudo apt-get install pip
sudo apt-get install virtualenv

virtualenv .env
source .env/bin/activate

pip install -r requirements.txt


Start scraper:
scrapy crawl <name>

example:
scrapy crawl eoliaseeds

csv file will be saved to data folder 
(if run one scraper several times, to csv write new rows to old file without deleting old raws)

also you want some enother filename you can use command:
scrapy crawl <name> -o <name_which_you_want>.csv

file saving in folder near this file README.md
