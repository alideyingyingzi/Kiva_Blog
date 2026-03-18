---
title: 知识思维导图
date: 2024-03-05 00:00:00
categories: 技术
tags: [思维导图，知识图谱，可视化]
location: 上海
---

# 知识思维导图

基于 D3.js 的知识思维导图可视化展示，数据实时从数据库加载。

<!-- 引入 D3.js -->
<script src="https://d3js.org/d3.v7.min.js"></script>

<div class="mindmap-container">
  <div class="mindmap-header">
    <h3>知识思维导图</h3>
    <div class="mindmap-controls">
      <button id="reload-mindmap" class="control-btn" title="刷新">
        <i class="fas fa-redo"></i>
      </button>
      <button id="zoom-in" class="control-btn" title="放大">
        <i class="fas fa-search-plus"></i>
      </button>
      <button id="zoom-out" class="control-btn" title="缩小">
        <i class="fas fa-search-minus"></i>
      </button>
      <button id="reset-view" class="control-btn" title="重置视图">
        <i class="fas fa-expand"></i>
      </button>
    </div>
  </div>
  
  <div class="mindmap-loading" id="mindmap-loading">
    <i class="fas fa-spinner fa-spin"></i>
    <p>正在加载思维导图...</p>
  </div>
  
  <div class="mindmap-content" id="mindmap-content">
    <!-- 思维导图将在这里渲染 -->
  </div>
  
  <div class="mindmap-node-detail" id="node-detail">
    <div class="detail-header">
      <h4 id="detail-title">节点详情</h4>
      <button class="close-detail" id="close-detail">
        <i class="fas fa-times"></i>
      </button>
    </div>
    <div class="detail-content" id="detail-content">
      <!-- 节点详细信息 -->
    </div>
  </div>
</div>

