AI Fan Message Responder 

An AI-powered auto-responder that generates emotionally intelligent replies to fan messages for online creators.

What It Does

- Accepts a fan message input via web form
- Uses OpenAI API to generate a warm, human-sounding reply
- Designed for creators on platforms like OnlyFans, Patreon, etc.
- Built with Flask and deployed via Replit / VS Code

Technologies Used

- Python
- Flask
- OpenAI API (chat completions)
- HTML/CSS (simple frontend)
- GitHub for version control

AI Prompt Logic

Prompt instructs the model to:
- Understand message tone (e.g. flirty, supportive, emotional)
- Respond in a creator’s voice (warm, casual, personal)
- Keep responses concise and natural

Setup Instructions

1. Clone the repo:
   git clone https://github.com/itsshivangi/novachat-ai-project.git
   cd novachat-ai-project
2. Install dependencies:
   pip install -r requirements.txt
3. Set your OpenAI API key as an environment variable:
   export OPENAI_API_KEY=your-key
4. Run the code
