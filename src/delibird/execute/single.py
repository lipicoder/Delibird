"""Single execution mode."""
from ..workflow import Workflow
from ..workflow.job import Job
from .worker import Worker


# pylint: disable=too-few-public-methods
class Single(Worker):
    """Multiprocess worker is a worker that executes jobs in multiprocess"""

    def run(self, execute_job, parameters=None):
        """Run multiprocess worker.

        Args:
            execute_job: job or workflow to be executed
            parameters: parameters of the job or workflow
        """
        # if instance is 'job' type, run this job
        if isinstance(execute_job, Job):
            execute_job()

        # if workflow, run workflow
        # todo: parameters need to change to args and kwargs?

        if isinstance(execute_job, Workflow):
            for job in execute_job.jobs:
                job(parameters)
