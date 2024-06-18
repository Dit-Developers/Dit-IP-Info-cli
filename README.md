
# DIT IP Info cli Tool

## Features:

- Get your IP address.
- Retrieve detailed information about any IP address.
- Information about the Developer.
- Ping an IP address.
- Get the IP address of a website.
- Get your local IP address.
- Perform an Nmap scan on an IP address.
- Perform web application enumeration.

## Usage:

The tool is designed to be run from the command line. It presents a menu where you can select various options to perform different IP-related tasks.

## Functions:

- `info(ip)`: Retrieves detailed information about the specified IP address using the ip-api.com API.
- `ping(ip)`: Sends ICMP echo requests to check the reachability of an IP address.
- `get_website_ip(website)`: Retrieves the IP address of a specified website using DNS resolution.
- `get_local_ip()`: Gets the local IP address of the system by creating a temporary socket connection.
- `clear_screen()`: Clears the terminal screen.
- `nmap_scan(ip, arguments='')`: Performs an Nmap scan on the specified IP address with optional Nmap arguments.
- `web_app_enum(ip)`: Performs web application enumeration (placeholder function).

## Mapping:

The tool maps user input to specific functions based on the selected menu option, allowing users to execute different tasks related to IP addresses and network scanning.

## Developer Name:

The tool is developed by DIT-Developers.
