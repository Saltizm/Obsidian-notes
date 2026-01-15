The sources detail numerous functions, methods, commands, and operations across various technologies including Hadoop (HDFS, MapReduce, YARN), Hive (HQL, data structures), OLAP concepts, HBase (Shell and Java API), and Spark (RDDs, DataFrames, Streaming).

Below is a comprehensive list of the functions and operational commands mentioned in the provided material, organized by context.

---

### I. Hadoop MapReduce Functions and Components

These functions define the data processing model or are carried out by core Hadoop components:

|Category|Function/Method|Description|Source(s)|
|:--|:--|:--|:--|
|**MapReduce Model**|`Map(in_key, in_value)`|The fundamental function applied to each key-value pair over a portion of the dataset (e.g., an HDFS block).|,,|
||`Reduce(intermediate_key, list(intermediate_value))`|The function executed by each Reducer task for an intermediate key and its associated list of values.|,,|
||`emit (w, 1)` / `emit (word, sum)`|An action within the Map/Reduce functions to output a key-value pair.||
||`Partition function` (Partitioner)|Ensures each key and its list of values is passed to one and only one Reduce task.||
||`Combiner function`|A Reduce function performed before the Shuffle-and-Sort phase to minimize data transfer, used if the operation is commutative and associative (like `sum` or `count`),.|,|
|**YARN ResourceManager (RM)**|`Scheduler`|Component run by the RM to determine resource allocation among the cluster.|,|
||_Tracks heartbeats_|Monitors heartbeats from NodeManagers.||
|**YARN ApplicationMaster (AM)**|_Requesting resources_|Requests resources with ResourceManager to run the application.|,|
|**YARN NodeManager (NM)**|_Auxiliary Services_|Provides services to YARN applications, specifically used by the MapReduce framework for its **shuffle and sort** operations.||

### II. HDFS Command-Line Shell Commands

The following commands (functions) are used via the file system shell (`hadoop fs` or `hdfs dfs`):

|Function/Command|Description|Source(s)|
|:--|:--|:--|
|`hadoop fs -mkdir`|Creates a directory in HDFS. Example: `bin/hadoop fs -mkdir input`.|,|
|`hadoop fs -ls`|Lists the files in a directory in HDFS.|,|
|`hadoop fs -put`|Uploads a file (or files) from the local filesystem to HDFS. Example: `bin/hadoop fs -put README.txt input`.|,|
|`hadoop fs -cat`|Reads the content of a file (or files) in HDFS.|,|
|`hadoop fs -copyFromLocal`|Copies a file from the local filesystem to HDFS (similar to `put`).||
|`hadoop fs -copyToLocal`|Copies a file (or files) from HDFS to the local filesystem.||
|`hadoop fs -rm`|Deletes a file (or files) in HDFS.||
|`hadoop fs -rm -r`|Deletes a directory in HDFS.||
|`jps`|Lists Hadoop daemons (in the shell context).||

### III. HDFS Java API Methods

These methods are used in Java applications to interact with HDFS:

|Class|Method|Description|Source(s)|
|:--|:--|:--|:--|
|`FileSystem` (Factory)|`get(Configuration conf)`|Gets a `FileSystem` instance.||
||`get(URI uri, Configuration conf)`|Gets a `FileSystem` instance using a URI.||
||`getLocal(Configuration conf)`|Gets a local `FileSystem` instance,.|,|
|`FileSystem` (File I/O)|`open(Path f)`|Gets the input stream for reading a file,.|,|
||`create(Path f)`|Gets the output stream for writing a file on HDFS,.|,|
|`FileSystem` (Management)|`mkdirs()`|Creates a directory.||
||`getFileStatus()`|Gets metadata for a file or directory.||
||`listStatus()`|Lists contents of files in a directory.||
||`exists()`|Checks whether a file exists.||
||`delete()`|Removes a file.||
|`Path`|`new Path(uri)`|Constructor used to create a Path object,.|,|
|`Configuration`|`new Configuration()`|Constructor used to create a Configuration object,.|,|
|`IOUtils`|`copyBytes()`|Copies data from an input stream to an output stream,.|,|
|`IntWritable`|`set()`|Sets the integer value encapsulated in the object,.|,|
||`get()`|Retrieves the integer value encapsulated in the object.||
|`Mapper` / `Reducer`|`setup()`|Optional code run before the `map()` or `reduce()` method,.|,|
||`cleanup()`|Optional code run after the `map()` or `reduce()` method,.|,|
|`Context`|`write()`|Used to emit the output data from Mapper and Reducer.||
|`Job`|`getInstance(conf, "word count")`|Instantiates a `Job` object.||
||`waitForCompletion(true)`|Submits a Job object and waits for it to complete synchronously,.|,|
|`ToolRunner`|`run(new Configuration(), new WordCount(), args)`|Static method used to execute a MapReduce job, often to parse command-line options.||

