#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

if ! command -v gh >/dev/null 2>&1; then
  echo '请先安装 GitHub CLI（gh）：https://cli.github.com/' >&2
  exit 1
fi
if ! gh auth status >/dev/null 2>&1; then
  echo '请先运行 gh auth login，登录你要发布到的 GitHub 账号。' >&2
  exit 1
fi
owner="$(gh api user --jq .login)"
repo="$owner/dopamine-life-system"
if gh repo view "$repo" >/dev/null 2>&1; then
  echo "同名仓库已存在：$repo。请核对已有内容后再决定如何合并。" >&2
  exit 1
fi
if [ ! -d .git ]; then
  git init -b main
  account_id="$(gh api user --jq .id)"
  git config user.name "$owner"
  git config user.email "$account_id+$owner@users.noreply.github.com"
  git add .
  git commit -m 'Publish Dopamine Life System bilingual templates'
fi
if git remote get-url origin >/dev/null 2>&1; then
  echo '已有 origin，请核对后发布。脚本不会覆盖现有远端。' >&2
  exit 1
fi
gh repo create "$repo" --public --source=. --remote=origin --push \
  --description '人生系统与账号规划的多巴胺风格双语网页模板。Colorful bilingual life systems and creator account planners.'
echo "已发布：https://github.com/$repo"
echo '可在 Settings → Pages 选择 main / root，开启网页试玩。'
