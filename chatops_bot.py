import sys

def check_status():
    print("System status: All systems operational.")

def deploy():
    print("Deploying application...")

def show_logs():
    print("Fetching logs...")

def main():
    if len(sys.argv) < 2:
        print("Usage: python chatops_bot.py [command]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "status":
        check_status()
    elif command == "deploy":
        deploy()
    elif command == "logs":
        show_logs()
    else:
        print("Unknown command. Available commands: status, deploy, logs")

if __name__ == "__main__":
    main()
