# CL4 — Big Data Analytics & Business Intelligence

**Subject:** Computer Laboratory IV (BDA + BI)  
**Institute:** Dr. D.Y. Patil Institute of Engineering, Management and Research, Akurdi, Pune  
**Class:** B.E. (AI & DS) | Roll No: BEAD-64

> **Step-by-step Hadoop setup guide:** See [`1/Lab1_README.md`](1/Lab1_README.md) — complete Windows (7 phases) + Ubuntu (10 phases) setup with all XML configs, commands, and troubleshooting tables.

---

## What is Hadoop?

**Apache Hadoop** is an open-source framework for distributed storage and processing of large datasets (Big Data) across clusters of computers using simple programming models.

- Developed by **Doug Cutting** and **Mike Cafarella** in 2005 (inspired by Google's GFS + MapReduce papers)
- Written in **Java**
- Can scale from a single server to thousands of machines
- Designed to detect and handle failures at the application layer (not hardware layer)
- Follows **"move computation to data"** principle (instead of moving large data to computation)

---

## Hadoop Architecture — 4 Core Components

### 1. HDFS (Hadoop Distributed File System)
- Distributed file system for storing data across multiple nodes
- **NameNode:** Master — stores metadata (file names, block locations, permissions)
- **DataNode:** Slaves — store actual data blocks
- **Block size:** 128 MB by default (HDFS splits files into 128 MB blocks)
- **Replication factor:** 3 by default (each block stored on 3 different DataNodes)
- Secondary NameNode: periodically merges NameNode logs (NOT a backup NameNode)

### 2. MapReduce
- Programming model for processing large datasets in parallel
- **Map phase:** Input data → split into key-value pairs (done by Mapper)
- **Shuffle & Sort phase:** Groups all values with the same key together
- **Reduce phase:** Aggregates/summarizes the grouped key-value pairs (done by Reducer)
- **Driver class:** Configures and submits the MapReduce job

### 3. YARN (Yet Another Resource Negotiator)
- Resource management layer (added in Hadoop 2.x)
- **ResourceManager:** Master — manages cluster resources, schedules jobs
- **NodeManager:** Slave on each node — manages resources on that node
- **ApplicationMaster:** Manages lifecycle of individual applications
- Separates resource management from data processing (unlike Hadoop 1.x where JobTracker did both)

### 4. Hadoop Common
- Set of shared utilities and libraries used by all Hadoop modules
- Includes Hadoop RPC, serialization, file system abstractions

---

## Hadoop Ecosystem

| Tool | Purpose |
|------|---------|
| **HDFS** | Distributed storage |
| **MapReduce** | Batch data processing |
| **YARN** | Resource management |
| **Hive** | SQL-like queries on HDFS data |
| **Pig** | High-level data flow scripting |
| **HBase** | NoSQL columnar database on HDFS |
| **Spark** | In-memory fast data processing (alternative to MapReduce) |
| **Sqoop** | Import/export data between HDFS and relational databases |
| **Flume** | Streaming log data into HDFS |
| **Oozie** | Workflow scheduler for Hadoop jobs |
| **ZooKeeper** | Coordination service for distributed applications |
| **Kafka** | Distributed event streaming platform |

---

## Cluster Modes

| Mode | Description | Use Case |
|------|-------------|---------|
| **Standalone** | Single JVM process, no HDFS | Testing and debugging |
| **Pseudo-distributed** | All daemons on one machine | Development / lab setup |
| **Fully distributed** | Multiple machines in a cluster | Production |

---

## Advantages of Hadoop

1. **Scalability** — Easily scale from a few nodes to thousands of nodes (horizontal scaling)
2. **Fault Tolerance** — Data replication (default 3x) ensures no data loss when nodes fail
3. **Cost Effective** — Runs on commodity hardware (no expensive servers needed)
4. **Flexibility** — Handles structured, semi-structured, and unstructured data
5. **High Throughput** — Processes massive datasets (terabytes/petabytes) efficiently
6. **Open Source** — Free to use, large community, actively maintained by Apache
7. **Data Locality** — Moves computation to data (reduces network overhead)
8. **Parallel Processing** — Multiple nodes process different chunks simultaneously

---

## Disadvantages of Hadoop

1. **High Latency** — Not suitable for real-time processing (batch processing only)
2. **Small File Problem** — Many small files overload NameNode memory
3. **No Random Access** — HDFS is designed for sequential reads, not random access
4. **Complexity** — Setting up and maintaining a Hadoop cluster is complex
5. **Security** — Kerberos security is complex to configure; not secure by default
6. **Not for OLTP** — Not designed for transactional (row-level insert/update/delete) workloads
7. **Verbose Code** — MapReduce programs require a lot of boilerplate Java code
8. **Memory Issues** — MapReduce writes intermediate results to disk (slower than in-memory Spark)

---

## Key Concepts

| Concept | Value / Description |
|---------|-------------------|
| Default block size | 128 MB |
| Default replication | 3 copies |
| NameNode port | 9000 (RPC), 9870 (Web UI) |
| YARN ResourceManager port | 8088 (Web UI) |
| NameNode | Stores metadata — filenames, block IDs, DataNode locations |
| DataNode | Stores actual data blocks, sends heartbeats to NameNode |
| Secondary NameNode | Merges edit logs with fsimage (NOT a failover/backup NameNode) |
| Heartbeat | DataNodes send heartbeat every 3 seconds; missing 10 = declared dead |
| Rack awareness | HDFS places replicas on different racks for fault tolerance |
| Speculative execution | Hadoop re-runs slow tasks on another node as backup |

---

## HDFS Commands Reference

```bash
# Filesystem operations
hdfs dfs -ls /                          # List root directory
hdfs dfs -ls /user/                     # List specific directory
hdfs dfs -mkdir /dirname               # Create directory
hdfs dfs -mkdir -p /a/b/c              # Create nested directories

# File operations
hdfs dfs -put localfile.txt /hdfs/path/   # Upload to HDFS
hdfs dfs -get /hdfs/path/file.txt ./      # Download from HDFS
hdfs dfs -cat /hdfs/path/file.txt         # Print file contents
hdfs dfs -cp /src/file.txt /dst/          # Copy within HDFS
hdfs dfs -mv /src/file.txt /dst/          # Move within HDFS

# Delete operations
hdfs dfs -rm /file.txt                    # Delete file
hdfs dfs -rm -r /directory/              # Delete directory recursively
hdfs dfs -rmdir /empty-directory/        # Delete empty directory

# Information
hdfs dfs -du -h /                         # Disk usage (human-readable)
hdfs dfs -df -h                           # Free space on HDFS
hdfs dfs -count /path                     # Count directories/files/bytes
hdfs dfs -stat /file.txt                  # File status

# Admin
hdfs dfsadmin -report                     # Cluster health report
hdfs namenode -format                     # Format NameNode (ONCE only!)
```

---

## MapReduce Job Flow

```
Input Data (HDFS)
      ↓
   InputFormat → splits file into InputSplits
      ↓
   RecordReader → converts splits to key-value pairs
      ↓
   Mapper → processes each key-value pair → emits intermediate key-value pairs
      ↓
   Combiner (optional) → mini-reducer on mapper output (local aggregation)
      ↓
   Partitioner → determines which Reducer handles each key
      ↓
   Shuffle & Sort → groups all values by key, sorted
      ↓
   Reducer → processes each key with its list of values → emits final output
      ↓
   OutputFormat → writes output to HDFS
      ↓
Output Data (HDFS)
```

---

## Hadoop Setup (Quick Reference)

> Full step-by-step guide with all XML configurations is in: **[`CL4/1/Lab1_README.md`](1/Lab1_README.md)**

### Windows Setup Summary (7 Phases)

| Phase | Task |
|-------|------|
| 1 | Install Java 8 (Adoptium Temurin), set JAVA_HOME |
| 2 | Download Hadoop 3.3.6, extract with 7-Zip, copy winutils.exe + hadoop.dll, set HADOOP_HOME |
| 3 | Edit 5 config files: core-site.xml, hdfs-site.xml, mapred-site.xml, yarn-site.xml, hadoop-env.cmd (use PROGRA~1) |
| 4 | Format NameNode: `hdfs namenode -format` (run ONCE) |
| 5 | Start: `start-dfs.cmd` + `start-yarn.cmd` → verify with `jps` + browser |
| 6 | Run WordCount: upload to HDFS → run JAR → read output |
| 7 | Stop: `stop-yarn.cmd` + `stop-dfs.cmd` |

### Ubuntu Setup Summary (10 Phases)

| Phase | Task |
|-------|------|
| 1 | `sudo apt install openjdk-8-jdk -y` |
| 2 | Add JAVA_HOME + HADOOP_HOME + PATH exports to `~/.bashrc`, then `source ~/.bashrc` |
| 3 | `wget` Hadoop 3.3.6 tarball → `tar -xvzf` → `mv` to `~/hadoop-3.3.6` |
| 4 | Edit 5 config files with `nano`: core-site.xml, hdfs-site.xml, mapred-site.xml, yarn-site.xml, hadoop-env.sh |
| 5 | SSH setup: `ssh-keygen` → `cat id_rsa.pub >> authorized_keys` → `chmod 600` → test `ssh localhost` |
| 6 | `mkdir -p ~/hadoopdata/namenode` and `~/hadoopdata/datanode` |
| 7 | Format NameNode: `hdfs namenode -format` (run ONCE) |
| 8 | Start: `start-dfs.sh` + `start-yarn.sh` → verify with `jps` + browser |
| 9 | Run WordCount: upload to HDFS → run JAR → read output |
| 10 | Stop: `stop-yarn.sh` + `stop-dfs.sh` |

---

## Cloud Alternatives (PS 1 scope)

| Platform | Description |
|----------|-------------|
| **Cloudera** | Enterprise Hadoop distribution with management tools (Cloudera Manager) |
| **Google Cloud BigQuery** | Serverless data warehouse — SQL queries on petabyte-scale data |
| **Databricks Lakehouse** | Unified analytics platform — Apache Spark + Delta Lake (cloud-based) |
| **Snowflake** | Cloud data warehouse — separate storage and compute, auto-scaling |
| **Amazon Redshift** | AWS cloud data warehouse — columnar storage, MPP architecture |

---

## Practicals Summary

| PS | Topic | Type | Folder |
|----|-------|------|--------|
| 1 | Hadoop Setup | BDA | `1/` |
| 2 | WordCount MapReduce | BDA | `2/` |
| 3 | Matrix Multiplication MapReduce | BDA | `3/` |
| 4 | Student Grades MapReduce | BDA | `4/` |
| 5 | Titanic Analysis MapReduce | BDA | `5/` |
| 6 | Import Data — Power BI | BI | `6/` |
| 7 | ETL + Visualization — Python | BI | `7/` |
| 8 | ETL Process — Power BI | BI | `8/` |
| 9 | Advanced Excel Charts | BI | `9/` |
| 10 | Data Classification (Logistic Regression) | BI | `10/` |

See [`INDEX.md`](INDEX.md) for detailed file contents of each practical folder.
