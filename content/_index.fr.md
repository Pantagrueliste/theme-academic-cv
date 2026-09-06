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
      title: Projets
      filters:
        folders:
          - project
      buttons:
        - name: Tous
          tag: '*'
        - name: Recherche en cours
          tag: Recherche en cours
        - name: Recherches passées
          tag: Recherches passées
        - name: Humanités numériques
          tag: Humanités numériques
        - name: Livres
          tag: Livres
      default_button_index: 0
    design:
      columns: 2
      fallback_icon: academic-cap
  - block: collection
    id: code
    content:
      title: Code
      count: 0
      filters:
        folders:
          - code
    design:
      view: card
      columns: 2
---
