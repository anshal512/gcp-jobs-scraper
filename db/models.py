import psycopg2
from psycopg2.extras import execute_values


class PostgresDB:
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()

    def insert_jobs(self, jobs):
        """
        Bulk insert jobs into linkedin_jobs table.
        Assumes schema:
            linkedin_jobs(
                id SERIAL PRIMARY KEY,
                title TEXT,
                company TEXT,
                location TEXT,
                date_posted DATE,
                link TEXT UNIQUE
            )
        """
        query = """
            INSERT INTO linkedin_jobs (title, company, location, date_posted, link)
            VALUES %s
            ON CONFLICT (link) DO NOTHING;
        """
        values = [
            (job["title"], job["company"], job["location"], job["date_posted"], job["link"])
            for job in jobs
        ]
        execute_values(self.cur, query, values)
        self.conn.commit()
        print(f"✅ Inserted {len(values)} jobs into Postgres (ignoring duplicates)")

    def close(self):
        self.cur.close()
        self.conn.close()
