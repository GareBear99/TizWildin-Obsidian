# Install / Merge Instructions

1. Open your local `TizWildin-Obsidian` repo folder.
2. Copy the contents of this additive package into the repo root.
3. Keep all existing folders and sample files exactly where they already are.
4. Do not rename `One_Shots`, `OneShots`, `E-Banjo`, or any existing uploaded directory unless you want to do a separate cleanup pass later.
5. Commit the additions.

## Suggested git flow

```bash
git checkout -b repo-package-additions
# copy files in
python3 Tools/validate_pack.py
git add .
git commit -m "Add repo package docs, inventory, and validation layer"
```

## What not to do in this pass

- do not reconvert audio
- do not move files between folders
- do not delete uploaded assets
- do not normalize names yet
