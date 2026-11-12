# DevOps Lab Internal-2 — complete practical runbook

## 1. Clone the repository on the lab PC

Run these commands in **PowerShell**:

```powershell
git clone https://github.com/kovid-reddy/Jenkins-Repo.git
cd Jenkins-Repo
```

All paths and commands below assume your terminal is in the cloned `Jenkins-Repo` root folder unless the command block first changes directory.

## 2. One-time setup

### Selenium

Install Selenium once:

```powershell
py -m pip install -r requirements.txt
```

Chrome must be installed. Selenium 4 normally uses Selenium Manager to manage the compatible ChromeDriver automatically.

### Check required tools

```powershell
java -version
javac -version
py --version
node --version
docker --version
docker compose version
```

For Jenkins, open the Jenkins URL provided by your lab, commonly `http://localhost:8080`.

---

# 3. Set-wise questions, file locations and exact commands

## SET 1

### 1A) Execute and Test Simple Hello World Java program through Jenkins.

**File:** `jenkins-workspaces/Hello-Java/HelloWorld.java`

**On Jenkins:**
1. Create a **Freestyle project** named `Hello-Java`.
2. Copy `HelloWorld.java` into that job's workspace.
3. Add **Build Steps → Execute Windows batch command**.

**Build command:**

```bat
javac HelloWorld.java
java HelloWorld
```

Expected output: `Hello World from Jenkins!`

**Command-line test outside Jenkins (optional):**

```powershell
cd jenkins-workspaces\Hello-Java
javac HelloWorld.java
java HelloWorld
cd ..\..
```

### 1B) Write a Selenium code using Python to open a Chrome browser, visit Wikipedia and take a screenshot.

**File:** `SET1/selenium/wiki_screenshot.py`

**Run from repository root:**

```powershell
py .\SET1\selenium\wiki_screenshot.py
```

Expected: Chrome opens Wikipedia, saves `wikipedia.png` in the current directory (the repository root), and closes.

---

## SET 2

### 2A) Write a Selenium code using Python to open a Chrome browser, visit Google website and search for content.

**File:** `SET2/selenium/google_search.py`

**Run:**

```powershell
py .\SET2\selenium\google_search.py
```

Expected: Chrome opens Google, searches for Docker, and stays open until you press Enter in the terminal.

### 2B) Execute and Test a Parameterized Java Program through Jenkins.

**File:** `jenkins-workspaces/Parameterized-Java/ParameterizedHello.java`

**On Jenkins:**
1. Create a **Freestyle project** named `Parameterized-Java`.
2. Copy `ParameterizedHello.java` into that job's workspace.
3. Enable **This project is parameterized → Add Parameter → String Parameter**.
4. Set **Name:** `NAME`; **Default Value:** `World`.
5. Add **Build Steps → Execute Windows batch command**.

**Build command:**

```bat
javac ParameterizedHello.java
java ParameterizedHello %NAME%
```

Click **Build with Parameters**, enter `Kovid` for NAME, and build. Expected output: `Hello Kovid!`

---

## SET 3

### 3A) Create and run Python program using Docker.

**Files:**
- `SET3/python-docker/hello.py`
- `SET3/python-docker/Dockerfile`

**Commands:**

```powershell
cd SET3\python-docker
docker build -t python-hello .
docker run --rm python-hello
cd ..\..
```

Expected output: `Hello World from Python Docker!`

### 3B) Write a Selenium code using Python to open a Chrome browser and visit Google website.

**File:** `SET3/selenium/google.py`

**Run from repository root:**

```powershell
py .\SET3\selenium\google.py
```

Expected: Chrome opens Google. Press Enter in the terminal to close it.

---

## SET 4

### 4A) Create and run Nginx server using user-defined HTML file using Docker Compose.

**Files:**
- `SET4/nginx-compose/index.html`
- `SET4/nginx-compose/compose.yaml`

**Commands:**

```powershell
cd SET4\nginx-compose
docker compose up -d
```

Open **http://localhost:8080** in Chrome to see the custom HTML page.

Stop and remove the container:

```powershell
docker compose down
cd ..\..
```

### 4B) Execute and Test Simple Hello World Python program through Jenkins.

**File:** `jenkins-workspaces/Python-Hello/hello.py`

