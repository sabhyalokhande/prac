# Lab Practical 1 — Hadoop Setup & Configuration

**Aim:** Set up and Configuration Hadoop Using CloudEra / Google Cloud BigQuery / Databricks Lakehouse Platform / Snowflake / Amazon Redshift.

---

## Quick Reference — Download Links

| Tool | Version | URL |
|------|---------|-----|
| Java 8 (Adoptium Temurin) | JDK 8 | https://adoptium.net → Temurin 8 (LTS) |
| Apache Hadoop | 3.3.6 | https://hadoop.apache.org/releases.html |
| 7-Zip (Windows only) | Latest | https://www.7-zip.org |
| winutils (Windows only) | Hadoop 3.3.0 | https://github.com/cdarlint/winutils |
| Eclipse IDE (optional) | Latest | https://www.eclipse.org/downloads/ |

---

## PART A: Hadoop Setup on Windows

---

### Phase 1: Install Java 8

1. Go to **https://adoptium.net**
2. Download **Temurin 8 (LTS)** → Windows x64 `.msi` installer
3. Run the installer → click **Next** repeatedly → click **Finish**
4. During installation, make sure **"Add to PATH"** and **"Set JAVA_HOME"** options are enabled (check all feature checkboxes)

**Verify Java installation:**
```cmd
java -version
```
Expected output:
```
openjdk version "1.8.0_xxx"
```

**Set JAVA_HOME manually (if not set automatically):**
1. Search **"Environment Variables"** in Windows search
2. Click **"Edit the system environment variables"** → **"Environment Variables"**
3. Under **System variables**, click **New**:
   - Variable name: `JAVA_HOME`
   - Variable value: `C:\Program Files\Eclipse Adoptium\jdk-8.x.x.x-hotspot` (your actual path)
4. Find **PATH** in system variables → click **Edit** → click **New** → add `%JAVA_HOME%\bin`
5. Click OK on all dialogs

---

### Phase 2: Download and Extract Hadoop

**Step 1: Download Hadoop**
1. Go to **https://hadoop.apache.org/releases.html**
2. Click **3.3.6** → download `hadoop-3.3.6.tar.gz`

**Step 2: Extract with 7-Zip**
1. Install **7-Zip** from https://www.7-zip.org
2. Right-click `hadoop-3.3.6.tar.gz` → **7-Zip** → **Extract Here** (extracts `.tar` file)
3. Right-click the resulting `.tar` file → **7-Zip** → **Extract Here** (extracts folder)
4. Move the `hadoop-3.3.6` folder to `C:\` so the path is:
   ```
   C:\hadoop-3.3.6\
   ```

**Step 3: Set up winutils**
1. Go to **https://github.com/cdarlint/winutils**
2. Navigate to `hadoop-3.3.0/bin/`
3. Download `winutils.exe` and `hadoop.dll`
4. Copy both files to: `C:\hadoop-3.3.6\bin\`

**Step 4: Set Hadoop Environment Variables**
1. Open **Environment Variables** (search in Windows)
2. Under **System variables**, click **New**:
   - Variable name: `HADOOP_HOME`
   - Variable value: `C:\hadoop-3.3.6`
3. Find **PATH** → **Edit** → **New** → add:
   - `%HADOOP_HOME%\bin`
   - `%HADOOP_HOME%\sbin`
4. Click OK on all dialogs

**Verify Hadoop:**
```cmd
hadoop version
```
Expected output:
```
Hadoop 3.3.6
```

---

### Phase 3: Configure XML Files

Navigate to: `C:\hadoop-3.3.6\etc\hadoop\`

#### File 1: core-site.xml

Open `core-site.xml` and replace the entire `<configuration>` block:

```xml
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>
```

---

#### File 2: hdfs-site.xml

Open `hdfs-site.xml` and replace the entire `<configuration>` block:

```xml
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>/C:/hadoop-3.3.6/data/namenode</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>/C:/hadoop-3.3.6/data/datanode</value>
  </property>
