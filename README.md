GCP Jobs Scraper

A Python project to scrape LinkedIn job postings for GCP Data Engineer roles in Bangalore, India, and store them in a Postgres database.

📌 Features

Scrapes job title, company, location, date posted, and job link from LinkedIn

Stores job records in a PostgreSQL database

Avoids duplicates using ON CONFLICT handling

Modular structure (scrapers, db models, utils) for easy extension

Ready for scheduling with Airflow or cron

⚡ Installation

Clone this repository:

git clone https://github.com/<your-username>/gcp-jobs-scraper.git
cd gcp-jobs-scraper


Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Configure PostgreSQL:

Create a database (example: linkdin_api)

Create a table:

CREATE TABLE linkedin_jobs (
    id SERIAL PRIMARY KEY,
    title TEXT,
    company TEXT,
    location TEXT,
    date_posted DATE,
    link TEXT UNIQUE
);

🚀 Usage

Run the scraper and save jobs to Postgres:

python main.py


Check jobs in Postgres:

SELECT * FROM linkedin_jobs ORDER BY date_posted DESC;

🛠️ Future Improvements

Add recruiter scraping + separate recruiters table

Integrate Airflow for daily job runs

Add logging + monitoring

Extend scraper to other locations/roles


