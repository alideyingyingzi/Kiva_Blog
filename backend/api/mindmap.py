from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import KnowledgeNode
from schemas import MindMapNode, MindMapResponse
from typing import List, Optional

router = APIRouter()

def build_tree(nodes: List[dict], parent_id: Optional[int] = None) -> List[dict]:
    """递归构建思维导图树形结构"""
    tree = []
    for node in nodes:
        if node.get('parent_id') == parent_id:
            children = build_tree(nodes, node['id'])
            node['children'] = children
            tree.append(node)
    return tree

@router.get("/mindmap", response_model=MindMapResponse)
def get_mindmap(topic: Optional[str] = None, db: Session = Depends(get_db)):
    """
    获取思维导图数据
    - topic: 可选，筛选特定主题的节点
    """
    try:
        query = db.query(KnowledgeNode).filter(KnowledgeNode.is_root == True)
        
        if topic:
            query = query.filter(KnowledgeNode.topic == topic)
        
        root_nodes = query.all()
        
        if not root_nodes:
            # 如果没有根节点，获取所有节点
            all_nodes = db.query(KnowledgeNode).all()
        else:
            # 获取所有节点用于构建树
            all_nodes = db.query(KnowledgeNode).all()
        
        # 转换为字典列表
        nodes_list = []
        for node in all_nodes:
            nodes_list.append({
                'id': node.id,
                'parent_id': node.parent_id,
                'title': node.title,
                'content': node.content,
                'topic': node.topic,
                'tags': node.tags.split(',') if node.tags else [],
                'level': node.level,
                'is_root': node.is_root
            })
        
        # 构建树形结构
        mindmap_tree = build_tree(nodes_list)
        
        return MindMapResponse(
            success=True,
            data=mindmap_tree,
            total=len(nodes_list),
            message="思维导图数据获取成功"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/mindmap/{node_id}")
def get_mindmap_node(node_id: int, db: Session = Depends(get_db)):
    """获取特定节点及其子节点"""
    try:
        node = db.query(KnowledgeNode).filter(KnowledgeNode.id == node_id).first()
        
        if not node:
            raise HTTPException(status_code=404, detail="节点不存在")
        
        # 获取所有节点
        all_nodes = db.query(KnowledgeNode).all()
        nodes_list = []
        for n in all_nodes:
            nodes_list.append({
                'id': n.id,
                'parent_id': n.parent_id,
                'title': n.title,
                'content': n.content,
                'topic': n.topic,
                'tags': n.tags.split(',') if n.tags else [],
                'level': n.level,
                'is_root': n.is_root
            })
        
        # 从该节点开始构建树
        tree = build_tree(nodes_list, node_id)
        
        return MindMapResponse(
            success=True,
            data=tree,
            total=len(nodes_list),
            message=f"节点 {node.title} 的思维导图获取成功"
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/mindmap/node")
def create_node(node_data: MindMapNode, db: Session = Depends(get_db)):
    """创建新的思维导图节点"""
    try:
        new_node = KnowledgeNode(
            parent_id=node_data.parent_id,
            title=node_data.title,
            content=node_data.content,
            topic=node_data.topic,
            tags=','.join(node_data.tags) if node_data.tags else None,
            level=node_data.level or 1,
            is_root=node_data.is_root or False
        )
        
        db.add(new_node)
        db.commit()
        db.refresh(new_node)
        
        return {
            'success': True,
            'data': {
                'id': new_node.id,
                'title': new_node.title,
                'parent_id': new_node.parent_id
            },
            'message': "节点创建成功"
        }
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
