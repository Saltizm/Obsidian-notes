---
index: true
course: "ISIT 312"
chapter: "Big data platforms"
concept: "Theory"
---

# Theory

### 1. Core Concepts: Cluster Computing and Big Data

• A **computer cluster** is defined as a collection of computers (nodes) connected via a high-speed network that work together to simulate a single, much more powerful computer system.

• **Cluster computing** is the process of sharing computation tasks among multiple computers included in a computer cluster.

• **Advantages of computer clusters** include faster processing speed, larger storage capacity, better data integrity, greater reliability, and wider availability of resources.

• **Big Data** is characterized by the so-called **3V features**:

    ◦ **Volume**: referring to the sheer size of the data, e.g., billions of rows or millions of columns.

    ◦ **Variety**: describing the complexity of data types and structures (e.g., handling unstructured and semi-structured data).

    ◦ **Velocity**: pertaining to the speed of new data creation and growth.

### 2. Hadoop Architecture and Components

Hadoop consists of a storage layer (**HDFS**), a coordination and management layer (**YARN**), and a processing layer (e.g., MapReduce).

Hadoop Distributed File System (HDFS) Key Daemons:

• **NameNode**: The HDFS master node process that manages the **filesystem metadata** (like file hierarchy and block locations) but **does not store the file data itself**.

• **DataNode**: The HDFS slave node process that runs on cluster nodes and manages **block storage and access** for reading or writing data and handles block replication. It sends periodic **heartbeats** and **block reports** to the NameNode.

• **SecondaryNameNode/Standby NameNode**: The **SecondaryNameNode** periodically backups the metadata in the primary NameNode for recovery, while the **Standby NameNode** is an optional hot node facilitating high-availability.

• **HDFS Block Parameters**: The default size of each HDFS block is **128MB**. The default number of replicates for blocks is **3**.

Yet Another Resource Negotiator (YARN) Daemons:

• **ResourceManager**: The YARN daemon (one per cluster) that manages the overall use of resources across the cluster, runs the Scheduler, and tracks heartbeats from NodeManagers. **It performs pure management and scheduling** and does not perform actual data processing.

• **NodeManager**: The YARN daemon running on each slave node, responsible for **launching and monitoring containers** (where tasks run) and managing resource consumption on its host machine.

• **ApplicationMaster**: Dedicated to a single YARN application. It is the first container allocated by the ResourceManager and is in charge of **requesting resources** from the ResourceManager and **managing task scheduling and execution** for that application.

• A **container** is a logical construct representing a specific amount of resources (memory and CPU processing cores) where mapper and reducer tasks run.

### 3. MapReduce Processing Model

• **MapReduce** is the most important processing framework in Hadoop. Its logic consists of a **Map phase** and a **Reduce phase**.

• MapReduce uses **key-value pairs** as its basic data model for input, output, and intermediate records.

• **Map Phase**: Applies a function to each input key-value pair over a portion of the dataset, typically an HDFS block. Each map task emits zero or more intermediate key-value pairs.

• **Partition Function (Partitioner)**: Ensures that each key and its list of values is passed to one and only one Reduce task.

• **Shuffle-and-Sort**: This crucial process transfers data from the Mapper tasks to the Reducer tasks. Its primary purpose is to **minimize data transmission** through the network.

• **Combine Phase (Combiner)**: An optional phase that runs the equivalent of the `Reduce` function locally on the map output _before_ the shuffle-and-sort phase. This is done only if the function is **commutative and associative** (like sum or count), aiming to minimize data transferred to the Reduce phase.

• **Hadoop Data Types**: In Java MapReduce applications, data elements (keys and values) must be objects that implement the **Writable** interface (for serialization) and often the **WritableComparable** interface (for comparison during sorting), rather than simple Java primitive types. Examples include `IntWritable` and `Text`.

### 4. Hive and Data Warehousing Concepts

Hive

• **Hive** provides a tabular view of data stored in HDFS and uses the SQL-like language **HQL (Hive Query Language)** to manipulate it. HQL statements are translated into a sequence of Java MapReduce operations.

• **Metastore** is a relational database component that contains the **mappings of tables to their directory locations in HDFS**.

• **Internal (Managed) Tables**: Hive manages the full lifecycle (data and metadata deletion).

• **External (Unmanaged) Tables**: Hive only deletes the metadata when the table is dropped; the underlying data in HDFS is retained.

• **Partitions**: Divide a table into subfolders in HDFS based on column values to **eliminate unnecessary scans** when querying a fragment of data.

