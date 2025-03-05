import os
from generate_workflows import WORKFLOWS

def generate_readme():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(base_dir, "README.md")
    
    lines = []
    lines.append("# Automation Workflows Using n8n")
    lines.append("")
    lines.append("> A curated collection of **62 production-ready n8n automation workflow templates** covering Gmail, Google Gemini, Drive, Google Sheets, Telegram, WhatsApp, Slack, Notion, Airtable, PostgreSQL, and more. Ready-to-import JSON workflows designed for AI agents, career automation, sales pipelines, productivity, and DevOps.")
    lines.append("")
    lines.append("<p align=\"center\">")
    lines.append("  <img src=\"https://img.shields.io/badge/Templates-62_Workflows-blue.svg?style=for-the-badge&logo=n8n\" alt=\"62 Workflows\" />")
    lines.append("  <img src=\"https://img.shields.io/badge/n8n-v1.0+-EA4B71.svg?style=for-the-badge&logo=n8n\" alt=\"n8n Version\" />")
    lines.append("  <img src=\"https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge\" alt=\"License MIT\" />")
    lines.append("  <img src=\"https://img.shields.io/badge/AI_Native-Gemini_|_OpenAI-orange.svg?style=for-the-badge\" alt=\"AI Native\" />")
    lines.append("  <img src=\"https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=for-the-badge\" alt=\"PRs Welcome\" />")
    lines.append("</p>")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Table of Contents")
    lines.append("")
    lines.append("- [Quick Start: How to Use These Workflows](#quick-start-how-to-use-these-workflows)")
    lines.append("- [Why n8n for AI & Workflow Automation?](#why-n8n-for-ai--workflow-automation)")
    lines.append("- [Complete Workflow Directory (All 62 Workflows)](#complete-workflow-directory-all-62-workflows)")
    lines.append("- [Workflows by Category](#workflows-by-category)")
    lines.append("  - [1. Gmail & Email Automation](#1-gmail--email-automation)")
    lines.append("  - [2. AI Job & Career Agent Suite](#2-ai-job--career-agent-suite)")
    lines.append("  - [3. Lead Generation, Sales & CRM](#3-lead-generation-sales--crm)")
    lines.append("  - [4. Team Productivity & Task Automation](#4-team-productivity--task-automation)")
    lines.append("  - [5. Chatbots (Telegram & WhatsApp)](#5-chatbots-telegram--whatsapp)")
    lines.append("  - [6. Document Processing, OCR & RAG](#6-document-processing-ocr--rag)")
    lines.append("  - [7. Social Media, Content & Marketing](#7-social-media-content--marketing)")
    lines.append("  - [8. DevOps, Cloud & System Monitoring](#8-devops-cloud--system-monitoring)")
    lines.append("  - [9. E-Commerce & Finance Automation](#9-e-commerce--finance-automation)")
    lines.append("- [Setup & Deployment Guide](#setup--deployment-guide)")
    lines.append("- [Contributing](#contributing)")
    lines.append("- [License](#license)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Quick Start: How to Use These Workflows")
    lines.append("")
    lines.append("1. **Set up n8n**: Run locally via Docker (`docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n docker.n8n.io/n8nio/n8n`), install via npm (`npm install n8n -g && n8n`), or use n8n Cloud.")
    lines.append("2. **Choose a Template**: Browse the [Complete Workflow Directory](#complete-workflow-directory-all-62-workflows) below and download or copy the raw `.json` file from the `templates/` folder.")
    lines.append("3. **Import into n8n**:")
    lines.append("   - Open your n8n web interface (`http://localhost:5678`).")
    lines.append("   - Go to **Workflows → Import from File** (or press `Ctrl/Cmd + V` directly on the n8n canvas).")
    lines.append("4. **Configure Credentials**: Set up API credentials for the corresponding services (e.g., Google OAuth2 for Gmail & Drive, Gemini API Key, Telegram Bot Token, Slack Bot Token, Notion API Key).")
    lines.append("5. **Test & Activate**: Test individual nodes by clicking **Test step**, verify data flow, and toggle the workflow **Active**!")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Why n8n for AI & Workflow Automation?")
    lines.append("")
    lines.append("- **AI Native**: Seamlessly integrates Google Gemini, OpenAI, Anthropic Claude, LangChain agents, memory vectors, and local LLMs (Ollama).")
    lines.append("- **Self-Hostable & Private**: Keep sensitive enterprise data, customer records, and API credentials within your own infrastructure.")
    lines.append("- **400+ Nodes & Custom Code**: Out-of-the-box support for leading SaaS tools plus full JavaScript and Python code execution.")
    lines.append("- **Zero Vendor Lock-in**: All workflows are stored as portable JSON files that can be versioned in Git.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Complete Workflow Directory (All 62 Workflows)")
    lines.append("")
    lines.append("| # | n8n Workflow | What it does | Main Integrations | Category | Template Link |")
    lines.append("|---|--------------|--------------|-------------------|----------|---------------|")
    
    category_titles = {
        "01-email-automation": "Email Automation",
        "02-job-career-ai": "Job & Career AI",
        "03-lead-generation-crm": "Sales & CRM",
        "04-productivity-tasks": "Productivity & Tasks",
        "05-chatbots-telegram-whatsapp": "Chatbots & Messaging",
        "06-document-processing-rag": "Doc Processing & RAG",
        "07-social-media-marketing": "Social & Marketing",
        "08-devops-system-monitoring": "DevOps & Monitoring",
        "09-finance-ecommerce": "Finance & E-Commerce"
    }

    for wf in WORKFLOWS:
        rel_link = f"templates/{wf['category']}/{wf['filename']}"
        cat_name = category_titles.get(wf['category'], wf['category'])
        lines.append(f"| {wf['id']} | **{wf['name']}** | {wf['description']} | {wf['integrations']} | {cat_name} | [JSON Template]({rel_link}) |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Workflows by Category")
    lines.append("")
    
    # Category deep-dives
    categories_order = [
        ("01-email-automation", "1. Gmail & Email Automation", "Streamline inbox processing, email categorization, scheduled cold outreach, automated responses, and threat detection with AI."),
        ("02-job-career-ai", "2. AI Job & Career Agent Suite", "Full autonomous career assistant suite from job alert scraping and resume parsing to tailored application generation and tracking."),
        ("03-lead-generation-crm", "3. Lead Generation, Sales & CRM", "Automate inbound lead capture, AI lead qualification (Hot/Warm/Cold), data enrichment, CRM synchronization, and customer churn detection."),
        ("04-productivity-tasks", "4. Team Productivity & Task Automation", "Automate daily standup notes, calendar reminders, Slack-to-Notion task conversions, Jira sprint blocker alerts, and employee onboarding."),
        ("05-chatbots-telegram-whatsapp", "5. Chatbots (Telegram & WhatsApp)", "Deploy conversational AI assistants, customer support bots, translation agents, and notification channels across Telegram, WhatsApp, and Discord."),
        ("06-document-processing-rag", "6. Document Processing, OCR & RAG", "Automate Google Drive file management, PDF invoice parsing with Gemini Vision, receipt OCR, contract compliance audits, and Notion knowledge base RAG search."),
        ("07-social-media-marketing", "7. Social Media, Content & Marketing", "Automate cross-posting to LinkedIn and Twitter/X, SEO-optimized WordPress drafting, app store sentiment tracking, and deep AI web research."),
        ("08-devops-system-monitoring", "8. DevOps, Cloud & System Monitoring", "Continuous website uptime monitoring, SSL expiration checks, PostgreSQL-to-Sheets syncing, Docker container crash alerting, and Supabase webhook logging."),
        ("09-finance-ecommerce", "9. E-Commerce & Finance Automation", "Automate Shopify order fulfillment, abandoned cart recovery sequences, competitor price monitoring, automated quiz grading, and executive KPI reports.")
    ]

    for cat_key, cat_heading, cat_desc in categories_order:
        lines.append(f"### {cat_heading}")
        lines.append("")
        lines.append(f"{cat_desc}")
        lines.append("")
        lines.append("| # | Title | What it does | Integrations | Link |")
        lines.append("|---|-------|--------------|--------------|------|")
        cat_wfs = [w for w in WORKFLOWS if w['category'] == cat_key]
        for w in cat_wfs:
            rel_link = f"templates/{w['category']}/{w['filename']}"
            lines.append(f"| {w['id']} | **{w['name']}** | {w['description']} | {w['integrations']} | [Download Template]({rel_link}) |")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Setup & Deployment Guide")
    lines.append("")
    lines.append("### Recommended Environment Variables")
    lines.append("When self-hosting n8n, configure these in your `.env` file:")
    lines.append("```bash")
    lines.append("GENERIC_TIMEZONE=UTC")
    lines.append("N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true")
    lines.append("N8N_DEFAULT_BINARY_DATA_MODE=filesystem")
    lines.append("EXECUTIONS_DATA_PRUNE=true")
    lines.append("EXECUTIONS_DATA_MAX_AGE=168")
    lines.append("```")
    lines.append("")
    lines.append("### Setting Up AI Models (Gemini & OpenAI)")
    lines.append("- For **Google Gemini**: Get an API key from [Google AI Studio](https://aistudio.google.com/), then add credentials in n8n under `Google Gemini API`.")
    lines.append("- For **OpenAI / Ollama**: Add credentials under `OpenAI API` or `Ollama` for local private model execution.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Contributing")
    lines.append("")
    lines.append("Contributions are welcome! If you have built an awesome n8n automation template:")
    lines.append("1. Fork this repository.")
    lines.append("2. Export your workflow JSON from n8n (**Workflows → Download**).")
    lines.append("3. Place it in the appropriate `templates/<category>/` folder.")
    lines.append("4. Open a Pull Request with a clear description and sample use cases.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append("This repository is licensed under the [MIT License](LICENSE). Feel free to use, adapt, and deploy these workflows for personal or commercial projects.")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"README.md successfully written to {readme_path}")

if __name__ == "__main__":
    generate_readme()
