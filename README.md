# STIGYA-project
this is the project for submission to stigya interview

## Project Overview
The project, aims to engineer a high-performance web application using either Django or FastAPI. This application will feature an advanced user management system with secure authentication, state-of-the-art Robotic Process Automation (RPA) functionalities using Selenium, and comprehensive data analytics capabilities. 
The key objectives of the project are:

Implement advanced user management and security features.
Integrate RPA functionalities for automation.
Develop a data analytics dashboard for insightful analytics.
Framework Selection and Scalability
We chose [Django/FastAPI] as the framework for this project due to its robustness, scalability, and extensive ecosystem of libraries and tools. To ensure scalability, we employed advanced caching techniques and optimized the database configuration. This enables the application to handle substantial real-world data loads efficiently.

## User Management and Security Enhancements
The user management system includes features such as email verification and Role-Based Access Control (RBAC) to enhance security. Email verification ensures that only valid users can access the system, while RBAC allows for granular control over user permissions, strengthening overall security.

## Database Design and Management
Product Master Table
Id: Unique identifier for each product.
Created_at: Timestamp of when the product was created.
Updated_at: Timestamp of the last update to the product.
Name: Name of the product.
ASIN: Amazon Standard Identification Number.
Brand: Brand of the product.
Is_Active: Boolean flag indicating if the product is active.
Product Update History Table
Id: Unique identifier for each update record.
Product_id: Foreign key referencing the Product Master table.
Created_at: Timestamp of when the update record was created.
Updated_at: Timestamp of the last update to the record.
Asin: Foreign key referencing the ASIN in Product Master.
Previous_attribute: Previous attribute value.
Current_attribute: Current attribute value.
Job Table
Id: Unique identifier for each job.
Created_at: Timestamp of when the job was created.
Updated_at: Timestamp of the last update to the job.
Name: Name of the job.
Total_count: Total count for the job.
Current_count: Current count for the job.
These tables are designed to efficiently manage user data, RPA tasks, and analytical processes within the application.

## Advanced RPA Integration with Selenium
The RPA module developed using Selenium automates web tasks effectively. It includes a user-friendly interface for managing tasks such as 'Add to Cart' and 'Product View.' The integration of RPA enhances the application's efficiency and productivity.

Data Analytics Dashboard
The data analytics dashboard provides insightful analytics on the performance and results of RPA tasks. It presents meaningful visualizations and metrics to help users understand and optimize their processes.

Performance Monitoring and Logging
We implemented cutting-edge monitoring tools and detailed logging mechanisms to ensure optimal performance and facilitate troubleshooting. These tools contribute to maintaining the application's reliability and performance.

## API Documentation
CRUD Operations APIs
GET /products: Retrieve all products.
GET /products/{id}: Retrieve a specific product by ID.
POST /products: Create a new product.
PUT /products/{id}: Update an existing product.
DELETE /products/{id}: Delete a product by ID.
## Additional APIs
POST /add-to-cart: Add a product to the cart based on ASIN.
POST /view-product: View product details based on ASIN.
Detailed API documentation, including request/response formats and authentication mechanisms, is provided in the API documentation section of this document.

Submission Guidelines
The project is to be submitted via a link to a public repository. The repository should include all setup instructions, documentation, and code required to run the application. Evaluation criteria include functionality, scalability, security, RPA innovation, data analytics, code quality, and documentation.

## Conclusion
This project demonstrates a comprehensive approach to building a high-performance web application with advanced features such as user management, RPA integration, and data analytics. The project meets the objectives outlined and provides a scalable, secure, and efficient solution for real-world applications.
