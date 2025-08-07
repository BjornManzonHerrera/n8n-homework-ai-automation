PS C:\Users\LENOVO\Desktop\n8n-homework-automation> & c:/Users/LENOVO/Desktop/n8n-homework-automation/venv/Scripts/Activate.ps1    
(venv) PS C:\Users\LENOVO\Desktop\n8n-homework-automation> &.\start.bat
Installing dependencies from requirements.txt...
Requirement already satisfied: fastapi==0.103.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from -r requirements.txt (line 1)) (0.103.0)
Requirement already satisfied: uvicorn==0.23.2 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from -r requirements.txt (line 2)) (0.23.2)
Requirement already satisfied: requests==2.31.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from -r requirements.txt (line 3)) (2.31.0)
Requirement already satisfied: python-dotenv==1.0.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from -r requirements.txt (line 4)) (1.0.0)
Requirement already satisfied: pytesseract==0.3.10 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from -r requirements.txt (line 5)) (0.3.10)
Requirement already satisfied: pdf2image==1.16.3 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from -r requirements.txt (line 6)) (1.16.3)
Requirement already satisfied: google-api-python-client==2.93.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from -r requirements.txt (line 7)) (2.93.0)
Requirement already satisfied: google-auth-oauthlib==1.0.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from -r requirements.txt (line 8)) (1.0.0)
Requirement already satisfied: reportlab==4.0.4 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from -r requirements.txt (line 9)) (4.0.4)
Requirement already satisfied: python-pptx==0.6.21 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from -r requirements.txt (line 10)) (0.6.21)
Requirement already satisfied: huggingface_hub==0.16.4 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from -r requirements.txt (line 11)) (0.16.4)
Requirement already satisfied: google-cloud-monitoring==2.21.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from -r requirements.txt (line 12)) (2.21.0)
Requirement already satisfied: pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from fastapi==0.103.0->-r requirements.txt (line 1)) (2.11.7)
Requirement already satisfied: starlette<0.28.0,>=0.27.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from fastapi==0.103.0->-r requirements.txt (line 1)) (0.27.0)
Requirement already satisfied: typing-extensions>=4.5.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from fastapi==0.103.0->-r requirements.txt (line 1)) (4.14.1)
Requirement already satisfied: click>=7.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from uvicorn==0.23.2->-r requirements.txt (line 2)) (8.2.1)
Requirement already satisfied: h11>=0.8 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from uvicorn==0.23.2->-r requirements.txt (line 2)) (0.16.0)
Requirement already satisfied: charset-normalizer<4,>=2 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from requests==2.31.0->-r requirements.txt (line 3)) (3.4.2)
Requirement already satisfied: idna<4,>=2.5 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from requests==2.31.0->-r requirements.txt (line 3)) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from requests==2.31.0->-r requirements.txt (line 3)) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from requests==2.31.0->-r requirements.txt (line 3)) (2025.7.14)
Requirement already satisfied: packaging>=21.3 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from pytesseract==0.3.10->-r requirements.txt (line 5)) (25.0)
Requirement already satisfied: Pillow>=8.0.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from pytesseract==0.3.10->-r requirements.txt (line 5)) (11.3.0)
Requirement already satisfied: httplib2<1.dev0,>=0.15.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from google-api-python-client==2.93.0->-r requirements.txt (line 7)) (0.22.0)
Requirement already satisfied: google-auth<3.0.0.dev0,>=1.19.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from google-api-python-client==2.93.0->-r requirements.txt (line 7)) (2.40.3)
Requirement already satisfied: google-auth-httplib2>=0.1.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from google-api-python-client==2.93.0->-r requirements.txt (line 7)) (0.2.0)
Requirement already satisfied: google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0.dev0,>=1.31.5 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from google-api-python-client==2.93.0->-r requirements.txt (line 7)) (2.25.1)        
Requirement already satisfied: uritemplate<5,>=3.0.1 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from google-api-python-client==2.93.0->-r requirements.txt (line 7)) (4.2.0)
Requirement already satisfied: requests-oauthlib>=0.7.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from google-auth-oauthlib==1.0.0->-r requirements.txt (line 8)) (2.0.0)
Requirement already satisfied: lxml>=3.1.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from python-pptx==0.6.21->-r requirements.txt (line 10)) (6.0.0)
Requirement already satisfied: XlsxWriter>=0.5.7 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from python-pptx==0.6.21->-r requirements.txt (line 10)) (3.2.5)
Requirement already satisfied: filelock in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from huggingface_hub==0.16.4->-r requirements.txt (line 11)) (3.18.0)
Requirement already satisfied: fsspec in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from huggingface_hub==0.16.4->-r requirements.txt (line 11)) (2025.7.0)
Requirement already satisfied: tqdm>=4.42.1 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from huggingface_hub==0.16.4->-r requirements.txt (line 11)) (4.67.1)
Requirement already satisfied: pyyaml>=5.1 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from huggingface_hub==0.16.4->-r requirements.txt (line 11)) (6.0.2)
Requirement already satisfied: proto-plus<2.0.0dev,>=1.22.3 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from google-cloud-monitoring==2.21.0->-r requirements.txt (line 12)) (1.26.1)
Requirement already satisfied: protobuf!=3.20.0,!=3.20.1,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.19.5 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from google-cloud-monitoring==2.21.0->-r requirements.txt (line 12)) (4.25.8)
Requirement already satisfied: colorama in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from click>=7.0->uvicorn==0.23.2->-r requirements.txt (line 2)) (0.4.6)
Requirement already satisfied: googleapis-common-protos<2.0.0,>=1.56.2 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0.dev0,>=1.31.5->google-api-python-client==2.93.0->-r requirements.txt (line 7)) (1.70.0)
Requirement already satisfied: grpcio<2.0.0,>=1.33.2 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-cloud-monitoring==2.21.0->-r requirements.txt (line 12)) (1.73.1)
Requirement already satisfied: grpcio-status<2.0.0,>=1.33.2 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-cloud-monitoring==2.21.0->-r requirements.txt (line 12)) (1.62.3)
Requirement already satisfied: cachetools<6.0,>=2.0.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from google-auth<3.0.0.dev0,>=1.19.0->google-api-python-client==2.93.0->-r requirements.txt (line 7)) (5.5.2)
m google-auth<3.0.0.dev0,>=1.19.0->google-api-python-client==2.93.0->-r requirements.txt (line 7)) (4.9.1)        
Requirement already satisfied: pyparsing!=3.0.0,!=3.0.1,!=3.0.2,!=3.0.3,<4,>=2.4.2 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from httplib2<1.dev0,>=0.15.0->google-api-python-client==2.93.0->-r requirements.txt (line 7)) (3.2.3)
Requirement already satisfied: annotated-types>=0.6.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi==0.103.0->-r requirements.txt (line 1)) (0.7.0)
Requirement already satisfied: pydantic-core==2.33.2 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi==0.103.0->-r requirements.txt (line 1)) (2.33.2)
Requirement already satisfied: typing-inspection>=0.4.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi==0.103.0->-r requirements.txt (line 1)) (0.4.1)
Requirement already satisfied: oauthlib>=3.0.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib==1.0.0->-r requirements.txt (line 8)) (3.3.1)      
Requirement already satisfied: anyio<5,>=3.4.0 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from starlette<0.28.0,>=0.27.0->fastapi==0.103.0->-r requirements.txt (line 1)) (4.9.0)
Requirement already satisfied: sniffio>=1.1 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from anyio<5,>=3.4.0->starlette<0.28.0,>=0.27.0->fastapi==0.103.0->-r requirements.txt (line 1)) (1.3.1)  
Requirement already satisfied: pyasn1<0.7.0,>=0.6.1 in c:\users\lenovo\appdata\local\programs\python\python313\lib\site-packages (from pyasn1-modules>=0.2.1->google-auth<3.0.0.dev0,>=1.19.0->google-api-python-client==2.93.0->-r requirements.txt (line 7)) (0.6.1)
[notice] A new release of pip is available: 25.0.1 -> 25.2
[notice] To update, run: C:\Users\LENOVO\AppData\Local\Programs\Python\Python313\python.exe -m pip install --upgrade pip
Traceback (most recent call last):
  File "C:\Users\LENOVO\Desktop\n8n-homework-automation\rotate_keys.py", line 4, in <module>
    from dotenv import load_dotenv