• **Buckets**: Divide a table into segments of files in HDFS by hashing the values in a specified column, helping to **speed up processing**.

OLAP and Multidimensional Model

• **OLTP (Online Transaction Processing)** focuses on day-to-day operations, concurrency control, online updates, and detailed, highly normalized data.

• **OLAP (Online Analytical Processing)** focuses on analytical queries, uses data warehouses, and relies on the **multidimensional model** (data cubes).

• A **data cube** is composed of **Dimensions** (perspectives for analysis, e.g., Product, Time, Customer) and **Facts** (cells containing numeric **Measures**, e.g., Quantity, Amount).

• **Measure Classifications (Additivity)**:

    ◦ **Additive**: Can be meaningfully summed along _all_ dimensions (e.g., Quantity).

    ◦ **Semiadditive**: Can be summed along _some_ dimensions (e.g., inventory quantities cannot be summed along the Time dimension).

    ◦ **Nonadditive**: Cannot be summed across _any_ dimension (e.g., item price).

• **Core OLAP Operations**:

    ◦ **Roll-up**: Aggregates measures to a **coarser granularity** along a dimension hierarchy (e.g., calculating sales by Country instead of City).

    ◦ **Drill-down**: Moves from a more general level to a **more detailed level** in a hierarchy (e.g., moving from Quarter to Month).

    ◦ **Slice**: Fixes a single value in a dimension level, resulting in a **2-dimensional sub-cube** (e.g., viewing sales only for 'Paris').

    ◦ **Dice**: Selects a **multi-dimensional sub-cube** based on a Boolean condition over dimension levels (e.g., sales for specific cities AND specific quarters).

### 5. HBase Data Model and Operations

• **HBase** is an open-source distributed database based on Google's BigTable, providing a sparse, distributed, persistent **multidimensional sorted map** view of data stored in HDFS.

• Data in HBase is uniquely indexed by a combination of **row key, column key, and timestamp**.

• A cell is uniquely identified by the combination of **row key, column family, and column qualifier** (or column name).

• **Column Families** must be **defined at table creation time**. **Column Qualifiers** are dynamic and can be **defined at write time**.

• **Atomicity** is guaranteed only at a **row level**; there are no multi-row transactions.

• All data (keys and values) in HBase tables are stored as **untyped sequences of bytes**.

### 6. Spark Data Abstractions and Operations

• **Key Spark Advantage**: Spark’s main feature is its **in-memory cluster computing**, which increases processing speed significantly compared to MapReduce, especially for interactive and iterative computations, by reducing hard-disk I/O overhead.

• **RDD (Resilient Distributed Datasets)**: The lowest-level, original Spark abstraction. It represents an immutable, partitioned collection of elements and **does not require a defined schema**.

• **DataFrame**: A distributed collection of data organized into **named columns** (schema). It is conceptually similar to a relational table and is considered **untyped** (typing is checked at runtime).

• **Dataset**: A higher-level distributed collection of data, restricted to JVM languages (Scala/Java). It is **typed** (typing is checked at compiling time). A DataFrame is essentially a Dataset of type `Row`.

• **Operations Types**: Spark operations are divided into two categories:

    ◦ **Transformations**: Operations (like `select()`, `filter()`, `map()`) that **return a new DataFrame/Dataset** and are **lazily evaluated** (meaning execution does not start until an Action is called).

    ◦ **Actions**: Operations (like `show()`, `count()`, `first()`) that **return a result** to the driver program or write data to storage, and **trigger the computation** of all pending transformations.

--------------------------------------------------------------------------------

**Analogy for Memorization**

To help memorize the key data processing components (HDFS, YARN, MapReduce), think of running a large business operation:

**HDFS (The Warehouse)**: This is where all the raw materials (data blocks) are stored on shelves (DataNodes). The central catalog (NameNode) knows exactly which shelf holds which box of materials, but the catalog itself doesn't contain the material.

**YARN (The Logistics Manager)**: This system coordinates the workforce and resources. The ResourceManager is the CEO who grants permission and schedules who gets to use what resources (containers). The NodeManagers are the floor supervisors managing the worker machines, ensuring they have the containers needed for the tasks. The ApplicationMaster is the Project Manager for a specific job, coordinating the resources allocated to achieve the project goal.

**MapReduce (The Assembly Line)**: The Map phase breaks down the task (like chopping vegetables) and prepares small intermediate items (key-value pairs). The Shuffle-and-Sort phase minimizes transport by efficiently bundling and routing all identical items together. The Reduce phase then aggregates and finalizes the product (like cooking the collected ingredients).