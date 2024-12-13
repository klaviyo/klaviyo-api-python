import time
import random
from openapi_client.exceptions import ApiException


class RetryWithExponentialBackoff:

    base_interval = 0.5
    rand_factor = 0.5
    multiplier = 1.5

    def __init__(self, retry_codes, num_retries = 3, max_interval = 60):
        self.retry_codes = retry_codes
        self.num_retries = num_retries
        self.max_interval = max_interval

    def with_retry(self, func_to_call, *args, **kwargs):
        last_request_retry_after = None
        last_request_timestamp = None
        attempt = 0
        iteration = 0

        while True:
            try:
                current_time = time.time()
                retry_after_value_elapsed = (last_request_retry_after is None or
                                             current_time - last_request_timestamp > last_request_retry_after)
                if retry_after_value_elapsed:
                    attempt += 1
                    return func_to_call(*args,**kwargs)
            except ApiException as e:
                if e.status not in self.retry_codes or attempt >= self.num_retries:
                    raise e
                response_headers = e.headers if e.headers is not None else {}
                last_request_retry_after = response_headers.get('Retry-After', None)
                if last_request_retry_after is not None:
                    last_request_retry_after = int(last_request_retry_after)
                last_request_timestamp = time.time()

            sleep_seconds = self.exponential_backoff(iteration)
            time.sleep(sleep_seconds)
            iteration += 1

    def exponential_backoff(self, iteration):
        wait_time = min(self.base_interval * (self.multiplier ** iteration), self.max_interval)

        # Apply randomness to avoid thundering herd
        delta = self.rand_factor * wait_time
        random_neg_1_to_1 = 2 * random.random() - 1
        return wait_time + delta * random_neg_1_to_1
