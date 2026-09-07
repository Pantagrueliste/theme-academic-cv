---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2022-10-24
type: landing

sections:
  - block: resume-biography
    id: about
    content:
      # A profile from `data/authors/`
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
      # Choose how many pages you would like to display (0 = all pages)
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
      title: Projekt
      filters:
        folders:
          - project
      # To show all items, set `tag` to "*". To filter by a tag, set `tag` to an existing tag name.
      buttons:
        - name: Alla
          tag: '*'
        - name: Pågående forskning
          tag: Current Research
        - name: Tidigare forskning
          tag: Past Research
        - name: Digital humaniora
          tag: Digital Humanities
        - name: Böcker
          tag: Books
      default_button_index: 0
    design:
      columns: 2
      fallback_icon: academic-cap
  - block: collection
    id: code
    content:
      title: Kod
      count: 0
      filters:
        folders:
          - code
    design:
      view: card
      columns: 2
---
