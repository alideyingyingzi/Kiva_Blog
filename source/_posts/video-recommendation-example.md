---
title: 视频推荐示例
date: 2024-03-05 00:00:00
categories: 生活
tags: [视频, 推荐]
location: 上海
---

# 视频推荐示例

这是一个使用卡片式布局推荐bilibili视频的示例，展示了如何在Hexo博客中美观地嵌入视频。

<!-- 引入 Font Awesome 图标库 -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<!-- 视频加载脚本 -->
<script>
  // 自动生成带时间戳的视频 URL，防止缓存
  function generateVideoUrl(baseUrl) {
    const timestamp = new Date().getTime();
    const separator = baseUrl.includes('?') ? '&' : '?';
    return baseUrl + separator + 't=' + timestamp;
  }
  
  // 当页面加载时处理所有视频 iframe
  document.addEventListener('DOMContentLoaded', function() {
    const iframes = document.querySelectorAll('iframe.bilibili-video');
    iframes.forEach(iframe => {
      const src = iframe.getAttribute('src');
      if (src && !src.includes('t=')) {
        // 添加时间戳参数防止缓存
        iframe.setAttribute('src', generateVideoUrl(src));
      }
      
      // 监听加载完成事件
      iframe.onload = function() {
        this.classList.add('loaded');
      };
      
      // 监听加载错误
      iframe.onerror = function() {
        console.error('视频加载失败:', this.getAttribute('src'));
        // 重新加载一次
        const currentSrc = this.getAttribute('src');
        if (currentSrc.includes('t=')) {
          const baseUrl = currentSrc.split('&t=')[0];
          this.setAttribute('src', generateVideoUrl(baseUrl));
        }
      };
    });
    
    // 页面可见性变化时（切换标签页）重新加载视频
    document.addEventListener('visibilitychange', function() {
      if (!document.hidden) {
        iframes.forEach(iframe => {
          const currentSrc = iframe.getAttribute('src');
          if (currentSrc.includes('t=')) {
            const baseUrl = currentSrc.split('&t=')[0];
            iframe.setAttribute('src', generateVideoUrl(baseUrl));
          }
        });
      }
    });
  });
</script>

## 推荐视频

### 卡片式视频推荐

<div class="video-card">
  <div class="video-thumbnail">
    <iframe 
      src="https://player.bilibili.com/player.html?bvid=BV1toPNzWE8R&page=1&high_quality=1&danmaku=0&autoplay=0" 
      scrolling="no" 
      border="0" 
      frameborder="no" 
      framespacing="0" 
      allowfullscreen="true" 
      class="bilibili-video">
    </iframe>
  </div>
  <div class="video-info">
    <!-- 视频标签 -->
    <div class="video-tags">
      <span class="tag">教程</span>
      <span class="tag">Python</span>
    </div>
    <h3 class="video-title">【教程】Python 零基础入门到精通</h3>
    <p class="video-description">本教程涵盖了 Python 的基础知识、面向对象编程、Web 开发等内容，适合零基础的同学学习。</p>
    <div class="video-meta">
    </div>
  </div>
</div>

<div class="video-card">
  <div class="video-thumbnail">
    <!-- 视频时长 -->
    <div class="video-duration">15:46</div>
    <iframe src="https://player.bilibili.com/player.html?isOutside=true&aid=116165678668685&bvid=BV1aBAfzVEEm&cid=36427598437&p=1&high_quality=1&as_wide=1&autoplay=0" 
            scrolling="no" 
            border="0" 
            frameborder="no" 
            framespacing="0" 
            allowfullscreen="true"
            class="bilibili-video">
    </iframe>
  </div>
  <div class="video-info">
    <!-- 视频标签 -->
    <div class="video-tags">
      <span class="tag">科普</span>
      <span class="tag">人工智能</span>
    </div>
    <h3 class="video-title">【科普】人工智能如何改变我们的生活</h3>
    <p class="video-description">探讨人工智能技术的发展历程，以及它如何影响我们的日常生活、工作和社会。</p>
    <div class="video-meta">
      <span class="video-author">UP 主：科技前沿</span>
      <span class="video-views">播放量：50 万+</span>
    </div>
  </div>
