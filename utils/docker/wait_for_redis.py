import socket
import time


def wait_for_redis(host, port, timeout=300):
    start_time = time.time()
    while True:
        try:
            with socket.create_connection((host, port), timeout=2):
                print("Redis is up and accepting connections.")
                return
        except OSError as ex:
            print("Waiting for Redis...")
            time.sleep(1)
            if time.time() - start_time > timeout:
                print("Timeout waiting for Redis to start.")
                raise TimeoutError(
                    "Redis did not start within the allotted time."
                ) from ex


if __name__ == "__main__":
    wait_for_redis("redis", 6379)