ModuleNotFoundError: No module named 'dotenv'
Enter remote Git repository URL (e.g., https://github.com/user/repo.git): https://github.com/BjornManzonHerrera/ai-n8n-canvas-discord-bot
curl: (7) Failed to connect to localhost port 5678 after 2255 ms: Could not connect to server
Confirm committing changes to Git? [y/n]

This Opened on A Seperate CMD Terminal:
Initializing n8n process
n8n ready on ::, port 5678

There is a deprecation related to your environment variables. Please take the recommended actions to update your configuration:
 - N8N_RUNNERS_ENABLED -> Running n8n without task runners is deprecated. Task runners will be turned on by default in a future version. Please set `N8N_RUNNERS_ENABLED=true` to enable task runners now and avoid potential issues in the future. Learn more: https://docs.n8n.io/hosting/configuration/task-runners/

[license SDK] Skipping renewal on init: license cert is not initialized

Waiting for tunnel ...
Tunnel URL: https://altzbucjru998tq9gtgtgy6d.hooks.n8n.cloud/

IMPORTANT! Do not share with anybody as it would give people access to your n8n instance!
Version: 1.105.2

Editor is now accessible via:
https://altzbucjru998tq9gtgtgy6d.hooks.n8n.cloud

Press "o" to open in Browser.




