---
title: ''
summary: ''
date: 2022-10-24
type: landing

sections:
  - block: resume-biography
    id: about
    content:
      username: clement
    design:
      avatar:
        size: medium
        shape: circle
  - block: collection
    id: posts
    content:
      title: Zibaldone
      subtitle: ''
      text: ''
      count: 5
      filters:
        folders:
          - post
      offset: 0
      order: desc
    design:
      view: article-grid
      columns: 2
  - block: portfolio
    id: projects
    content:
      title: 项目
      filters:
        folders:
          - project
      buttons:
        - name: 全部
          tag: '*'
        - name: 当前研究
          tag: 当前研究
        - name: 过往研究
          tag: 过往研究
        - name: 数字人文
          tag: 数字人文
        - name: 著作
          tag: 著作
      default_button_index: 0
    design:
      columns: 2
      fallback_icon: academic-cap
  - block: collection
    id: code
    content:
      title: 代码
      count: 0
      filters:
        folders:
          - code
    design:
      view: card
      columns: 2
---
