import requests
from bs4 import BeautifulSoup
from datetime import datetime


class LinkedInScraper:
    BASE_URL = "https://www.linkedin.com/jobs/search/"
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    def __init__(self, keyword="GCP Data Engineer", location="Bangalore, Karnataka, India"):
        self.keyword = keyword
        self.location = location

    def build_url(self):
        return (
            f"{self.BASE_URL}?keywords={self.keyword.replace(' ', '%20')}"
            f"&location={self.location.replace(' ', '%20')}"
        )

    def fetch_page(self):
        url = self.build_url()
        response = requests.get(url, headers=self.HEADERS)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def parse_jobs(self, soup):
        jobs = []
        for job_card in soup.select(".base-card"):
            title = job_card.select_one(".base-search-card__title")
            company = job_card.select_one(".base-search-card__subtitle")
            location = job_card.select_one(".job-search-card__location")
            link = job_card.get("href")
            date_tag = job_card.select_one("time")

            if title and "GCP" in title.get_text() and "Engineer" in title.get_text():
                jobs.append({
                    "title": title.get_text(strip=True),
                    "company": company.get_text(strip=True) if company else None,
                    "location": location.get_text(strip=True) if location else None,
                    "date_posted": datetime.strptime(date_tag["datetime"], "%Y-%m-%d").date() if date_tag else None,
                    "link": link
                })
        return jobs

    def scrape(self):
        soup = self.fetch_page()
        return self.parse_jobs(soup)
