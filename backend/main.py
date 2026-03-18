from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.knowledge_graph import router as knowledge_graph_router
from api.mindmap import router as mindmap_router
from database import engine, Base
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 创建 FastAPI 应用
app = FastAPI(
    title="Knowledge Graph API",
    description="API for managing knowledge graph data",
    version="1.0.0"
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(knowledge_graph_router)
app.include_router(mindmap_router)

# 根路径
@app.get("/")
def read_root():
    return {"message": "Knowledge Graph API", "version": "1.0.0"}

# 健康检查
@app.get("/health")
def health_check():
    return {"status": "healthy"}
