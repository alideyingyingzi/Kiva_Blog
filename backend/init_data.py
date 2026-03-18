from database import SessionLocal, engine, Base
from models import Node, Link

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 初始化数据
def init_data():
    db = SessionLocal()
    try:
        # 检查是否已有数据
        if db.query(Node).count() > 0:
            print("数据库已有数据，跳过初始化")
            return
        
        # 知识图谱数据
        nodes_data = [
            {"id": 1, "name": "Hexo", "group": 1, "description": "静态博客生成器"},
            {"id": 2, "name": "Anzhiyu", "group": 1, "description": "Hexo主题"},
            {"id": 3, "name": "知识图谱", "group": 2, "description": "知识可视化"},
            {"id": 4, "name": "JavaScript", "group": 3, "description": "编程语言"},
            {"id": 5, "name": "Markdown", "group": 3, "description": "标记语言"},
            {"id": 6, "name": "Node.js", "group": 3, "description": "JavaScript运行时"},
            {"id": 7, "name": "D3.js", "group": 4, "description": "数据可视化库"},
            {"id": 8, "name": "CSS", "group": 3, "description": "样式表语言"},
            {"id": 9, "name": "HTML", "group": 3, "description": "超文本标记语言"},
            {"id": 10, "name": "Pug", "group": 5, "description": "模板引擎"},
            {"id": 11, "name": "Stylus", "group": 5, "description": "CSS预处理器"},
            {"id": 12, "name": "可视化", "group": 2, "description": "数据可视化"}
        ]
        
        links_data = [
            {"source_id": 1, "target_id": 2, "value": 1, "label": "使用"},
            {"source_id": 1, "target_id": 4, "value": 1, "label": "基于"},
            {"source_id": 1, "target_id": 5, "value": 1, "label": "支持"},
            {"source_id": 1, "target_id": 6, "value": 1, "label": "运行于"},
            {"source_id": 2, "target_id": 3, "value": 1, "label": "包含"},
            {"source_id": 2, "target_id": 10, "value": 1, "label": "使用"},
            {"source_id": 2, "target_id": 11, "value": 1, "label": "使用"},
            {"source_id": 3, "target_id": 7, "value": 1, "label": "使用"},
            {"source_id": 3, "target_id": 12, "value": 1, "label": "属于"},
            {"source_id": 4, "target_id": 7, "value": 1, "label": "开发"},
            {"source_id": 4, "target_id": 8, "value": 1, "label": "配合"},
            {"source_id": 4, "target_id": 9, "value": 1, "label": "配合"},
            {"source_id": 7, "target_id": 12, "value": 1, "label": "实现"}
        ]
        
        # 插入节点数据
        for node_data in nodes_data:
            node = Node(**node_data)
            db.add(node)
        
        # 插入连接数据
        for link_data in links_data:
            link = Link(**link_data)
            db.add(link)
        
        db.commit()
        print("数据初始化成功")
    except Exception as e:
        print(f"数据初始化失败: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_data()
