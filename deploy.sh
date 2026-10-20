#!/usr/bin/env bash
# Rebuild portfolio.html and publish it to GitHub Pages (gh-pages branch, as index.html).
# Live at https://thoumma.github.io/portfolio/
set -e
cd "$(dirname "$0")"
py build.py

W=$(mktemp -d)
git fetch -q origin gh-pages
git worktree add -q "$W" origin/gh-pages
cp portfolio.html "$W/index.html"
touch "$W/.nojekyll"
(
  cd "$W"
  git add index.html .nojekyll
  if git diff --cached --quiet; then echo "No changes to deploy."; else
    git commit -q -m "Deploy portfolio"
    git push -q origin HEAD:gh-pages
    echo "Deployed: https://thoumma.github.io/portfolio/ (live in about 1 minute)"
  fi
)
git worktree remove --force "$W"
