import pydantic
import typing
class Code(pydantic.BaseModel):
    code:typing.Optional[str]=None
    lang:str=None
    stdin=""