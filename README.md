# Agentic-AI Workshop


## Introduction

### Myths:
- AI = LLMs only
- AI = need huge training data
- AI = need expertise in DL (can use no-code)
- AI = need expertise in programming

### Objectives:
- Streamline repetitive workflows
- Prompts, RAG, Agents, RL-based Agents
- Launch and deploy


## Environment

### Git:
- Open-Source, Portfolio
- CI/CD Pipeline (testing, deployment)

### Google Colab
- No need local setup
- Configure secrets (`GOOGLE_API_KEY`)

### Gemini API
- Free LLM for generation


## Prompt Engineering

### Basic Instructions Prompting
`"Explain Quantum Computing"`

### Role-Playing Prompting
`"You are ..."`

### Constraint + Structured Prompting
`"Limit to 150 words"` <br>
`"Use academic tone"` <br>
`"List exactly 3 ..."` <br>
`"Provide in JSON format with these keys: ..."` <br>

### Few-Shot Prompting
```
"<child>: ...
<gradnparent>: ...

<child>: ..."
```

### Chain-of-Thought Prompting
`"Show your reasoning before giving the final answer"`

### Iterative Prompt Development
E.g flow: initial -> add constraints -> add role, structure, further constraints, audience -> add style, citations

### Model Limitations: Hallucinations
E.g: asking about some new toothbrush, though it doesn't exist


## Agentic AI

Basic AI: Query `-- Process -->` LLM `-- No Iteration -->` Output/Summary/Response <br>
Agentic AI: Query `-- Reason -->` Agent Logic/Plan & Act `<-- Iterate and Feedback -->` Output/Goal-Oriented Result
  - Reasoning w/ LLMs, Tools for actions

Relation with Agents: LLMs `-- Builds -->` AI Agents `-- Advances to -->` Agentic AI

### LLMs
- Language-focused, task-specific, human-guided
- basic usage: chatbots, text-generation

#### Limitations
- Stateless (no memory)
- Context window constraints

### Agents
- Autonomous, goal-oriented, environment interaction
- usage: virtual assistant, robotic vacuum

#### Hands-On - Meeting Scheduler
- Query -> Gemini -> `Select Time` -> Output
  - `Select Time` is an action

#### Limitations
- Limited knowledge
- Hallucination
- No contextual updates (new information)
- Scalability due to hard-coded logic

### Retrieval Augmented Generation
- External knowledge base
- Flow: query -> retrieve chunks -> LLM -> output

- AI Agent features + external data retrieval
- usage: customer support, research assistant, diagnostic agent, legal agent

#### Vector DB
- Store high-dimensional vectors for fast similarity-based searches
- e.g: ChromaDB, Pinecone

### RAG Agent
- Grounded in data
- Accuracy based on embedding quality

#### Hands-On - LLM+RAG Chatbot
#### RAG Agent with Voice Stack

### Agentic AI
- High autonomy, advanced reasoning, proactive
- usage: project management, self-adapting system

#### ReAct - Reason+Act
- Step-by-step, tool-usage
- Flow: Reason -> Act -> Iterate

#### Hands-On
- Multi-agent content creation crew
  - Researcher
  - Writer
  - Editor
- Tech: LangChain, CrewAI, Google Generative API, Serper Search


## Reinforcement Learning for Agentic AI
- Provide reward as feedback
- Observation, Action/Tool, Thoughts, Response

### Q-Learning Agent for a Grid-Wolrd


## No-Code Automation
- n8n, make.com, Zapier

### N8N
- Flow: Txt (Google Drive) -> Google Sheets -> GMail Summary
- Need: N8N account, Google API, Google Sheets ID, Google Drive ID, GMail API
- Steps:
  - Enable APIs (Google Sheets, Drive and GMail)
  - Add OAuth screen (under Credentials)
  - Add OAuth client (with Web app option)
  - Link Google OAuth and N8N:
    - Create new workflow in N8N
    - Add Google Drive or any service (to get to credentials screen)
    - Will ask for Credentials, so create new Credentials
    - Use its Redirect URI in Google OAuth client
    - Save and Use OAuth client's information in n8n's credential (client ID and secret)
  - (Maybe Optional) Go to Data Access and add these Scopes: `	.../auth/gmail.send`, `.../auth/drive`, `.../auth/drive.file`, `.../auth/drive.metadata.readonly`, `../auth/gmail.readonly`, `.../auth/drive.readonly`, `.../auth/docs`, `.../auth/drive.metadata`, `.../auth/spreadsheets`, `.../auth/spreadsheets.readonly`
  - Go to Audience, add a user under Test Users, enter your email and save
  - Go back to the n8n credentials screen and now click on Sign in With Google and follow the steps
  - Create a new Google Sheet and note the ID from the URL (between `/d` and `/edit`)
  - Create a new folder in Google Drive, make it public and note the ID from the URL (all after `/folders`)
  - Import the JSON workflow for no-code automation
  - Go to each node, then:
    - Check the credentials
    - Sign in with Google
    - Check the file/folder IDs


  ## Rapid Prototyping
  - Replit, Cursor, Claude, etc

  ### Educational Content Generator
  - Tech: Render, Streamlit, Claude
