from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Node(Base):
    __tablename__ = "nodes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    group = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)
    
    # 关系
    source_links = relationship("Link", back_populates="source_node", foreign_keys="Link.source_id")
    target_links = relationship("Link", back_populates="target_node", foreign_keys="Link.target_id")

class Link(Base):
    __tablename__ = "links"
    
    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer, ForeignKey("nodes.id"), nullable=False)
    target_id = Column(Integer, ForeignKey("nodes.id"), nullable=False)
    value = Column(Integer, default=1)
    label = Column(String(255), nullable=False)
    
    # 关系
    source_node = relationship("Node", back_populates="source_links", foreign_keys=[source_id])
    target_node = relationship("Node", back_populates="target_links", foreign_keys=[target_id])

# 思维导图节点模型
class KnowledgeNode(Base):
    __tablename__ = "knowledge_nodes"
    
    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("knowledge_nodes.id"), nullable=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)
    topic = Column(String(100), nullable=True)
    tags = Column(String(500), nullable=True)
    level = Column(Integer, default=1)
    is_root = Column(Boolean, default=False)
