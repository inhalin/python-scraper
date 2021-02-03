from flask import Flask, render_template, request,redirect, send_file
from scraper import get_jobs
from exporter import save_to_file

app = Flask("SuperScraper")

db = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  query = request.args.get('query')
  if query:
    query = query.lower()
    existing_jobs = db.get(query)
    if existing_jobs:
      jobs = existing_jobs
    else:
      jobs = get_jobs(query)
      db[query] = jobs
  else:
    return redirect('/')
  return render_template(
    "report.html", 
    query=query,
    results_number=len(jobs),
    jobs=jobs
  )

@app.route("/export")
def export():
  try:
    query = request.args.get('query')
    if not query:
      raise Exception()
    query = query.lower()
    jobs = db.get(query)
    if not jobs:
      raise Exception()
    save_to_file(query, jobs)
    return send_file(f"{query}_jobs.csv", as_attachment=True)
  except:
    return redirect('/')

app.run(host="0.0.0.0")