**On Jenkins:**
1. Create a **Freestyle project** named `Python-Hello`.
2. Copy `hello.py` into the job's workspace.
3. Add **Build Steps → Execute Windows batch command**.

**Build command:**

```bat
python hello.py
```

If Jenkins reports that Python is not recognized, run `where.exe python` in PowerShell and use the full path to that PC's `python.exe`, for example:

```bat
"C:\\Users\\YOUR_USER\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" hello.py
```

Expected output: `Hello World from Jenkins!`

---

## SET 5

### 5A) Create a Jenkins Pipeline script with at least two stages.

**File to paste into Jenkins:** `jenkins-workspaces/Pipeline/Pipeline.groovy`

**On Jenkins:**
1. Click **New Item**, enter `Two-Stage-Pipeline`, and select **Pipeline**.
2. In the Pipeline section, select **Pipeline script**.
3. Paste the contents of `jenkins-workspaces/Pipeline/Pipeline.groovy`.
4. Click **Save → Build Now**.

The two stages are **Build** and **Test**. Do not run this Groovy file as a Windows batch command.

### 5B) Write a Selenium code using Python to open a Chrome browser, visit Wikipedia and take a screenshot.

**File:** `SET5/selenium/wiki_screenshot.py`

**Run:**

```powershell
py .\SET5\selenium\wiki_screenshot.py
```

Expected: `wikipedia.png` is saved in the current directory.

---

## SET 6

### 6A) Execute three programs: Java program-JDK-17, Python program and Node.js programs using Docker Compose.

**Files:** `SET6/multi-compose/`
- Java: `java/Hello.java`, `java/Dockerfile` (uses JDK 17)
- Python: `python/hello.py`, `python/Dockerfile`
- Node.js: `node/hello.js`, `node/Dockerfile`
- Compose: `compose.yaml`

**Commands:**

```powershell
cd SET6\multi-compose
docker compose up --build
```

Expected output includes:
- `Hello from Java 17!`
- `Hello from Python!`
- `Hello from Node.js!`

Stop and remove containers:

```powershell
docker compose down
cd ..\..
```

### 6B) Execute and Test a Parameterized Python Program through Jenkins.

**File:** `jenkins-workspaces/Parameterized-Python/hello.py`

**On Jenkins:**
1. Create a **Freestyle project** named `Parameterized-Python`.
2. Copy `hello.py` into its workspace.
3. Enable **This project is parameterized → String Parameter**.
4. Set **Name:** `NAME`; **Default Value:** `World`.
5. Add **Build Steps → Execute Windows batch command**.

**Build command:**

```bat
python hello.py %NAME%
```

If the Jenkins service cannot find Python, use the full path to `python.exe` before `hello.py`, e.g. `"C:\\Path\\To\\python.exe" hello.py %NAME%`.

Click **Build with Parameters**, enter `Kovid`, and build. Expected output: `Hello Kovid`.

---

## SET 7

### 7A) Create a Java file in GitHub that reverses a number, clone it and execute it through Jenkins.

**Java file in this GitHub repository:** `SET7/github-java-reverse/ReverseNumber.java`

**On Jenkins:**
1. Create a **Freestyle project** named `GitHub-ReverseNumber`.
2. Under **Source Code Management → Git**, enter:
   `https://github.com/kovid-reddy/Jenkins-Repo.git`
3. Add **Build Steps → Execute Windows batch command**.

**Build command (run after Jenkins checks out the repository):**

```bat
javac SET7\github-java-reverse\ReverseNumber.java
java -cp SET7\github-java-reverse ReverseNumber
```

Expected output: `Reversed number: 54321`.

A ready-to-copy standalone version is also at `jenkins-workspaces/GitHub-ReverseNumber/ReverseNumber.java`.

### 7B) Create and run Nginx server using user-defined HTML file using Docker Compose.

**Files:**
- `SET7/nginx-compose/index.html`
- `SET7/nginx-compose/compose.yaml`

**Commands:**

```powershell
cd SET7\nginx-compose
docker compose up -d
```

Open **http://localhost:8080**. Stop the service:

```powershell
docker compose down
cd ..\..
```

---

## SET 8

### 8A) Create a Node.js file in GitHub that creates a new file, clone it and execute it through Jenkins.

**Node.js file in this GitHub repository:** `SET8/github-node-create-file/createfile.js`

