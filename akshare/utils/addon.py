import requests
import time
import pickle


def cached(func):
    name = func.__name__

    def wrapper(*args, **kwargs):
        try:
            with open(f"{name}.pkl", "rb") as f:
                obj = pickle.load(f)
                print(f"Use cached {name}")
                return obj
        except Exception:
            pass

        result = func(*args, **kwargs)

        with open(f"{name}.pkl", "wb") as f:
            pickle.dump(result, f)

        return result

    return wrapper


def get_repeat(url, params={}, timeout: int = 15):
    while True:
        try:
            r = requests.get(url, params=params, timeout=timeout)
            return r
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
