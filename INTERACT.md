[notice] A new release of pip is available: 25.0.1 -> 25.2
[notice] To update, run: python.exe -m pip install --upgrade pip

[INFO] Rotating API key...
Traceback (most recent call last):
  File "C:\Users\LENOVO\Desktop\n8n-homework-automation\rotate_keys.py", line 102, in <module>
    rotate_keys()
    ~~~~~~~~~~~^^
  File "C:\Users\LENOVO\Desktop\n8n-homework-automation\rotate_keys.py", line 59, in rotate_keys
    env_files = glob.glob('.env.account*', include_gitignored=True)
TypeError: glob() got an unexpected keyword argument 'include_gitignored'

[INFO] Loading environment variables...

[INFO] Starting background services...

[INFO] Starting ngrok tunnel...

Waiting for 0 seconds, press a key to continue ...
[SUCCESS] ngrok tunnel started at: Your ngrok-agent version "2.3.41" is too old. The minimum supported agent version for your account is "3.7.0". Please update to a newer version with `ngrok update`, by downloading from https://ngrok.com/download, or by updating your SDK version. Paid accounts are currently excluded from minimum agent version requirements. To begin handling traffic immediately without updating your agent, upgrade to a paid plan: https://dashboard.ngrok.com/billing/subscription.

[INFO] Waiting for n8n to initialize...

Waiting for  0 seconds, press a key to continue ...

[INFO] Updating n8n webhook...
curl: (6) Could not resolve host: ngrok-agent
curl: (6) Could not resolve host: version
curl: (28) Failed to connect to 2.3.0.41 port 80 after 21036 ms: Could not connect to server
curl: (6) Could not resolve host: is
curl: (6) Could not resolve host: too
curl: (6) Could not resolve host: old.
curl: (6) Could not resolve host: The
curl: (6) Could not resolve host: minimum
curl: (6) Could not resolve host: supported
curl: (6) Could not resolve host: agent
curl: (6) Could not resolve host: version
curl: (6) Could not resolve host: for
curl: (6) Could not resolve host: your
curl: (6) Could not resolve host: account
curl: (6) Could not resolve host: is
curl: (6) Could not resolve host: 3.7.0.
curl: (6) Could not resolve host: Please
curl: (6) Could not resolve host: update
curl: (6) Could not resolve host: to
curl: (6) Could not resolve host: a
curl: (6) Could not resolve host: newer
curl: (6) Could not resolve host: version
curl: (6) Could not resolve host: with
curl: (3) URL rejected: Bad hostname
curl: (3) URL rejected: Bad hostname
curl: (6) Could not resolve host: by
curl: (6) Could not resolve host: downloading
curl: (6) Could not resolve host: from
<html>
<head><title>405 Not Allowed</title></head>
<body>
<center><h1>405 Not Allowed</h1></center>
<hr><center>openresty</center>
</body>
</html>
curl: (6) Could not resolve host: or
curl: (6) Could not resolve host: by
curl: (6) Could not resolve host: updating