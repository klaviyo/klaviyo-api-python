from openapi_client.paths.api_lists_id_.get import ApiForget
from openapi_client.paths.api_lists_id_.delete import ApiFordelete
from openapi_client.paths.api_lists_id_.patch import ApiForpatch


class ApiListsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
