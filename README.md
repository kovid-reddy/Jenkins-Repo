# DevOps Lab Internal-2 — practical pack

Clone the repository on the lab PC:

```powershell
git clone https://github.com/kovid-reddy/Jenkins-Repo.git
cd Jenkins-Repo
```

All paths below are relative to the cloned `Jenkins-Repo` folder. Open the folder that contains the listed `Dockerfile` or `compose.yaml` before running Docker commands.

## Exact question-to-file map

### SET 1
- **1A — Simple Hello World Java through Jenkins**
  - Java source: `jenkins-workspaces/Hello-Java/HelloWorld.java`
  - Jenkins instructions: `jenkins-workspaces/Hello-Java/JENKINS-COMMAND.txt`
- **1B — Selenium: open Wikipedia and take screenshot**
  - Python source: `SET1/selenium/wiki_screenshot.py`
  - Run from that folder: `py wiki_screenshot.py`
  - Screenshot output: `wikipedia.png` in the current working folder.

### SET 2
- **2A — Selenium: open Google and search content**
  - Python source: `SET2/selenium/google_search.py`
  - Run from that folder: `py google_search.py`
- **2B — Parameterized Java through Jenkins**
  - Java source: `jenkins-workspaces/Parameterized-Java/ParameterizedHello.java`
  - Jenkins instructions: `jenkins-workspaces/Parameterized-Java/JENKINS-COMMAND.txt`
  - Jenkins String Parameter name: `NAME`; Windows batch argument: `%NAME%`.

### SET 3
- **3A — Create and run Python program using Docker**
  - Files: `SET3/python-docker/hello.py` and `SET3/python-docker/Dockerfile`
  - Commands (run from `SET3/python-docker`):
    ```powershell
    docker build -t python-hello .
    docker run --rm python-hello
    ```
- **3B — Selenium: open Google**
  - Python source: `SET3/selenium/google.py`
  - Run from that folder: `py google.py`

### SET 4
- **4A — Nginx with user-defined HTML using Docker Compose**
  - HTML: `SET4/nginx-compose/index.html`
  - Compose file: `SET4/nginx-compose/compose.yaml`
  - Commands (run from `SET4/nginx-compose`): `docker compose up -d`; open http://localhost:8080; stop with `docker compose down`.
- **4B — Python Hello World through Jenkins**
  - Python source: `jenkins-workspaces/Python-Hello/hello.py`
  - Jenkins instructions: `jenkins-workspaces/Python-Hello/JENKINS-COMMAND.txt`

### SET 5
- **5A — Jenkins Pipeline with at least two stages**
  - Pipeline script: `jenkins-workspaces/Pipeline/Pipeline.groovy`
  - Alternate copy: `SET5/jenkins-pipeline/Pipeline.groovy`
  - Jenkins instructions: `jenkins-workspaces/Pipeline/JENKINS-COMMAND.txt`
- **5B — Selenium: open Wikipedia and take screenshot**
  - Python source: `SET5/selenium/wiki_screenshot.py`

### SET 6
- **6A — Java JDK 17, Python and Node.js programs using Docker Compose**
  - Compose file: `SET6/multi-compose/compose.yaml`
  - Java source and Dockerfile: `SET6/multi-compose/java/Hello.java`, `SET6/multi-compose/java/Dockerfile`
  - Python source and Dockerfile: `SET6/multi-compose/python/hello.py`, `SET6/multi-compose/python/Dockerfile`
  - Node source and Dockerfile: `SET6/multi-compose/node/hello.js`, `SET6/multi-compose/node/Dockerfile`
  - Command (run from `SET6/multi-compose`): `docker compose up --build`; stop with `docker compose down`.
- **6B — Parameterized Python through Jenkins**
  - Python source: `jenkins-workspaces/Parameterized-Python/hello.py`
  - Jenkins instructions: `jenkins-workspaces/Parameterized-Python/JENKINS-COMMAND.txt`
  - Jenkins String Parameter name: `NAME`; Windows batch argument: `%NAME%`.

### SET 7
- **7A — Java reverse-number program on GitHub, cloned and executed through Jenkins**
  - Main Java source: `SET7/github-java-reverse/ReverseNumber.java`
  - Jenkins-ready copy: `jenkins-workspaces/GitHub-ReverseNumber/ReverseNumber.java`
  - Jenkins instructions and build commands: `jenkins-workspaces/GitHub-ReverseNumber/JENKINS-COMMAND.txt`
  - Repository URL for Jenkins Git SCM: `https://github.com/kovid-reddy/Jenkins-Repo.git`
