from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import pendulum

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def fetch_topics_with_scrapy():
    process = CrawlerProcess(get_project_settings())
    process.crawl('topics')
    process.start() # the script will block here until the crawling is finished

# Define the DAG
default_args = {
    'owner': 'ayshrimali',
    'email': ['ayshrimali@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'start_date': pendulum.datetime(2023, 12, 5),
    'depends_on_past': False, 
}

# A DAG represents a workflow, a collection of tasks
with DAG(
        dag_id="topics_communitiy_openai_new_dag",
        default_args = default_args,
        schedule_interval = '*/20 * * * *', # this dag will run every 20 minutes
        catchup = False
    ) as dag:

    # Tasks are represented as operators
    topics = BashOperator(task_id="topics", bash_command="scrapy crawl topics &> /tmp/scrapy.log")
    # topics = PythonOperator(task_id="topics", python_callable = fetch_topics_with_scrapy, dag = dag)

    @task()
    def finish():
        # this task can be used to send mail or post success message somewhere
        print("done")

    # Set dependencies between tasks
    topics >> finish()