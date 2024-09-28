# Evaluation

## Scenario
Maungawhau College is upgrading its attendance system. This system allows lecturers to enter student attendance. Students can also view their attendance on the system. 

## Programming languages for web development
Several languages can be used for the server side of web development, such as Java, Python, Golang, etc. In this paper, I will compare Python and Golang to discuss their advantages and disadvantages in the web development field. I chose two of them to compare because they are very representative.

### Learning
Python is easy to learn for users, especially for beginners. For example, developers do not need to write 'var' to declare a new variable. It also does not need to write data type for every variable explicitly; the system treats these things for the user. It is more likely like natural language.

As for Golang, it looks odd at first glance. People need to spend more time to become familiar with its syntax and mechanism. For example, its Struct can be used as a class, but its features are much different, which will cause confusion. 

### Performance
Golang is faster than Python. Go is translated to machine code, which causes better performance for CPU-intensive tasks. Python is an interpreter language, and it translates code when running. It is better for rapid development but unsuitable for higher-performance projects. 

### Concurrency
Python's concurrency depends on threads and multiprocessors of the operating system, which means more memory cost and a lower schedule of threads. 

Compared to Golang, it has self-designed goroutines and channels, which make much lower memory costs and are also much more efficient. It is much better for higher-load network applications.

### Memory Management
Both of them have garbage collection mechanisms. Go's garbage collection manages memory more efficiently, which leads to better performance in long-running applications. Python's garbage collection works are less predictable, especially in projects that hold short-lived objects.

### Libraries and frameworks
Python has vibrant libraries and frameworks, such as Flask and Django, for web development. It also has pandas for treating data files. All of these libraries are supported well by communities. Go has a growing ecosystem; it also has well-supported frameworks for web development, such as Gin. Its built-in server and its template system can work well. However, for some tasks, such as loading data files, the Developer should be more careful choosing libraries for their work, as it is harder to compare and make the decision when selecting library work. Because most libraries for data treatment are developed by individuals, which means some libraries are not supported well in the long run.

### conclusion
If Developers focus on quick implementation for a business solution at the beginning, they should choose Python; it is easy to use and more powerful depending on its variety and well-supported libraries. Otherwise, if performance is more critical, Developer should choose Golang.

## Data access
The two ways to access relational databases are to use SQL language and ORM. Even though the NoSQL database can be an option, it is not suitable for this project because there are several models and relationships between them.

### SQL
SQL is a standard query language for manipulating relation databases. It can directly control the project database. Also, it can query data in flexible ways for different business requirements, such as JOINs for expanding fields, subqueries, and aggregate functions for count and average results. The Developer can optimize these sentences for better performance. However, it is not friendly for beginners, especially in complex projects. 

### ORM
ORM is a programming technique that allows developers to interact with the databases in their preferred programming language. Developers just need to know how to build up the relationship between models instead of learning more SQL skills. During the project's progress, developers can easily update the tables by changing models and their relationships because ORM also provides migration tools for these tasks. Meanwhile, these tools also generate the migration files, which means the Developer can manage the version of the database by version-control software, such as git. Under this mechanism, databases are easier to trace when changing during updating.

## Recommend
Everything has its downside and upside. After comparing two languages and two ways to access the database, it can be found that the business purpose and current situation will cause the choice of technique. 

As for this project, based on the scenario at the start of this paper, the attendance system of a college does not need high performance during its long-time running for students and lectures because the active users just use it at the start of class of every day, which means most of the time, the load of the system is very low. Even though some colleges have large numbers of students, but before the start of classes, there are huge requests in minutes. Developers should consider a middle system to make all requests as a queue, then consumed by the attendance system one by one. Even though Golang is beneficial for this situation, its cost of development is much higher than that of Python.

Moreover, the cost is sensitive for the college, including development fees, maintenance fees, and duration of development. So Python with Django is more suitable for this project. Python is easier to learn, which means that hiring a Developer will cost less. Django includes lots of features, and its user system and admin system can save lots of time. These are ready to use. Django's ORM can help developers focus on design models and their relationships instead of experiencing more SQL tests.

Plus, the features of uploading users by treating Excel files are much easier because developers can use well-designed and supported libraries to solve this. In the future, if the college needs more features, such as statistics, it's much easier to find the package to solve it.

Finally, Python with Django is more suitable for this project.
