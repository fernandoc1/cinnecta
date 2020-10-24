#! /bin/bash

curl -X POST "https://us-central1-weebah-com.cloudfunctions.net/receive_text" -H "Content-Type:application/json"  -d '{"name":"Jane"}'

