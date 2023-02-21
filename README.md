# jenkins-ecs

![image](https://user-images.githubusercontent.com/2573865/220243442-6c468ad7-e211-4cab-92db-f230c32e466d.png)

This project deliver a complete infra-structure using ECS - FARGATE) after you make your changes, run this line bellow to get rid the .terraform trash to commit without .

git filter-branch -f --index-filter 'git rm --cached -r --ignore-unmatch .terraform/'
