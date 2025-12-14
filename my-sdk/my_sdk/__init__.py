from typing import Dict , Any
__version__ = "0.0.1"
__all__ = ["sql"]

def get_provider_info()->Dict[str,Any]:
        return {
                "package-name" : "my-sdk",
                "name" : "My SDK",
                "description" :"My sdk is a package that provides",
                "version" : [__version__],
                "task-decorator" : [
                        {
                        "name":"sql",
                        "class-name" : "my_sdk.decorators.sql.sql_task"
                        }
                ]
        }