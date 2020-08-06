"""
Created on: 06/08/20
Author: Pavankumar Pamuru

"""
from elasticsearch_dsl import connections

connections.create_connection(hosts=['localhost'], timeout=20)

from elasticsearch_dsl import Index, Document, Text, analyzer

blogs = Index('blogs')

# define custom settings
blogs.settings(
    number_of_shards=1,
    number_of_replicas=0
)

# define aliases
blogs.aliases(
    old_blogs={}
)


@blogs.document
class Post(Document):
    title = Text()


# You can attach custom analyzers to the index

html_strip = analyzer('html_strip',
                      tokenizer="standard",
                      filter=["standard", "lowercase", "stop", "snowball"],
                      char_filter=["html_strip"]
                      )

blogs.analyzer(html_strip)

# delete the index, ignore if it doesn't exist
blogs.delete(ignore=404)

# create the index in elasticsearch
blogs.create()
