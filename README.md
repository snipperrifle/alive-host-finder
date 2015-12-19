# alive-host-finder
This script is used to find alive hosts Base on the tcp connection if we can connect on port 80 and firewall allows it the application will find that PC.
      - Works with arguments
      - default ip is 192.168.1.0
      - default sunet 255.255.255.0
###basic usage:
  -   required options
  ```sh
  python alive-host-finder.py --ip 192.168.1.1 --subnet 255.255.255.0
  ```
  
  
  -   additional options with single dash "-"
  ```sh
  python alive-host-finder.py --ip 192.168.1.1 --subnet 255.255.255.0 -timeout 0.5
  python alive-host-finder.py --ip 192.168.1.1 --subnet 255.255.255.0 -timeout 0.5 -verbose
  ```
