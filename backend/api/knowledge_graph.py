from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Node, Link
from schemas import Node as NodeSchema, NodeCreate, Link as LinkSchema, LinkCreate, KnowledgeGraph

router = APIRouter(prefix="/api/knowledge-graph", tags=["knowledge-graph"])

# 获取完整知识图谱
@router.get("/", response_model=KnowledgeGraph)
def get_knowledge_graph(db: Session = Depends(get_db)):
    nodes = db.query(Node).all()
    links = db.query(Link).all()
    return {"nodes": nodes, "links": links}

# 获取所有节点
@router.get("/nodes", response_model=list[NodeSchema])
def get_nodes(db: Session = Depends(get_db)):
    return db.query(Node).all()

# 获取单个节点
@router.get("/nodes/{node_id}", response_model=NodeSchema)
def get_node(node_id: int, db: Session = Depends(get_db)):
    node = db.query(Node).filter(Node.id == node_id).first()
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")
    return node

# 创建节点
@router.post("/nodes", response_model=NodeSchema)
def create_node(node: NodeCreate, db: Session = Depends(get_db)):
    db_node = Node(**node.model_dump())
    db.add(db_node)
    db.commit()
    db.refresh(db_node)
    return db_node

# 更新节点
@router.put("/nodes/{node_id}", response_model=NodeSchema)
def update_node(node_id: int, node: NodeCreate, db: Session = Depends(get_db)):
    db_node = db.query(Node).filter(Node.id == node_id).first()
    if not db_node:
        raise HTTPException(status_code=404, detail="Node not found")
    for key, value in node.model_dump().items():
        setattr(db_node, key, value)
    db.commit()
    db.refresh(db_node)
    return db_node

# 删除节点
@router.delete("/nodes/{node_id}")
def delete_node(node_id: int, db: Session = Depends(get_db)):
    db_node = db.query(Node).filter(Node.id == node_id).first()
    if not db_node:
        raise HTTPException(status_code=404, detail="Node not found")
    db.delete(db_node)
    db.commit()
    return {"message": "Node deleted successfully"}

# 获取所有连接
@router.get("/links", response_model=list[LinkSchema])
def get_links(db: Session = Depends(get_db)):
    return db.query(Link).all()

# 创建连接
@router.post("/links", response_model=LinkSchema)
def create_link(link: LinkCreate, db: Session = Depends(get_db)):
    # 检查源节点和目标节点是否存在
    source_node = db.query(Node).filter(Node.id == link.source_id).first()
    target_node = db.query(Node).filter(Node.id == link.target_id).first()
    if not source_node or not target_node:
        raise HTTPException(status_code=404, detail="Source or target node not found")
    db_link = Link(**link.model_dump())
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

# 删除连接
@router.delete("/links/{link_id}")
def delete_link(link_id: int, db: Session = Depends(get_db)):
    db_link = db.query(Link).filter(Link.id == link_id).first()
    if not db_link:
        raise HTTPException(status_code=404, detail="Link not found")
    db.delete(db_link)
    db.commit()
    return {"message": "Link deleted successfully"}