</div>

## 相关推荐

<div class="related-videos">
  <h3>你可能还喜欢</h3>
  <div class="related-video-list">
    <div class="related-video-item">
      <div class="related-thumbnail" style="background-image: url('https://i0.hdslb.com/bfs/archive/1a2b3c4d5e6f7g8h9i0.jpg')"></div>
      <div class="related-info">
        <h4>Python 高级特性详解</h4>
        <p>UP主：编程爱好者</p>
      </div>
    </div>
    <div class="related-video-item">
      <div class="related-thumbnail" style="background-image: url('https://i0.hdslb.com/bfs/archive/0i9h8g7f6e5d4c3b2a1.jpg')"></div>
      <div class="related-info">
        <h4>人工智能入门教程</h4>
        <p>UP主：科技前沿</p>
      </div>
    </div>
    <div class="related-video-item">
      <div class="related-thumbnail" style="background-image: url('https://i0.hdslb.com/bfs/archive/2a3b4c5d6e7f8g9h0i1.jpg')"></div>
      <div class="related-info">
        <h4>Web开发实战指南</h4>
        <p>UP主：编程爱好者</p>
      </div>
    </div>
  </div>
</div>

## 如何使用

1. **获取视频嵌入代码**：
   - 打开bilibili视频页面
   - 点击视频下方的「分享」按钮
   - 选择「嵌入代码」
   - 复制生成的iframe代码

2. **替换视频信息**：
   - 将iframe中的`aid`和`cid`替换为你想要嵌入的视频ID
   - 修改视频标题、描述、UP主和播放量信息

3. **添加更多视频**：
   - 复制整个`video-card`结构
   - 修改相应的视频信息

## 技术说明

- **响应式设计**：视频卡片会根据屏幕尺寸自动调整大小
- **悬停效果**：鼠标悬停时卡片会轻微上浮，增加交互感
- **美观布局**：使用卡片式设计，包含视频播放器和详细信息
- **主题适配**：使用主题的颜色变量，与博客风格保持一致
- **高清播放**：添加了 `high_quality=1` 和 `as_wide=1` 参数，确保视频正常加载

<style>
.video-card {
  background: var(--anzhiyu-card-bg, #fff);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--anzhiyu-shadow, 0 4px 12px rgba(0,0,0,0.1));
  margin: 20px 0;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.video-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
}

.video-thumbnail {
  position: relative;
  width: 100%;
  background: transparent;
  padding-bottom: 56.25%; /* 16:9 比例 = 9/16 = 0.5625 = 56.25% */
  height: 0;
  overflow: hidden;
}

.video-thumbnail iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: none;
  margin: 0;
  padding: 0;
}

.video-duration {
  position: absolute;
  bottom: 10px;
  right: 10px;
  background: rgba(0,0,0,0.8);
  color: #fff;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
}

.video-info {
  padding: 20px;
}

.video-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 10px;
  flex-wrap: wrap;
}

.tag {
  background: var(--anzhiyu-main, #409EFF);
  color: #fff;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
}

.video-title {
  font-size: 18px;
  font-weight: 600;
  color: var(--text-highlight-color, #1a1a1a);
  margin: 10px 0;
  line-height: 1.4;
}

.video-description {
  font-size: 14px;
  color: var(--font-color, #666);
  line-height: 1.6;
  margin: 10px 0;
}

.video-meta {
  display: flex;
  gap: 20px;
  margin-top: 15px;
  font-size: 13px;
  color: var(--light-grey, #999);
}

.video-author,
.video-views {
  display: flex;
  align-items: center;
  gap: 5px;
}

@media (max-width: 768px) {
  .video-thumbnail {
    padding-bottom: 56.25%; /* 移动端也保持 16:9 */
  }
  
  .video-title {
    font-size: 16px;
  }
  
  .video-description {
    font-size: 13px;
  }
}
</style>

你可以根据自己的需求修改视频信息和样式，创建属于自己的视频推荐页面！