# Asma DevOps Practice App
# This file is for GitHub Actions Python linter practice.

APP_NAME = "Asma DevOps App"
AUTHOR = "Asma Saiyed"
ROLE = "DevOps Engineer"


def print_header():
    print("=" * 40)
    print(APP_NAME)
    print("Created by:", AUTHOR)
    print("Learning role:", ROLE)
    print("=" * 40)


def show_learning_topics():
    topics = [
        "Linux",
        "Git and GitHub",
        "GitHub Actions",
        "Docker",
        "CI/CD Pipeline",
        "AWS EC2",
        "PostgreSQL",
        "Kubernetes",
    ]

    print("\nToday I am learning:")
    for topic in topics:
        print("-", topic)


def calculate_progress(completed_days, total_days):
    progress = (completed_days / total_days) * 100
    return progress


def show_pipeline_steps():
    steps = [
        "Clone the code",
        "Install dependencies",
        "Run tests",
        "Build Docker image",
        "Push image to registry",
        "Deploy application",
    ]

    print("\nBasic CI/CD pipeline steps:")
    for number, step in enumerate(steps, start=1):
        print(f"{number}. {step}")


def main():
    print_header()
    show_learning_topics()

    completed_days = 37
    total_days = 90
    progress = calculate_progress(completed_days, total_days)

    print(f"\n90DaysOfDevOps progress: {progress:.2f}%")

    show_pipeline_steps()

    print("\nWorkflow is running successfully.")
    print("Keep going, Asma. You are doing great!")


if __name__ == "__main__":
    main()
