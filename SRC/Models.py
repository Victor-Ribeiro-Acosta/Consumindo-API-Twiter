from pydantic import BaseModel

class TrendItem(BaseModel):
  name: 'string'
  url: 'string'