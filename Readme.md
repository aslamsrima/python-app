# Setup
- Install scrapy - https://docs.scrapy.org/en/latest/intro/install.html
- Install airflow - https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html
- Setup postgres in local or start with docker using script `start-docker.sh`
- To stop, use `stop-docker.sh`
- To start local airflow instance for testing, use `start-local-airflow.sh`
- Install dependencies `cd openaicommentstoscrape && pip install -r requirements.txt`

# Test
- To run scrapy crawler directly, `./run-scrapy-crawler.sh`
- To run through airflow, copy custom DAG `topics-community-openai-new-dags.py` to `dags` folder of airflow installation and refresh airflow DAGs list

> Refer video to review that in action