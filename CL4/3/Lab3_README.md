# Lab Practical 3 — MapReduce Matrix Multiplication (Windows)

**Aim:** Develop a MapReduce program to implement Matrix Multiplication.

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

## Practical 3 — Steps

### Step 1: Create Working Directory
```cmd
mkdir C:\matrixmultiply
cd C:\matrixmultiply
```

---

### Step 2: Create Combined Input File (input.txt)
```cmd
notepad input.txt
```

Enter the following content (format: `matrix_name,row,column,value`):
```
M,0,0,1
M,0,1,2
M,0,2,3
M,1,0,4
M,1,1,5
M,1,2,6
N,0,0,7
N,0,1,8
N,1,0,9
N,1,1,10
N,2,0,11
N,2,1,12
```

This represents:
- Matrix M (2×3): `[[1,2,3],[4,5,6]]`
- Matrix N (3×2): `[[7,8],[9,10],[11,12]]`

---

### Step 3: Create Multiply.java
```cmd
notepad Multiply.java
```

Paste this code:

```java
import java.io.IOException;
import java.util.*;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class MatrixMultiply {

    public static class Map extends Mapper<LongWritable, Text, Text, Text> {
        public void map(LongWritable key, Text value, Context context)
                throws IOException, InterruptedException {
            String[] val = value.toString().split(",");
            if (val[0].equals("A")) {
                for (int k = 0; k < 2; k++) {
                    context.write(new Text(val[1] + "," + k),
                            new Text("A," + val[2] + "," + val[3]));
                }
            }
            if (val[0].equals("B")) {
                for (int i = 0; i < 2; i++) {
                    context.write(new Text(i + "," + val[2]),
                            new Text("B," + val[1] + "," + val[3]));
                }
            }
        }
    }

    public static class Reduce extends Reducer<Text, Text, Text, IntWritable> {
        public void reduce(Text key, Iterable<Text> values, Context context)
                throws IOException, InterruptedException {
            int[] a = new int[2];
            int[] b = new int[2];
            for (Text val : values) {
                String[] data = val.toString().split(",");
                if (data[0].equals("A"))
                    a[Integer.parseInt(data[1])] = Integer.parseInt(data[2]);
                else
                    b[Integer.parseInt(data[1])] = Integer.parseInt(data[2]);
            }
            int sum = 0;
            for (int i = 0; i < 2; i++)
                sum += a[i] * b[i];
            context.write(key, new IntWritable(sum));
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Matrix Multiplication");
        job.setJarByClass(MatrixMultiply.class);
        job.setMapperClass(Map.class);
        job.setReducerClass(Reduce.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

---

### Step 4: Compile the Java Program
```cmd
javac -classpath "%HADOOP_HOME%\share\hadoop\common\hadoop-common-3.3.6.jar;%HADOOP_HOME%\share\hadoop\mapreduce\hadoop-mapreduce-client-core-3.3.6.jar;%HADOOP_HOME%\share\hadoop\common\lib\commons-cli-1.2.jar" MatrixMultiply.java
```

---

### Step 5: Create JAR File
```cmd
jar cf multiply.jar Multiply*.class
```

---

### Step 6: Upload Input File to HDFS
```cmd
hadoop fs -put C:\matrixmultiply\input.txt /
hadoop fs -ls /
```

---

### Step 7: Delete Old Output (if exists)
```cmd
hadoop fs -rm -r /matrix_output
```

---

### Step 8: Run the MapReduce Job
```cmd
hadoop jar multiply.jar Multiply /input.txt /matrix_output
```

---

### Step 9: View the Output
```cmd
hadoop fs -cat /matrix_output/part-r-00000
```

Expected output (result of M × N):
```
0,0    58
0,1    64
1,0    139
1,1    154
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
