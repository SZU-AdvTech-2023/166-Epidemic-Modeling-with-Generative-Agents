# GABM文件：生成式代理人模型
A new modeling technique using generative AI applied to an epidemic to incorporate human reasoning and decision making.
## Installation
在本地部署了Vicuna-7B的情况下，你将不需要openai.api_key,将这一项设为空。main.py中的openai.api_base = ""设置为本地API服务器的地址，例如“http://localhost:8000/v1”

Step 1: Install the required packages using `pip install -r requirements.txt` <br>
Step 2: In main.py, Now you can replicate our results by running `python main.py --name GABM`. You can check all the available hyperparameters that you can change in detail by running `python main.py --help`. <br>
Currently, the default values of the hyperparameters are: <br>
| Hyperparameter | Value |
| --- | --- |
| name | GABM |
| contact_rate | 4 |
| infection_rate | 0.1 |
| no_init_healthy | 98 |
| no_init_infect | 2 |
| no_days | 50 |
| time_to_heal | 6 |
| no_of_runs | 1 |
| offset | 0 |
| load_from_run | 0 |

# FastChat文件：本地部署的LLM

1. navigate to the FastChat folder
```bash
cd FastChat
```
2. Install Package
```bash
pip3 install --upgrade pip  # enable PEP 660 support
pip3 install -e ".[model_worker,webui]"
```
3. Start the model controller
```
python3 −m fastchat.serve.controller
```
4. Load and run the model
```
python3 −m fastchat.serve.model_worker −−model−path lmsys/vicuna−7b 
```
If failed due to network you might need to check your https connection or download the model weights in https://huggingface.co/lmsys/vicuna-7b-v1.5 manually,then cache the files locally.

5. Start the API server 
```
python3 −m fastchat.serve.openaiapiserver −−host localhost −−port 8000
```