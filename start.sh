#!/bin/bash
# Start the Lobster Trap Mock Proxy in the background
python3 scripts/mock_proxy.py &

# Wait a moment for the proxy to initialize
sleep 2

# Start the Streamlit UI
streamlit run ui/app.py --server.address=0.0.0.0
