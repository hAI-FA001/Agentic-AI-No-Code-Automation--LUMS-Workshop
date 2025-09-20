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

