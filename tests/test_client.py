from delibird.client import Chat
import asyncio

test_map = [
    {
        "name": "chatglm",
        "model": "glm-3-turbo",
    },
    {
        "name": "ernie",
        "model": "ernie-bot-turbo",
    },
]


async def stream_fetch():
    """Test client."""

    messages = [
        {"role": "user", "content": "Python 如何构建类"},
    ]

    # test index
    index = 0

    host = "localhost"
    port = 8000
    router = test_map[index]["name"]
    url = f"http://{host}:{port}/{router}/chat/completion"

    chat = Chat(test_map[index]["model"])

    async for result in chat.stream_fetch(messages, url):
        # 不要自动加换行
        print(result, end="")


def test_client():
    asyncio.run(stream_fetch())
