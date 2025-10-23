# DAL.py
import sqlite3
from pathlib import Path

DB_PATH = Path("projects.db")

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    image_filename TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute(SCHEMA_SQL)
        conn.commit()

def seed():
    # Optional: add a couple of demo rows if table is empty
    with get_connection() as conn:
        cur = conn.execute("SELECT COUNT(*) as c FROM projects")
        if cur.fetchone()["c"] == 0:
            conn.executemany(
                "INSERT INTO projects (title, description, image_filename) VALUES (?, ?, ?)",
                [
                    ("Deloitte Data Challenge",
                     "Analyzed 15,000+ sales rows and modeled scenarios for up to 18% revenue growth.",
                     "deloitte_challenge.jpg"),
                    ("IU Foundation Analytics Dashboard",
                     "Built Tableau KPIs and dashboards to inform donor engagement decisions.",
                     "IUF_photo.jpg"),
                    ("Dance Studio Database System",
                     "Designed and implemented a comprehensive database system for a dance studio company to streamline operations and enhance customer experience.",
                     "dance_studio_db.jpg"),
                    ("Personal Portfolio Website",
                     "Built a responsive personal portfolio website showcasing academic projects, professional experience, and technical skills.",
                     "portfolio_website.jpg"),
                    ("Volunteer Management System",
                     "Developed a database-driven volunteer management system for Boys & Girls Club to track 20+ volunteers, manage scheduling, and analyze attendance trends.",
                     "volunteer_management.jpg"),
                    ("Social Media Analytics Tool",
                     "Created analytics tools for Underrepresented in Tech to track social media performance across Instagram, LinkedIn, and email newsletters.",
                     "social_media_analytics.jpg")
                ],
            )
            conn.commit()

def get_projects():
    init_db()  # ensure schema
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, title, description, image_filename, created_at FROM projects ORDER BY created_at DESC"
        ).fetchall()
    return rows

def insert_project(title: str, description: str, image_filename: str):
    init_db()  # ensure schema
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO projects (title, description, image_filename) VALUES (?, ?, ?)",
            (title.strip(), description.strip(), image_filename.strip()),
        )
        conn.commit()