**On Jenkins:**
1. Create a **Freestyle project** named `GitHub-Node-CreateFile`.
2. Under **Source Code Management → Git**, enter:
   `https://github.com/kovid-reddy/Jenkins-Repo.git`
3. Add **Build Steps → Execute Windows batch command**.

**Build command (run after Jenkins checks out the repository):**

```bat
node SET8\github-node-create-file\createfile.js
```

Expected output: `File created successfully.` The program creates `newfile.txt` in the Jenkins job workspace.

A ready-to-copy standalone version is also at `jenkins-workspaces/GitHub-Node-CreateFile/createfile.js`.

### 8B) Write a Selenium code using Python to open a Chrome browser, visit Google website and search for content.

**File:** `SET8/selenium/google_search.py`

**Run:**

```powershell
py .\SET8\selenium\google_search.py
```

Expected: Chrome opens Google and searches for Jenkins.

---

## SET 9

### 9A) Create a Jenkins Pipeline script with at least two stages.

**File to paste into Jenkins:** `jenkins-workspaces/Pipeline/Pipeline.groovy`

**On Jenkins:** create a **Pipeline** job, paste the Groovy file contents into **Pipeline script**, click **Save → Build Now**. The script contains **Build** and **Test** stages.

### 9B) Create and run Java program using Docker Compose.

**Files:**
- `SET9/java-compose/Hello.java`
- `SET9/java-compose/Dockerfile`
- `SET9/java-compose/compose.yaml`

**Commands:**

```powershell
cd SET9\java-compose
docker compose up --build
```

Expected output: `Hello World from Java Docker Compose!`

Stop and remove the container:

```powershell
docker compose down
cd ..\..
```

---

## SET 10

### 10A) Create and run Hello World Docker.

**File:** `SET10/hello-docker/Dockerfile`

**Commands:**

```powershell
cd SET10\hello-docker
docker build -t hello-docker .
docker run --rm hello-docker
cd ..\..
```

Expected output: `Hello World from Docker!`

### 10B) Create and run Hello World Docker Compose.

**File:** `SET10/hello-compose/compose.yaml`

**Commands:**

```powershell
cd SET10\hello-compose
docker compose up
```

Expected output: `Hello World from Docker Compose!` Stop with Ctrl+C, then run:

```powershell
docker compose down
cd ..\..
```

### 10C) Write a Selenium code using Python to open a Chrome browser and visit Google website.

**File:** `SET10/selenium/google.py`

**Run:**

```powershell
py .\SET10\selenium\google.py
```

Expected: Chrome opens Google. Press Enter in the terminal to close it.

---

# 4. Jenkins workspace file quick reference

These folders contain the files to copy into the matching Jenkins job workspace:

| Practical | Copy from this folder |
|---|---|
| Set 1A — Java Hello World | `jenkins-workspaces/Hello-Java/` |
| Set 2B — Parameterized Java | `jenkins-workspaces/Parameterized-Java/` |
| Set 4B — Python Hello World | `jenkins-workspaces/Python-Hello/` |
| Set 6B — Parameterized Python | `jenkins-workspaces/Parameterized-Python/` |
| Set 7A — Java reverse number | `jenkins-workspaces/GitHub-ReverseNumber/` |
| Set 8A — Node file creation | `jenkins-workspaces/GitHub-Node-CreateFile/` |
| Set 5A / 9A — Pipeline | `jenkins-workspaces/Pipeline/Pipeline.groovy` (paste into a Pipeline job) |

Each Jenkins workspace folder includes a `JENKINS-COMMAND.txt` with the matching build command and configuration notes.

## 5. Important Windows/Jenkins notes

- In Windows batch build steps, use `%NAME%` to read a Jenkins String Parameter named `NAME`.
- Java receives command-line parameters in `args[0]`; Python receives them in `sys.argv[1]`.
- Jenkins installed as a Windows service may run under a different account/PATH. If `python` works in your PowerShell but not Jenkins, run `where.exe python` in PowerShell and use that machine's full `python.exe` path in the Jenkins batch command.
- Jenkins jobs, build history, credentials and workspace state belong to that Jenkins installation; GitHub carries the source files and scripts.
- Docker commands must be run from the directory containing the relevant Dockerfile or Compose file, as shown above.
