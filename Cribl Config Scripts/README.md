# cribl scripts

## cribl_stream.py

Written to deploy the initial Cribl stream server (to serve as a leader node).

To run the script, use the following command:

```
sudo python3 cribl_stream.py
```

Once complete the Cribl UI will be available at: http://server-ip-address:9000

## cribl_worker.py

Written to add a worker to a defined Cribl Stream leader. Input provided at runtime be end user, requires IP address for the Cribl Stream leader and the auth token.

To run the script, use the following command:

```
sudo python3 cribl_worker.py
```

Enter the IP address of the leader node as well as the auth token to complete the deployment.

## cribl_edge.py

Written to add an edge node to a defined Cribl Stream leader. Input provided at runtime be end user, requires IP address for the Cribl Stream leader and the auth token.

To run the script, use the following command:

```
sudo python3 cribl_edge.py
```

Enter the IP address of the leader node as well as the auth token to complete the deployment.