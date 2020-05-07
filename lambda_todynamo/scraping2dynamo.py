import os


from scrapinghub import ScrapinghubClient
client = ScrapinghubClient(os.environ['SCRAPINGHUB_KEY'])

def read_job_items(event):
    project = client.get_project(event['projectname'])
    jobs_summary = project.jobs.iter()
    job_keys = [j['key'] for j in jobs_summary]
    for job_key in job_keys:
        job_key = job_keys[0]
        job = project.jobs.get(job_key)
        items = job.items.iter()
        yield map(lambda item:item, items)


def handler(event, context):
    read_job_items(event)
    return "1"

if __name__ == "__main__":
    event = {
        "projectname": 446349
    }
    list_of_list_of_items = list(read_job_items(event))
    list_of_items = [item for sublist in list_of_list_of_items for item in sublist]
    print(list_of_items)