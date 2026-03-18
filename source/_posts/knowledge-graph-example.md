---
title: 知识图谱示例
date: 2024-03-04 00:00:00
categories: 技术
tags: [知识图谱, D3.js, 可视化]
cover: /images/tinyBlocks_1.1update.png
location: 上海
---

# 知识图谱示例

这是一个使用 D3.js 实现的知识图谱示例，展示了 Hexo 博客相关的技术栈关系。

## 知识图谱

<div id="knowledge-graph" style="width: 100%; height: 600px; margin: 20px 0; border: 1px solid #eee; border-radius: 8px;"></div>

<script>
  // 从后端 API 获取知识图谱数据
  let nodes = [];
  let links = [];
  
  // API 基础 URL
  const API_BASE_URL = "http://localhost:8000";
  
  // 加载数据
  async function loadKnowledgeGraphData() {
    try {
      const response = await fetch(`${API_BASE_URL}/api/knowledge-graph/`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      
      // 转换数据格式，确保 links 中的 source 和 target 是节点对象
      nodes = data.nodes;
      links = data.links.map(link => ({
        ...link,
        source: nodes.find(node => node.id === link.source_id),
        target: nodes.find(node => node.id === link.target_id),
        label: link.label
      }));
      
      // 初始化图谱
      initGraph();
    } catch (error) {
      console.error("Error loading knowledge graph data:", error);
      // 使用默认数据作为 fallback
      useDefaultData();
    }
  }
  
  // // 使用默认数据
  // function useDefaultData() {
  //   nodes = [
  //     { id: 1, name: "Hexo", group: 1, description: "静态博客生成器" },
  //     { id: 2, name: "Anzhiyu", group: 1, description: "Hexo主题" },
  //     { id: 3, name: "知识图谱", group: 2, description: "知识可视化" },
  //     { id: 4, name: "JavaScript", group: 3, description: "编程语言" },
  //     { id: 5, name: "Markdown", group: 3, description: "标记语言" },
  //     { id: 6, name: "Node.js", group: 3, description: "JavaScript运行时" },
  //     { id: 7, name: "D3.js", group: 4, description: "数据可视化库" },
  //     { id: 8, name: "CSS", group: 3, description: "样式表语言" },
  //     { id: 9, name: "HTML", group: 3, description: "超文本标记语言" },
  //     { id: 10, name: "Pug", group: 5, description: "模板引擎" },
  //     { id: 11, name: "Stylus", group: 5, description: "CSS预处理器" },
  //     { id: 12, name: "可视化", group: 2, description: "数据可视化" }
  //   ];
    
  //   links = [
  //     { source: 1, target: 2, value: 1, label: "使用" },
  //     { source: 1, target: 4, value: 1, label: "基于" },
  //     { source: 1, target: 5, value: 1, label: "支持" },
  //     { source: 1, target: 6, value: 1, label: "运行于" },
  //     { source: 2, target: 3, value: 1, label: "包含" },
  //     { source: 2, target: 10, value: 1, label: "使用" },
  //     { source: 2, target: 11, value: 1, label: "使用" },
  //     { source: 3, target: 7, value: 1, label: "使用" },
  //     { source: 3, target: 12, value: 1, label: "属于" },
  //     { source: 4, target: 7, value: 1, label: "开发" },
  //     { source: 4, target: 8, value: 1, label: "配合" },
  //     { source: 4, target: 9, value: 1, label: "配合" },
  //     { source: 7, target: 12, value: 1, label: "实现" }
  //   ];
    
  //   // 初始化图谱
  //   initGraph();
  // }
  
  // 初始化图谱
  function initGraph() {
    // 清空容器
    container.selectAll("*").remove();
    
    // 创建SVG和缩放行为
    const svg = container.append("svg")
      .attr("width", "100%")
      .attr("height", "100%");
    
    // 创建缩放行为
    const zoom = d3.zoom()
      .scaleExtent([0.1, 4]) // 缩放范围
      .on("zoom", (event) => {
        g.attr("transform", event.transform);
      });
    
    // 应用缩放行为到SVG
    svg.call(zoom);
    
    // 创建一个g元素作为所有图形元素的容器
    const g = svg.append("g");
    
    // 颜色比例尺
    const color = d3.scaleOrdinal(d3.schemeCategory10);
    
    // 力导向模拟
    const simulation = d3.forceSimulation(nodes)
      .force("link", d3.forceLink(links).id(d => d.id).distance(120))
      .force("charge", d3.forceManyBody().strength(-300))
      .force("center", d3.forceCenter(600, 300));
    
    // 创建连接线
    const link = g.append("g")
      .selectAll("line")
      .data(links)
      .enter()
      .append("line")
      .attr("stroke", "#999")
      .attr("stroke-opacity", 0.6)
      .attr("stroke-width", d => Math.sqrt(d.value));
    
    // 创建节点
    const node = g.append("g")
      .selectAll("circle")
      .data(nodes)
      .enter()
      .append("circle")
      .attr("r", 20)
      .attr("fill", d => color(d.group))
      .attr("stroke", "white")
      .attr("stroke-width", 2)
      .call(d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended));
    
    // 获取当前主题模式
    const isDarkMode = document.documentElement.getAttribute('data-theme') === 'dark';
    
    // 根据主题模式设置颜色
    const textColor = isDarkMode ? '#f7f7fa' : '#363636';
    const linkTextColor = isDarkMode ? '#a1a2b8' : '#666';
    const strokeColor = isDarkMode ? '#18171d' : '#ffffff';
    
    // 添加节点标签
    const label = g.append("g")
      .selectAll("text")
      .data(nodes)
      .enter()
      .append("text")
      .text(d => d.name)
      .attr("font-size", "14px")
      .attr("font-weight", "bold")
      .attr("dx", 25)
      .attr("dy", 5)
      .attr("fill", textColor)
      .attr("pointer-events", "none")
      .attr("stroke", strokeColor)
      .attr("stroke-width", 2)
      .attr("paint-order", "stroke");
    
    // 添加连接线标签
    const linkLabel = g.append("g")
      .selectAll("text")
      .data(links)
      .enter()
      .append("text")
      .attr("font-size", "12px")
      .attr("font-weight", "bold")
      .attr("fill", linkTextColor)
      .attr("text-anchor", "middle")
      .attr("pointer-events", "none")
      .attr("stroke", strokeColor)
      .attr("stroke-width", 2)
      .attr("paint-order", "stroke")
      .text(d => d.label);
    
    // 监听主题变化
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.attributeName === 'data-theme') {
          const newIsDarkMode = document.documentElement.getAttribute('data-theme') === 'dark';
          const newTextColor = newIsDarkMode ? '#f7f7fa' : '#363636';
          const newLinkTextColor = newIsDarkMode ? '#a1a2b8' : '#666';
          const newStrokeColor = newIsDarkMode ? '#18171d' : '#ffffff';
          
          // 更新标签颜色
          label.attr("fill", newTextColor).attr("stroke", newStrokeColor);
          linkLabel.attr("fill", newLinkTextColor).attr("stroke", newStrokeColor);
        }
      });
    });
    
    // 开始观察
    observer.observe(document.documentElement, { attributes: true });
    
    // 添加节点点击事件
    node.on("click", (event, d) => {
      alert(`${d.name}: ${d.description}`);
    });
    
    // 模拟更新
    simulation.on("tick", () => {
      link
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);
      
      node
        .attr("cx", d => d.x)
        .attr("cy", d => d.y);
      
      label
        .attr("x", d => d.x)
        .attr("y", d => d.y);
      
      // 更新连接线标签位置
      linkLabel
        .attr("x", d => (d.source.x + d.target.x) / 2)
        .attr("y", d => (d.source.y + d.target.y) / 2);
    });
    
    // 拖拽函数
    function dragstarted(event, d) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }
    
    function dragged(event, d) {
      d.fx = event.x;
      d.fy = event.y;
    }
    
    function dragended(event, d) {
      if (!event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    }
  }
  
  // 创建图谱容器
  const container = d3.select("#knowledge-graph");
  
  // 页面加载时加载数据
  loadKnowledgeGraphData();
</script>

## 如何使用

1. **数据定义**：在 `nodes` 和 `links` 数组中定义知识图谱的数据
2. **样式定制**：可以修改节点颜色、大小、连接线样式等
3. **交互功能**：支持节点拖拽，可自由调整图谱布局
4. **响应式**：图谱会自适应容器大小

## 技术说明

- **D3.js**：使用 D3.js v7 实现力导向图
- **力导向布局**：自动计算节点位置，创建美观的布局
- **交互功能**：支持节点拖拽和力导向模拟
- **颜色编码**：不同组的节点使用不同颜色

你可以根据自己的需求修改数据和样式，创建属于自己的知识图谱！