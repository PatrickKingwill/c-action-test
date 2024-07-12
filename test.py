import os, subprocess

#Settings 
TEST_DIR = "."
CODE_FILE= "main.c"
COMPILER_TIMEOUT = 10.0
RUN_TIMEOUT = 10.0

# Create absolute path 
code_path = os.path.join(TEST_DIR,CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")
print('Building...')

try:
    ret = subprocess.run(["gcc", code_path, "-o", app_path], 
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         timeout=COMPILER_TIMEOUT)
except Exception as e:
    print("ERROR: Compilation failed", str(e))
    exit(1)
    
#Parse Output
output =ret.stdout.decode("utf-8")
print("OUTPUT:",output)
output = ret.stderr.decode("utf-8")
print(output)

#Check to see if the program compiled successfully 
if ret.returncode != 0:
    print("Compliation Failed")
    exit(1)

# Run the compiled program 
print("RUNNING.....")
try: 
    ret = subprocess.run([app_path],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         timeout=RUN_TIMEOUT)
    
except Exception as e:
    print("ERROR: run failed", str(e))
    exit(1)
    
output =ret.stdout.decode("utf-8")
print("OUTPUT:",output)

print("all tests passed")
exit(0)