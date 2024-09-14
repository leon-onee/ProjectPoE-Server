from pydantic import BaseModel


class POBUrlRequest(BaseModel):
    pob_url: str