### IV. OLAP and SQL/OLAP Functions

These functions are fundamental to multidimensional analysis and SQL extensions for data warehousing:

|Category|Function/Operator|Description|Source(s)|
|:--|:--|:--|:--|
|**OLAP Algebraic Ops**|`ROLLUP`|Aggregates measures along a dimension hierarchy to obtain measures at a coarser granularity.||
||`ROLLUP*` (Extended)|Similar to `ROLLUP`, but drops all dimensions not involved in the operation.||
||`RECROLLUP` (Recursive)|Aggregates over a recursive hierarchy.||
||`DRILLDOWN`|Moves from a more general level to a more detailed level in a hierarchy.||
||`SORT`|Returns a cube where members of a dimension have been sorted.||
||`PIVOT`|Rotates the axes of the cube.||
||`SLICE`|Fixes a single value in a dimension level.||
||`DICE`|Defines a sub-cube based on a Boolean condition.||
|**Standard Aggregation**|`count`, `sum`, `minimum`, `maximum`|Distributive measures that can be computed in a distributed way.||
||`average`|Algebraic measure, computed by dividing the sum by the count.||
|**SQL/OLAP Extensions**|`ROLLUP` (SQL clause)|Computes group subtotals in the order given by a list of attributes.||
||`CUBE` (SQL clause)|Computes all totals of a list of attributes,.|,|
||`GROUPING SETS`|A powerful operator that `ROLLUP` and `CUBE` are shorthands for.||
|**Window Functions**|`PARTITION BY`|Used to create a window (partition) for comparison/aggregation.|,|
||`MAX()` (Window)|Aggregation function used over a defined window,.|,|
||`RANK()`|Ranking function used to compute rankings within an ordered window.||
||`AVG()` (Window)|Statistical function used to compute statistics like moving averages over a frame,.|,|
||`SUM()` (Window)|Statistical function used to compute totals like year-to-date sums over a frame.||

### V. Hive Query Language (HQL) Functions and Statements

Hive uses SQL-like statements (`HQL`) which are then translated into MapReduce operations:

|Category|Function/Statement/Clause|Description|Source(s)|
|:--|:--|:--|:--|
|**Data Definition Language (DDL)**|`CREATE DATABASE`, `DROP DATABASE`|Used for creating and deleting schema objects,.|,|
||`DESCRIBE DATABASE`|Provides information about a database.||
||`USE`|Makes a database "current".||
||`CREATE TABLE`, `CREATE EXTERNAL TABLE`|Creates internal or external tables,,.|,,|
||`ALTER TABLE ADD PARTITION`|Adds a partition to a table.||
||`show partitions`|Lists partitions of a table.||
||`CREATE VIEW`|Creates a logical data structure that simplifies queries.||
|**Data Manipulation Language (DML)**|`LOAD DATA`|Loads data into Hive tables from local file system or HDFS,,.|,,|
||`EXPORT` / `IMPORT`|Used for data migration, exporting/importing both data and metadata,.|,|
||`SELECT` (Data Selection)|Projects the rows satisfying query conditions,.|,|
||`JOIN` (e.g., INNER, MAPJOIN, LEFT SEMI JOIN)|Links data between tables,,.|,,|
||`UNION ALL`|Combines multiple `SELECT` statements.||
||`ORDER BY`|Sorts results globally across all reducers.||
||`SORT BY`|Sorts data locally within each reducer,.|,|
||`DISTRIBUTE BY`|Partitions rows to matching reducers,.|,|
||`CLUSTER BY`|Shorthand for `DISTRIBUTE BY` and `SORT BY`,.|,|
|**Aggregation and Analytic Functions**|`GROUP BY`|Performs basic aggregation.||
||`collect_set`|Aggregation function used to aggregate into sets.||
||`GROUPING SETS`, `ROLLUP`, `CUBE`|Clauses implementing advanced multiple aggregation levels.||
||`GROUPING__ID`|Distinguishes entire rows in aggregation results.||
||`HAVING`|Used for conditional filtering of `GROUP BY` results.||
||`function (...) OVER ([PARTITION BY...])`|Syntax for analytic functions including `COUNT()`, `SUM()`, `MIN()`, `MAX()`, `AVG()`.||
||`RANK()`, `DENSE_RANK()`|Analytic ranking functions.||
||`FIRST_VALUE()`, `LAST_VALUE()`|Analytic value functions.||
||`RAND()`|Used with `LIMIT` for random sampling.||
||`TABLESAMPLE()`|Used for block sampling or bucket table sampling.||
|**Complex Type Functions**|`array()`|Creates an ARRAY structure.||
||`map()`|Creates a MAP (key-value pairs) structure.||
||`named_struct()`|Creates a STRUCT structure.||

