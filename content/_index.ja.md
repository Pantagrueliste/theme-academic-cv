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
      title: プロジェクト
      filters:
        folders:
          - project
      buttons:
        - name: すべて
          tag: '*'
        - name: 現在の研究
          tag: 現在の研究
        - name: 過去の研究
          tag: 過去の研究
        - name: デジタル・ヒューマニティーズ
          tag: デジタル・ヒューマニティーズ
        - name: 書籍
          tag: 書籍
      default_button_index: 0
    design:
      columns: 2
      fallback_icon: academic-cap
  - block: collection
    id: code
    content:
      title: コード
      count: 0
      filters:
        folders:
          - code
    design:
      view: card
      columns: 2
---
