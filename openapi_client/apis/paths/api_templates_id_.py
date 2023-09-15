from openapi_client.paths.api_templates_id_.get import ApiForget
from openapi_client.paths.api_templates_id_.delete import ApiFordelete
from openapi_client.paths.api_templates_id_.patch import ApiForpatch


class ApiTemplatesId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
