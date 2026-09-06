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
      title: المشاريع
      filters:
        folders:
          - project
      buttons:
        - name: الكل
          tag: '*'
        - name: البحوث الجارية
          tag: البحوث الجارية
        - name: البحوث السابقة
          tag: البحوث السابقة
        - name: الإنسانيات الرقمية
          tag: الإنسانيات الرقمية
        - name: كتب
          tag: كتب
      default_button_index: 0
    design:
      columns: 2
      fallback_icon: academic-cap
  - block: collection
    id: code
    content:
      title: الكود
      count: 0
      filters:
        folders:
          - code
    design:
      view: card
      columns: 2
---
