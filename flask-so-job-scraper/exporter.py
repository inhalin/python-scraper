import csv

def save_to_file(query, jobs):
  file = open(f'{query}_jobs.csv', mode='w', encoding='utf-8')
  writer = csv.writer(file)
  writer.writerow(['title', 'company', 'location', 'link'])
  for job in jobs:
    writer.writerow(list(job.values()))