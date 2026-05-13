# Lab Practical 5 — MapReduce Titanic Analysis (Windows)

**Aim:** Develop a MapReduce program to analyze Titanic ship data and find:
- **(a)** Average age of dead male passengers
- **(b)** Number of dead female passengers per class

---

## One-Time Setup (Run ONLY once when setting up Hadoop for the first time)

```cmd
hdfs namenode -format
```

---

## Starting Hadoop Services (Every Time)

> Always open CMD as **Administrator** before running these commands!

### Step 1: Start HDFS
```cmd
start-dfs.cmd
```

### Step 2: Start YARN
```cmd
start-yarn.cmd
```

### Step 3: Exit Safe Mode
```cmd
hdfs dfsadmin -safemode leave
```

### Step 4: Check Running Services
```cmd
jps
```

Expected: `NameNode`, `DataNode`, `ResourceManager`, `NodeManager`

---

## Practical 5 — Steps

### Step 1: Create Working Directory
```cmd
mkdir C:\titanic
cd C:\titanic
```

---

### Step 2: Download Titanic Dataset
```cmd
curl -o Titanic.csv https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
```

---

### Step 3: Upload Dataset to HDFS
```cmd
hadoop fs -put C:\titanic\Titanic.csv /
hadoop fs -ls /
```

---

## Part A: Average Age of Dead Male Passengers

### Step 4: Create DeadMaleMapper.java
```cmd
notepad DeadMaleMapper.java
```

Paste this code:

```java
import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Mapper;

public class DeadMaleMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {
        String line = value.toString();
        if (line.startsWith("PassengerId")) return;
        String[] str = line.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)");
        if (str.length > 5 && str[1].equals("0") && str[4].equals("male")) {
            if (!str[5].isEmpty()) {
                try {
                    int age = (int) Float.parseFloat(str[5]);
                    context.write(new Text("Dead_Male"), new IntWritable(age));
                } catch (Exception e) {}
            }
        }
    }
}
```

---

### Step 5: Create DeadMaleReducer.java
```cmd
notepad DeadMaleReducer.java
```

Paste this code:

```java
import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Reducer;

public class DeadMaleReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {
        int sum = 0, count = 0;
        for (IntWritable val : values) {
            sum += val.get();
            count++;
        }
        context.write(key, new IntWritable(sum / count));
    }
}
```

---

### Step 6: Create DeadMaleDriver.java
```cmd
notepad DeadMaleDriver.java
```

Paste this code:

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class DeadMaleDriver {
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Dead Male Avg Age");
        job.setJarByClass(DeadMaleDriver.class);
        job.setMapperClass(DeadMaleMapper.class);
        job.setReducerClass(DeadMaleReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

---

## Part B: Dead Female Count per Passenger Class

### Step 7: Create FemaleClassMapper.java
```cmd
notepad FemaleClassMapper.java
```

Paste this code:

```java
import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Mapper;

public class FemaleClassMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {
        String line = value.toString();
        if (line.startsWith("PassengerId")) return;
        String[] str = line.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)");
        if (str.length > 4 && str[1].equals("0") && str[4].equals("female")) {
            context.write(new Text("Class_" + str[2]), new IntWritable(1));
        }
    }
}
```

---

### Step 8: Create FemaleClassReducer.java
```cmd
notepad FemaleClassReducer.java
```

Paste this code:

```java
import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Reducer;

public class FemaleClassReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {
        int sum = 0;
        for (IntWritable val : values)
            sum += val.get();
        context.write(key, new IntWritable(sum));
    }
}
```

---

### Step 9: Create FemaleClassDriver.java
```cmd
notepad FemaleClassDriver.java
```

Paste this code:

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class FemaleClassDriver {
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Dead Female Per Class");
        job.setJarByClass(FemaleClassDriver.class);
        job.setMapperClass(FemaleClassMapper.class);
        job.setReducerClass(FemaleClassReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

---

## Compile and Run

### Step 10: Compile All Java Files
```cmd
javac -classpath "%HADOOP_HOME%\share\hadoop\common\hadoop-common-3.3.6.jar;%HADOOP_HOME%\share\hadoop\mapreduce\hadoop-mapreduce-client-core-3.3.6.jar;%HADOOP_HOME%\share\hadoop\common\lib\commons-cli-1.2.jar" *.java
```

---

### Step 11: Create JAR Files
```cmd
jar cf deadmale.jar DeadMale*.class
jar cf femaleclass.jar FemaleClass*.class
```

---

### Step 12: Delete Old Outputs (if exist)
```cmd
hadoop fs -rm -r /output1
hadoop fs -rm -r /output2
```

---

### Step 13: Run Average Age Job (Part A)
```cmd
hadoop jar deadmale.jar DeadMaleDriver /Titanic.csv /output1
```

### Step 14: View Average Age Output
```cmd
hadoop fs -cat /output1/part-r-00000
```

Expected output:
```
Dead_Male    31
```

---

### Step 15: Run Dead Female Per Class Job (Part B)
```cmd
hadoop jar femaleclass.jar FemaleClassDriver /Titanic.csv /output2
```

### Step 16: View Non-Survivor Count Output
```cmd
hadoop fs -cat /output2/part-r-00000
```

Expected output:
```
Class_1    3
Class_2    6
Class_3    72
```

---

## Stopping Hadoop Services

> Always stop Hadoop properly before closing CMD windows!

### Step 1: Stop YARN
```cmd
stop-yarn.cmd
```

### Step 2: Stop HDFS
```cmd
stop-dfs.cmd
```
