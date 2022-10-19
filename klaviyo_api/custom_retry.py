import tenacity

class retry_if_qualifies(tenacity.retry_if_exception):
    """Retry strategy that retries if the exception is an ``HTTPError`` with
    given status code.
    """

    def __init__(self, statuses):
        def qualifies_for_retry(exception):

            if 'status' in dir(exception):

                return (
                    exception.status in statuses
                )

            else:

                return False

        super().__init__(predicate=qualifies_for_retry)