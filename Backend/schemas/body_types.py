from typing import Dict,Literal, Optional, Union
from pydantic import BaseModel, Field, HttpUrl

class TextBody(BaseModel):
    type: Literal["text"] = "text"
    query: str = Field(..., min_length=1, description="User Text Prompt")

class TextMetaBody(BaseModel): #텍스트는 같은데 판단 기준이 달라져야함(해석에 쓰이는 데이터)
    type: Literal["text_meta"] = "text_meta"
    query: str = Field(..., min_length=1)
    metadata : Dict[str, str] = Field(default_factory=dict, description="Key-value metadata")

class VisionBody(BaseModel):
    type: Literal["vision"] = "vision"
    query: str = Field(..., min_length=1)
    image_url: HttpUrl = Field(..., description="Image URL")
    image_id: Optional[str] = Field(default=None, description="Optional internal image reference")

class RagBody(BaseModel):
    type: Literal["rag"] = "rag"
    query: str = Field(..., min_length=1)
    top_k: int = Field(default=5, le=20, description="Number of retrieved chunks")
    namespace: Optional[str] = Field(default=None, description="Optional index namespace")

RequestBody = Union[TextBody, TextMetaBody, VisionBody, RagBody]