import os
import boto3
from urllib.parse import urlparse, urlencode

from scrapinghub import ScrapinghubClient
client = ScrapinghubClient(os.environ['SCRAPINGHUB_KEY'])


def link_prepare(link_text):
    url = urlparse(link_text)
    netloc = url.netloc
    scheme = url.scheme
    if not url.netloc:
        netloc = "medium.com"
        scheme = "https"
    url = url._replace(query = "", netloc=netloc, scheme=scheme)
    return url.geturl()


def read_job_items(event):
    project = client.get_project(event['projectname'])
    jobs_summary = project.jobs.iter()
    job_keys = [j['key'] for j in jobs_summary]
    for job_key in job_keys:
        job = project.jobs.get(job_key)
        items = job.items.iter()
        encoded_items = []
        for item in items:
            # old_keys = item.keys()
            # old_values = item.values()
            # new_keys = [item.decode("utf-8") for item in old_keys]
            # new_values = [item.decode("utf-8") for item in old_values]
            # encoded_item = dict(zip(new_keys, new_values))
            encoded_item = item
            if 'link' in encoded_item:
                encoded_item['link'] = link_prepare(encoded_item['link'])
            encoded_items.append(encoded_item)
        yield map(lambda item:item, encoded_items)


def write_to_dynamo(items):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('medium')
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(
                Item=item
            )


def remove_duplicates(items):
    items_map = {item["link"]: item for item in items}
    return items_map.values()


def handler(event, context):
    list_of_list_of_items = list(read_job_items(event))[:event["jobs_count"]]
    list_of_items = [item for sublist in list_of_list_of_items for item in sublist]
    list_of_items = remove_duplicates(list_of_items)
    write_to_dynamo(list_of_items)
    return {
        "items": list(list_of_items)
    }


if __name__ == "__main__":
    event = {
        "projectname": 446349,
        "jobs_count": 2
    }
    items = handler(event, None)
    print(items)
