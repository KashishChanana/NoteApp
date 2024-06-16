from tasks.blog_task import BlogTask
from tasks.key_concepts_task import KeyConceptsTask
from tasks.qa_task import QATask
from tasks.summary_task import SummaryTask

class TaskFactory:
    _tasks = {
        "Key Concepts": KeyConceptsTask,
        "Summary": SummaryTask,
        "Blog": BlogTask,
        "QATask": QATask
    }

    @staticmethod
    def get_task(task_name):
        task_class = TaskFactory._tasks.get(task_name)
        if task_class is None:
            raise ValueError(f"Task '{task_name}' not recognized")
        return task_class()