# How to remove a file from all commits.md
**Command Execution Steps**
```bash
1. cd <project directory>
2. pip install git-filter-repo
3. git filter-repo --path <file name> --invert-paths --force
4. git push origin --force --all
```
**Verify ignore status**
```bash
git check-ignore -v <file name>
# expected output: .gitignore:6:.env  .env
# 6: the line in .gitignore
# .env (first one): actually working ignore mode
# .env (second): file matched in current path
```
