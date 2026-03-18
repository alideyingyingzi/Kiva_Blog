from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, KnowledgeNode

# 创建表
Base.metadata.create_all(bind=engine)

def init_mindmap_data():
    db = SessionLocal()
    
    try:
        # 检查是否已有数据
        if db.query(KnowledgeNode).count() > 0:
            print("思维导图数据已存在，跳过初始化")
            return
        
        # 创建根节点
        root_nodes = [
            KnowledgeNode(
                id=1,
                title="仿真软件",
                content="工程仿真软件分类",
                topic="simulation",
                tags="仿真，CAE，工程软件",
                level=0,
                is_root=True
            ),
            KnowledgeNode(
                id=2,
                title="编程开发",
                content="编程语言和技术",
                topic="programming",
                tags="编程，开发，语言",
                level=0,
                is_root=True
            ),
            KnowledgeNode(
                id=3,
                title="大模型技术",
                content="AI 大模型相关技术",
                topic="ai",
                tags="AI，大模型，深度学习",
                level=0,
                is_root=True
            )
        ]
        
        # 创建子节点
        child_nodes = [
            # 仿真软件子节点
            KnowledgeNode(id=10, parent_id=1, title="ABAQUS", content="有限元分析软件", topic="simulation", tags="有限元，力学仿真", level=1),
            KnowledgeNode(id=11, parent_id=1, title="COMSOL", content="多物理场仿真软件", topic="simulation", tags="多物理场，耦合", level=1),
            KnowledgeNode(id=12, parent_id=1, title="Star-CCM+", content="计算流体力学软件", topic="simulation", tags="CFD，流体", level=1),
            KnowledgeNode(id=13, parent_id=1, title="ANSYS", content="综合仿真软件", topic="simulation", tags="结构，热，流体", level=1),
            
            # 编程开发子节点
            KnowledgeNode(id=20, parent_id=2, title="C++", content="高性能编程语言", topic="programming", tags="系统编程，面向对象", level=1),
            KnowledgeNode(id=21, parent_id=2, title="Python", content="通用编程语言", topic="programming", tags="脚本，AI，Web", level=1),
            KnowledgeNode(id=22, parent_id=2, title="子程序开发", content="CAE 软件二次开发", topic="programming", tags="Fortran，UMAT，UEL", level=1),
            
            # 大模型技术子节点
            KnowledgeNode(id=30, parent_id=3, title="模型架构", content="Transformer 等架构", topic="ai", tags="Transformer，Attention", level=1),
            KnowledgeNode(id=31, parent_id=3, title="训练技术", content="模型训练方法", topic="ai", tags="预训练，微调", level=1),
            KnowledgeNode(id=32, parent_id=3, title="应用开发", content="大模型应用", topic="ai", tags="RAG，Agent", level=1),
            
            # 更深层节点
            KnowledgeNode(id=100, parent_id=10, title="用户子程序", content="ABAQUS 二次开发", topic="simulation", tags="UMAT，UEL，VUMAT", level=2),
            KnowledgeNode(id=101, parent_id=10, title="材料模型", content="材料本构关系", topic="simulation", tags="弹性，塑性，损伤", level=2),
            
            KnowledgeNode(id=200, parent_id=20, title="STL 编程", content="C++ 标准模板库", topic="programming", tags="容器，算法，迭代器", level=2),
            KnowledgeNode(id=201, parent_id=21, title="Web 开发", content="Python Web 框架", topic="programming", tags="Flask，Django，FastAPI", level=2),
        ]
        
        # 添加到数据库
        db.add_all(root_nodes)
        db.add_all(child_nodes)
        db.commit()
        
        print(f"成功初始化 {len(root_nodes) + len(child_nodes)} 个思维导图节点")
        
    except Exception as e:
        db.rollback()
        print(f"初始化失败：{e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_mindmap_data()
