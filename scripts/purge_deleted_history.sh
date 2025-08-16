#!/usr/bin/env bash
set -euo pipefail
MODE_ARG="${1:-}"
ensure_filter_repo(){ if command -v git-filter-repo >/dev/null 2>&1;then return 0;fi; if command -v python3 >/dev/null 2>&1;then python3 -m pip install --user git-filter-repo >/dev/null 2>&1 || true; PYUSERBIN="$(python3 -m site --user-base)/bin"; case ":$PATH:" in *":$PYUSERBIN:"*) ;; *) export PATH="$PYUSERBIN:$PATH";; esac;fi; if ! command -v git-filter-repo >/dev/null 2>&1 && command -v brew >/dev/null 2>&1;then brew install git-filter-repo >/dev/null 2>&1 || true;fi; if ! command -v git-filter-repo >/dev/null 2>&1;then mkdir -p .git-filter-repo-bin; curl -fsSL https://raw.githubusercontent.com/newren/git-filter-repo/main/git-filter-repo.py -o .git-filter-repo-bin/git-filter-repo.py; chmod +x .git-filter-repo-bin/git-filter-repo.py; ln -sf "$(pwd)/.git-filter-repo-bin/git-filter-repo.py" .git-filter-repo-bin/git-filter-repo; export PATH="$(pwd)/.git-filter-repo-bin:$PATH";fi; command -v git-filter-repo >/dev/null 2>&1 || { echo "[!] No se pudo instalar git-filter-repo."; exit 1;};}
echo "== PURGA HISTORIAL (archivos eliminados 'D') =="; echo "ADVERTENCIA: reescribe historia y hará push --force."
ensure_filter_repo
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"; cd "$ROOT"
BACKUP="../MENTALIA_backup_mirror_$(date +%Y%m%d_%H%M%S)"; echo "[+] Backup: $BACKUP"; git clone --mirror . "$BACKUP" >/dev/null
git log --all --diff-filter=D --name-only --no-merges | sed '/^$/d' | sort -u > deleted_all_paths.txt
[ ! -s deleted_all_paths.txt ] && { echo "Nada que purgar."; exit 0; }
echo "[i] Total: $(wc -l < deleted_all_paths.txt)"
TARGET="deleted_all_paths.txt"
echo "[+] Ejecutando git-filter-repo (ALL)..."
git filter-repo --invert-paths --paths-from-file "$TARGET"
git push --force origin main