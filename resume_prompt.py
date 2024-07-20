import openai
import json


def parse_resume_to_json(resume_text):
    prompt = f"""
    You are an AI assistant. I will provide you with the text content of a resume. Your task is to parse this content and convert it into a structured JSON format.

    Here is the resume content:

    ---
    {resume_text}
    ---

    Please convert the above resume content into the following JSON structure:

    {{
      "name": "Bharat Singh",
      "contact": {{
        "address": "Sector 2, Faridabad, 2115500036",
        "email": "bharat.singh_cs.aiml21@gla.ac.in",
        "phone": "+91 9582273527"
      }},
      "education": [
        {{
          "degree": "Bachelor of Technology in Computer Science with spec. in AIML",
          "institution": "GLA University, Mathura",
          "cpi": 8.09,
          "graduation_date": "June 2025"
        }},
        {{
          "degree": "Intermediate",
          "institution": "DAV Public School, Faridabad",
          "percentage": 88.88,
          "graduation_date": "May 2021"
        }},
        {{
          "degree": "High School",
          "institution": "DAV Public School, Faridabad",
          "percentage": 86.8,
          "graduation_date": "May 2019"
        }}
      ],
      "internships": [
        {{
          "title": "Job Oriented Value Added Course",
          "company": "GLA University, Mathura",
          "duration": "June 2023 – July 2023",
          "role": "Trainee",
          "tasks": [
            "Learnt basics of DevOps using AWS",
            "Created a project implementing various AWS tools"
          ]
        }}
      ],
      "projects": [
        {{
          "title": "Air Quality Monitoring System",
          "date": "Mar 2023",
          "technologies": ["Python", "Logistic Regression", "Decision Tree", "Random Forest"],
          "description": "Built an AI-based application that alerts the authorities and helps check the condition of the air."
        }},
        {{
          "title": "Pneumonia Detection",
          "technologies": ["Python", "CNN", "Data Augmentation"],
          "description": "Built a machine learning model that detects the presence of pneumonia by analyzing X-rays."
        }},
        {{
          "title": "My Portfolio Link",
          "technologies": ["HTML", "CSS", "Javascript", "Bootstrap"],
          "description": "Created a responsive webpage of my portfolio."
        }}
      ],
      "skills": {{
        "technical": {{
          "core": ["Object Oriented Programming", "Machine Learning"],
          "languages": ["Java(Core)", "Python", "HTML", "CSS", "JavaScript", "SQL (MySQL)"],
          "libraries": ["React.js", "Numpy", "Pandas"],
          "developer_tools": ["Visual Studio Code"]
        }},
        "professional": ["Effective Analytical Skills", "Problem Solving Skills", "Leadership Skills"]
      }},
      "achievements": [
        "President Of Wrestling Club GLAU"
      ],
      "extra_curricular": [
        "Wrestling Gold Medal Aagaaz 2024(GLA)",
        "Inter State Kabaddi Silver Medal (Kreeda Bharti, Mathura) 2024",
        "IIT BHU Hammer Throw Bronze Medal 2023",
        "Aagaaz Tug Of War Gold Medal (GLA University, 2024)",
        "Organised various Inter University and Intra University Sports Events in GLAU"
      ],
      "declaration": "I hereby declare that all the above mentioned information is true and correct to the best of my knowledge."
    }}
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        temperature=0
    )

    return json.loads(response.choices[0].text.strip())

# Example usage:
resume_text = """
BHARAT SINGH
Sector 2 ● Faridabad, 2115500036
bharat.singh_cs.aiml21@gla.ac.in ● +91 9582273527

EDUCATION
Bachelor of Technology in Computer Science with spec. in AIML, GLA University, Mathura (CPI-8.09) June 2025
Intermediate, DAV Public School, Faridabad (88.88%) May 2021
High School, DAV Public School, Faridabad (86.8%) May 2019

INTERNSHIP/TRAINING EXPERIENCE
Job Oriented Value Added Course, GLA University, Mathura June 2023 – July 2023
Trainee
Learnt basics of DevOps using AWS
Post completing the training, created a Project, Implementing various AWS tools.

PROJECTS
Air Quality Monitoring System Mar 2023
Python, Logistic Regression, Decision Tree, Random Forest
Built an AI based Application that “Alert” the Authorities and also help to check the condition of Air.
Created using Python, Kaggle, ML Libraries.

Pneumonia Detection
Python, CNN, Data Augmentation
Build a Machine Learning model that detects the presence of pneumonia by analyzing the X-Ray.
Efficient for Healthcare Industry.
Created using Python, Kaggle, and ML Libraries.

My Portfolio Link
HTML, CSS, Javascript, Bootstrap
Create a responsive webpage of my portfolio.

SKILLS
Technical Skills
Core: Object Oriented Programing, Machine Learning
Languages: Java(Core), Python, HTML, CSS, JavaScript, SQL (MySQL)
Libraries: React.js, Numpy, Pandas
Developer Tools: Visual Studio Code

Professional Skills
Effective Analytical Skills
Problem Solving Skills
Leadership Skills

ACHIEVEMENTS
President Of Wrestling Club GLAU

EXTRA/CO-CURRICULAR ACTIVITIES
Wrestling Gold Medal Aagaaz 2024(GLA).
Inter State Kabaddi Silver Medal (Kreeda Bharti, Mathura) 2024
IIT BHU Hammer Throw Bronze Medal 2023
Aagaaz Tug Of War Gold Medal (GLA University, 2024).
Organised various Inter University and Intra University Sports Events in GLAU.

DECLARATION
I hereby declare that all the above mentioned information is true and correct to the best of my knowledge.
"""

parsed_resume = parse_resume_to_json(resume_text)
print(json.dumps(parsed_resume, indent=2))
