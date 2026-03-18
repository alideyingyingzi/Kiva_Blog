from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class NodeBase(BaseModel):
    name: str
    group: int
    description: Optional[str] = None

class NodeCreate(NodeBase):
    pass

class Node(NodeBase):
    id: int
    
    class Config:
        from_attributes = True

class LinkBase(BaseModel):
    source_id: int
    target_id: int
    value: int = 1
    label: str

class LinkCreate(LinkBase):
    pass

class Link(LinkBase):
    id: int
    
    class Config:
        from_attributes = True

class KnowledgeGraph(BaseModel):
    nodes: List[Node]
    links: List[Link]

# 思维导图相关 Schema
class MindMapNode(BaseModel):
    id: Optional[int] = None
    parent_id: Optional[int] = None
    title: str
    content: Optional[str] = None
    topic: Optional[str] = None
    tags: Optional[List[str]] = None
    level: Optional[int] = 1
    is_root: Optional[bool] = False
    children: Optional[List[Dict[str, Any]]] = []

class MindMapResponse(BaseModel):
    success: bool
    data: List[Dict[str, Any]]
    total: int
    message: str
