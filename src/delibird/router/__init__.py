from delibird.router.spark import send as spark_send
from delibird.router.qwen import send as qwen_send
from delibird.router.ernie import send as ernie_send


def send(config, request, router):
    """发送消息"""


__all__ = ["spark_send", "qwen_send", "ernie_send"]
