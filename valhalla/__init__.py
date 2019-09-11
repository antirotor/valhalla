import os
import sys

node_path = os.path.join(os.path.dirname(__file__), "..", "vendor", "NodeGraphQt")
print(node_path)
sys.path.insert(0, node_path)
