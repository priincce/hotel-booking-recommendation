from google.cloud import storage

client = storage.Client()
buckets = list(client.list_buckets())
print([bucket.name for bucket in buckets])
