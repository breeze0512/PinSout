# __Getting Start__
- This document describes the procedure for running MovingFeature Service.

## 1. Procedure for executing Moving Feature Service

- This service will operate in the following environments:

    !!! note "__MovingFeature Service Running Environment__"

            | <h2>__Essential Environment__</h2> | <h2>__Version__</h2>|
            | ---------- | ---------- |
            | <h2>__Java__</h2> | <h2>__OpenJDK8__</h2> |
            | <h2>__Apache Spark__</h2> | <h2>__Apache Spark 2.4.3__</h2> |
            | <h2>__Cassandra__</h2> | <h2>__Cassandra 3.11.3__</h2> |
            | <h2>__Stratio's Cassandra Lucene Index__</h2> | <h2>__cassandra-lucene-index 3.11.3__</h2> |


- The user can obtain the detailed information for installing Cassandra from the [__2. Build Cassandra and set up extended library__](#2-build-cassandra-and-set-up-extended-libraries) part
    - ==The user must connect to Cassandra before the server is starting==

- The user can obtain the detailed information for installing Apache Spark from the [__3. Build Apache Spark__](#3-build-apache-spark) part
  
  
---

### 1.1 Building MovingFeature Service

- This service is provided as a zip file. To extract the zip file from the machine on which the service runs.

    ```sh
    $ unzip mfjson.zip
    ```
  
- MovingFeature Service Directory Configuration

![Directory](img/directory.png)

- MovingFeature Service File List

    !!! note "__Information for Service File__"

        | <h2>__Created File__</h2> | <h2>__Version__</h2>|
        | ---------- | ---------- |
        | <h2>__run_noatuh.sh__</h2> | <h2>__Executable file without pntml__<br>(Execute on Local system) </h2> |
        | <h2>__run_pntml.sh__</h2> | <h2>__Executable file with pntml__ </h2></h2> |
        | <h2>__application.yaml__</h2> | <h2>__Web Configuration File__</h2> |
        | <h2>__engine.yaml__</h2> | <h2>__Engine Configuration File (Apache Spark)__</h2> |
        | <h2>__store.yaml__</h2> | <h2>__Store Configuration File (Cassandra)__</h2> |
        | <h2>__drop-keyspaces.cql__</h2> | <h2>__Delete Existing Data CQL__</h2> |
        | <h2>__initialize-auth.cql__</h2> | <h2>__Generation the unique user id for Cassandra__</h2> |
        | <h2>__initialize-data.cql__</h2> | <h2>__Cassandra Initialization CQL__</h2> |
        | <h2>__insert-users.cql__</h2> | <h2>__Cassandra Initialization CQL__</h2> |
        | <h2>__job-result.cql__</h2> | <h2>__Cassandra Initialization CQL__</h2> |
        | <h2>__movingfeature-web-0.3.0-SNAPSHOT.jar__</h2> | <h2>__MovingFeature Service Main__</h2> |

- The following files must be edited for your environment prior to running the service:

    --> ==__Web configuration file__== : __mfjson/bin/config/application.yaml__  
    --> ==__Engine configuration file__== : __mfjson/bin/config/engine.yaml__  
    --> ==__Store configuration file__== : __mfjson/bin/config/store.yaml__


#### 1.1.1 To set up a Web configuration file 

Web settings by editing the <__mfjosn/bin/config/application.yaml__>.

1.  Configuring Moving Features Service URLs 

    - Set the server address for the user to access the Moving Features Service.

    ```yaml
    movingfeature:
        url: "Moving Features Service URL"
    ```

    !!! example "Service URL Configuration Example"
        ![Service_URL_Configuration_Example](img/Service_URL_Configuration_Example.png)
    

#### 1.1.2 To set up a store configuration file

Store settings are done by editing <__mfjson/bin/config/store.yaml__>.  
Before configuring this configuration, create a Cassandra environment.  
Reference: [Building 2 Cassandra](#2-build-cassandra-and-set-up-extended-libraries) and Configuring Extended Libraries.

1. Configuring Cassandra to Connect
    
    - Configure the connection destination for Cassandra to store data.

    ```yaml
    nodes:
        - host: "HostName or IP address"
          port: "Port Number"
    ```

    !!! example "Cassandra Configuration Example"
        ![Cassandra_Configuration_Example](img/Cassandra_Configuration_Example.png)

2. Access User Settings

    - If you have limited access to Cassandra, you must configure a username and password for the user who can access it.

    ```yaml
    authentication:
        user: "UserName"
        password: "Password"
    ```

#### 1.1.3 To set up a engine configuration file

Engine settings are done by editing <__mfjson/bin/config/engine.yaml__>.  
Before configuring this configuration, create a Apache Spark environment.  
Reference: [Building 3 Apache Spark](#3-build-apache-spark).

1. Configuring Apache Spark to Connect

- Configure the connection destination for Cassandra to store data.

    !!! example "Apache Spark Configuration Example"

        === "Information of the setting items"

            - For more detailed information, please refer to the [Spark Configuration](https://spark.apache.org/docs/latest/configuration.html){:target="_blank"} section of the official document.
                - Link for [Spark Configuration](https://spark.apache.org/docs/latest/configuration.html){:target="_blank"}

            ```yaml
            spark:
                home:
                master: # Run Spark locally with as many worker threads as logical cores on your machine.
                appname: # The name of your application. This will appear in the UI and in log data.
                deploymode: # The deploy mode of Spark driver program, either "client" or "cluster", Which means to launch driver program locally ("client") or remotely ("cluster") on one of the nodes inside the cluster.
                verbose: # Print out fine-grained debugging information by running spark-submit
                conf:
                    - key: "spark.default.parallelism"
                    value: # Default number of partitions in RDDs returned by transformations like join, reduceByKey, and parallelize when not set by user
                    - key: "spark.executor.cores"
                    value: # Number of virtual cores
                    - key: "spark.executor.memory"
                    value: # Size of memory to use for each executor that runs the task
                    - key: "spark.driver.memory"
                    value: # Size of memory to use for the driver
                    - key: "spark.driver.cores"
                    value: # Number of virtual cores to use for the driver
                    - key: "spark.driver.maxResultSize"
                    value: # Limit of total size of serialized results of all partitions for each Spark action (e.g. collect) in bytes. Should be at least 1M, or 0 for unlimited.
                    - key: "spark.driver.port"
                    value: # Port for the driver to listen on
                    - key: "spark.blockManager.port"
                    value: # Port for all block managers to listen on
                    - key: "spark.driver.blockManager.port"
                    value: # Driver-specific port for the block manager to listen on, for cases where it cannot use the same configuration as executors.
                    - key: "spark.broadcast.port"
                    value: # Port for the driver's HTTP broadcast server to listen on.
                    - key: "spark.cores.max"
                    value: # The maximum amount of CPU cores to request for the application from across the cluster
                    - key: "spark.rpc.message.maxSize"
                    value: # Maximum message size (in MiB) to allow in "control plane" communication
                jarsPath: ../sparkjars
                serverClassPath: /mnt/PnTML/MF/lib/
                parallel: 1 # threads of job
                lastScanSecond:  0.1
            ```

        === "Example for configuration"

            ```yaml
            spark:
                home:
                master: local[*]
                appname: movingfeature-
                deploymode: client
                verbose: true
                conf:
                    - key: "spark.default.parallelism"
                    value: 20
                    - key: "spark.executor.cores"
                    value: 2
                    - key: "spark.executor.memory"
                    value: 10g
                    - key: "spark.driver.memory"
                    value: 10g
                    - key: "spark.driver.cores"
                    value: 2
                    - key: "spark.driver.maxResultSize"
                    value: 4g
                    - key: "spark.driver.port"
                    value: 30055
                    - key: "spark.blockManager.port"
                    value: 30060
                    - key: "spark.driver.blockManager.port"
                    value: 30060
                    - key: "spark.broadcast.port"
                    value: 30065
                    - key: "spark.cores.max"
                    value: 20
                    - key: "spark.rpc.message.maxSize"
                    value: 256
                jarsPath: ../sparkjars
                serverClassPath: /mnt/PnTML/MF/lib/
                parallel: 1 # threads of job
                lastScanSecond:  0.1
            ```
    
    !!! error "__Reminder__"

        <h3>If the value of master included in engine.yaml is not __"local"__, users must copy the all of jars included in the sparkjars to the lib of the worker in each Spark Cluster.<h3>

---

### 1.2 Starting and Stopping MovingFeature Service

1. MovingFeature service is started by executing the __sh__ file.

    - If the user can access to Moving Features Server, running the "__mfjson/bin/run_pntml.sh__"

    ```sh
    $ sh mfjson/bin/run_pntml.sh
    ```

    - If the user can not access to Moving Features Server, running the "__mfjson/bin/run_noauth.sh__"
  
    ```sh
    $ sh mfjson/bin/run_noauth.sh
    ```

    - If End product initialize is displayed on the screen, the boot is complete.

    !!! example "Example of MovingFeature Service launch indication"

        ```sh
        2019-04-05 15:10:01.044 INFO 195 [main] o.a.c.m.s.connector.cassandra.Connector : Close connection.
        2019-04-05 15:10:03.293 INFO 195 [main] o.a.c.m.s.connector.cassandra.Connector : Closed connection.
        2019-04-05 15:10:03.296 INFO 195 [main] o.a.c.m.w.i.ProductionInitializer : End product initialize.
        ```

2. Services performed in __sh__ will stop at CTRL+C

---

## 2. Build Cassandra and set up extended libraries

This document only describes the basic construction of Cassandra.  
Please visit Cassandra's website for detailed configuration and tuning.  

### 2.1 Building Cassandra

MovingFeature Service works with version __3.11.3__ Cassandra.

1. Download Cassandra

    Click this [Download Cassandra](http://archive.apache.org/dist/cassandra/3.11.3/apache-cassandra-3.11.3-bin.tar.gz)

    Please download the version 3.11.3.

    ```sh
    wget http://archive.apache.org/dist/cassandra/3.11.3/apache-cassandra-3.11.3-bin.tar.gz
    ```

2. Deploy the Cassandra

    Extract and deploy the downloaded tar.gz to your machine.  
    Location can be anywhere, but a location with more storage capacity is recommended __/home/mf/cassandra__ in this document.

    ```sh
    $ tar xzvf apache-cassandra-3.11.3-bin.tar.gz
    $ mv apache-cassandra-3.11.3 /home/mf/cassandra
    ```

### 2.2 Deployment of Stratio's Cassandra Lucene Index Library

To use the Moving Feature Service, you must deploy the Library Stratio's Cassandra Lucene Index in Cassandra, which adds text search capabilities for Lucene.  
Please install the library as the same version with Cassandra.

#### 2.2.1 Install the library from Maven Repository

This library can be downloaded from the Maven Repository.

1. Download the library from the Maven Repository website

    ```sh
    $ wget https://repo1.maven.org/maven2/com/stratio/cassandra/cassandra-lucene-index-plugin/3.11.3.0/cassandra-lucene-index-plugin-3.11.3.0.jar    
    ```

2. Library deployment
   
    Deployment of the downloaded library in Cassandra.  
    The location is <CASSANDRA_HOME>/lib/.  
    In this document, it is deployed in "/home/mf/cassandra/lib/".  

    ```sh
    $ cp cassandra-lucene-index-plugin-3.11.3.0.jar /home/mf/cassandra/lib/
    ```

#### 2.2.2 Creating a Library from a Source

This library can also be created from sources.
Create from source using OpenJDK8, Git, and Maven.
If it is not already installed, please install it.

1. Obtaining Sources and Creating Libraries

    The source can be obtained from GitHub.  
    You can get it from GitHub anywhere.  

    ```sh
    $ git clone https://github.com/Stratio/cassandra-lucene-index.git
    ```

    Go to the created directory.

    ```sh
    $ cd cassandra-lucene-index
    ```

    Switch branch to branch-3.11.3

    ```sh
    $ git checkout branch-3.11.3
    ```

    Create a library.

    ```sh
    $ mvn clean package
    ```

    The library is created with the following name.  
    The end of the version may vary depending on when you got it from GitHub.

    ```sh
    plugin/target/cassandra-lucene-index-plugin-3.11.3.1-RC1-SNAPSHOT.jar
    ```

2. Library deployment

    Deployment of the downloaded library in Cassandra.  
    The location is <CASSANDRA_HOME>/lib/.  
    In this document, it is deployed in "/home/mf/cassandra/lib/".  

    ```sh
    $ cp plugin/target/cassandra-lucene-index-plugin-3.11.3.1-RC1-SNAPSHOT.jar /home/mf/cassandra/lib/
    ```

### 2.3 Deployment of JTS Topology Suite library

Stratio's Cassandra Lucene Index library uses JTS Topology Suite library when handling location information.  
Since MovingFeature Service searches by location information, this library also needs to be placed in Cassandra.  
It must same the version of the library to the version required by Stratio's Cassandra Lucene Index. 
(As of April 8, 2019: jts-core-1.14.0.jar)  
This library can be downloaded from Maven Repository.  

1. Download the library from the Maven Repository website

    ```sh
    wget https://repo1.maven.org/maven2/com/vividsolutions/jts-core/1.14.0/jts-core-1.14.0.jar
    ```

2. Library deployment

    Deployment of the downloaded library in Cassandra.  
    The location is <CASSANDRA_HOME>/lib/.  
    In this document, it is deployed in "/home/mf/cassandra/lib/".  

    ```sh
    $ cp jts-core-1.14.0.jar /home/mf/cassandra/lib/
    ```

---

## 3. Build Apache Spark

This document only describes the basic construction of Apache Spark.  
Please visit Apache Spark's website for detailed configuration and tuning.  

### 3.1 Build Apache Spark 

MovingFeature Service works with version __2.4.3__ Apache Spark.

1. Download Apache Spark

    Click this [Download Apache Spark](http://archive.apache.org/dist/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz)

    Please download the version 2.4.3

    ```sh
    wget http://archive.apache.org/dist/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz
    ```

2. Deploy the Apache Spark

    Extract and deploy the downloaded tar.gz to your machine.     
    Location can be anywhere, but a location with more storage capacity is recommended "__/home/mf/spark__" in this document.
<!-- /opt/spark -->
    ```sh
    $ tar xzvf spark-2.4.3-bin-hadoop2.7.tgz
    $ sudo mv spark-2.4.3-bin-hadoop2.7/ /home/mf/spark 
    ```

### 3.2 Set Apache Spark environment

1. Set the Apache Spark execution path

```sh
$ vim ~/.bashrc
```
2. Add the path of sprak in the "__~/.bashrc__"

```vim
export SPARK_HOME=/home/mf/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
```
3. Activate the changes.

```sh
$ source ~/.bashrc
```