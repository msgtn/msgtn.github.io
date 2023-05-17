---
layout: category
title: IMAGE
category: image
permalink: /image
---
<!-- test -->
{% assign image_files = site.static_files | where: "photo", true %}
{% for myimage in image_files %}
  <a data-lightbox="img" href="{{ myimage.path }}">
    <img src="{{ myimage.path }}">
  </a>
{% endfor %}
<!-- testin -->