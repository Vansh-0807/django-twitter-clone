# Create a test file
from pathlib import Path
from dotenv import load_dotenv
import os

print(f"Current directory: {Path.cwd()}")
print(f".env file exists: {Path('.env').exists()}")

if Path('.env').exists():
    print("File size:", Path('.env').stat().st_size, "bytes")
    
# Try to load it
result = load_dotenv()
print(f"load_dotenv() returned: {result}")

# Check if DATABASE_URL is now in environment
print(f"DATABASE_URL in os.environ: {'DATABASE_URL' in os.environ}")
if 'DATABASE_URL' in os.environ:
    print(f"DATABASE_URL starts with: {os.environ['DATABASE_URL'][:30]}...")