### VI. HBase Commands and API Methods

HBase provides Data Definition and Data Manipulation commands via its JRuby-based shell, as well as a Java API:

|Category|Function/Command/Method|Description|Source(s)|
|:--|:--|:--|:--|
|**HBase Shell (DDL)**|`source 'file-name.hb'`|Executes a script of HBase commands.||
||`create 'table','cf'`|Creates a table with specified column families.||
||`describe 'table'`|Shows the structure of a table.||
||`alter 'table', {NAME=>...}`|Modifies table or column family settings (e.g., adding a column family, increasing versions),.|,|
|**HBase Shell (DML)**|`count 'table'`|Counts the total number of rows.||
||`put 'table','rk','cf:q','val'`|Inserts a value into a cell.||
||`get 'table','rk', {options}`|Retrieves specific cells or versions for a given row key,.|,|
||`scan 'table', {options}`|Lists or retrieves data from the table (supports various options and filters),,.|,,|
||`delete 'table','rk','cf:q'`|Deletes a specific cell.||
||`deleteall 'table', 'rk'`|Deletes an entire row.||
||`QualifierFilter()`, `ValueFilter()`|Filters used within a `scan` command,.|,|
|**HBase Java API**|`HBaseAdmin.createTable()`|Creates a table.||
||`admin.isTableAvailable()`|Checks if a table is available.||
||`Put.add()`|Adds a cell modification to a `Put` operation.||
||`HTable.put(put)`|Executes the data insertion.||
||`HTable.get(get)`|Executes the data retrieval.||
||`get.setMaxVersions()`|Sets the maximum number of versions to retrieve.||
||`Result.getValue()`|Gets a specific cell value from the result object.||

### VII. Spark Operations (RDD, DataFrame, Dataset)

Spark operations are categorized primarily into Transformations (which create a new object and are lazily evaluated) and Actions (which return a result or write to storage, triggering computation),.

|Category|Function/Method|Description|Source(s)|
|:--|:--|:--|:--|
|**Data Creation/Loading**|`sparkContext.parallelize()`|Creates an RDD from a local collection.||
||`sparkContext.textFile()`|Creates an RDD from a file, reading line-by-line.||
||`spark.read.json()` / `spark.read.parquet()`|Creates a DataFrame by reading structured data sources,.|,|
||`spark.read.textFile()`|Reads unstructured data as a Dataset.||
||`spark.readStream`|Reads streaming data.||
||`toDS()` / `toDF()`|Converts collections/RDDs/DataFrames between Dataset/DataFrame types,.|,|
|**Transformations (General)**|`map(func)`|Passes each element through a function,.|,|
||`filter(func)`|Selects elements where a function returns true,.|,|
||`flatMap(func)`|Applies a function to elements, returning a flattened collection,.|,|
||`select(...)`|Performs projection on a DataFrame/Dataset,.|,|
||`distinct()`|Eliminates duplicates from an RDD,.|,|
||`union(otherDataset)`|Unions two RDDs.||
||`intersection(otherDataset)`|Finds the intersection of two RDDs.||
||`sortBy(func)`|Sorts an RDD,.|,|
|**Transformations (Grouping/Aggregation)**|`reduceByKey(func)`|Aggregates elements by key on key-value RDD pairs,.|,|
||`groupByKey(identity)`|Groups elements by key on a Dataset.||
||`groupBy("column")`|Groups DataFrame rows by column.||
|**Actions**|`count()`|Returns the number of elements,.|,|
||`reduce(func)`|Reduces an RDD to a single value.||
||`collect()`|Returns all elements of the Dataset/RDD as an array to the driver,.|,|
||`first()`|Returns the first element,.|,|
||`show()`|Prints the contents of a DataFrame/Dataset,.|,|
||`take(n)`|Returns the first _n_ elements.||
|**Spark SQL Integration**|`spark.sql("query")`|Executes SQL queries,.|,|
||`createOrReplaceTempView("name")`|Registers a DataFrame as a temporary view,.|,|
|**Utility Functions**|`printSchema()`|Displays the schema of a DataFrame.||
||`spark.stop()`|Stops the Spark session.||
||`writeStream.start()`|Starts the continuous streaming query.||