<style>
.mindmap-container {
  position: relative;
  width: 100%;
  height: 80vh;
  background: var(--anzhiyu-card-bg, #fff);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--anzhiyu-shadow, 0 4px 12px rgba(0,0,0,0.1));
  margin: 20px 0;
}

.mindmap-header {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  z-index: 10;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  background: linear-gradient(to bottom, var(--anzhiyu-card-bg, #fff), transparent);
  pointer-events: none;
}

.mindmap-header h3 {
  margin: 0;
  font-size: 18px;
  font-weight: 600;
  color: var(--text-highlight-color, #1a1a1a);
  pointer-events: auto;
}

.mindmap-controls {
  display: flex;
  gap: 8px;
  pointer-events: auto;
}

.control-btn {
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 8px;
  background: var(--anzhiyu-card-bg-secondary, #f5f5f5);
  color: var(--font-color, #666);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  font-size: 16px;
}

.control-btn:hover {
  background: var(--anzhiyu-main, #409EFF);
  color: #fff;
  transform: translateY(-2px);
}

.mindmap-loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  z-index: 5;
}

.mindmap-loading i {
  font-size: 48px;
  color: var(--anzhiyu-main, #409EFF);
  display: block;
  margin-bottom: 15px;
}

.mindmap-loading p {
  font-size: 14px;
  color: var(--font-color, #666);
  margin: 0;
}

.mindmap-content {
  width: 100%;
  height: 100%;
}

.mindmap-content svg {
  width: 100%;
  height: 100%;
}

/* 思维导图节点样式 */
.mindmap-nodes rect {
  cursor: pointer;
  transition: all 0.3s ease;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
}

.mindmap-nodes rect:hover {
  filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
  transform: scale(1.05);
}

/* 思维导图连线样式 */
.mindmap-links path {
  stroke: #ddd;
  stroke-width: 2px;
  fill: none;
}

/* 节点详情面板 */
.mindmap-node-detail {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 320px;
  max-height: 400px;
  background: var(--anzhiyu-card-bg, #fff);
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.15);
  z-index: 20;
  overflow: hidden;
  display: none;
  flex-direction: column;
}

.mindmap-node-detail.show {
  display: flex;
}

.detail-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  border-bottom: 1px solid var(--anzhiyu-border-color, #e0e0e0);
  background: var(--anzhiyu-card-bg-secondary, #f5f5f5);
}

.detail-header h4 {
  margin: 0;
  font-size: 16px;
  font-weight: 600;
  color: var(--text-highlight-color, #1a1a1a);
}

.close-detail {
  background: none;
  border: none;
  font-size: 20px;
  color: var(--light-grey, #999);
  cursor: pointer;
  padding: 0;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  transition: all 0.3s ease;
}

.close-detail:hover {
  background: var(--anzhiyu-main, #409EFF);
  color: #fff;
}

.detail-content {
  padding: 20px;
  overflow-y: auto;
  max-height: 340px;
}

.detail-content h5 {
  margin: 0 0 10px 0;
  font-size: 14px;
  font-weight: 600;
  color: var(--anzhiyu-main, #409EFF);
}

.detail-content p {
  margin: 0 0 15px 0;
  font-size: 13px;
  line-height: 1.6;
  color: var(--font-color, #666);
}

.detail-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 10px;
}

.detail-tag {
  background: var(--anzhiyu-card-bg-secondary, #f5f5f5);
  color: var(--anzhiyu-main, #409EFF);
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 11px;
  font-weight: 500;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .mindmap-container {
    height: 60vh;
  }
  
  .mindmap-node-detail {
    width: calc(100% - 40px);
    right: 20px;
    left: 20px;
    max-height: 300px;
  }
  
  .mindmap-header h3 {
    font-size: 16px;
  }
  
  .control-btn {
    width: 32px;
    height: 32px;
    font-size: 14px;
  }
}
</style>

<script>
(function() {
  // 思维导图配置
  const config = {
    width: 0,
    height: 0,
    nodeWidth: 180,
    nodeHeight: 50,
    levelDistance: 220,
    siblingDistance: 60,
    colors: [
      '#409EFF', '#67C23A', '#E6A23C', '#F56C6C', 
      '#909399', '#A0CFFF', '#B3E19D', '#D3D4D6'
    ]
  };

  let svg, g, zoom;
  let allNodes = [];
  let allLinks = [];
  let expandedNodes = new Set(); // 记录展开的节点
  
  // 初始化思维导图
  async function initMindMap() {
    const container = document.getElementById('mindmap-content');
    const loading = document.getElementById('mindmap-loading');
    
    // 获取容器尺寸
    config.width = container.clientWidth;
    config.height = container.clientHeight;
    
    try {
      // 从后端 API 获取数据
      const response = await fetch('http://localhost:8000/mindmap');
      const result = await response.json();
      
      if (!result.success) {
        throw new Error(result.message || '获取数据失败');
      }
      
      console.log('获取到的数据:', result.data);
      
      // 隐藏加载提示
      loading.style.display = 'none';
      
      // 保存所有节点
      allNodes = result.data;
      
      // 默认展开所有节点
      function markExpanded(nodes) {
        nodes.forEach(node => {
          expandedNodes.add(node.id);
          if (node.children && node.children.length > 0) {
            markExpanded(node.children);
          }
        });
      }
      markExpanded(result.data);
      
      // 创建 SVG 和 g
      createSVG(container);
      
      // 渲染思维导图
      renderMindMap();
      
    } catch (error) {
      console.error('加载思维导图失败:', error);
      loading.innerHTML = `
        <i class="fas fa-exclamation-circle" style="color: #F56C6C;"></i>
        <p>加载失败：${error.message}</p>
        <button onclick="initMindMap()" style="margin-top:10px;padding:8px 16px;background:#409EFF;color:#fff;border:none;border-radius:4px;cursor:pointer;">
          <i class="fas fa-redo"></i> 重试
        </button>
      `;
    }
  }
  
  // 创建 SVG
  function createSVG(container) {
    // 清空容器
    container.innerHTML = '';
    
    // 创建 SVG
    svg = d3.select(container)
      .append('svg')
      .attr('width', config.width)
      .attr('height', config.height)
      .attr('viewBox', [0, 0, config.width, config.height]);
    
    // 添加缩放功能
    zoom = d3.zoom()
      .scaleExtent([0.1, 4])
      .on('zoom', (event) => {
        g.attr('transform', event.transform);
      });
    
    svg.call(zoom);
    
    // 创建组
    g = svg.append('g');
  }
  
  // 渲染思维导图
  function renderMindMap() {
    // 第一次遍历：获取所有可见节点（不计算位置）
    function collectNodes(nodes, depth = 0) {
      const collected = [];
      
      nodes.forEach(node => {
        if (!expandedNodes.has(node.id)) return;
        
        collected.push({
          id: node.id,
          name: node.title,
          content: node.content,
          topic: node.topic,
          tags: node.tags,
          level: depth,
          is_root: node.is_root,
          children: node.children || [],
          hasChildren: node.children && node.children.length > 0
        });
        
        if (node.children && node.children.length > 0 && expandedNodes.has(node.id)) {
          collected.push(...collectNodes(node.children, depth + 1));
        }
      });
      
      return collected;
    }
    
    const allVisibleNodes = collectNodes(allNodes);
    
    if (allVisibleNodes.length === 0) {
      console.error('没有节点可渲染！');
      return;
    }
    
    // 第二次遍历：计算位置
    function calculatePositions(nodes, depth = 0, startY = 0) {
      const positionedNodes = [];
      const links = [];
      let currentY = startY;
      
      nodes.forEach(node => {
        if (!expandedNodes.has(node.id)) return;
        
        const x = depth * config.levelDistance + 100;
        const y = currentY;
        
        const positionedNode = {
          ...node,
          x: x,
          y: y
        };
        
        positionedNodes.push(positionedNode);
        currentY += config.nodeHeight + config.siblingDistance;
        
        // 创建连接到子节点
        if (node.children && node.children.length > 0 && expandedNodes.has(node.id)) {
          const childResult = calculatePositions(node.children, depth + 1, currentY);
          
          // 添加连接到第一个子节点
          if (childResult.nodes.length > 0) {
            links.push({
              source: { x: x, y: y },
              target: { x: childResult.nodes[0].x, y: childResult.nodes[0].y }
            });
          }
          
          positionedNodes.push(...childResult.nodes);
          links.push(...childResult.links);
          currentY = childResult.nextY;
        }
      });
      
      return { nodes: positionedNodes, links: links, nextY: currentY };
    }
    
    // 计算整体高度，居中显示
    const totalHeight = allVisibleNodes.length * (config.nodeHeight + config.siblingDistance);
    const centeredStartY = (config.height - totalHeight) / 2;
    
    const result = calculatePositions(allNodes, 0, centeredStartY);
    
    console.log('渲染数据:', result);
    
    if (result.nodes.length === 0) {
      console.error('没有节点可渲染！');
      return;
    }
    
    // 清空并重新绘制
    g.selectAll('*').remove();
    
    // 绘制连接线（使用曲线）
    const linkGenerator = d3.linkHorizontal()
      .x(d => d.x)
      .y(d => d.y);
    
    g.append('g')
      .attr('class', 'mindmap-links')
      .selectAll('path')
      .data(result.links)
      .join('path')
      .attr('d', d => linkGenerator({ source: d.source, target: d.target }))
      .attr('stroke', '#ddd')
      .attr('stroke-width', 2)
      .attr('fill', 'none');
    
    // 创建节点组
    const nodeGroups = g.append('g')
      .attr('class', 'mindmap-nodes')
      .selectAll('g')
      .data(result.nodes)
      .join('g')
      .attr('transform', d => `translate(${d.x},${d.y})`);
    
    // 添加节点背景矩形（圆角）
    nodeGroups.append('rect')
      .attr('x', -config.nodeWidth / 2)
      .attr('y', -config.nodeHeight / 2)
      .attr('width', config.nodeWidth)
      .attr('height', config.nodeHeight)
      .attr('rx', 8)
      .attr('ry', 8)
      .attr('fill', (d, i) => config.colors[i % config.colors.length])
      .attr('stroke', '#fff')
      .attr('stroke-width', 2)
      .attr('cursor', 'pointer')
      .attr('class', 'mindmap-node-rect')
      .on('click', (event, d) => {
        event.stopPropagation();
        if (d.hasChildren) {
          toggleNode(d);
        } else {
          showNodeDetail(d);
        }
      });
    
    // 添加展开/收起图标（如果有子节点）
    nodeGroups.filter(d => d.hasChildren)
      .append('circle')
      .attr('cx', config.nodeWidth / 2 - 5)
      .attr('cy', 0)
      .attr('r', 8)
      .attr('fill', '#fff')
      .attr('stroke', config.colors[0])
      .attr('stroke-width', 2)
      .attr('cursor', 'pointer')
      .on('click', (event, d) => {
        event.stopPropagation();
        toggleNode(d);
      });
    
    // 添加展开/收起图标文字
    nodeGroups.filter(d => d.hasChildren)
      .append('text')
      .attr('x', config.nodeWidth / 2 - 5)
      .attr('y', 4)
      .attr('text-anchor', 'middle')
      .attr('fill', config.colors[0])
      .attr('font-size', '12px')
      .attr('font-weight', 'bold')
      .attr('cursor', 'pointer')
      .attr('pointer-events', 'none')
      .text(d => expandedNodes.has(d.id) ? '-' : '+');
    
    // 添加节点文字
    nodeGroups.append('text')
      .text(d => d.name)
      .attr('text-anchor', 'middle')
      .attr('dy', 5)
      .attr('fill', '#fff')
      .attr('font-size', '13px')
      .attr('font-weight', '600')
      .attr('pointer-events', 'none')
      .attr('width', config.nodeWidth - 20);
    
    // 点击空白处关闭详情
    svg.on('click', () => {
      document.getElementById('node-detail').classList.remove('show');
    });
  }

// 切换节点展开/收起状态
function toggleNode(node) {
  if (expandedNodes.has(node.id)) {
    expandedNodes.delete(node.id);
  } else {
    expandedNodes.add(node.id);
  }
  renderMindMap();
}

// 显示节点详情
function showNodeDetail(node) {
    const detailPanel = document.getElementById('node-detail');
    const detailTitle = document.getElementById('detail-title');
    const detailContent = document.getElementById('detail-content');
    
    detailTitle.textContent = node.name;
    
    let html = '';
    
    if (node.content) {
      html += `<h5>内容</h5><p>${node.content}</p>`;
    }
    
    if (node.topic) {
      html += `<h5>主题</h5><p>${node.topic}</p>`;
    }
    
    if (node.tags && node.tags.length > 0) {
      html += `<h5>标签</h5><div class="detail-tags">`;
      node.tags.forEach(tag => {
        html += `<span class="detail-tag">${tag}</span>`;
      });
      html += `</div>`;
    }
    
    if (!node.content && !node.topic && (!node.tags || node.tags.length === 0)) {
      html = '<p>暂无详细信息</p>';
    }
    
    detailContent.innerHTML = html;
    detailPanel.classList.add('show');
  }
  
  // 控制按钮事件
  document.getElementById('reload-mindmap').addEventListener('click', initMindMap);
  
  document.getElementById('zoom-in').addEventListener('click', () => {
    svg.transition().call(zoom.scaleBy, 1.3);
  });
  
  document.getElementById('zoom-out').addEventListener('click', () => {
    svg.transition().call(zoom.scaleBy, 0.7);
  });
  
  document.getElementById('reset-view').addEventListener('click', () => {
    svg.transition().call(
      zoom.transform,
      d3.zoomIdentity,
      d3.zoomTransform(svg.node()).invert([config.width / 2, config.height / 2])
    );
  });
  
  document.getElementById('close-detail').addEventListener('click', () => {
    document.getElementById('node-detail').classList.remove('show');
  });
  
  // 页面加载完成后初始化
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMindMap);
  } else {
    initMindMap();
  }
})();
</script>

## 使用说明

### 功能特性

- **📊 实时数据** - 从数据库实时加载知识节点
- **🎨 可视化展示** - 使用力导向图展示知识结构
- **🔍 缩放平移** - 支持缩放和平移操作
- **📝 节点详情** - 点击节点查看详细信息
- **🎯 拖拽交互** - 可以拖拽节点调整位置

### 操作指南

1. **查看思维导图**
   - 页面加载时自动从数据库获取数据
   - 不同颜色的节点代表不同的知识分类

2. **交互操作**
   - **点击节点** - 查看节点详细信息
   - **拖拽节点** - 调整节点位置
   - **滚轮缩放** - 放大缩小视图
   - **拖动空白处** - 平移视图

3. **控制按钮**
   - 🔄 **刷新** - 重新加载数据
   - 🔍+ **放大** - 放大视图
   - 🔍- **缩小** - 缩小视图
   - ⛶ **重置** - 重置视图到初始状态

### 数据来源

思维导图数据来自后端 API：`GET /mindmap`

数据从数据库的 `knowledge_nodes` 表中读取，支持树形结构展示。
