from scraper.linkedin_scraper import LinkedInScraper
from db.models import PostgresDB

if __name__ == "__main__":
    # 1. Run scraper
    scraper = LinkedInScraper()
    jobs = scraper.scrape()
    print(f"Scraped {len(jobs)} jobs")

    # 2. Save to Postgres
    if jobs:
        db = PostgresDB(
            dbname="linkdin_api",
            user="myuser",
            password="password",
            host="localhost",
            port="5432"
        )
        db.insert_jobs(jobs)
        db.close()
