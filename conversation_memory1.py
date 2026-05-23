memory_store = []


def save_memory(user, bot):
    memory_store.append({"user": user, "bot": bot})


def get_memory():
    return memory_store


def clear_memory():
    memory_store.clear()