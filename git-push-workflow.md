# Git Push Steps

```bash
$ cd <project directory>
$ git checkout -b <branch-name>
     # create a new local branch and swtich to it
$ git add .
    # add all files unders the project directory to the new-created local branch
$ git commit -m "feat: add new feature"
    # push the the code change from the local branch to staging area.
    # if you are fixing a bug you can change it to "fix: fix logout bug"
$ git push -u origin <remote branch name>
    # push the code change to your target remote branch
    # If the branch does not exist, the command creates it. If the branch exists, the command pushes the code onto it.

```
**Overall Flow**
```mermaid
sequenceDiagram
    participant W as 工作目录(working directory)
    participant S as 暂存区(staging area)
    participant L as 本地分支(local branch)
    participant R as 远程分支(remote branch)
    
    W->>S: git add .（将工作区变更放入暂存区）
    S->>L: git commit（将暂存区快照存入当前分支）
    L->>R: git push（将本地分支推送到远程）
```
