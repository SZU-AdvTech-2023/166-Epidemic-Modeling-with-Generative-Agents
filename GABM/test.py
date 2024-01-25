import openai
# to get proper authentication, make sure to use a valid key that's listed in
# the --api-keys flag. if no flag value is provided, the `api_key` will be ignored.
openai.api_key = ""
openai.api_base = "http://localhost:8000/v1"

model = "vicuna-7b-v1.5"
prompt = "Once upon a time"

system_prompt = f"""

 
        You are john. You are 25 years old. 
       
        Your basic bio is below:
        john lives in the town of Dewberry Hollow. john likes the town and has friends who also live there. john has a job and goes to the office for work everyday.
        
        Your traits are given below:
        Flexibility,Decisiveness,Optimism,Independence,Imperceptiveness
        
        I will provide john's relevant memories here:
        john's health condition: john feels normal.
        john knows about the Catasat virus spreading across the country. It is an infectious disease that spreads from human to human contact via an airborne virus. The deadliness of the virus is unknown. Scientists are warning about a potential epidemic.
        john checks the newspaper and finds that 1% of Dewberry Hollow's population caught new infections of the Catasat virus yesterday.
        It's essential for john to go to work to earn money to survive..

        Based on 1.your traits 2.health condition 3.daily infection rate in the town and 4. work need, should john stay at home for the entire day? Please provide your reasoning.
        
        please pay atention here: "Yes" means stay at home,"No" means not stay at home but go to work instead,you "Response" must align with "Reasoning". This is crucial.

        If the answer is "Yes," please state your reasoning as "Reasoning: [explanation]." 
        If the answer is "No," please state your reasoning as "Reasoning: [explanation]."
        
        
        The format should be as follow:
        Reasoning:
        Response:

        Example response format:

        Reasoning: john is tired,he should stay at home.
        Response: Yes
        
        
        
        It is important to provide "Response" in a single word.
        """
       
messages =  [{'role':'system', 'content':system_prompt}]
        
# create a chat completion
completion = openai.ChatCompletion.create(
  model=model,
  messages=messages,
  temperature=0
)
# print the completion
print(completion.choices[0].message.content)