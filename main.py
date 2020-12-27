# https://www.indeed.com/jobs?q=python&limit=50

from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_pages=extract_indeed_pages()

indeed_jobs=extract_indeed_jobs(last_indeed_pages)