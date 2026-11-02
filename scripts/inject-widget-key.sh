#!/usr/bin/env bash
# Swaps the Mpliphi widget's placeholder API key for the real one before
# `firebase deploy` uploads public/, then restores the placeholder so the
# working tree (and git) never holds the real key.
#
# Wired into firebase.json as predeploy/postdeploy hooks. Run manually with
# "inject"/"restore" if you ever need to do a deploy by hand.
set -euo pipefail
cd "$(dirname "$0")/.."

case "${1:-}" in
  inject)
    : "${MPLIPHI_API_KEY:?Set MPLIPHI_API_KEY before deploying (see .env.example)}"
    sed -i "s/__MPLIPHI_API_KEY__/${MPLIPHI_API_KEY}/" public/index.html
    ;;
  restore)
    git checkout -- public/index.html
    ;;
  *)
    echo "usage: $0 inject|restore" >&2
    exit 1
    ;;
esac
