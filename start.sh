#!/bin/bash

# Service name
SERVICE_NAME="core-transfer"

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Function to generate the service file
generate_service_file() {
    cat << EOF > /etc/systemd/system/${SERVICE_NAME}.service
[Unit]
Description=${SERVICE_NAME} service
After=network.target

[Service]
ExecStart=/bin/bash ${SCRIPT_DIR}/$(basename "$0") run
WorkingDirectory=${SCRIPT_DIR}
User=$(whoami)
Group=$(id -gn)
Restart=always

[Install]
WantedBy=multi-user.target
EOF
    echo "Service file generated: /etc/systemd/system/${SERVICE_NAME}.service"
    sudo systemctl daemon-reload
}

# Function to enable the service
enable_service() {
    sudo systemctl enable ${SERVICE_NAME}
    echo "${SERVICE_NAME} service enabled"

    sudo systemctl start ${SERVICE_NAME}
    sudo systemctl status ${SERVICE_NAME}
}

# Function to disable the service
disable_service() {
    sudo systemctl disable ${SERVICE_NAME}
    echo "${SERVICE_NAME} service disabled"
}

# Function to check the service status
check_service() {
    sudo systemctl is-active --quiet ${SERVICE_NAME}
    if [ $? -eq 0 ]; then
        echo "${SERVICE_NAME} is running"
    else
        echo "${SERVICE_NAME} is not running"
    fi
}

# Function to view service logs
log() {
    sudo journalctl -u ${SERVICE_NAME} -l
}

# Function to view service status
status() {
    sudo systemctl status ${SERVICE_NAME}
}

start() {
    sudo systemctl start ${SERVICE_NAME}
    sudo systemctl status ${SERVICE_NAME}
}

restart() {
    sudo systemctl restart ${SERVICE_NAME}
    sudo systemctl status ${SERVICE_NAME}
}

# Function to run the main script
run_script() {
    # Change to the project's directory
    export PYTHONPATH=$(pwd)
    echo "project root directory: $(pwd)"
    source venv/bin/activate
    echo "working directory: $(pwd)"
    python3 monitor.py
}

# Main logic
case "$1" in
    generate)
        generate_service_file
        ;;
    enable)
        enable_service
        ;;
    disable)
        disable_service
        ;;
    check)
        check_service
        ;;
    log)
        log
        ;;
    status)
        status
        ;;
    start)
        start
        ;;
    restart)
        restart
        ;;
    run)
        run_script
        ;;
    *)
        run_script
        ;;
esac

exit 0