</configuration>
```

**Create the directories:**
```cmd
mkdir C:\hadoop-3.3.6\data\namenode
mkdir C:\hadoop-3.3.6\data\datanode
```

---

#### File 3: mapred-site.xml

Open `mapred-site.xml` and replace the entire `<configuration>` block:

```xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
  <property>
    <name>mapreduce.application.classpath</name>
    <value>%HADOOP_HOME%/share/hadoop/mapreduce/*,%HADOOP_HOME%/share/hadoop/mapreduce/lib/*</value>
  </property>
</configuration>
```

---

#### File 4: yarn-site.xml

Open `yarn-site.xml` and replace the entire `<configuration>` block:

```xml
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
  <property>
    <name>yarn.nodemanager.env-whitelist</name>
    <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
  </property>
</configuration>
```

---

#### File 5: hadoop-env.cmd

Open `hadoop-env.cmd` and find the line with `JAVA_HOME`. Replace it with:

```cmd
set JAVA_HOME=C:\PROGRA~1\Eclipse Adoptium\jdk-8.x.x.x-hotspot
```

> **Important:** Use `PROGRA~1` instead of `Program Files` — spaces in path names cause errors on Windows.

To find your exact JDK folder name:
```cmd
dir "C:\Program Files\Eclipse Adoptium\"
```

---

### Phase 4: Format NameNode (Run ONCE)

Open **Command Prompt as Administrator** and run:

```cmd
hdfs namenode -format
```

> **Warning:** Run this command only once. Running it again will delete all existing HDFS data.

Look for this in the output:
```
Storage directory C:\hadoop-3.3.6\data\namenode has been successfully formatted.
```

---

### Phase 5: Start Hadoop Services

Open **Command Prompt as Administrator** in `C:\hadoop-3.3.6\sbin\`:

```cmd
start-dfs.cmd
start-yarn.cmd
```

Or run from any directory:
```cmd
%HADOOP_HOME%\sbin\start-dfs.cmd
%HADOOP_HOME%\sbin\start-yarn.cmd
```

**Verify services are running:**
```cmd
jps
```
Expected output (4 processes):
```
xxxx NameNode
xxxx DataNode
xxxx ResourceManager
xxxx NodeManager
```

**Verify in browser:**
- HDFS NameNode UI: http://localhost:9870
- YARN ResourceManager UI: http://localhost:8088

---

### Phase 6: Run WordCount Example

**Step 1: Create input directory in HDFS**
```cmd
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/input
```

**Step 2: Create a test input file**
```cmd
echo Hello Hadoop World Hello > C:\input.txt
hdfs dfs -put C:\input.txt /user/input/
```

**Step 3: Run the WordCount JAR**
```cmd
hadoop jar %HADOOP_HOME%\share\hadoop\mapreduce\hadoop-mapreduce-examples-3.3.6.jar wordcount /user/input /user/output
```

**Step 4: View output**
```cmd
hdfs dfs -cat /user/output/part-r-00000
```

Expected output:
```
Hadoop  1
Hello   2
World   1
```

---

### Phase 7: Stop Hadoop Services

```cmd
%HADOOP_HOME%\sbin\stop-yarn.cmd
%HADOOP_HOME%\sbin\stop-dfs.cmd
```

---

### Windows Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `JAVA_HOME is incorrectly set` | Spaces in path | Use `PROGRA~1` instead of `Program Files` in hadoop-env.cmd |
| `jps not found` | JDK not in PATH | Add `%JAVA_HOME%\bin` to system PATH |
| `winutils.exe not found` | Missing winutils | Copy winutils.exe + hadoop.dll to `%HADOOP_HOME%\bin\` |
| `Connection refused` on port 9000 | NameNode not started | Run `start-dfs.cmd` as Administrator |
| NameNode not in jps output | Format needed | Run `hdfs namenode -format` (first time only) |
| Port 9870 shows nothing | Services not started | Check jps output — all 4 processes must be running |
| Permission denied in HDFS | Wrong directory owner | Run CMD as Administrator |

---

## PART B: Hadoop Setup on Ubuntu

---

### Phase 1: Install Java 8

```bash
sudo apt update
sudo apt install openjdk-8-jdk -y
java -version
```

Expected output:
```
openjdk version "1.8.0_xxx"
```

---

### Phase 2: Set Environment Variables

Edit the `.bashrc` file:
```bash
nano ~/.bashrc
```

Add these lines at the **bottom** of the file:
```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_HOME=~/hadoop-3.3.6
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
```

Save the file: `Ctrl+O` → Enter → `Ctrl+X`

Apply changes:
```bash
source ~/.bashrc
```

---

### Phase 3: Download and Extract Hadoop

```bash
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xvzf hadoop-3.3.6.tar.gz
mv hadoop-3.3.6 ~/hadoop-3.3.6
```

---

### Phase 4: Configure XML Files

Navigate to Hadoop config directory:
```bash
cd ~/hadoop-3.3.6/etc/hadoop/
```

#### File 1: core-site.xml

```bash
nano core-site.xml
```

Replace `<configuration>` block:
```xml
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>
```

---

#### File 2: hdfs-site.xml

```bash
nano hdfs-site.xml
```

Replace `<configuration>` block:
```xml
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///home/YOUR_USERNAME/hadoopdata/namenode</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>file:///home/YOUR_USERNAME/hadoopdata/datanode</value>
  </property>
</configuration>
```

> Replace `YOUR_USERNAME` with your actual Linux username (run `whoami` to check).

---

#### File 3: mapred-site.xml

```bash
nano mapred-site.xml
```

Replace `<configuration>` block:
```xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
  <property>
    <name>mapreduce.application.classpath</name>
    <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
  </property>
</configuration>
```

---

#### File 4: yarn-site.xml

```bash
nano yarn-site.xml
```

Replace `<configuration>` block:
```xml
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
  <property>
    <name>yarn.nodemanager.env-whitelist</name>
    <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
  </property>
</configuration>
```

---

#### File 5: hadoop-env.sh

```bash
nano hadoop-env.sh
```

Find the line with `# export JAVA_HOME=` and replace with:
```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

---

### Phase 5: Configure SSH

Hadoop requires passwordless SSH to start services:

```bash
ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

**Test SSH (should connect without password):**
```bash
ssh localhost
```

If it asks to confirm fingerprint, type `yes` → then type `exit` to return.

---

### Phase 6: Create Hadoop Data Directories

```bash
mkdir -p ~/hadoopdata/namenode
mkdir -p ~/hadoopdata/datanode
```

---

### Phase 7: Format NameNode (Run ONCE)

```bash
hdfs namenode -format
```

> **Warning:** Run this only once. Running again will delete all HDFS data.

Look for:
```
Storage directory /home/username/hadoopdata/namenode has been successfully formatted.
```

---

### Phase 8: Start Hadoop Services

```bash
start-dfs.sh
start-yarn.sh
jps
```

Expected `jps` output:
```
xxxx NameNode
xxxx DataNode
xxxx ResourceManager
xxxx NodeManager
xxxx Jps
```

**Verify in browser:**
- HDFS NameNode UI: http://localhost:9870
- YARN ResourceManager UI: http://localhost:8088

---

### Phase 9: Run WordCount Example

**Step 1: Create input directory in HDFS**
```bash
hdfs dfs -mkdir -p /user/input
```

**Step 2: Create a test file and upload**
```bash
echo "Hello Hadoop World Hello" > ~/input.txt
hdfs dfs -put ~/input.txt /user/input/
```

**Step 3: Run the WordCount JAR**
```bash
hadoop jar ~/hadoop-3.3.6/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar wordcount /user/input /user/output
```

**Step 4: View output**
```bash
hdfs dfs -cat /user/output/part-r-00000
```

Expected output:
```
Hadoop  1
Hello   2
World   1
```

---

### Phase 10: Stop Hadoop Services

```bash
stop-yarn.sh
stop-dfs.sh
```

---

### Ubuntu Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `JAVA_HOME not set` | bashrc not sourced | Run `source ~/.bashrc` |
| `ssh: connect to host localhost` | SSH not configured | Run ssh-keygen steps in Phase 5 |
| `DataNode not in jps output` | Format issue or port conflict | Stop all, delete hadoopdata contents, re-format |
| `Connection refused` on port 9000 | NameNode not started | Run `start-dfs.sh` and check jps |
| `Permission denied` on HDFS | Wrong directory permissions | Run `chmod 755 ~/hadoopdata` |
| Port 9870 not accessible | NameNode not running | Verify 4 processes in jps output |
| `Could not find or load main class` | Classpath issue | Verify HADOOP_HOME in bashrc is correct |

---

## Common HDFS Commands

```bash
# List files
hdfs dfs -ls /

# Create directory
hdfs dfs -mkdir /dirname

# Upload file to HDFS
hdfs dfs -put localfile.txt /hdfs/path/

# Download file from HDFS
hdfs dfs -get /hdfs/path/file.txt ./local/

# Read file contents
hdfs dfs -cat /hdfs/path/file.txt

# Delete file
hdfs dfs -rm /hdfs/path/file.txt

# Delete directory (recursive)
hdfs dfs -rm -r /hdfs/path/directory/

# Check HDFS disk usage
hdfs dfs -du -h /
```

---

## Result

Hadoop 3.3.6 successfully set up and configured:
- **Java 8** installed and JAVA_HOME configured
- **Hadoop 3.3.6** extracted and HADOOP_HOME configured
- **XML config files** set: core-site.xml, hdfs-site.xml, mapred-site.xml, yarn-site.xml, hadoop-env
- **NameNode formatted** (once)
- **Services started:** NameNode, DataNode, ResourceManager, NodeManager
- **WordCount example** executed successfully on HDFS
- **Web UIs accessible:** HDFS at :9870, YARN at :8088
