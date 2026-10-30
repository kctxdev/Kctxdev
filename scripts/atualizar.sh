#!/usr/bin/env bash
# Atualiza os painéis na sua máquina e envia para o GitHub (alternativa ao workflow).
set -e
cd "$(dirname "$0")/.."
export GH_USER="${GH_USER:-kctxdev}"
command -v gh >/dev/null 2>&1 && export GITHUB_TOKEN="${GITHUB_TOKEN:-$(gh auth token 2>/dev/null)}"
python3 scripts/gen_stats.py
git add assets/stats.svg
git diff --staged --quiet || git commit -m "chore: atualizar stats"
git push
