# Automation Workflows Using n8n

> A curated collection of **62 production-ready n8n automation workflow templates** covering Gmail, Google Gemini, Drive, Google Sheets, Telegram, WhatsApp, Slack, Notion, Airtable, PostgreSQL, and more. Ready-to-import JSON workflows designed for AI agents, career automation, sales pipelines, productivity, and DevOps.

<p align="center">
  <img src="https://img.shields.io/badge/Templates-62_Workflows-blue.svg?style=for-the-badge&logo=n8n" alt="62 Workflows" />
  <img src="https://img.shields.io/badge/n8n-v1.0+-EA4B71.svg?style=for-the-badge&logo=n8n" alt="n8n Version" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License MIT" />
  <img src="https://img.shields.io/badge/AI_Native-Gemini_|_OpenAI-orange.svg?style=for-the-badge" alt="AI Native" />
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=for-the-badge" alt="PRs Welcome" />
</p>

---

## Table of Contents

- [Quick Start: How to Use These Workflows](#quick-start-how-to-use-these-workflows)
- [Why n8n for AI & Workflow Automation?](#why-n8n-for-ai--workflow-automation)
- [Complete Workflow Directory (All 62 Workflows)](#complete-workflow-directory-all-62-workflows)
- [Workflows by Category](#workflows-by-category)
  - [1. Gmail & Email Automation](#1-gmail--email-automation)
  - [2. AI Job & Career Agent Suite](#2-ai-job--career-agent-suite)
  - [3. Lead Generation, Sales & CRM](#3-lead-generation-sales--crm)
  - [4. Team Productivity & Task Automation](#4-team-productivity--task-automation)
  - [5. Chatbots (Telegram & WhatsApp)](#5-chatbots-telegram--whatsapp)
  - [6. Document Processing, OCR & RAG](#6-document-processing-ocr--rag)
  - [7. Social Media, Content & Marketing](#7-social-media-content--marketing)
  - [8. DevOps, Cloud & System Monitoring](#8-devops-cloud--system-monitoring)
  - [9. E-Commerce & Finance Automation](#9-e-commerce--finance-automation)
- [Setup & Deployment Guide](#setup--deployment-guide)
- [Contributing](#contributing)
- [License](#license)

---

## Quick Start: How to Use These Workflows

1. **Set up n8n**: Run locally via Docker (`docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n docker.n8n.io/n8nio/n8n`), install via npm (`npm install n8n -g && n8n`), or use n8n Cloud.
2. **Choose a Template**: Browse the [Complete Workflow Directory](#complete-workflow-directory-all-62-workflows) below and download or copy the raw `.json` file from the `templates/` folder.
3. **Import into n8n**:
   - Open your n8n web interface (`http://localhost:5678`).
   - Go to **Workflows → Import from File** (or press `Ctrl/Cmd + V` directly on the n8n canvas).
4. **Configure Credentials**: Set up API credentials for the corresponding services (e.g., Google OAuth2 for Gmail & Drive, Gemini API Key, Telegram Bot Token, Slack Bot Token, Notion API Key).
5. **Test & Activate**: Test individual nodes by clicking **Test step**, verify data flow, and toggle the workflow **Active**!

---

## Why n8n for AI & Workflow Automation?

- **AI Native**: Seamlessly integrates Google Gemini, OpenAI, Anthropic Claude, LangChain agents, memory vectors, and local LLMs (Ollama).
- **Self-Hostable & Private**: Keep sensitive enterprise data, customer records, and API credentials within your own infrastructure.
- **400+ Nodes & Custom Code**: Out-of-the-box support for leading SaaS tools plus full JavaScript and Python code execution.
- **Zero Vendor Lock-in**: All workflows are stored as portable JSON files that can be versioned in Git.

---

## Complete Workflow Directory (All 62 Workflows)

| # | n8n Workflow | What it does | Main Integrations | Category | Template Link |
|---|--------------|--------------|-------------------|----------|---------------|
| 1 | **Multi-Customer Email Sender** | Send personalized emails to 20–100 customers from Google Sheets with dynamic templating and delay throttling. | Gmail + Google Sheets | Email Automation | [JSON Template](templates/01-email-automation/01-Multi-Customer-Email-Sender.json) |
| 2 | **AI Job Application Generator** | Take a Job Description (JD) via Webhook/Form → generate tailored resume bullet points + custom cover letter via Gemini and export to Drive. | Gemini + Gmail + Google Drive | Job & Career AI | [JSON Template](templates/02-job-career-ai/02-AI-Job-Application-Generator.json) |
| 3 | **Auto Job Application Tracker** | Track applied jobs automatically by listening to Gmail application confirmations and appending details to Google Sheets & Notion. | Gmail + Google Sheets + Notion | Job & Career AI | [JSON Template](templates/02-job-career-ai/03-Auto-Job-Application-Tracker.json) |
| 4 | **Job Alert AI Match** | Read incoming LinkedIn/Indeed job alerts from Gmail, extract role details, and score them against your resume using Gemini AI. | Gmail + Google Gemini | Job & Career AI | [JSON Template](templates/02-job-career-ai/04-Job-Alert-AI-Match.json) |
| 5 | **AI Auto Email Reply** | Classify incoming emails (inquiry, support, spam, feedback) and generate contextual, professional replies using Google Gemini. | Gmail + Google Gemini | Email Automation | [JSON Template](templates/01-email-automation/05-AI-Auto-Email-Reply.json) |
| 6 | **Meeting Reminder Bot** | Send timely reminders to Telegram and Slack channels 15 minutes before scheduled Google Calendar meetings. | Google Calendar + Telegram + Slack | Productivity & Tasks | [JSON Template](templates/04-productivity-tasks/06-Meeting-Reminder-Bot.json) |
| 7 | **Form to Email Automation** | New website form submission triggers instant personalized confirmation email and notifies team. | Google Forms / Webhook + Gmail | Email Automation | [JSON Template](templates/01-email-automation/07-Form-To-Email-Automation.json) |
| 8 | **Customer Lead Collector** | Capture leads from landing pages via Webhooks, validate emails, and save them automatically to Google Sheets & CRM. | Webhook + Google Sheets | Sales & CRM | [JSON Template](templates/03-lead-generation-crm/08-Customer-Lead-Collector.json) |
| 9 | **AI Lead Qualification** | Score leads as Hot/Warm/Cold using Gemini AI based on company size, budget, and message intent. | Google Sheets + Google Gemini | Sales & CRM | [JSON Template](templates/03-lead-generation-crm/09-AI-Lead-Qualification.json) |
| 10 | **Daily Email Summary** | Summarize important received emails every evening using Gemini AI and deliver an executive briefing to your inbox. | Gmail + Google Gemini | Email Automation | [JSON Template](templates/01-email-automation/10-Daily-Email-Summary.json) |
| 11 | **Telegram AI Assistant** | Interactive Telegram bot powered by Google Gemini that answers questions, maintains context, and assists with daily queries. | Telegram + Google Gemini | Chatbots & Messaging | [JSON Template](templates/05-chatbots-telegram-whatsapp/11-Telegram-AI-Assistant.json) |
| 12 | **Invoice Reminder** | Detect unpaid invoices from Google Sheets and automatically dispatch friendly payment reminders via Gmail. | Google Sheets + Gmail | Email Automation | [JSON Template](templates/01-email-automation/12-Invoice-Reminder.json) |
| 13 | **Google Drive File Organizer** | Automatically classify and organize uploaded files into designated Drive folders (Invoices, Resumes, Contracts, Media) using Gemini AI. | Google Drive + Google Gemini | Doc Processing & RAG | [JSON Template](templates/06-document-processing-rag/13-Google-Drive-File-Organizer.json) |
| 14 | **Resume Analyzer** | Upload a candidate resume PDF to Drive → extract skills, years of experience, work history, and keywords into a structured JSON record. | Google Drive + Google Gemini | Job & Career AI | [JSON Template](templates/02-job-career-ai/14-Resume-Analyzer.json) |
| 15 | **JD vs Resume Matcher** | Compare job descriptions directly against a candidate resume and produce an ATS match percentage with gap analysis. | Google Gemini + Webhook | Job & Career AI | [JSON Template](templates/02-job-career-ai/15-JD-vs-Resume-Matcher.json) |
| 16 | **AI Cover Letter Generator** | Provide JD + Company name → produce customized, highly compelling cover letter saved directly to Google Drive as a Google Doc. | Google Gemini + Google Drive | Job & Career AI | [JSON Template](templates/02-job-career-ai/16-AI-Cover-Letter-Generator.json) |
| 17 | **Customer Feedback Analyzer** | Analyze incoming customer reviews & feedback, classify sentiment (positive, neutral, negative), and tag key issue areas. | Google Sheets + Google Gemini | Sales & CRM | [JSON Template](templates/03-lead-generation-crm/17-Customer-Feedback-Analyzer.json) |
| 18 | **Slack Task Creator** | Detect action items and task requests in Slack messages or reaction emojis and create tasks automatically in Notion. | Slack + Notion | Productivity & Tasks | [JSON Template](templates/04-productivity-tasks/18-Slack-Task-Creator.json) |
| 19 | **News AI Summary to Telegram** | Fetch top news via RSS / News API, summarize the top 5 stories with Google Gemini, and broadcast an elegant morning digest to Telegram. | RSS/API + Google Gemini + Telegram | Chatbots & Messaging | [JSON Template](templates/05-chatbots-telegram-whatsapp/19-News-AI-Summary-Telegram.json) |
| 20 | **Complete AI Job Agent** | End-to-end career copilot: Find JD → Analyze requirements → Tailor resume → Draft cover letter → Request human approval → Log to Sheets. | Gmail + Google Gemini + Google Drive + Google Sheets | Job & Career AI | [JSON Template](templates/02-job-career-ai/20-Complete-AI-Job-Agent.json) |
| 21 | **AI Phishing & Security Email Screener** | Scan suspicious incoming emails with Gemini AI to detect phishing, spoofing, and malicious links, quarantining threats automatically. | Gmail + Google Gemini + Slack | Email Automation | [JSON Template](templates/01-email-automation/21-AI-Phishing-Security-Email-Screener.json) |
| 22 | **YouTube Video Transcriber & AI Summarizer** | Download YouTube captions, summarize key points and timestamps with Gemini AI, and save structured notes into Notion. | YouTube + Google Gemini + Notion | Doc Processing & RAG | [JSON Template](templates/06-document-processing-rag/22-YouTube-Video-Transcriber-AI-Summarizer.json) |
| 23 | **WhatsApp Business Customer Support Bot** | Receive WhatsApp Cloud messages, retrieve FAQ answers with Gemini, and provide real-time automated conversational support. | WhatsApp Business Cloud + Google Gemini + Google Sheets | Chatbots & Messaging | [JSON Template](templates/05-chatbots-telegram-whatsapp/23-WhatsApp-Business-Customer-Support-Bot.json) |
| 24 | **PostgreSQL to Google Sheets Automated Sync** | Daily scheduled query pulling latest revenue and customer analytics from PostgreSQL and upserting directly into Google Sheets dashboards. | PostgreSQL + Google Sheets + Cron | DevOps & Monitoring | [JSON Template](templates/08-devops-system-monitoring/24-PostgreSQL-To-Google-Sheets-Automated-Sync.json) |
| 25 | **Discord Community Welcome & Role Assigner** | Automatically send a customized welcome DM and assign initial roles to new Discord community members via webhook. | Discord + Webhook | Chatbots & Messaging | [JSON Template](templates/05-chatbots-telegram-whatsapp/25-Discord-Community-Welcome-Role-Assigner.json) |
| 26 | **Automated PDF Invoice Data Extractor** | Extract vendor name, invoice date, line items, tax, and total amount from PDF invoices using Gemini Vision and store into Airtable. | Google Drive + Gemini Vision + Airtable | Doc Processing & RAG | [JSON Template](templates/06-document-processing-rag/26-Automated-PDF-Invoice-Data-Extractor.json) |
| 27 | **GitHub Issue to Notion Task Synchronizer** | Automatically mirror new GitHub issues and bug reports into your Notion engineering backlog with tags, labels, and links. | GitHub + Notion | Productivity & Tasks | [JSON Template](templates/04-productivity-tasks/27-GitHub-Issue-To-Notion-Task-Synchronizer.json) |
| 28 | **Website Uptime & SSL Expiry Monitor** | Ping critical website endpoints and check SSL certificates every 5 minutes; send immediate Telegram alerts if downtime occurs. | HTTP Request + Telegram Alert + Cron | DevOps & Monitoring | [JSON Template](templates/08-devops-system-monitoring/28-Website-Uptime-SSL-Expiry-Monitor.json) |
| 29 | **Social Media Cross-Poster** | Write post in Google Sheets → automatically publish across LinkedIn, Twitter/X, and Buffer simultaneously with asset attachments. | Google Sheets + LinkedIn + Twitter/X + Buffer | Social & Marketing | [JSON Template](templates/07-social-media-marketing/29-Social-Media-Cross-Poster.json) |
| 30 | **Google Calendar to Slack Daily Standup Notifier** | Extract today's agenda, milestones, and meeting links from Google Calendar at 9 AM and broadcast formatted agenda to team Slack channel. | Google Calendar + Slack | Productivity & Tasks | [JSON Template](templates/04-productivity-tasks/30-Google-Calendar-To-Slack-Daily-Standup-Notifier.json) |
| 31 | **App Store Review Sentiment Monitor** | Fetch iOS App Store and Google Play reviews via RSS, score sentiment with Gemini, and alert product team on negative feedback. | RSS + Google Gemini + Slack | Social & Marketing | [JSON Template](templates/07-social-media-marketing/31-App-Store-Review-Sentiment-Monitor.json) |
| 32 | **Stripe Failed Payment Recovery Dunning Bot** | Catch Stripe charge.failed webhooks, notify finance team in Slack, and send automated polite card update request to customer. | Stripe + Gmail + Slack | Email Automation | [JSON Template](templates/01-email-automation/32-Stripe-Failed-Payment-Recovery-Dunning-Bot.json) |
| 33 | **Notion Database Auto-Backup to Drive** | Weekly automated backup of critical Notion databases exported to JSON/CSV and saved in organized Google Drive backup archives. | Notion API + Google Drive + Cron | Doc Processing & RAG | [JSON Template](templates/06-document-processing-rag/33-Notion-Database-Auto-Backup-To-Drive.json) |
| 34 | **Airtable B2B Lead Enrichment Pipeline** | When a new lead is added to Airtable, enrich company revenue, employee count, and CEO contact via Hunter/Clearbit APIs. | Airtable + Hunter/Clearbit API + Google Sheets | Sales & CRM | [JSON Template](templates/03-lead-generation-crm/34-Airtable-B2B-Lead-Enrichment-Pipeline.json) |
| 35 | **AI Audio Meeting Notes & Action Item Extractor** | Upload recorded meeting audio to Drive → transcribe with Whisper/Gemini → extract key action items and create Notion tasks. | Drive Audio + Whisper/Gemini + Notion | Productivity & Tasks | [JSON Template](templates/04-productivity-tasks/35-AI-Audio-Meeting-Notes-Action-Item-Extractor.json) |
| 36 | **Shopify New Order Fulfillment & SMS Notifier** | Trigger on new paid Shopify orders, record in fulfillment Google Sheets, and send tracking SMS to customer via Twilio. | Shopify + Twilio + Google Sheets | Finance & E-Commerce | [JSON Template](templates/09-finance-ecommerce/36-Shopify-New-Order-Fulfillment-SMS-Notifier.json) |
| 37 | **Competitor Price Monitor & Alert** | Scrape competitor product pages every 6 hours, track pricing fluctuations in Google Sheets, and email alerts on price drops. | HTTP Scraping + HTML Node + Sheets + Gmail | Finance & E-Commerce | [JSON Template](templates/09-finance-ecommerce/37-Competitor-Price-Monitor-Alert.json) |
| 38 | **Telegram Multi-Language Translation Bot** | Instant Telegram translation bot: detects language of incoming messages or audio and returns accurate translations in 50+ languages. | Telegram + Google Gemini Translator | Chatbots & Messaging | [JSON Template](templates/05-chatbots-telegram-whatsapp/38-Telegram-Multi-Language-Translation-Bot.json) |
| 39 | **Zendesk Critical Ticket Escalator** | Detect VIP or urgent priority tickets in Zendesk, immediately page on-call engineers via Slack and SMS escalation. | Zendesk + Slack On-Call + Twilio SMS | Chatbots & Messaging | [JSON Template](templates/05-chatbots-telegram-whatsapp/39-Zendesk-Critical-Ticket-Escalator.json) |
| 40 | **WordPress Auto-Publisher & SEO Optimizer** | Generate SEO-optimized blog posts with Gemini AI from keyword briefs, format headings & meta tags, and publish as WordPress drafts. | Gemini + WordPress API + Yoast | Social & Marketing | [JSON Template](templates/07-social-media-marketing/40-WordPress-Auto-Publisher-SEO-Optimizer.json) |
| 41 | **Expense Receipt Scanner & Categorizer** | Snap a receipt image via Telegram or Drive → parse merchant, category, date, and amount with Gemini Vision → log into expense sheet. | Telegram/Drive + Gemini Vision + Google Sheets | Doc Processing & RAG | [JSON Template](templates/06-document-processing-rag/41-Expense-Receipt-Scanner-Categorizer.json) |
| 42 | **RSS Feed to Newsletter Draft Generator** | Collect weekly industry articles, generate curated newsletter commentary with Gemini AI, and draft Mailchimp / Gmail campaigns. | RSS + Google Gemini + Gmail / Mailchimp | Email Automation | [JSON Template](templates/01-email-automation/42-RSS-Feed-To-Newsletter-Draft-Generator.json) |
| 43 | **Supabase Database Change Webhook to Slack** | Listen to Supabase Database Webhooks on insert/update in critical tables (e.g., users, subscriptions) and alert Slack with change diff. | Supabase + Slack Notification | DevOps & Monitoring | [JSON Template](templates/08-devops-system-monitoring/43-Supabase-Database-Change-Webhook-To-Slack.json) |
| 44 | **Google Forms Quiz Auto-Grader & Certificate Generator** | Automatically grade student quiz submissions from Google Forms, calculate scores, generate PDF certificates, and email recipients. | Forms + Sheets + PDF + Gmail | Finance & E-Commerce | [JSON Template](templates/09-finance-ecommerce/44-Google-Forms-Quiz-Auto-Grader-Certificate-Generator.json) |
| 45 | **Customer Churn Risk Analyzer** | Analyze usage metrics, ticket frequency, and login patterns to identify churn risk and trigger customer success retention playbooks. | Sheets/Postgres + Google Gemini + Slack Alert | Sales & CRM | [JSON Template](templates/03-lead-generation-crm/45-Customer-Churn-Risk-Analyzer.json) |
| 46 | **Automated Weekly KPI Analytics Report** | Aggregate weekly revenue, customer acquisition cost, active users, and conversions into an executive Gemini AI briefing. | Sheets + Google Gemini + Gmail + Slack | Finance & E-Commerce | [JSON Template](templates/09-finance-ecommerce/46-Automated-Weekly-KPI-Analytics-Report.json) |
| 47 | **Jira Sprint Digest & Blocker Alert** | Check active Jira sprint status daily, flag stale or blocked tickets, and broadcast status to engineering team Slack channel. | Jira Software + Slack | Productivity & Tasks | [JSON Template](templates/04-productivity-tasks/47-Jira-Sprint-Digest-Blocker-Alert.json) |
| 48 | **Voice Memo to Todoist Task Converter** | Send a Telegram voice memo on the go → transcribe audio with Gemini → extract task title, due date, and priority → create Todoist task. | Telegram Voice + Whisper/Gemini + Todoist | Productivity & Tasks | [JSON Template](templates/04-productivity-tasks/48-Voice-Memo-To-Todoist-Task-Converter.json) |
| 49 | **HubSpot Deal Stage Change Automator** | Trigger on HubSpot deal status progression, notify account executives in Slack, and create onboarding checklists when deals close-won. | HubSpot + Slack + Google Sheets | Sales & CRM | [JSON Template](templates/03-lead-generation-crm/49-HubSpot-Deal-Stage-Change-Automator.json) |
| 50 | **Docker Container Health & Restart Alert** | Listen to Docker container daemon crash events or exit codes via webhook/socket and send high-priority Telegram alerts. | Webhook + SSH/Bash + Telegram | DevOps & Monitoring | [JSON Template](templates/08-devops-system-monitoring/50-Docker-Container-Health-Restart-Alert.json) |
| 51 | **Contract Clause Extractor & Compliance Auditor** | Scan legal agreements and NDAs in Drive, extract indemnity, termination, and confidentiality clauses, and audit against company policy. | Google Drive + Google Gemini + Airtable | Doc Processing & RAG | [JSON Template](templates/06-document-processing-rag/51-Contract-Clause-Extractor-Compliance-Auditor.json) |
| 52 | **Multi-Language Webhook FAQ Assistant** | Embeddable API endpoint connecting web apps to a Gemini-powered RAG vector store for instant, accurate product FAQ answers. | Webhook + Google Gemini RAG + Pinecone | Chatbots & Messaging | [JSON Template](templates/05-chatbots-telegram-whatsapp/52-Multi-Language-Webhook-FAQ-Assistant.json) |
| 53 | **Creative Asset Prompt & Cloudinary Uploader** | Convert marketing copy into Midjourney/DALL-E image prompts with Gemini AI, process output, and organize on Cloudinary CDN. | Google Gemini + Cloudinary API | Social & Marketing | [JSON Template](templates/07-social-media-marketing/53-Creative-Asset-Prompt-Cloudinary-Uploader.json) |
| 54 | **Trello Board Auto-Archiver & Weekly Digest** | Clean completed cards from Trello 'Done' columns automatically every Friday and dispatch summary of completed deliverables via email. | Trello + Gmail | Productivity & Tasks | [JSON Template](templates/04-productivity-tasks/54-Trello-Board-Auto-Archiver-Weekly-Digest.json) |
| 55 | **Typeform NPS Survey Sentiment Dashboard** | Receive new Typeform Net Promoter Score (NPS) surveys, classify detractors vs promoters with Gemini AI, and log in Google Sheets. | Typeform + Google Gemini + Google Sheets | Sales & CRM | [JSON Template](templates/03-lead-generation-crm/55-Typeform-NPS-Survey-Sentiment-Dashboard.json) |
| 56 | **Google Drive Duplicate File Cleanup Helper** | Scan designated Google Drive shared drives, detect duplicate files by MD5 checksum and filename, and generate cleanup report. | Google Drive + Code Node | Doc Processing & RAG | [JSON Template](templates/06-document-processing-rag/56-Google-Drive-Duplicate-File-Cleanup-Helper.json) |
| 57 | **Real Estate Listing Scraper & Lead Matcher** | Monitor property listings via API / scraping, match features against buyer criteria with Gemini, and dispatch instant Telegram alerts. | HTTP Request + Google Gemini + Telegram | Finance & E-Commerce | [JSON Template](templates/09-finance-ecommerce/57-Real-Estate-Listing-Scraper-Lead-Matcher.json) |
| 58 | **Employee Onboarding Automation Pipeline** | Triggered when candidate signs offer letter: creates Google Workspace account, invites to Slack channels, and provisions Notion onboarding page. | Google Forms + Google Workspace + Slack + Notion | Productivity & Tasks | [JSON Template](templates/04-productivity-tasks/58-Employee-Onboarding-Automation-Pipeline.json) |
| 59 | **LinkedIn Connection Request Follow-Up Scheduler** | Schedule staggered, personalized follow-up sequences for prospective LinkedIn connections and log touchpoints in Google Sheets. | Webhook + Google Sheets + LinkedIn | Sales & CRM | [JSON Template](templates/03-lead-generation-crm/59-LinkedIn-Connection-Request-Follow-Up-Scheduler.json) |
| 60 | **E-Commerce Abandoned Cart Recovery Sequence** | Detect abandoned checkouts in Shopify/WooCommerce, wait 2 hours, and dispatch a 10% discount recovery email sequence. | Shopify / WooCommerce + Gmail + Delay Timers | Finance & E-Commerce | [JSON Template](templates/09-finance-ecommerce/60-Ecommerce-Abandoned-Cart-Recovery-Sequence.json) |
| 61 | **Notion Knowledge Base RAG Assistant** | Index Notion workspace documents into Qdrant/Pinecone vector embeddings; query company policies via conversational Telegram/Slack bot. | Notion + Google Gemini + Qdrant/Pinecone + Telegram | Doc Processing & RAG | [JSON Template](templates/06-document-processing-rag/61-Notion-Knowledge-Base-RAG-Assistant.json) |
| 62 | **Autonomous AI Deep Web Research Agent** | Autonomous multi-step research agent: takes a research question, performs live web queries via SerpAPI, synthesizes findings with Gemini, and produces an executive Google Doc. | SerpAPI + Google Gemini + Google Docs / Drive | Social & Marketing | [JSON Template](templates/07-social-media-marketing/62-Autonomous-AI-Deep-Web-Research-Agent.json) |

---

## Workflows by Category

### 1. Gmail & Email Automation

Streamline inbox processing, email categorization, scheduled cold outreach, automated responses, and threat detection with AI.

| # | Title | What it does | Integrations | Link |
|---|-------|--------------|--------------|------|
| 1 | **Multi-Customer Email Sender** | Send personalized emails to 20–100 customers from Google Sheets with dynamic templating and delay throttling. | Gmail + Google Sheets | [Download Template](templates/01-email-automation/01-Multi-Customer-Email-Sender.json) |
| 5 | **AI Auto Email Reply** | Classify incoming emails (inquiry, support, spam, feedback) and generate contextual, professional replies using Google Gemini. | Gmail + Google Gemini | [Download Template](templates/01-email-automation/05-AI-Auto-Email-Reply.json) |
| 7 | **Form to Email Automation** | New website form submission triggers instant personalized confirmation email and notifies team. | Google Forms / Webhook + Gmail | [Download Template](templates/01-email-automation/07-Form-To-Email-Automation.json) |
| 10 | **Daily Email Summary** | Summarize important received emails every evening using Gemini AI and deliver an executive briefing to your inbox. | Gmail + Google Gemini | [Download Template](templates/01-email-automation/10-Daily-Email-Summary.json) |
| 12 | **Invoice Reminder** | Detect unpaid invoices from Google Sheets and automatically dispatch friendly payment reminders via Gmail. | Google Sheets + Gmail | [Download Template](templates/01-email-automation/12-Invoice-Reminder.json) |
| 21 | **AI Phishing & Security Email Screener** | Scan suspicious incoming emails with Gemini AI to detect phishing, spoofing, and malicious links, quarantining threats automatically. | Gmail + Google Gemini + Slack | [Download Template](templates/01-email-automation/21-AI-Phishing-Security-Email-Screener.json) |
| 32 | **Stripe Failed Payment Recovery Dunning Bot** | Catch Stripe charge.failed webhooks, notify finance team in Slack, and send automated polite card update request to customer. | Stripe + Gmail + Slack | [Download Template](templates/01-email-automation/32-Stripe-Failed-Payment-Recovery-Dunning-Bot.json) |
| 42 | **RSS Feed to Newsletter Draft Generator** | Collect weekly industry articles, generate curated newsletter commentary with Gemini AI, and draft Mailchimp / Gmail campaigns. | RSS + Google Gemini + Gmail / Mailchimp | [Download Template](templates/01-email-automation/42-RSS-Feed-To-Newsletter-Draft-Generator.json) |

### 2. AI Job & Career Agent Suite

Full autonomous career assistant suite from job alert scraping and resume parsing to tailored application generation and tracking.

| # | Title | What it does | Integrations | Link |
|---|-------|--------------|--------------|------|
| 2 | **AI Job Application Generator** | Take a Job Description (JD) via Webhook/Form → generate tailored resume bullet points + custom cover letter via Gemini and export to Drive. | Gemini + Gmail + Google Drive | [Download Template](templates/02-job-career-ai/02-AI-Job-Application-Generator.json) |
| 3 | **Auto Job Application Tracker** | Track applied jobs automatically by listening to Gmail application confirmations and appending details to Google Sheets & Notion. | Gmail + Google Sheets + Notion | [Download Template](templates/02-job-career-ai/03-Auto-Job-Application-Tracker.json) |
| 4 | **Job Alert AI Match** | Read incoming LinkedIn/Indeed job alerts from Gmail, extract role details, and score them against your resume using Gemini AI. | Gmail + Google Gemini | [Download Template](templates/02-job-career-ai/04-Job-Alert-AI-Match.json) |
| 14 | **Resume Analyzer** | Upload a candidate resume PDF to Drive → extract skills, years of experience, work history, and keywords into a structured JSON record. | Google Drive + Google Gemini | [Download Template](templates/02-job-career-ai/14-Resume-Analyzer.json) |
| 15 | **JD vs Resume Matcher** | Compare job descriptions directly against a candidate resume and produce an ATS match percentage with gap analysis. | Google Gemini + Webhook | [Download Template](templates/02-job-career-ai/15-JD-vs-Resume-Matcher.json) |
| 16 | **AI Cover Letter Generator** | Provide JD + Company name → produce customized, highly compelling cover letter saved directly to Google Drive as a Google Doc. | Google Gemini + Google Drive | [Download Template](templates/02-job-career-ai/16-AI-Cover-Letter-Generator.json) |
| 20 | **Complete AI Job Agent** | End-to-end career copilot: Find JD → Analyze requirements → Tailor resume → Draft cover letter → Request human approval → Log to Sheets. | Gmail + Google Gemini + Google Drive + Google Sheets | [Download Template](templates/02-job-career-ai/20-Complete-AI-Job-Agent.json) |

### 3. Lead Generation, Sales & CRM

Automate inbound lead capture, AI lead qualification (Hot/Warm/Cold), data enrichment, CRM synchronization, and customer churn detection.

| # | Title | What it does | Integrations | Link |
|---|-------|--------------|--------------|------|
| 8 | **Customer Lead Collector** | Capture leads from landing pages via Webhooks, validate emails, and save them automatically to Google Sheets & CRM. | Webhook + Google Sheets | [Download Template](templates/03-lead-generation-crm/08-Customer-Lead-Collector.json) |
| 9 | **AI Lead Qualification** | Score leads as Hot/Warm/Cold using Gemini AI based on company size, budget, and message intent. | Google Sheets + Google Gemini | [Download Template](templates/03-lead-generation-crm/09-AI-Lead-Qualification.json) |
| 17 | **Customer Feedback Analyzer** | Analyze incoming customer reviews & feedback, classify sentiment (positive, neutral, negative), and tag key issue areas. | Google Sheets + Google Gemini | [Download Template](templates/03-lead-generation-crm/17-Customer-Feedback-Analyzer.json) |
| 34 | **Airtable B2B Lead Enrichment Pipeline** | When a new lead is added to Airtable, enrich company revenue, employee count, and CEO contact via Hunter/Clearbit APIs. | Airtable + Hunter/Clearbit API + Google Sheets | [Download Template](templates/03-lead-generation-crm/34-Airtable-B2B-Lead-Enrichment-Pipeline.json) |
| 45 | **Customer Churn Risk Analyzer** | Analyze usage metrics, ticket frequency, and login patterns to identify churn risk and trigger customer success retention playbooks. | Sheets/Postgres + Google Gemini + Slack Alert | [Download Template](templates/03-lead-generation-crm/45-Customer-Churn-Risk-Analyzer.json) |
| 49 | **HubSpot Deal Stage Change Automator** | Trigger on HubSpot deal status progression, notify account executives in Slack, and create onboarding checklists when deals close-won. | HubSpot + Slack + Google Sheets | [Download Template](templates/03-lead-generation-crm/49-HubSpot-Deal-Stage-Change-Automator.json) |
| 55 | **Typeform NPS Survey Sentiment Dashboard** | Receive new Typeform Net Promoter Score (NPS) surveys, classify detractors vs promoters with Gemini AI, and log in Google Sheets. | Typeform + Google Gemini + Google Sheets | [Download Template](templates/03-lead-generation-crm/55-Typeform-NPS-Survey-Sentiment-Dashboard.json) |
| 59 | **LinkedIn Connection Request Follow-Up Scheduler** | Schedule staggered, personalized follow-up sequences for prospective LinkedIn connections and log touchpoints in Google Sheets. | Webhook + Google Sheets + LinkedIn | [Download Template](templates/03-lead-generation-crm/59-LinkedIn-Connection-Request-Follow-Up-Scheduler.json) |

### 4. Team Productivity & Task Automation

Automate daily standup notes, calendar reminders, Slack-to-Notion task conversions, Jira sprint blocker alerts, and employee onboarding.

| # | Title | What it does | Integrations | Link |
|---|-------|--------------|--------------|------|
| 6 | **Meeting Reminder Bot** | Send timely reminders to Telegram and Slack channels 15 minutes before scheduled Google Calendar meetings. | Google Calendar + Telegram + Slack | [Download Template](templates/04-productivity-tasks/06-Meeting-Reminder-Bot.json) |
| 18 | **Slack Task Creator** | Detect action items and task requests in Slack messages or reaction emojis and create tasks automatically in Notion. | Slack + Notion | [Download Template](templates/04-productivity-tasks/18-Slack-Task-Creator.json) |
| 27 | **GitHub Issue to Notion Task Synchronizer** | Automatically mirror new GitHub issues and bug reports into your Notion engineering backlog with tags, labels, and links. | GitHub + Notion | [Download Template](templates/04-productivity-tasks/27-GitHub-Issue-To-Notion-Task-Synchronizer.json) |
| 30 | **Google Calendar to Slack Daily Standup Notifier** | Extract today's agenda, milestones, and meeting links from Google Calendar at 9 AM and broadcast formatted agenda to team Slack channel. | Google Calendar + Slack | [Download Template](templates/04-productivity-tasks/30-Google-Calendar-To-Slack-Daily-Standup-Notifier.json) |
| 35 | **AI Audio Meeting Notes & Action Item Extractor** | Upload recorded meeting audio to Drive → transcribe with Whisper/Gemini → extract key action items and create Notion tasks. | Drive Audio + Whisper/Gemini + Notion | [Download Template](templates/04-productivity-tasks/35-AI-Audio-Meeting-Notes-Action-Item-Extractor.json) |
| 47 | **Jira Sprint Digest & Blocker Alert** | Check active Jira sprint status daily, flag stale or blocked tickets, and broadcast status to engineering team Slack channel. | Jira Software + Slack | [Download Template](templates/04-productivity-tasks/47-Jira-Sprint-Digest-Blocker-Alert.json) |
| 48 | **Voice Memo to Todoist Task Converter** | Send a Telegram voice memo on the go → transcribe audio with Gemini → extract task title, due date, and priority → create Todoist task. | Telegram Voice + Whisper/Gemini + Todoist | [Download Template](templates/04-productivity-tasks/48-Voice-Memo-To-Todoist-Task-Converter.json) |
| 54 | **Trello Board Auto-Archiver & Weekly Digest** | Clean completed cards from Trello 'Done' columns automatically every Friday and dispatch summary of completed deliverables via email. | Trello + Gmail | [Download Template](templates/04-productivity-tasks/54-Trello-Board-Auto-Archiver-Weekly-Digest.json) |
| 58 | **Employee Onboarding Automation Pipeline** | Triggered when candidate signs offer letter: creates Google Workspace account, invites to Slack channels, and provisions Notion onboarding page. | Google Forms + Google Workspace + Slack + Notion | [Download Template](templates/04-productivity-tasks/58-Employee-Onboarding-Automation-Pipeline.json) |

### 5. Chatbots (Telegram & WhatsApp)

Deploy conversational AI assistants, customer support bots, translation agents, and notification channels across Telegram, WhatsApp, and Discord.

| # | Title | What it does | Integrations | Link |
|---|-------|--------------|--------------|------|
| 11 | **Telegram AI Assistant** | Interactive Telegram bot powered by Google Gemini that answers questions, maintains context, and assists with daily queries. | Telegram + Google Gemini | [Download Template](templates/05-chatbots-telegram-whatsapp/11-Telegram-AI-Assistant.json) |
| 19 | **News AI Summary to Telegram** | Fetch top news via RSS / News API, summarize the top 5 stories with Google Gemini, and broadcast an elegant morning digest to Telegram. | RSS/API + Google Gemini + Telegram | [Download Template](templates/05-chatbots-telegram-whatsapp/19-News-AI-Summary-Telegram.json) |
| 23 | **WhatsApp Business Customer Support Bot** | Receive WhatsApp Cloud messages, retrieve FAQ answers with Gemini, and provide real-time automated conversational support. | WhatsApp Business Cloud + Google Gemini + Google Sheets | [Download Template](templates/05-chatbots-telegram-whatsapp/23-WhatsApp-Business-Customer-Support-Bot.json) |
| 25 | **Discord Community Welcome & Role Assigner** | Automatically send a customized welcome DM and assign initial roles to new Discord community members via webhook. | Discord + Webhook | [Download Template](templates/05-chatbots-telegram-whatsapp/25-Discord-Community-Welcome-Role-Assigner.json) |
| 38 | **Telegram Multi-Language Translation Bot** | Instant Telegram translation bot: detects language of incoming messages or audio and returns accurate translations in 50+ languages. | Telegram + Google Gemini Translator | [Download Template](templates/05-chatbots-telegram-whatsapp/38-Telegram-Multi-Language-Translation-Bot.json) |
| 39 | **Zendesk Critical Ticket Escalator** | Detect VIP or urgent priority tickets in Zendesk, immediately page on-call engineers via Slack and SMS escalation. | Zendesk + Slack On-Call + Twilio SMS | [Download Template](templates/05-chatbots-telegram-whatsapp/39-Zendesk-Critical-Ticket-Escalator.json) |
| 52 | **Multi-Language Webhook FAQ Assistant** | Embeddable API endpoint connecting web apps to a Gemini-powered RAG vector store for instant, accurate product FAQ answers. | Webhook + Google Gemini RAG + Pinecone | [Download Template](templates/05-chatbots-telegram-whatsapp/52-Multi-Language-Webhook-FAQ-Assistant.json) |

### 6. Document Processing, OCR & RAG

Automate Google Drive file management, PDF invoice parsing with Gemini Vision, receipt OCR, contract compliance audits, and Notion knowledge base RAG search.

| # | Title | What it does | Integrations | Link |
|---|-------|--------------|--------------|------|
| 13 | **Google Drive File Organizer** | Automatically classify and organize uploaded files into designated Drive folders (Invoices, Resumes, Contracts, Media) using Gemini AI. | Google Drive + Google Gemini | [Download Template](templates/06-document-processing-rag/13-Google-Drive-File-Organizer.json) |
| 22 | **YouTube Video Transcriber & AI Summarizer** | Download YouTube captions, summarize key points and timestamps with Gemini AI, and save structured notes into Notion. | YouTube + Google Gemini + Notion | [Download Template](templates/06-document-processing-rag/22-YouTube-Video-Transcriber-AI-Summarizer.json) |
| 26 | **Automated PDF Invoice Data Extractor** | Extract vendor name, invoice date, line items, tax, and total amount from PDF invoices using Gemini Vision and store into Airtable. | Google Drive + Gemini Vision + Airtable | [Download Template](templates/06-document-processing-rag/26-Automated-PDF-Invoice-Data-Extractor.json) |
| 33 | **Notion Database Auto-Backup to Drive** | Weekly automated backup of critical Notion databases exported to JSON/CSV and saved in organized Google Drive backup archives. | Notion API + Google Drive + Cron | [Download Template](templates/06-document-processing-rag/33-Notion-Database-Auto-Backup-To-Drive.json) |
| 41 | **Expense Receipt Scanner & Categorizer** | Snap a receipt image via Telegram or Drive → parse merchant, category, date, and amount with Gemini Vision → log into expense sheet. | Telegram/Drive + Gemini Vision + Google Sheets | [Download Template](templates/06-document-processing-rag/41-Expense-Receipt-Scanner-Categorizer.json) |
| 51 | **Contract Clause Extractor & Compliance Auditor** | Scan legal agreements and NDAs in Drive, extract indemnity, termination, and confidentiality clauses, and audit against company policy. | Google Drive + Google Gemini + Airtable | [Download Template](templates/06-document-processing-rag/51-Contract-Clause-Extractor-Compliance-Auditor.json) |
| 56 | **Google Drive Duplicate File Cleanup Helper** | Scan designated Google Drive shared drives, detect duplicate files by MD5 checksum and filename, and generate cleanup report. | Google Drive + Code Node | [Download Template](templates/06-document-processing-rag/56-Google-Drive-Duplicate-File-Cleanup-Helper.json) |
| 61 | **Notion Knowledge Base RAG Assistant** | Index Notion workspace documents into Qdrant/Pinecone vector embeddings; query company policies via conversational Telegram/Slack bot. | Notion + Google Gemini + Qdrant/Pinecone + Telegram | [Download Template](templates/06-document-processing-rag/61-Notion-Knowledge-Base-RAG-Assistant.json) |

### 7. Social Media, Content & Marketing

Automate cross-posting to LinkedIn and Twitter/X, SEO-optimized WordPress drafting, app store sentiment tracking, and deep AI web research.

| # | Title | What it does | Integrations | Link |
|---|-------|--------------|--------------|------|
| 29 | **Social Media Cross-Poster** | Write post in Google Sheets → automatically publish across LinkedIn, Twitter/X, and Buffer simultaneously with asset attachments. | Google Sheets + LinkedIn + Twitter/X + Buffer | [Download Template](templates/07-social-media-marketing/29-Social-Media-Cross-Poster.json) |
| 31 | **App Store Review Sentiment Monitor** | Fetch iOS App Store and Google Play reviews via RSS, score sentiment with Gemini, and alert product team on negative feedback. | RSS + Google Gemini + Slack | [Download Template](templates/07-social-media-marketing/31-App-Store-Review-Sentiment-Monitor.json) |
| 40 | **WordPress Auto-Publisher & SEO Optimizer** | Generate SEO-optimized blog posts with Gemini AI from keyword briefs, format headings & meta tags, and publish as WordPress drafts. | Gemini + WordPress API + Yoast | [Download Template](templates/07-social-media-marketing/40-WordPress-Auto-Publisher-SEO-Optimizer.json) |
| 53 | **Creative Asset Prompt & Cloudinary Uploader** | Convert marketing copy into Midjourney/DALL-E image prompts with Gemini AI, process output, and organize on Cloudinary CDN. | Google Gemini + Cloudinary API | [Download Template](templates/07-social-media-marketing/53-Creative-Asset-Prompt-Cloudinary-Uploader.json) |
| 62 | **Autonomous AI Deep Web Research Agent** | Autonomous multi-step research agent: takes a research question, performs live web queries via SerpAPI, synthesizes findings with Gemini, and produces an executive Google Doc. | SerpAPI + Google Gemini + Google Docs / Drive | [Download Template](templates/07-social-media-marketing/62-Autonomous-AI-Deep-Web-Research-Agent.json) |

### 8. DevOps, Cloud & System Monitoring

Continuous website uptime monitoring, SSL expiration checks, PostgreSQL-to-Sheets syncing, Docker container crash alerting, and Supabase webhook logging.

| # | Title | What it does | Integrations | Link |
|---|-------|--------------|--------------|------|
| 24 | **PostgreSQL to Google Sheets Automated Sync** | Daily scheduled query pulling latest revenue and customer analytics from PostgreSQL and upserting directly into Google Sheets dashboards. | PostgreSQL + Google Sheets + Cron | [Download Template](templates/08-devops-system-monitoring/24-PostgreSQL-To-Google-Sheets-Automated-Sync.json) |
| 28 | **Website Uptime & SSL Expiry Monitor** | Ping critical website endpoints and check SSL certificates every 5 minutes; send immediate Telegram alerts if downtime occurs. | HTTP Request + Telegram Alert + Cron | [Download Template](templates/08-devops-system-monitoring/28-Website-Uptime-SSL-Expiry-Monitor.json) |
| 43 | **Supabase Database Change Webhook to Slack** | Listen to Supabase Database Webhooks on insert/update in critical tables (e.g., users, subscriptions) and alert Slack with change diff. | Supabase + Slack Notification | [Download Template](templates/08-devops-system-monitoring/43-Supabase-Database-Change-Webhook-To-Slack.json) |
| 50 | **Docker Container Health & Restart Alert** | Listen to Docker container daemon crash events or exit codes via webhook/socket and send high-priority Telegram alerts. | Webhook + SSH/Bash + Telegram | [Download Template](templates/08-devops-system-monitoring/50-Docker-Container-Health-Restart-Alert.json) |

### 9. E-Commerce & Finance Automation

Automate Shopify order fulfillment, abandoned cart recovery sequences, competitor price monitoring, automated quiz grading, and executive KPI reports.

| # | Title | What it does | Integrations | Link |
|---|-------|--------------|--------------|------|
| 36 | **Shopify New Order Fulfillment & SMS Notifier** | Trigger on new paid Shopify orders, record in fulfillment Google Sheets, and send tracking SMS to customer via Twilio. | Shopify + Twilio + Google Sheets | [Download Template](templates/09-finance-ecommerce/36-Shopify-New-Order-Fulfillment-SMS-Notifier.json) |
| 37 | **Competitor Price Monitor & Alert** | Scrape competitor product pages every 6 hours, track pricing fluctuations in Google Sheets, and email alerts on price drops. | HTTP Scraping + HTML Node + Sheets + Gmail | [Download Template](templates/09-finance-ecommerce/37-Competitor-Price-Monitor-Alert.json) |
| 44 | **Google Forms Quiz Auto-Grader & Certificate Generator** | Automatically grade student quiz submissions from Google Forms, calculate scores, generate PDF certificates, and email recipients. | Forms + Sheets + PDF + Gmail | [Download Template](templates/09-finance-ecommerce/44-Google-Forms-Quiz-Auto-Grader-Certificate-Generator.json) |
| 46 | **Automated Weekly KPI Analytics Report** | Aggregate weekly revenue, customer acquisition cost, active users, and conversions into an executive Gemini AI briefing. | Sheets + Google Gemini + Gmail + Slack | [Download Template](templates/09-finance-ecommerce/46-Automated-Weekly-KPI-Analytics-Report.json) |
| 57 | **Real Estate Listing Scraper & Lead Matcher** | Monitor property listings via API / scraping, match features against buyer criteria with Gemini, and dispatch instant Telegram alerts. | HTTP Request + Google Gemini + Telegram | [Download Template](templates/09-finance-ecommerce/57-Real-Estate-Listing-Scraper-Lead-Matcher.json) |
| 60 | **E-Commerce Abandoned Cart Recovery Sequence** | Detect abandoned checkouts in Shopify/WooCommerce, wait 2 hours, and dispatch a 10% discount recovery email sequence. | Shopify / WooCommerce + Gmail + Delay Timers | [Download Template](templates/09-finance-ecommerce/60-Ecommerce-Abandoned-Cart-Recovery-Sequence.json) |

---

## Setup & Deployment Guide

### Recommended Environment Variables
When self-hosting n8n, configure these in your `.env` file:
```bash
GENERIC_TIMEZONE=UTC
N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true
N8N_DEFAULT_BINARY_DATA_MODE=filesystem
EXECUTIONS_DATA_PRUNE=true
EXECUTIONS_DATA_MAX_AGE=168
```

### Setting Up AI Models (Gemini & OpenAI)
- For **Google Gemini**: Get an API key from [Google AI Studio](https://aistudio.google.com/), then add credentials in n8n under `Google Gemini API`.
- For **OpenAI / Ollama**: Add credentials under `OpenAI API` or `Ollama` for local private model execution.

---

## Contributing

Contributions are welcome! If you have built an awesome n8n automation template:
1. Fork this repository.
2. Export your workflow JSON from n8n (**Workflows → Download**).
3. Place it in the appropriate `templates/<category>/` folder.
4. Open a Pull Request with a clear description and sample use cases.

---

## License

This repository is licensed under the [MIT License](LICENSE). Feel free to use, adapt, and deploy these workflows for personal or commercial projects.