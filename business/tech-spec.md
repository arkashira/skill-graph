# Tech Spec
## Stack
* Language: Python 3.10
* Framework: FastAPI
* Runtime: uvicorn
* Database: PostgreSQL 14
* Frontend: React 18
* UI Library: Material-UI 5

## Hosting
* Platform: AWS
* Services:
	+ Compute: AWS Lambda (free tier)
	+ Database: AWS RDS (free tier)
	+ Storage: AWS S3 (free tier)
	+ API Gateway: AWS API Gateway (free tier)
* Alternative platforms:
	+ Google Cloud Platform (GCP)
	+ Microsoft Azure

## Data Model
### Tables/Collections
* **Skills**
	+ id (primary key, UUID)
	+ name (string)
	+ description (text)
	+ dependencies (array of skill IDs)
* **Dependencies**
	+ id (primary key, UUID)
	+ skill_id (foreign key referencing Skills.id)
	+ dependent_skill_id (foreign key referencing Skills.id)
* **Users**
	+ id (primary key, UUID)
	+ username (string)
	+ email (string)
	+ password (string, hashed)

## API Surface
### Endpoints
1. **GET /skills**: Retrieve a list of all skills
	* Method: GET
	* Path: /skills
	* Purpose: Retrieve a list of all skills
2. **GET /skills/{skill_id}**: Retrieve a specific skill by ID
	* Method: GET
	* Path: /skills/{skill_id}
	* Purpose: Retrieve a specific skill by ID
3. **POST /skills**: Create a new skill
	* Method: POST
	* Path: /skills
	* Purpose: Create a new skill
4. **PUT /skills/{skill_id}**: Update a specific skill by ID
	* Method: PUT
	* Path: /skills/{skill_id}
	* Purpose: Update a specific skill by ID
5. **DELETE /skills/{skill_id}**: Delete a specific skill by ID
	* Method: DELETE
	* Path: /skills/{skill_id}
	* Purpose: Delete a specific skill by ID
6. **GET /dependencies**: Retrieve a list of all dependencies
	* Method: GET
	* Path: /dependencies
	* Purpose: Retrieve a list of all dependencies
7. **GET /dependencies/{dependency_id}**: Retrieve a specific dependency by ID
	* Method: GET
	* Path: /dependencies/{dependency_id}
	* Purpose: Retrieve a specific dependency by ID
8. **POST /dependencies**: Create a new dependency
	* Method: POST
	* Path: /dependencies
	* Purpose: Create a new dependency
9. **PUT /dependencies/{dependency_id}**: Update a specific dependency by ID
	* Method: PUT
	* Path: /dependencies/{dependency_id}
	* Purpose: Update a specific dependency by ID
10. **DELETE /dependencies/{dependency_id}**: Delete a specific dependency by ID
	* Method: DELETE
	* Path: /dependencies/{dependency_id}
	* Purpose: Delete a specific dependency by ID

## Security Model
* **Authentication**: JSON Web Tokens (JWT)
* **Authorization**: Role-Based Access Control (RBAC)
* **Secrets Management**: AWS Secrets Manager
* **IAM**: AWS Identity and Access Management (IAM)

## Observability
* **Logs**: AWS CloudWatch Logs
* **Metrics**: AWS CloudWatch Metrics
* **Traces**: AWS X-Ray

## Build/CI
* **Build Tool**: GitHub Actions
* **CI Pipeline**: GitHub Actions workflow
* **Deployment**: AWS CodeDeploy
* **Testing**: Pytest, Unittest
* **Code Quality**: SonarQube, CodeCoverage
* **Code Review**: GitHub Code Review
* **Code Formatting**: Black, Pylint
* **Dependency Management**: pip, requirements.txt