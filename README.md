# DevOps Lab Internal-2 — practical pack

Clone on the lab PC:
```powershell
git clone https://github.com/kovid-reddy/Jenkins-Repo.git
cd Jenkins-Repo
```

Install Selenium if needed: `py -m pip install selenium`. Chrome must be installed. Modern Selenium uses Selenium Manager to manage ChromeDriver.

## Docker
From a folder containing a Dockerfile: `docker build -t app-name .`, then `docker run --rm app-name`.
From a folder containing compose.yaml: `docker compose up --build`, then `docker compose down`.
For Nginx: `docker compose up -d`, open http://localhost:8080, then `docker compose down`.

## Jenkins on Windows
Create a Freestyle project and copy the required source file(s) from `jenkins-workspaces/<job-folder>/` into that job's workspace. See the matching JENKINS-COMMAND.txt.

If Jenkins says Python is not recognized, run `where.exe python` in PowerShell and use the full python.exe path. Jenkins may run as a Windows service with a different PATH.

For parameterized jobs, add a String Parameter named `NAME`; Windows batch expands it as `%NAME%`. Java receives it in `args[0]`; Python receives it in `sys.argv[1]`.

For Pipeline tasks, create a Pipeline job and paste `jenkins-workspaces/Pipeline/Pipeline.groovy` into the Pipeline script box.

## Set map
1. Jenkins Java Hello World; Selenium Wikipedia screenshot
2. Selenium Google search; parameterized Java through Jenkins
3. Python Docker; Selenium open Google
4. Nginx custom HTML with Compose; Jenkins Python Hello World
5. Jenkins Pipeline with two stages; Wikipedia screenshot
6. Java 17 + Python + Node Compose; parameterized Python through Jenkins
7. GitHub Java reverse number through Jenkins; Nginx Compose
8. GitHub Node file creation through Jenkins; Selenium Google search
9. Jenkins Pipeline; Java with Docker Compose
10. Hello World Docker; Hello World Compose; Selenium open Google

Jenkins configuration, jobs, and workspaces are local to each Jenkins installation. This repo carries portable source/config files, not Jenkins credentials or job history.