- **7B — Nginx with user-defined HTML using Docker Compose**
  - HTML: `SET7/nginx-compose/index.html`
  - Compose file: `SET7/nginx-compose/compose.yaml`
  - Run from `SET7/nginx-compose`: `docker compose up -d`; open http://localhost:8080; stop with `docker compose down`.

### SET 8
- **8A — Node.js file-creation program on GitHub, cloned and executed through Jenkins**
  - Main Node source: `SET8/github-node-create-file/createfile.js`
  - Jenkins-ready copy: `jenkins-workspaces/GitHub-Node-CreateFile/createfile.js`
  - Jenkins instructions and build command: `jenkins-workspaces/GitHub-Node-CreateFile/JENKINS-COMMAND.txt`
  - Repository URL for Jenkins Git SCM: `https://github.com/kovid-reddy/Jenkins-Repo.git`
- **8B — Selenium: open Google and search content**
  - Python source: `SET8/selenium/google_search.py`

### SET 9
- **9A — Jenkins Pipeline with at least two stages**
  - Pipeline script: `jenkins-workspaces/Pipeline/Pipeline.groovy`
  - Jenkins instructions: `jenkins-workspaces/Pipeline/JENKINS-COMMAND.txt`
  - Alternate copy: `SET9/jenkins-pipeline/Pipeline.groovy`
- **9B — Java program using Docker Compose**
  - Java source: `SET9/java-compose/Hello.java`
  - Dockerfile: `SET9/java-compose/Dockerfile`
  - Compose file: `SET9/java-compose/compose.yaml`
  - Commands (run from `SET9/java-compose`): `docker compose up --build`; stop with `docker compose down`.

### SET 10
- **10A — Hello World Docker**
  - Dockerfile: `SET10/hello-docker/Dockerfile`
  - Commands (run from `SET10/hello-docker`): `docker build -t hello-docker .` then `docker run --rm hello-docker`.
- **10B — Hello World Docker Compose**
  - Compose file: `SET10/hello-compose/compose.yaml`
  - Commands (run from `SET10/hello-compose`): `docker compose up`; stop with `docker compose down`.
- **10C — Selenium: open Google**
  - Python source: `SET10/selenium/google.py`

## Jenkins workspace files at a glance

These folders are prepared specifically for copying into the matching Jenkins job workspace:

| Jenkins practical | Copy this folder's source file(s) |
|---|---|
| Java Hello World | `jenkins-workspaces/Hello-Java/` |
| Parameterized Java | `jenkins-workspaces/Parameterized-Java/` |
| Python Hello World | `jenkins-workspaces/Python-Hello/` |
| Parameterized Python | `jenkins-workspaces/Parameterized-Python/` |
| GitHub Java reverse | `jenkins-workspaces/GitHub-ReverseNumber/` |
| GitHub Node file creation | `jenkins-workspaces/GitHub-Node-CreateFile/` |
| Jenkins Pipeline | `jenkins-workspaces/Pipeline/Pipeline.groovy` (paste into a Pipeline job's script box) |

For **Set 7A and Set 8A**, configure Jenkins **Source Code Management → Git** with this repository URL:
`https://github.com/kovid-reddy/Jenkins-Repo.git`. The Jenkins-ready build commands use paths relative to the cloned repository in the job workspace.

## Setup notes

### Selenium
Install once on the lab PC if needed:

```powershell
py -m pip install -r requirements.txt
```

Chrome must be installed. Selenium 4 uses Selenium Manager to manage the browser driver automatically in normal supported setups.

### Docker
- Dockerfile project: run `docker build -t IMAGE_NAME .` and then `docker run --rm IMAGE_NAME` from the folder containing the Dockerfile.
- Compose project: run `docker compose up --build` from the folder containing `compose.yaml`; use `docker compose down` to stop and remove the containers.
- Nginx examples use host port 8080 and container port 80.

### Jenkins on Windows
Jenkins jobs, configuration and workspaces are local to each Jenkins installation. This repository contains the code and scripts, not Jenkins credentials or job history.

For a Freestyle project, copy the relevant source file(s) from `jenkins-workspaces/<folder>/` into that job's workspace and follow its `JENKINS-COMMAND.txt`.

If Jenkins reports that Python is not recognized, run `where.exe python` in PowerShell and use the full path to `python.exe` in the Jenkins batch command. Jenkins may run as a Windows service with a different PATH.

For parameterized jobs, enable **This project is parameterized**, add a String Parameter named `NAME`, and use `%NAME%` in a Windows batch command. Java reads the argument as `args[0]`; Python reads it as `sys.argv[1]`.

For Pipeline practicals, create a **Pipeline** job and paste the contents of `jenkins-workspaces/Pipeline/Pipeline.groovy` into the Pipeline script box. Do not run the Groovy file as a Windows batch command.
