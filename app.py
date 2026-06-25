# =========================================
# Asma DevOps Practice Application
# =========================================

# Application Information
APP_NAME = "Asma DevOps Practice App"
AUTHOR = "Asma Saiyed"
ROLE = "DevOps Engineer"
VERSION = "1.0"


# =========================================
# Function: Print Application Header
# =========================================
def print_header():
    print("=" * 50)
    print("WELCOME TO", APP_NAME)
    print("=" * 50)
    print("Author :", AUTHOR)
    print("Role   :", ROLE)
    print("Version:", VERSION)
    print("=" * 50)


# =========================================
# Function: Display Learning Topics
# =========================================
def show_learning_topics():

    topics = [
        "Linux Administration",
        "Git and GitHub",
        "GitHub Actions",
        "CI/CD Pipeline",
        "Docker",
        "AWS EC2",
        "PostgreSQL",
        "Kubernetes",
        "Terraform",
        "Monitoring Tools",
    ]

    print("\nDevOps Learning Topics:\n")

    for number, topic in enumerate(topics, start=1):
        print(f"{number}. {topic}")


# =========================================
# Function: Calculate Progress
# =========================================
def calculate_progress(completed_days, total_days):

    progress = (completed_days / total_days) * 100

    return progress


# =========================================
# Function: Display Pipeline Stages
# =========================================
def show_pipeline_steps():

    pipeline_steps = [
        "Clone Repository",
        "Install Dependencies",
        "Run Unit Tests",
        "Run Linter",
        "Build Docker Image",
        "Push Image to Docker Hub",
        "Deploy Application",
        "Monitor Application",
    ]

    print("\nCI/CD Pipeline Stages:\n")

    for number, step in enumerate(pipeline_steps, start=1):
        print(f"Stage {number}: {step}")


# =========================================
# Function: Display Environment Information
# =========================================
def show_environment():

    environment = {
        "Operating System": "Ubuntu Linux",
        "Cloud Platform": "AWS",
        "Container Tool": "Docker",
        "CI/CD Tool": "GitHub Actions",
        "Database": "PostgreSQL",
    }

    print("\nProject Environment Details:\n")

    for key, value in environment.items():
        print(f"{key}: {value}")


# =========================================
# Function: Simple Health Check
# =========================================
def application_health_check():

    print("\nApplication Health Check Running...")

    status = "Healthy"

    print("Application Status:", status)


# =========================================
# Main Function
# =========================================
def main():

    print_header()

    show_learning_topics()

    completed_days = 37
    total_days = 90

    progress = calculate_progress(completed_days, total_days)

    print(f"\n90DaysOfDevOps Progress: {progress:.2f}%")

    show_pipeline_steps()

    show_environment()

    application_health_check()

    print("\nWorkflow executed successfully.")
    print("Keep learning and keep building projects.")
    print("Great job Asma!")


# =========================================
# Program Entry Point
# =========================================
if __name__ == "__main__":
    main()
