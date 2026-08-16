# Serve the site locally with live reload
serve:
    bundle exec jekyll serve --livereload

# Install/update gem dependencies
install:
    bundle install

# Build the site into _site/
build:
    bundle exec jekyll build
