---
layout: page
title: TEXT
category: text
permalink: /text
---
<!-- test -->
{% assign image_files = site.static_files | where: "photo", true %}
{% for myimage in image_files %}
  <img src="{{ myimage.path }}">
{% endfor %}
<!-- testin -->