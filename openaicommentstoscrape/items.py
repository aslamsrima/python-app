# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# TopicItem model will hold data and push to db through scrapy pipeline
class TopicItem(scrapy.Item):
    topic_name = scrapy.Field()
    replies = scrapy.Field()
    views = scrapy.Field()
    activity = scrapy.Field()
    topic_url = scrapy.Field()

# CommentsItem model will hold data and push to db through scrapy pipeline
class CommentsItem(scrapy.Item):
    topic = scrapy.Field()
    author = scrapy.Field()
    author_link = scrapy.Field()
    comment_time = scrapy.Field()
    comment_body = scrapy.Field()
    comment_likes = scrapy.Field()