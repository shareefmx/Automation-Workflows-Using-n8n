import json
import os
import uuid

# Define the 62 workflows with full metadata and node specifications
WORKFLOWS = [
    # 01 - Email Automation
    {
        "id": 1,
        "name": "Multi-Customer Email Sender",
        "category": "01-email-automation",
        "filename": "01-Multi-Customer-Email-Sender.json",
        "description": "Send personalized emails to 20–100 customers from Google Sheets with dynamic templating and delay throttling.",
        "integrations": "Gmail + Google Sheets",
        "department": "Marketing / Sales",
        "nodes": [
            ("Schedule Trigger", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "hours", "hoursInterval": 24}]}}, [220, 300]),
            ("Fetch Customer List", "n8n-nodes-base.googleSheets", 4.5, {"operation": "read", "documentId": {"__rl": True, "value": "GOOGLE_SHEET_ID", "mode": "id"}, "sheetName": {"__rl": True, "value": "Customers", "mode": "name"}}, [440, 300]),
            ("Personalize Email Template", "n8n-nodes-base.code", 2, {"mode": "runOnceForEachItem", "jsCode": "const customer = $input.item.json;\nconst subject = `Exclusive Update for ${customer.name}`;\nconst body = `Hi ${customer.name},\\n\\nWe noticed you are exploring our automation tools. Here is your custom invite: https://example.com/invite?code=${customer.invite_code}\\n\\nBest,\\nThe Team`;\nreturn {\n  json: {\n    email: customer.email,\n    subject: subject,\n    body: body\n  }\n};"}, [660, 300]),
            ("Throttled Send via Gmail", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "={{ $json.email }}", "subject": "={{ $json.subject }}", "message": "={{ $json.body }}"}, [880, 300]),
            ("Update Delivery Status", "n8n-nodes-base.googleSheets", 4.5, {"operation": "update", "documentId": {"__rl": True, "value": "GOOGLE_SHEET_ID", "mode": "id"}, "sheetName": {"__rl": True, "value": "Customers", "mode": "name"}, "columns": {"mappingMode": "defineBelow", "value": {"Status": "Sent", "SentAt": "={{ $now.toISO() }}"}}}, [1100, 300])
        ]
    },
    {
        "id": 2,
        "name": "AI Job Application Generator",
        "category": "02-job-career-ai",
        "filename": "02-AI-Job-Application-Generator.json",
        "description": "Take a Job Description (JD) via Webhook/Form → generate tailored resume bullet points + custom cover letter via Gemini and export to Drive.",
        "integrations": "Gemini + Gmail + Google Drive",
        "department": "Career / AI",
        "nodes": [
            ("JD Webhook Trigger", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "submit-job-description", "responseMode": "onReceived"}, [220, 300]),
            ("Read Master Resume from Drive", "n8n-nodes-base.googleDrive", 3, {"operation": "download", "fileId": {"__rl": True, "value": "MASTER_RESUME_DOC_ID", "mode": "id"}}, [440, 300]),
            ("Gemini AI Tailor Prompt", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Analyze the following Job Description:\\n{{ $('JD Webhook Trigger').item.json.body.job_description }}\\n\\nAnd master background:\\n{{ $json.data }}\\n\\nGenerate: 1) Tailored Resume Bullets highlighting matching skills, 2) A persuasive cover letter addressed to the hiring team."}, [660, 300]),
            ("Save Application to Google Docs", "n8n-nodes-base.googleDrive", 3, {"operation": "createFromText", "name": "=Application - {{ $('JD Webhook Trigger').item.json.body.company }} - {{ $('JD Webhook Trigger').item.json.body.role }}.txt"}, [880, 300]),
            ("Email Review Copy to Applicant", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "me@example.com", "subject": "=Ready to Apply: {{ $('JD Webhook Trigger').item.json.body.company }} - {{ $('JD Webhook Trigger').item.json.body.role }}", "message": "={{ $('Gemini AI Tailor Prompt').item.json.output }}"}, [1100, 300])
        ]
    },
    {
        "id": 3,
        "name": "Auto Job Application Tracker",
        "category": "02-job-career-ai",
        "filename": "03-Auto-Job-Application-Tracker.json",
        "description": "Track applied jobs automatically by listening to Gmail application confirmations and appending details to Google Sheets & Notion.",
        "integrations": "Gmail + Google Sheets + Notion",
        "department": "Career / Productivity",
        "nodes": [
            ("Gmail Application Sent Trigger", "n8n-nodes-base.gmailTrigger", 1.1, {"pollTimes": {"item": [{"mode": "everyMinute"}]}, "filters": {"q": "subject:(Application OR Applied OR \"Thank you for applying\")"}}, [220, 300]),
            ("Extract Job Metadata", "n8n-nodes-base.code", 2, {"mode": "runOnceForEachItem", "jsCode": "const email = $input.item.json;\nconst subject = email.subject || '';\nconst from = email.from || '';\nconst date = email.date || new Date().toISOString();\nreturn { json: { company: from.split('<')[0].replace(/\"/g, '').trim(), subject, date, snippet: email.snippet } };"}, [440, 300]),
            ("Log in Google Sheets Tracker", "n8n-nodes-base.googleSheets", 4.5, {"operation": "append", "documentId": {"__rl": True, "value": "JOB_TRACKER_SHEET_ID", "mode": "id"}, "sheetName": {"__rl": True, "value": "Applications", "mode": "name"}}, [660, 300]),
            ("Create Notion Application Card", "n8n-nodes-base.notion", 2.2, {"resource": "databasePage", "operation": "create", "databaseId": "NOTION_DB_ID"}, [880, 300])
        ]
    },
    {
        "id": 4,
        "name": "Job Alert AI Match",
        "category": "02-job-career-ai",
        "filename": "04-Job-Alert-AI-Match.json",
        "description": "Read incoming LinkedIn/Indeed job alerts from Gmail, extract role details, and score them against your resume using Gemini AI.",
        "integrations": "Gmail + Google Gemini",
        "department": "Career / AI",
        "nodes": [
            ("Job Alert Email Trigger", "n8n-nodes-base.gmailTrigger", 1.1, {"pollTimes": {"item": [{"mode": "everyMinute"}]}, "filters": {"q": "from:(linkedin.com OR indeed.com) subject:(\"job alert\" OR \"recommended job\")"}}, [220, 300]),
            ("Gemini Relevance Matcher", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Evaluate this job alert email body:\\n{{ $json.snippet }}\\n\\nCandidate Profile: Senior Automation Engineer & Python/Typescript Developer with n8n and AI workflow expertise.\\nProvide: 1) Score (0-100), 2) Recommendation (Apply / Skip), 3) Key matching keywords."}, [440, 300]),
            ("Filter High Score (>80)", "n8n-nodes-base.if", 2.2, {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict"}, "conditions": [{"id": "c1", "leftValue": "={{ $json.score }}", "rightValue": 80, "operator": {"type": "number", "operation": "gte"}}], "combinator": "and"}}, [660, 300]),
            ("Send Priority Notification", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "me@example.com", "subject": "🔥 High Match Job Alert Detected!", "message": "={{ $json.analysis }}"}, [880, 200])
        ]
    },
    {
        "id": 5,
        "name": "AI Auto Email Reply",
        "category": "01-email-automation",
        "filename": "05-AI-Auto-Email-Reply.json",
        "description": "Classify incoming emails (inquiry, support, spam, feedback) and generate contextual, professional replies using Google Gemini.",
        "integrations": "Gmail + Google Gemini",
        "department": "Customer Support / Ops",
        "nodes": [
            ("New Email Trigger", "n8n-nodes-base.gmailTrigger", 1.1, {"pollTimes": {"item": [{"mode": "everyMinute"}]}, "filters": {"q": "is:unread -category:promotions"}}, [220, 300]),
            ("Gemini Email Classifier & Drafter", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Analyze incoming email:\\nSubject: {{ $json.subject }}\\nFrom: {{ $json.from }}\\nBody: {{ $json.textPlain }}\\n\\nTask: 1) Classify category: [Support, Sales Inquiry, Partnership, Urgent, Spam]. 2) If not Spam, draft a polite, helpful reply on behalf of Support Team."}, [440, 300]),
            ("Check Category", "n8n-nodes-base.if", 2.2, {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict"}, "conditions": [{"id": "c1", "leftValue": "={{ $json.category }}", "rightValue": "Spam", "operator": {"type": "string", "operation": "notEquals"}}], "combinator": "and"}}, [660, 300]),
            ("Create Gmail Reply Draft", "n8n-nodes-base.gmail", 2.1, {"operation": "createDraft", "threadId": "={{ $('New Email Trigger').item.json.threadId }}", "message": "={{ $json.draftReply }}"}, [880, 200])
        ]
    },
    {
        "id": 6,
        "name": "Meeting Reminder Bot",
        "category": "04-productivity-tasks",
        "filename": "06-Meeting-Reminder-Bot.json",
        "description": "Send timely reminders to Telegram and Slack channels 15 minutes before scheduled Google Calendar meetings.",
        "integrations": "Google Calendar + Telegram + Slack",
        "department": "Productivity / Ops",
        "nodes": [
            ("Cron Every 15 Minutes", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "minutes", "minutesInterval": 15}]}}, [220, 300]),
            ("Fetch Upcoming Events", "n8n-nodes-base.googleCalendar", 1.2, {"operation": "getAll", "calendar": {"__rl": True, "value": "primary", "mode": "id"}, "options": {"timeMin": "={{ $now.toISO() }}", "timeMax": "={{ $now.plus({ minutes: 30 }).toISO() }}"}}, [440, 300]),
            ("Send Telegram Reminder", "n8n-nodes-base.telegram", 1.2, {"operation": "sendMessage", "chatId": "@team_alerts", "text": "=📅 Reminder: *{{ $json.summary }}* starts in 15 minutes!\\n🔗 Link: {{ $json.hangoutLink || 'In-person / Calendar link' }}"}, [660, 200]),
            ("Post to Slack Channel", "n8n-nodes-base.slack", 2.2, {"operation": "postMessage", "channel": "#general", "text": "=📅 Reminder: *{{ $json.summary }}* is starting shortly!"}, [660, 400])
        ]
    },
    {
        "id": 7,
        "name": "Form to Email Automation",
        "category": "01-email-automation",
        "filename": "07-Form-To-Email-Automation.json",
        "description": "New website form submission triggers instant personalized confirmation email and notifies team.",
        "integrations": "Google Forms / Webhook + Gmail",
        "department": "Marketing / Customer Success",
        "nodes": [
            ("Form Submission Webhook", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "lead-form-submit", "responseMode": "lastNode"}, [220, 300]),
            ("Send User Confirmation Email", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "={{ $json.body.email }}", "subject": "Thank you for reaching out, {{ $json.body.name }}!", "message": "=Hi {{ $json.body.name }},\\n\\nWe received your request regarding: \"{{ $json.body.interest }}\". A specialist will reach out within 24 hours.\\n\\nWarm regards,\\nCustomer Team"}, [440, 300]),
            ("Notify Internal Ops Team", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "ops@example.com", "subject": "🚨 New Lead Form Submitted: {{ $json.body.name }}", "message": "=New submission details:\\nName: {{ $json.body.name }}\\nEmail: {{ $json.body.email }}\\nMessage: {{ $json.body.message }}"}, [660, 300]),
            ("Return Success Response", "n8n-nodes-base.respondToWebhook", 1.1, {"options": {"responseCode": 200}, "respondWith": "json", "responseBody": "{\"status\": \"success\", \"message\": \"Form received successfully\"}"}, [880, 300])
        ]
    },
    {
        "id": 8,
        "name": "Customer Lead Collector",
        "category": "03-lead-generation-crm",
        "filename": "08-Customer-Lead-Collector.json",
        "description": "Capture leads from landing pages via Webhooks, validate emails, and save them automatically to Google Sheets & CRM.",
        "integrations": "Webhook + Google Sheets",
        "department": "Sales / Growth",
        "nodes": [
            ("Lead Ingestion Webhook", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "customer-lead-capture", "responseMode": "onReceived"}, [220, 300]),
            ("Data Sanitization Code", "n8n-nodes-base.code", 2, {"mode": "runOnceForEachItem", "jsCode": "const lead = $input.item.json.body;\nreturn {\n  json: {\n    first_name: lead.first_name ? lead.first_name.trim() : 'Valued',\n    last_name: lead.last_name ? lead.last_name.trim() : 'Customer',\n    email: lead.email ? lead.email.toLowerCase().trim() : '',\n    company: lead.company ? lead.company.trim() : 'N/A',\n    source: lead.source || 'Website',\n    captured_at: new Date().toISOString()\n  }\n};"}, [440, 300]),
            ("Append to Google Sheets CRM", "n8n-nodes-base.googleSheets", 4.5, {"operation": "append", "documentId": {"__rl": True, "value": "LEAD_SHEET_ID", "mode": "id"}, "sheetName": {"__rl": True, "value": "Leads", "mode": "name"}}, [660, 300])
        ]
    },
    {
        "id": 9,
        "name": "AI Lead Qualification",
        "category": "03-lead-generation-crm",
        "filename": "09-AI-Lead-Qualification.json",
        "description": "Score leads as Hot/Warm/Cold using Gemini AI based on company size, budget, and message intent.",
        "integrations": "Google Sheets + Google Gemini",
        "department": "Sales / Operations",
        "nodes": [
            ("Poll Unqualified Leads", "n8n-nodes-base.googleSheets", 4.5, {"operation": "read", "documentId": {"__rl": True, "value": "LEAD_SHEET_ID", "mode": "id"}, "sheetName": {"__rl": True, "value": "Leads", "mode": "name"}}, [220, 300]),
            ("Filter Status Pending", "n8n-nodes-base.if", 2.2, {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict"}, "conditions": [{"id": "c1", "leftValue": "={{ $json.Score }}", "rightValue": "", "operator": {"type": "string", "operation": "empty"}}], "combinator": "and"}}, [440, 300]),
            ("Gemini AI Lead Scorer", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Analyze lead details:\\nCompany: {{ $json.company }}\\nBudget: {{ $json.budget }}\\nMessage: {{ $json.message }}\\n\\nCategorize into: [Hot, Warm, Cold] and assign score from 0-100 with 1 sentence rationale."}, [660, 300]),
            ("Update Lead Tier in Sheets", "n8n-nodes-base.googleSheets", 4.5, {"operation": "update", "documentId": {"__rl": True, "value": "LEAD_SHEET_ID", "mode": "id"}, "sheetName": {"__rl": True, "value": "Leads", "mode": "name"}}, [880, 300])
        ]
    },
    {
        "id": 10,
        "name": "Daily Email Summary",
        "category": "01-email-automation",
        "filename": "10-Daily-Email-Summary.json",
        "description": "Summarize important received emails every evening using Gemini AI and deliver an executive briefing to your inbox.",
        "integrations": "Gmail + Google Gemini",
        "department": "Executive / Productivity",
        "nodes": [
            ("Daily 6 PM Trigger", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "hours", "hoursInterval": 24}]}}, [220, 300]),
            ("Fetch Today's Unread Emails", "n8n-nodes-base.gmail", 2.1, {"operation": "getAll", "filters": {"q": "after:{{ $now.minus({ hours: 12 }).format('yyyy/MM/dd') }} is:unread"}}, [440, 300]),
            ("Aggregate Email Contents", "n8n-nodes-base.code", 2, {"mode": "runOnceForAllItems", "jsCode": "const items = $input.all();\nconst textList = items.map(item => `From: ${item.json.from} | Subject: ${item.json.subject} | Snippet: ${item.json.snippet}`).join('\\n---\\n');\nreturn [{ json: { full_digest: textList, count: items.length } }];"}, [660, 300]),
            ("Gemini Digest Generator", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=You are an executive chief of staff. Review the following {{ $json.count }} emails received today:\\n{{ $json.full_digest }}\\n\\nGroup into: 1) Urgent Action Items, 2) Key Updates, 3) FYIs/Newsletters."}, [880, 300]),
            ("Send Evening Briefing Email", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "me@example.com", "subject": "📋 Your Daily Executive Email Briefing", "message": "={{ $json.output }}"}, [1100, 300])
        ]
    },
    {
        "id": 11,
        "name": "Telegram AI Assistant",
        "category": "05-chatbots-telegram-whatsapp",
        "filename": "11-Telegram-AI-Assistant.json",
        "description": "Interactive Telegram bot powered by Google Gemini that answers questions, maintains context, and assists with daily queries.",
        "integrations": "Telegram + Google Gemini",
        "department": "Support / AI",
        "nodes": [
            ("Telegram Inbound Message", "n8n-nodes-base.telegramTrigger", 1.1, {"updates": ["message"]}, [220, 300]),
            ("Gemini Conversational Agent", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=User Message from Telegram: {{ $json.message.text }}\\n\\nRespond concisely and helpfully in markdown format."}, [440, 300]),
            ("Send Telegram Reply", "n8n-nodes-base.telegram", 1.2, {"operation": "sendMessage", "chatId": "={{ $('Telegram Inbound Message').item.json.message.chat.id }}", "text": "={{ $json.output }}"}, [660, 300])
        ]
    },
    {
        "id": 12,
        "name": "Invoice Reminder",
        "category": "01-email-automation",
        "filename": "12-Invoice-Reminder.json",
        "description": "Detect unpaid invoices from Google Sheets and automatically dispatch friendly payment reminders via Gmail.",
        "integrations": "Google Sheets + Gmail",
        "department": "Finance / Operations",
        "nodes": [
            ("Weekday 9 AM Cron", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "hours", "hoursInterval": 24}]}}, [220, 300]),
            ("Read Invoices Sheet", "n8n-nodes-base.googleSheets", 4.5, {"operation": "read", "documentId": {"__rl": True, "value": "INVOICES_SHEET_ID", "mode": "id"}, "sheetName": {"__rl": True, "value": "Invoices", "mode": "name"}}, [440, 300]),
            ("Filter Due or Overdue", "n8n-nodes-base.if", 2.2, {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict"}, "conditions": [{"id": "c1", "leftValue": "={{ $json.Status }}", "rightValue": "Unpaid", "operator": {"type": "string", "operation": "equals"}}], "combinator": "and"}}, [660, 300]),
            ("Dispatch Payment Reminder", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "={{ $json.ClientEmail }}", "subject": "=Friendly Reminder: Invoice #{{ $json.InvoiceNumber }} Due", "message": "=Dear {{ $json.ClientName }},\\n\\nThis is a friendly reminder that invoice #{{ $json.InvoiceNumber }} for ${{ $json.Amount }} is due on {{ $json.DueDate }}.\\n\\nPlease review your payment portal here: {{ $json.PaymentLink }}\\n\\nThank you!"}, [880, 200])
        ]
    },
    {
        "id": 13,
        "name": "Google Drive File Organizer",
        "category": "06-document-processing-rag",
        "filename": "13-Google-Drive-File-Organizer.json",
        "description": "Automatically classify and organize uploaded files into designated Drive folders (Invoices, Resumes, Contracts, Media) using Gemini AI.",
        "integrations": "Google Drive + Google Gemini",
        "department": "Operations / IT",
        "nodes": [
            ("Drive New File Trigger", "n8n-nodes-base.googleDriveTrigger", 1, {"pollTimes": {"item": [{"mode": "everyMinute"}]}}, [220, 300]),
            ("Gemini File Category Classifier", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Given file name: '{{ $json.name }}' and mimeType: '{{ $json.mimeType }}'.\\nClassify into one folder ID:\\n- Invoices: FOLDER_ID_INVOICES\\n- Contracts: FOLDER_ID_CONTRACTS\\n- Resumes: FOLDER_ID_RESUMES\\n- General Media: FOLDER_ID_MEDIA\\nReturn ONLY the chosen target folder ID."}, [440, 300]),
            ("Move File to Target Folder", "n8n-nodes-base.googleDrive", 3, {"operation": "move", "fileId": "={{ $('Drive New File Trigger').item.json.id }}", "folderId": "={{ $json.output.trim() }}"}, [660, 300])
        ]
    },
    {
        "id": 14,
        "name": "Resume Analyzer",
        "category": "02-job-career-ai",
        "filename": "14-Resume-Analyzer.json",
        "description": "Upload a candidate resume PDF to Drive → extract skills, years of experience, work history, and keywords into a structured JSON record.",
        "integrations": "Google Drive + Google Gemini",
        "department": "HR / Recruiting",
        "nodes": [
            ("Resume File Upload Trigger", "n8n-nodes-base.googleDriveTrigger", 1, {"pollTimes": {"item": [{"mode": "everyMinute"}]}}, [220, 300]),
            ("Extract Resume Text", "n8n-nodes-base.googleDrive", 3, {"operation": "download", "fileId": "={{ $json.id }}"}, [440, 300]),
            ("Gemini AI Skills Extractor", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Extract from resume text: 1) Candidate Full Name, 2) Contact Email/Phone, 3) Primary Technical Skills, 4) Total Years of Experience, 5) Recent Companies and Titles. Format output as valid JSON."}, [660, 300]),
            ("Save to HR Candidate Database", "n8n-nodes-base.googleSheets", 4.5, {"operation": "append", "documentId": {"__rl": True, "value": "HR_CANDIDATE_SHEET", "mode": "id"}, "sheetName": {"__rl": True, "value": "Candidates", "mode": "name"}}, [880, 300])
        ]
    },
    {
        "id": 15,
        "name": "JD vs Resume Matcher",
        "category": "02-job-career-ai",
        "filename": "15-JD-vs-Resume-Matcher.json",
        "description": "Compare job descriptions directly against a candidate resume and produce an ATS match percentage with gap analysis.",
        "integrations": "Google Gemini + Webhook",
        "department": "Recruiting / Career",
        "nodes": [
            ("Match Request Webhook", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "match-jd-resume", "responseMode": "lastNode"}, [220, 300]),
            ("Gemini Deep Match Evaluator", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Compare Candidate Resume with Job Description:\\n\\nJob Description:\\n{{ $json.body.job_description }}\\n\\nResume:\\n{{ $json.body.resume_text }}\\n\\nOutput in JSON: { match_percentage: number, missing_skills: string[], strong_matches: string[], recommendations: string }"}, [440, 300]),
            ("Respond with Match Report", "n8n-nodes-base.respondToWebhook", 1.1, {"options": {"responseCode": 200}, "respondWith": "json", "responseBody": "={{ $json.output }}"}, [660, 300])
        ]
    },
    {
        "id": 16,
        "name": "AI Cover Letter Generator",
        "category": "02-job-career-ai",
        "filename": "16-AI-Cover-Letter-Generator.json",
        "description": "Provide JD + Company name → produce customized, highly compelling cover letter saved directly to Google Drive as a Google Doc.",
        "integrations": "Google Gemini + Google Drive",
        "department": "Career / AI",
        "nodes": [
            ("Cover Letter Trigger Webhook", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "generate-cover-letter", "responseMode": "lastNode"}, [220, 300]),
            ("Gemini AI Writer", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Write a personalized 3-paragraph cover letter for the role of {{ $json.body.role }} at {{ $json.body.company }}.\\nKey candidate highlights:\\n{{ $json.body.experience_highlights }}\\nMake tone professional, confident and engaging."}, [440, 300]),
            ("Save to Google Drive Document", "n8n-nodes-base.googleDrive", 3, {"operation": "createFromText", "name": "=Cover Letter - {{ $('Cover Letter Trigger Webhook').item.json.body.company }} - {{ $('Cover Letter Trigger Webhook').item.json.body.role }}.doc"}, [660, 300]),
            ("Return Download Link", "n8n-nodes-base.respondToWebhook", 1.1, {"options": {"responseCode": 200}, "respondWith": "json", "responseBody": "{\"status\": \"created\", \"cover_letter\": \"{{ $('Gemini AI Writer').item.json.output }}\", \"file_id\": \"{{ $json.id }}\"}"}, [880, 300])
        ]
    },
    {
        "id": 17,
        "name": "Customer Feedback Analyzer",
        "category": "03-lead-generation-crm",
        "filename": "17-Customer-Feedback-Analyzer.json",
        "description": "Analyze incoming customer reviews & feedback, classify sentiment (positive, neutral, negative), and tag key issue areas.",
        "integrations": "Google Sheets + Google Gemini",
        "department": "Customer Success / Product",
        "nodes": [
            ("Fetch New Feedback Rows", "n8n-nodes-base.googleSheets", 4.5, {"operation": "read", "documentId": {"__rl": True, "value": "FEEDBACK_SHEET_ID", "mode": "id"}, "sheetName": {"__rl": True, "value": "Responses", "mode": "name"}}, [220, 300]),
            ("Gemini Sentiment Classifier", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Analyze feedback text: '{{ $json.FeedbackText }}'.\\nDetermine: 1) Sentiment: [Positive, Neutral, Negative], 2) Primary Category: [Bug, UX, Feature Request, Pricing, Praise], 3) Executive 1-line summary."}, [440, 300]),
            ("Update Analyzed Sentiment", "n8n-nodes-base.googleSheets", 4.5, {"operation": "update", "documentId": {"__rl": True, "value": "FEEDBACK_SHEET_ID", "mode": "id"}, "sheetName": {"__rl": True, "value": "Responses", "mode": "name"}}, [660, 300])
        ]
    },
    {
        "id": 18,
        "name": "Slack Task Creator",
        "category": "04-productivity-tasks",
        "filename": "18-Slack-Task-Creator.json",
        "description": "Detect action items and task requests in Slack messages or reaction emojis and create tasks automatically in Notion.",
        "integrations": "Slack + Notion",
        "department": "Engineering / Project Management",
        "nodes": [
            ("Slack Reaction Added Trigger", "n8n-nodes-base.slackTrigger", 1, {"updates": ["reaction_added"]}, [220, 300]),
            ("Filter Bookmark Emoji", "n8n-nodes-base.if", 2.2, {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict"}, "conditions": [{"id": "c1", "leftValue": "={{ $json.reaction }}", "rightValue": "white_check_mark", "operator": {"type": "string", "operation": "equals"}}], "combinator": "and"}}, [440, 300]),
            ("Fetch Original Slack Message", "n8n-nodes-base.slack", 2.2, {"operation": "getMessage", "channel": "={{ $json.item.channel }}", "timestamp": "={{ $json.item.ts }}"}, [660, 200]),
            ("Create Task in Notion", "n8n-nodes-base.notion", 2.2, {"resource": "databasePage", "operation": "create", "databaseId": "TASKS_DATABASE_ID"}, [880, 200])
        ]
    },
    {
        "id": 19,
        "name": "News AI Summary to Telegram",
        "category": "05-chatbots-telegram-whatsapp",
        "filename": "19-News-AI-Summary-Telegram.json",
        "description": "Fetch top news via RSS / News API, summarize the top 5 stories with Google Gemini, and broadcast an elegant morning digest to Telegram.",
        "integrations": "RSS/API + Google Gemini + Telegram",
        "department": "Marketing / Media",
        "nodes": [
            ("Morning 8 AM Schedule", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "hours", "hoursInterval": 24}]}}, [220, 300]),
            ("Fetch Tech RSS Feed", "n8n-nodes-base.rssFeedRead", 1.1, {"url": "https://news.ycombinator.com/rss"}, [440, 300]),
            ("Gemini AI News Digest", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Summarize these top news headlines into 5 bullet points with key takeaways and emojis:\\n{{ $json.title }} - {{ $json.link }}"}, [660, 300]),
            ("Broadcast to Telegram Channel", "n8n-nodes-base.telegram", 1.2, {"operation": "sendMessage", "chatId": "@tech_digest_daily", "text": "={{ $json.output }}"}, [880, 300])
        ]
    },
    {
        "id": 20,
        "name": "Complete AI Job Agent",
        "category": "02-job-career-ai",
        "filename": "20-Complete-AI-Job-Agent.json",
        "description": "End-to-end career copilot: Find JD → Analyze requirements → Tailor resume → Draft cover letter → Request human approval → Log to Sheets.",
        "integrations": "Gmail + Google Gemini + Google Drive + Google Sheets",
        "department": "Career / Autonomous AI",
        "nodes": [
            ("Inbound Job Alert Trigger", "n8n-nodes-base.gmailTrigger", 1.1, {"pollTimes": {"item": [{"mode": "everyMinute"}]}}, [220, 300]),
            ("Gemini Autonomous Career Agent", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=You are an elite career agent. Parse the job opportunity from this email:\\n{{ $json.snippet }}\\n\\n1. Extract company, role, salary range, stack.\\n2. Generate tailored resume highlights.\\n3. Draft custom cover letter."}, [440, 300]),
            ("Store Tailored Pack in Drive", "n8n-nodes-base.googleDrive", 3, {"operation": "createFromText", "name": "=Application Pack - {{ $json.company }}.txt"}, [660, 300]),
            ("Log in Application Sheet", "n8n-nodes-base.googleSheets", 4.5, {"operation": "append", "documentId": {"__rl": True, "value": "JOB_TRACKER_SHEET", "mode": "id"}, "sheetName": {"__rl": True, "value": "Applications", "mode": "name"}}, [880, 300]),
            ("Send Approval Notification to Candidate", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "me@example.com", "subject": "🚀 Review Tailored Application: Ready for Approval", "message": "={{ $json.output }}"}, [1100, 300])
        ]
    },

    # Additional Curated Workflows (21 to 62)
    {
        "id": 21,
        "name": "AI Phishing & Security Email Screener",
        "category": "01-email-automation",
        "filename": "21-AI-Phishing-Security-Email-Screener.json",
        "description": "Scan suspicious incoming emails with Gemini AI to detect phishing, spoofing, and malicious links, quarantining threats automatically.",
        "integrations": "Gmail + Google Gemini + Slack",
        "department": "Security / IT",
        "nodes": [
            ("New Suspicious Email Trigger", "n8n-nodes-base.gmailTrigger", 1.1, {"pollTimes": {"item": [{"mode": "everyMinute"}]}}, [220, 300]),
            ("Gemini Security Risk Evaluator", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Inspect email for security threats: From: {{ $json.from }}, Subject: {{ $json.subject }}, Content: {{ $json.snippet }}. Classify threat level: [Safe, Low, Suspicious, Malicious Phishing]."}, [440, 300]),
            ("Check Malicious", "n8n-nodes-base.if", 2.2, {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict"}, "conditions": [{"id": "c1", "leftValue": "={{ $json.threatLevel }}", "rightValue": "Malicious Phishing", "operator": {"type": "string", "operation": "equals"}}], "combinator": "and"}}, [660, 300]),
            ("Post Security Alert to Slack", "n8n-nodes-base.slack", 2.2, {"operation": "postMessage", "channel": "#sec-ops", "text": "🚨 Phishing Threat Quarantined: {{ $('New Suspicious Email Trigger').item.json.subject }}"}, [880, 200])
        ]
    },
    {
        "id": 22,
        "name": "YouTube Video Transcriber & AI Summarizer",
        "category": "06-document-processing-rag",
        "filename": "22-YouTube-Video-Transcriber-AI-Summarizer.json",
        "description": "Download YouTube captions, summarize key points and timestamps with Gemini AI, and save structured notes into Notion.",
        "integrations": "YouTube + Google Gemini + Notion",
        "department": "Content / Research",
        "nodes": [
            ("Webhook Video URL Input", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "summarize-youtube"}, [220, 300]),
            ("Fetch Video Captions API", "n8n-nodes-base.httpRequest", 4.2, {"url": "=https://api.kome.ai/api/tools/youtube-transcripts?video_id={{ $json.body.video_id }}"}, [440, 300]),
            ("Gemini Comprehensive Summarizer", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Summarize this YouTube transcript into executive overview, key concepts, and actionable insights with timestamps: {{ $json.transcript }}"}, [660, 300]),
            ("Save Page in Notion Library", "n8n-nodes-base.notion", 2.2, {"resource": "databasePage", "operation": "create", "databaseId": "NOTION_RESEARCH_DB"}, [880, 300])
        ]
    },
    {
        "id": 23,
        "name": "WhatsApp Business Customer Support Bot",
        "category": "05-chatbots-telegram-whatsapp",
        "filename": "23-WhatsApp-Business-Customer-Support-Bot.json",
        "description": "Receive WhatsApp Cloud messages, retrieve FAQ answers with Gemini, and provide real-time automated conversational support.",
        "integrations": "WhatsApp Business Cloud + Google Gemini + Google Sheets",
        "department": "Customer Support",
        "nodes": [
            ("WhatsApp Inbound Webhook", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "whatsapp-webhook"}, [220, 300]),
            ("Gemini Multilingual Agent", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Provide helpful customer support for query: {{ $json.body.entry[0].changes[0].value.messages[0].text.body }}"}, [440, 300]),
            ("Dispatch WhatsApp Reply", "n8n-nodes-base.httpRequest", 4.2, {"method": "POST", "url": "https://graph.facebook.com/v18.0/PHONE_NUMBER_ID/messages"}, [660, 300])
        ]
    },
    {
        "id": 24,
        "name": "PostgreSQL to Google Sheets Automated Sync",
        "category": "08-devops-system-monitoring",
        "filename": "24-PostgreSQL-To-Google-Sheets-Automated-Sync.json",
        "description": "Daily scheduled query pulling latest revenue and customer analytics from PostgreSQL and upserting directly into Google Sheets dashboards.",
        "integrations": "PostgreSQL + Google Sheets + Cron",
        "department": "Data / Analytics",
        "nodes": [
            ("Daily 1 AM Sync Trigger", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "hours", "hoursInterval": 24}]}}, [220, 300]),
            ("Query Postgres Production DB", "n8n-nodes-base.postgres", 2.5, {"operation": "executeQuery", "query": "SELECT date_trunc('day', created_at) as date, count(*) as signups, sum(amount) as revenue FROM orders WHERE created_at >= NOW() - INTERVAL '30 days' GROUP BY 1 ORDER BY 1 DESC;"}, [440, 300]),
            ("Sync to Sheets Dashboard", "n8n-nodes-base.googleSheets", 4.5, {"operation": "appendOrUpdate", "documentId": {"__rl": True, "value": "METRICS_SHEET_ID", "mode": "id"}, "sheetName": {"__rl": True, "value": "RevenueSync", "mode": "name"}}, [660, 300])
        ]
    },
    {
        "id": 25,
        "name": "Discord Community Welcome & Role Assigner",
        "category": "05-chatbots-telegram-whatsapp",
        "filename": "25-Discord-Community-Welcome-Role-Assigner.json",
        "description": "Automatically send a customized welcome DM and assign initial roles to new Discord community members via webhook.",
        "integrations": "Discord + Webhook",
        "department": "Community / Marketing",
        "nodes": [
            ("Discord Member Join Webhook", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "discord-member-joined"}, [220, 300]),
            ("Format Welcome DM", "n8n-nodes-base.code", 2, {"mode": "runOnceForEachItem", "jsCode": "const user = $input.item.json.body.user;\nreturn { json: { content: `Welcome <@${user.id}> to our developer hub! 🚀 Read #rules to get started.` } };"}, [440, 300]),
            ("Send Discord Channel Welcome", "n8n-nodes-base.discord", 2, {"operation": "sendMessage", "channelId": "WELCOME_CHANNEL_ID", "content": "={{ $json.content }}"}, [660, 300])
        ]
    },
    {
        "id": 26,
        "name": "Automated PDF Invoice Data Extractor",
        "category": "06-document-processing-rag",
        "filename": "26-Automated-PDF-Invoice-Data-Extractor.json",
        "description": "Extract vendor name, invoice date, line items, tax, and total amount from PDF invoices using Gemini Vision and store into Airtable.",
        "integrations": "Google Drive + Gemini Vision + Airtable",
        "department": "Finance / Accounting",
        "nodes": [
            ("Invoices Folder File Watcher", "n8n-nodes-base.googleDriveTrigger", 1, {"pollTimes": {"item": [{"mode": "everyMinute"}]}}, [220, 300]),
            ("Download Invoice File", "n8n-nodes-base.googleDrive", 3, {"operation": "download", "fileId": "={{ $json.id }}"}, [440, 300]),
            ("Gemini Vision Invoice Extraction", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Extract JSON data from this invoice: { vendor: string, invoice_number: string, date: string, subtotal: number, tax: number, total: number, items: array }"}, [660, 300]),
            ("Upsert Airtable Accounting Ledger", "n8n-nodes-base.airtable", 2.1, {"operation": "append", "base": "ACCOUNTING_BASE", "table": "Invoices"}, [880, 300])
        ]
    },
    {
        "id": 27,
        "name": "GitHub Issue to Notion Task Synchronizer",
        "category": "04-productivity-tasks",
        "filename": "27-GitHub-Issue-To-Notion-Task-Synchronizer.json",
        "description": "Automatically mirror new GitHub issues and bug reports into your Notion engineering backlog with tags, labels, and links.",
        "integrations": "GitHub + Notion",
        "department": "Engineering / DevOps",
        "nodes": [
            ("GitHub Issue Created Webhook", "n8n-nodes-base.githubTrigger", 1, {"events": ["issues"]}, [220, 300]),
            ("Filter Action Opened", "n8n-nodes-base.if", 2.2, {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict"}, "conditions": [{"id": "c1", "leftValue": "={{ $json.action }}", "rightValue": "opened", "operator": {"type": "string", "operation": "equals"}}], "combinator": "and"}}, [440, 300]),
            ("Create Notion Engineering Task", "n8n-nodes-base.notion", 2.2, {"resource": "databasePage", "operation": "create", "databaseId": "NOTION_DEV_BACKLOG"}, [660, 200])
        ]
    },
    {
        "id": 28,
        "name": "Website Uptime & SSL Expiry Monitor",
        "category": "08-devops-system-monitoring",
        "filename": "28-Website-Uptime-SSL-Expiry-Monitor.json",
        "description": "Ping critical website endpoints and check SSL certificates every 5 minutes; send immediate Telegram alerts if downtime occurs.",
        "integrations": "HTTP Request + Telegram Alert + Cron",
        "department": "DevOps / Infrastructure",
        "nodes": [
            ("Every 5 Minutes Checker", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "minutes", "minutesInterval": 5}]}}, [220, 300]),
            ("Healthcheck HTTP Ping", "n8n-nodes-base.httpRequest", 4.2, {"url": "https://example.com/api/health", "options": {"timeout": 5000}}, [440, 300]),
            ("Evaluate Status Code != 200", "n8n-nodes-base.if", 2.2, {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict"}, "conditions": [{"id": "c1", "leftValue": "={{ $json.statusCode }}", "rightValue": 200, "operator": {"type": "number", "operation": "notEquals"}}], "combinator": "and"}}, [660, 300]),
            ("Dispatch Telegram Down Alert", "n8n-nodes-base.telegram", 1.2, {"operation": "sendMessage", "chatId": "@infra_alerts", "text": "🚨 CRITICAL: Service example.com is DOWN! Status code: {{ $json.statusCode }}"}, [880, 200])
        ]
    },
    {
        "id": 29,
        "name": "Social Media Cross-Poster",
        "category": "07-social-media-marketing",
        "filename": "29-Social-Media-Cross-Poster.json",
        "description": "Write post in Google Sheets → automatically publish across LinkedIn, Twitter/X, and Buffer simultaneously with asset attachments.",
        "integrations": "Google Sheets + LinkedIn + Twitter/X + Buffer",
        "department": "Marketing / Social",
        "nodes": [
            ("Poll Ready Posts from Sheets", "n8n-nodes-base.googleSheets", 4.5, {"operation": "read", "documentId": {"__rl": True, "value": "CONTENT_CALENDAR_SHEET", "mode": "id"}, "sheetName": {"__rl": True, "value": "Posts", "mode": "name"}}, [220, 300]),
            ("Filter Status Ready", "n8n-nodes-base.if", 2.2, {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict"}, "conditions": [{"id": "c1", "leftValue": "={{ $json.Status }}", "rightValue": "Ready", "operator": {"type": "string", "operation": "equals"}}], "combinator": "and"}}, [440, 300]),
            ("Post to LinkedIn API", "n8n-nodes-base.httpRequest", 4.2, {"method": "POST", "url": "https://api.linkedin.com/v2/ugcPosts"}, [660, 200]),
            ("Post to Twitter / X", "n8n-nodes-base.twitter", 2, {"operation": "create", "text": "={{ $json.Content }}"}, [660, 400]),
            ("Mark Post Published in Sheets", "n8n-nodes-base.googleSheets", 4.5, {"operation": "update", "documentId": {"__rl": True, "value": "CONTENT_CALENDAR_SHEET", "mode": "id"}, "sheetName": {"__rl": True, "value": "Posts", "mode": "name"}}, [880, 300])
        ]
    },
    {
        "id": 30,
        "name": "Google Calendar to Slack Daily Standup Notifier",
        "category": "04-productivity-tasks",
        "filename": "30-Google-Calendar-To-Slack-Daily-Standup-Notifier.json",
        "description": "Extract today's agenda, milestones, and meeting links from Google Calendar at 9 AM and broadcast formatted agenda to team Slack channel.",
        "integrations": "Google Calendar + Slack",
        "department": "Productivity / Team",
        "nodes": [
            ("9 AM Weekday Trigger", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "hours", "hoursInterval": 24}]}}, [220, 300]),
            ("Retrieve Daily Calendar Events", "n8n-nodes-base.googleCalendar", 1.2, {"operation": "getAll", "options": {"timeMin": "={{ $now.startOf('day').toISO() }}", "timeMax": "={{ $now.endOf('day').toISO() }}"}}, [440, 300]),
            ("Format Slack Standup Message", "n8n-nodes-base.code", 2, {"mode": "runOnceForAllItems", "jsCode": "const items = $input.all();\nconst eventLines = items.map(i => `• *${i.json.summary}* (${i.json.start.dateTime ? new Date(i.json.start.dateTime).toLocaleTimeString() : 'All day'})`).join('\\n');\nreturn [{ json: { text: `☀️ *Good Morning Team! Here is today's schedule:*\\n\\n${eventLines}` } }];"}, [660, 300]),
            ("Broadcast to #standup Slack", "n8n-nodes-base.slack", 2.2, {"operation": "postMessage", "channel": "#daily-standup", "text": "={{ $json.text }}"}, [880, 300])
        ]
    },
    {
        "id": 31,
        "name": "App Store Review Sentiment Monitor",
        "category": "07-social-media-marketing",
        "filename": "31-App-Store-Review-Sentiment-Monitor.json",
        "description": "Fetch iOS App Store and Google Play reviews via RSS, score sentiment with Gemini, and alert product team on negative feedback.",
        "integrations": "RSS + Google Gemini + Slack",
        "department": "Product / Mobile",
        "nodes": [
            ("Check App Reviews RSS Hourly", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "hours", "hoursInterval": 1}]}}, [220, 300]),
            ("Fetch App Store RSS Feed", "n8n-nodes-base.rssFeedRead", 1.1, {"url": "https://itunes.apple.com/us/rss/customerreviews/id=YOUR_APP_ID/xml"}, [440, 300]),
            ("Gemini Sentiment Analysis", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Review: {{ $json.content }}. Identify sentiment, rating, and whether it mentions a critical bug or crash."}, [660, 300]),
            ("Alert Slack on Negative / Bug", "n8n-nodes-base.slack", 2.2, {"operation": "postMessage", "channel": "#product-feedback", "text": "⚠️ *New Critical App Review:*\\n{{ $json.output }}"}, [880, 300])
        ]
    },
    {
        "id": 32,
        "name": "Stripe Failed Payment Recovery Dunning Bot",
        "category": "01-email-automation",
        "filename": "32-Stripe-Failed-Payment-Recovery-Dunning-Bot.json",
        "description": "Catch Stripe charge.failed webhooks, notify finance team in Slack, and send automated polite card update request to customer.",
        "integrations": "Stripe + Gmail + Slack",
        "department": "Finance / Revenue Ops",
        "nodes": [
            ("Stripe Charge Failed Webhook", "n8n-nodes-base.stripeTrigger", 1, {"events": ["charge.failed"]}, [220, 300]),
            ("Send Customer Dunning Email", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "={{ $json.data.object.billing_details.email }}", "subject": "Action Needed: Update Payment Method for Your Subscription", "message": "=Hi {{ $json.data.object.billing_details.name }},\\n\\nWe were unable to process your recent payment of ${{ $json.data.object.amount / 100 }}. Please update your billing details here to avoid service interruption: https://billing.example.com"}, [440, 300]),
            ("Post to Slack Revenue Recovery", "n8n-nodes-base.slack", 2.2, {"operation": "postMessage", "channel": "#failed-payments", "text": "⚠️ Failed Charge: ${{ $json.data.object.amount / 100 }} from {{ $json.data.object.billing_details.email }}"}, [660, 300])
        ]
    },
    {
        "id": 33,
        "name": "Notion Database Auto-Backup to Drive",
        "category": "06-document-processing-rag",
        "filename": "33-Notion-Database-Auto-Backup-To-Drive.json",
        "description": "Weekly automated backup of critical Notion databases exported to JSON/CSV and saved in organized Google Drive backup archives.",
        "integrations": "Notion API + Google Drive + Cron",
        "department": "DevOps / IT",
        "nodes": [
            ("Weekly Sunday Midnight Cron", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "weeks", "weeksInterval": 1}]}}, [220, 300]),
            ("Query Entire Notion Database", "n8n-nodes-base.notion", 2.2, {"resource": "databasePage", "operation": "getAll", "databaseId": "NOTION_KNOWLEDGE_DB"}, [440, 300]),
            ("Serialize to JSON Archive", "n8n-nodes-base.code", 2, {"mode": "runOnceForAllItems", "jsCode": "return [{ json: { filename: `notion_backup_${new Date().toISOString().split('T')[0]}.json`, data: JSON.stringify($input.all()) } }];"}, [660, 300]),
            ("Upload Backup to Google Drive", "n8n-nodes-base.googleDrive", 3, {"operation": "createFromText", "name": "={{ $json.filename }}"}, [880, 300])
        ]
    },
    {
        "id": 34,
        "name": "Airtable B2B Lead Enrichment Pipeline",
        "category": "03-lead-generation-crm",
        "filename": "34-Airtable-B2B-Lead-Enrichment-Pipeline.json",
        "description": "When a new lead is added to Airtable, enrich company revenue, employee count, and CEO contact via Hunter/Clearbit APIs.",
        "integrations": "Airtable + Hunter/Clearbit API + Google Sheets",
        "department": "Sales / Growth",
        "nodes": [
            ("Airtable New Lead Trigger", "n8n-nodes-base.airtableTrigger", 1, {"table": "Leads"}, [220, 300]),
            ("Enrich Company via Clearbit API", "n8n-nodes-base.httpRequest", 4.2, {"url": "=https://company.clearbit.com/v2/companies/find?domain={{ $json.fields.Domain }}"}, [440, 300]),
            ("Update Airtable Enriched Data", "n8n-nodes-base.airtable", 2.1, {"operation": "update", "table": "Leads"}, [660, 300])
        ]
    },
    {
        "id": 35,
        "name": "AI Audio Meeting Notes & Action Item Extractor",
        "category": "04-productivity-tasks",
        "filename": "35-AI-Audio-Meeting-Notes-Action-Item-Extractor.json",
        "description": "Upload recorded meeting audio to Drive → transcribe with Whisper/Gemini → extract key action items and create Notion tasks.",
        "integrations": "Drive Audio + Whisper/Gemini + Notion",
        "department": "Executive / Operations",
        "nodes": [
            ("Watch Meeting Recordings Folder", "n8n-nodes-base.googleDriveTrigger", 1, {"pollTimes": {"item": [{"mode": "everyMinute"}]}}, [220, 300]),
            ("Download Audio Recording", "n8n-nodes-base.googleDrive", 3, {"operation": "download", "fileId": "={{ $json.id }}"}, [440, 300]),
            ("Gemini Meeting Analyzer", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Extract meeting summary, decisions reached, and specific action items with assignees from this meeting recording transcript."}, [660, 300]),
            ("Create Meeting Notes in Notion", "n8n-nodes-base.notion", 2.2, {"resource": "databasePage", "operation": "create", "databaseId": "NOTION_MEETINGS_DB"}, [880, 300])
        ]
    },
    {
        "id": 36,
        "name": "Shopify New Order Fulfillment & SMS Notifier",
        "category": "09-finance-ecommerce",
        "filename": "36-Shopify-New-Order-Fulfillment-SMS-Notifier.json",
        "description": "Trigger on new paid Shopify orders, record in fulfillment Google Sheets, and send tracking SMS to customer via Twilio.",
        "integrations": "Shopify + Twilio + Google Sheets",
        "department": "E-Commerce / Fulfillment",
        "nodes": [
            ("Shopify Order Paid Trigger", "n8n-nodes-base.shopifyTrigger", 1, {"event": "orders/paid"}, [220, 300]),
            ("Record in Orders Google Sheet", "n8n-nodes-base.googleSheets", 4.5, {"operation": "append", "documentId": {"__rl": True, "value": "SHOPIFY_ORDERS_SHEET", "mode": "id"}, "sheetName": {"__rl": True, "value": "Orders", "mode": "name"}}, [440, 300]),
            ("Send Twilio Shipping SMS", "n8n-nodes-base.twilio", 1, {"operation": "send", "to": "={{ $json.phone }}", "message": "=Order #{{ $json.order_number }} confirmed! We are preparing your shipment. Track updates here: {{ $json.order_status_url }}"}, [660, 300])
        ]
    },
    {
        "id": 37,
        "name": "Competitor Price Monitor & Alert",
        "category": "09-finance-ecommerce",
        "filename": "37-Competitor-Price-Monitor-Alert.json",
        "description": "Scrape competitor product pages every 6 hours, track pricing fluctuations in Google Sheets, and email alerts on price drops.",
        "integrations": "HTTP Scraping + HTML Node + Sheets + Gmail",
        "department": "E-Commerce / Pricing Strategy",
        "nodes": [
            ("Every 6 Hours Trigger", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "hours", "hoursInterval": 6}]}}, [220, 300]),
            ("Fetch Competitor Webpage", "n8n-nodes-base.httpRequest", 4.2, {"url": "https://competitor.com/product/widget"}, [440, 300]),
            ("Extract Price HTML", "n8n-nodes-base.html", 1.2, {"operation": "extractHtmlContent", "dataPropertyName": "data", "extractionValues": {"values": [{"key": "price", "cssSelector": ".product-price", "returnValue": "text"}]}}, [660, 300]),
            ("Compare & Log in Sheets", "n8n-nodes-base.googleSheets", 4.5, {"operation": "append", "documentId": {"__rl": True, "value": "COMPETITOR_PRICES_SHEET", "mode": "id"}, "sheetName": {"__rl": True, "value": "Prices", "mode": "name"}}, [880, 300])
        ]
    },
    {
        "id": 38,
        "name": "Telegram Multi-Language Translation Bot",
        "category": "05-chatbots-telegram-whatsapp",
        "filename": "38-Telegram-Multi-Language-Translation-Bot.json",
        "description": "Instant Telegram translation bot: detects language of incoming messages or audio and returns accurate translations in 50+ languages.",
        "integrations": "Telegram + Google Gemini Translator",
        "department": "Support / International",
        "nodes": [
            ("Telegram Inbound Text", "n8n-nodes-base.telegramTrigger", 1.1, {"updates": ["message"]}, [220, 300]),
            ("Gemini Multilingual Translator", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Translate the following message into English, Spanish, German, and Arabic with language tags:\\n{{ $json.message.text }}"}, [440, 300]),
            ("Send Translated Message", "n8n-nodes-base.telegram", 1.2, {"operation": "sendMessage", "chatId": "={{ $('Telegram Inbound Text').item.json.message.chat.id }}", "text": "={{ $json.output }}"}, [660, 300])
        ]
    },
    {
        "id": 39,
        "name": "Zendesk Critical Ticket Escalator",
        "category": "05-chatbots-telegram-whatsapp",
        "filename": "39-Zendesk-Critical-Ticket-Escalator.json",
        "description": "Detect VIP or urgent priority tickets in Zendesk, immediately page on-call engineers via Slack and SMS escalation.",
        "integrations": "Zendesk + Slack On-Call + Twilio SMS",
        "department": "Support / Engineering Ops",
        "nodes": [
            ("Zendesk Ticket Webhook", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "zendesk-ticket-alert"}, [220, 300]),
            ("Check Priority Urgent", "n8n-nodes-base.if", 2.2, {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict"}, "conditions": [{"id": "c1", "leftValue": "={{ $json.body.priority }}", "rightValue": "urgent", "operator": {"type": "string", "operation": "equals"}}], "combinator": "and"}}, [440, 300]),
            ("Post to On-Call Slack", "n8n-nodes-base.slack", 2.2, {"operation": "postMessage", "channel": "#incident-room", "text": "🚨 URGENT ZENDESK TICKET: {{ $json.body.subject }} from {{ $json.body.requester_email }}"}, [660, 200])
        ]
    },
    {
        "id": 40,
        "name": "WordPress Auto-Publisher & SEO Optimizer",
        "category": "07-social-media-marketing",
        "filename": "40-WordPress-Auto-Publisher-SEO-Optimizer.json",
        "description": "Generate SEO-optimized blog posts with Gemini AI from keyword briefs, format headings & meta tags, and publish as WordPress drafts.",
        "integrations": "Gemini + WordPress API + Yoast",
        "department": "Marketing / Content",
        "nodes": [
            ("New Topic in Sheets", "n8n-nodes-base.googleSheets", 4.5, {"operation": "read", "documentId": {"__rl": True, "value": "WP_TOPICS_SHEET", "mode": "id"}, "sheetName": {"__rl": True, "value": "Drafts", "mode": "name"}}, [220, 300]),
            ("Gemini Article & SEO Meta Writer", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Write an in-depth 1500-word blog post on '{{ $json.Topic }}' including HTML headings (h2, h3), meta title, meta description, and tags."}, [440, 300]),
            ("Create WordPress Draft Post", "n8n-nodes-base.wordpress", 1, {"operation": "create", "title": "={{ $json.Topic }}", "content": "={{ $json.output }}"}, [660, 300])
        ]
    },
    {
        "id": 41,
        "name": "Expense Receipt Scanner & Categorizer",
        "category": "06-document-processing-rag",
        "filename": "41-Expense-Receipt-Scanner-Categorizer.json",
        "description": "Snap a receipt image via Telegram or Drive → parse merchant, category, date, and amount with Gemini Vision → log into expense sheet.",
        "integrations": "Telegram/Drive + Gemini Vision + Google Sheets",
        "department": "Finance / Personal Operations",
        "nodes": [
            ("Telegram Photo Receipt", "n8n-nodes-base.telegramTrigger", 1.1, {"updates": ["message"]}, [220, 300]),
            ("Download Photo File", "n8n-nodes-base.telegram", 1.2, {"operation": "getFile", "fileId": "={{ $json.message.photo.slice(-1)[0].file_id }}"}, [440, 300]),
            ("Gemini Vision Receipt OCR", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Extract receipt details: { merchant: string, date: string, category: [Meals, Travel, Software, Office], amount: number, currency: string }"}, [660, 300]),
            ("Append to Expenses Sheet", "n8n-nodes-base.googleSheets", 4.5, {"operation": "append", "documentId": {"__rl": True, "value": "EXPENSES_SHEET_ID", "mode": "id"}, "sheetName": {"__rl": True, "value": "Receipts", "mode": "name"}}, [880, 300])
        ]
    },
    {
        "id": 42,
        "name": "RSS Feed to Newsletter Draft Generator",
        "category": "01-email-automation",
        "filename": "42-RSS-Feed-To-Newsletter-Draft-Generator.json",
        "description": "Collect weekly industry articles, generate curated newsletter commentary with Gemini AI, and draft Mailchimp / Gmail campaigns.",
        "integrations": "RSS + Google Gemini + Gmail / Mailchimp",
        "department": "Marketing / Editorial",
        "nodes": [
            ("Weekly Friday Cron", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "weeks", "weeksInterval": 1}]}}, [220, 300]),
            ("Read Curated RSS Feeds", "n8n-nodes-base.rssFeedRead", 1.1, {"url": "https://techcrunch.com/feed/"}, [440, 300]),
            ("Gemini Newsletter Curator", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Compose this week's 5-minute tech dispatch newsletter from top articles:\\n{{ $json.title }} - {{ $json.snippet }}"}, [660, 300]),
            ("Save Gmail Newsletter Draft", "n8n-nodes-base.gmail", 2.1, {"operation": "createDraft", "subject": "📰 This Week in Automation - Curated Digest", "message": "={{ $json.output }}"}, [880, 300])
        ]
    },
    {
        "id": 43,
        "name": "Supabase Database Change Webhook to Slack",
        "category": "08-devops-system-monitoring",
        "filename": "43-Supabase-Database-Change-Webhook-To-Slack.json",
        "description": "Listen to Supabase Database Webhooks on insert/update in critical tables (e.g., users, subscriptions) and alert Slack with change diff.",
        "integrations": "Supabase + Slack Notification",
        "department": "DevOps / Engineering",
        "nodes": [
            ("Supabase Webhook Trigger", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "supabase-db-changes"}, [220, 300]),
            ("Format Change Event", "n8n-nodes-base.code", 2, {"mode": "runOnceForEachItem", "jsCode": "const change = $input.item.json.body;\nreturn { json: { text: `🔔 *Supabase Table [${change.table}]* event: *${change.type}*\\nRecord ID: ${change.record ? change.record.id : 'N/A'}` } };"}, [440, 300]),
            ("Post to Engineering Slack", "n8n-nodes-base.slack", 2.2, {"operation": "postMessage", "channel": "#db-activity", "text": "={{ $json.text }}"}, [660, 300])
        ]
    },
    {
        "id": 44,
        "name": "Google Forms Quiz Auto-Grader & Certificate Generator",
        "category": "09-finance-ecommerce",
        "filename": "44-Google-Forms-Quiz-Auto-Grader-Certificate-Generator.json",
        "description": "Automatically grade student quiz submissions from Google Forms, calculate scores, generate PDF certificates, and email recipients.",
        "integrations": "Forms + Sheets + PDF + Gmail",
        "department": "Education / Operations",
        "nodes": [
            ("Quiz Submission Trigger", "n8n-nodes-base.googleSheets", 4.5, {"operation": "read", "documentId": {"__rl": True, "value": "QUIZ_RESPONSES_SHEET", "mode": "id"}, "sheetName": {"__rl": True, "value": "Submissions", "mode": "name"}}, [220, 300]),
            ("Calculate Score Code", "n8n-nodes-base.code", 2, {"mode": "runOnceForEachItem", "jsCode": "const sub = $input.item.json;\nconst score = (sub.q1 === 'A' ? 25 : 0) + (sub.q2 === 'C' ? 25 : 0) + (sub.q3 === 'B' ? 25 : 0) + (sub.q4 === 'D' ? 25 : 0);\nreturn { json: { ...sub, score, passed: score >= 75 } };"}, [440, 300]),
            ("Send Completion Certificate Email", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "={{ $json.email }}", "subject": "🎓 Congratulations! Your Certificate of Completion", "message": "=Hi {{ $json.name }},\\n\\nYou scored {{ $json.score }}%! You passed the automation proficiency test." }, [660, 300])
        ]
    },
    {
        "id": 45,
        "name": "Customer Churn Risk Analyzer",
        "category": "03-lead-generation-crm",
        "filename": "45-Customer-Churn-Risk-Analyzer.json",
        "description": "Analyze usage metrics, ticket frequency, and login patterns to identify churn risk and trigger customer success retention playbooks.",
        "integrations": "Sheets/Postgres + Google Gemini + Slack Alert",
        "department": "Customer Success",
        "nodes": [
            ("Weekly Usage Ingestion", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "weeks", "weeksInterval": 1}]}}, [220, 300]),
            ("Read Customer Activity", "n8n-nodes-base.googleSheets", 4.5, {"operation": "read", "documentId": {"__rl": True, "value": "CUSTOMER_ACTIVITY_SHEET", "mode": "id"}, "sheetName": {"__rl": True, "value": "Accounts", "mode": "name"}}, [440, 300]),
            ("Gemini Churn Risk Predictor", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Analyze account activity for {{ $json.company }}: logins decreased by {{ $json.login_drop }}%, opened {{ $json.support_tickets }} support tickets. Predict churn risk (High/Medium/Low) and recommend retention action."}, [660, 300]),
            ("Alert CS Team on Slack", "n8n-nodes-base.slack", 2.2, {"operation": "postMessage", "channel": "#customer-retention", "text": "⚠️ *High Churn Risk Detected:*\\n{{ $json.output }}"}, [880, 300])
        ]
    },
    {
        "id": 46,
        "name": "Automated Weekly KPI Analytics Report",
        "category": "09-finance-ecommerce",
        "filename": "46-Automated-Weekly-KPI-Analytics-Report.json",
        "description": "Aggregate weekly revenue, customer acquisition cost, active users, and conversions into an executive Gemini AI briefing.",
        "integrations": "Sheets + Google Gemini + Gmail + Slack",
        "department": "Executive / Finance",
        "nodes": [
            ("Monday 8 AM Trigger", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "weeks", "weeksInterval": 1}]}}, [220, 300]),
            ("Collect KPI Metrics from Sheets", "n8n-nodes-base.googleSheets", 4.5, {"operation": "read", "documentId": {"__rl": True, "value": "KPI_METRICS_SHEET", "mode": "id"}, "sheetName": {"__rl": True, "value": "Weekly", "mode": "name"}}, [440, 300]),
            ("Gemini Executive Synthesis", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Create a concise weekly KPI leadership briefing with MoM trends, green/yellow/red indicators, and focus areas: {{ JSON.stringify($json) }}"}, [660, 300]),
            ("Email Leadership Team", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "execs@example.com", "subject": "📊 Weekly Executive KPI Summary", "message": "={{ $json.output }}"}, [880, 300])
        ]
    },
    {
        "id": 47,
        "name": "Jira Sprint Digest & Blocker Alert",
        "category": "04-productivity-tasks",
        "filename": "47-Jira-Sprint-Digest-Blocker-Alert.json",
        "description": "Check active Jira sprint status daily, flag stale or blocked tickets, and broadcast status to engineering team Slack channel.",
        "integrations": "Jira Software + Slack",
        "department": "Engineering / Agile",
        "nodes": [
            ("Daily 9:30 AM Sprint Check", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "hours", "hoursInterval": 24}]}}, [220, 300]),
            ("Fetch Blocked Jira Issues", "n8n-nodes-base.jira", 1, {"operation": "getAll", "jql": "sprint in openSprints() AND (status = 'Blocked' OR flag = 'Impediment')"}, [440, 300]),
            ("Broadcast Blockers to Slack", "n8n-nodes-base.slack", 2.2, {"operation": "postMessage", "channel": "#dev-sprint", "text": "🚧 *Sprint Impediments Found:*\\n{{ $json.key }}: {{ $json.fields.summary }} (Assigned: {{ $json.fields.assignee.displayName }})"}, [660, 300])
        ]
    },
    {
        "id": 48,
        "name": "Voice Memo to Todoist Task Converter",
        "category": "04-productivity-tasks",
        "filename": "48-Voice-Memo-To-Todoist-Task-Converter.json",
        "description": "Send a Telegram voice memo on the go → transcribe audio with Gemini → extract task title, due date, and priority → create Todoist task.",
        "integrations": "Telegram Voice + Whisper/Gemini + Todoist",
        "department": "Productivity / Personal",
        "nodes": [
            ("Telegram Voice Note Trigger", "n8n-nodes-base.telegramTrigger", 1.1, {"updates": ["message"]}, [220, 300]),
            ("Download Audio Memo", "n8n-nodes-base.telegram", 1.2, {"operation": "getFile", "fileId": "={{ $json.message.voice.file_id }}"}, [440, 300]),
            ("Gemini Voice Task Extractor", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Extract task from voice note: { task_name: string, due_date: string, priority: [1,2,3,4] }"}, [660, 300]),
            ("Create Todoist Task", "n8n-nodes-base.todoist", 2, {"operation": "create", "content": "={{ $json.task_name }}", "dueString": "={{ $json.due_date }}"}, [880, 300])
        ]
    },
    {
        "id": 49,
        "name": "HubSpot Deal Stage Change Automator",
        "category": "03-lead-generation-crm",
        "filename": "49-HubSpot-Deal-Stage-Change-Automator.json",
        "description": "Trigger on HubSpot deal status progression, notify account executives in Slack, and create onboarding checklists when deals close-won.",
        "integrations": "HubSpot + Slack + Google Sheets",
        "department": "Sales / Operations",
        "nodes": [
            ("HubSpot Deal Stage Trigger", "n8n-nodes-base.hubspotTrigger", 1, {"events": ["deal.propertyChange"]}, [220, 300]),
            ("Check Won Status", "n8n-nodes-base.if", 2.2, {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict"}, "conditions": [{"id": "c1", "leftValue": "={{ $json.propertyValue }}", "rightValue": "closedwon", "operator": {"type": "string", "operation": "equals"}}], "combinator": "and"}}, [440, 300]),
            ("Celebrate Closed Deal in Slack", "n8n-nodes-base.slack", 2.2, {"operation": "postMessage", "channel": "#sales-wins", "text": "🎉 *DEAL CLOSED WON!* Deal ID: {{ $json.objectId }}"}, [660, 200]),
            ("Log in Won Deals Ledger", "n8n-nodes-base.googleSheets", 4.5, {"operation": "append", "documentId": {"__rl": True, "value": "WON_DEALS_SHEET", "mode": "id"}, "sheetName": {"__rl": True, "value": "Wins", "mode": "name"}}, [660, 400])
        ]
    },
    {
        "id": 50,
        "name": "Docker Container Health & Restart Alert",
        "category": "08-devops-system-monitoring",
        "filename": "50-Docker-Container-Health-Restart-Alert.json",
        "description": "Listen to Docker container daemon crash events or exit codes via webhook/socket and send high-priority Telegram alerts.",
        "integrations": "Webhook + SSH/Bash + Telegram",
        "department": "DevOps / Infrastructure",
        "nodes": [
            ("Docker Event Webhook", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "docker-events"}, [220, 300]),
            ("Filter Die or OOM Events", "n8n-nodes-base.if", 2.2, {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict"}, "conditions": [{"id": "c1", "leftValue": "={{ $json.body.Action }}", "rightValue": "die", "operator": {"type": "string", "operation": "equals"}}], "combinator": "and"}}, [440, 300]),
            ("Alert On-Call via Telegram", "n8n-nodes-base.telegram", 1.2, {"operation": "sendMessage", "chatId": "@ops_alerts", "text": "🔥 DOCKER CONTAINER CRASHED: {{ $json.body.Actor.Attributes.name }} (ExitCode: {{ $json.body.Actor.Attributes.exitCode }})"}, [660, 200])
        ]
    },
    {
        "id": 51,
        "name": "Contract Clause Extractor & Compliance Auditor",
        "category": "06-document-processing-rag",
        "filename": "51-Contract-Clause-Extractor-Compliance-Auditor.json",
        "description": "Scan legal agreements and NDAs in Drive, extract indemnity, termination, and confidentiality clauses, and audit against company policy.",
        "integrations": "Google Drive + Google Gemini + Airtable",
        "department": "Legal / Operations",
        "nodes": [
            ("Drive Contract Added Trigger", "n8n-nodes-base.googleDriveTrigger", 1, {"pollTimes": {"item": [{"mode": "everyMinute"}]}}, [220, 300]),
            ("Download Agreement PDF", "n8n-nodes-base.googleDrive", 3, {"operation": "download", "fileId": "={{ $json.id }}"}, [440, 300]),
            ("Gemini Legal Clause Auditor", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Extract and evaluate clauses: 1) Governing Law, 2) Term & Termination, 3) Limitation of Liability, 4) Non-compete scope. Flag non-standard terms."}, [660, 300]),
            ("Log in Legal Audit Database", "n8n-nodes-base.airtable", 2.1, {"operation": "append", "base": "LEGAL_BASE", "table": "Agreements"}, [880, 300])
        ]
    },
    {
        "id": 52,
        "name": "Multi-Language Webhook FAQ Assistant",
        "category": "05-chatbots-telegram-whatsapp",
        "filename": "52-Multi-Language-Webhook-FAQ-Assistant.json",
        "description": "Embeddable API endpoint connecting web apps to a Gemini-powered RAG vector store for instant, accurate product FAQ answers.",
        "integrations": "Webhook + Google Gemini RAG + Pinecone",
        "department": "Support / Engineering",
        "nodes": [
            ("Inbound FAQ API Request", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "api/v1/ask-faq", "responseMode": "lastNode"}, [220, 300]),
            ("Gemini Knowledge Base Agent", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Answer question based on verified product knowledge base: {{ $json.body.question }}"}, [440, 300]),
            ("Return JSON API Response", "n8n-nodes-base.respondToWebhook", 1.1, {"options": {"responseCode": 200}, "respondWith": "json", "responseBody": "{\"status\": 200, \"answer\": \"{{ $json.output }}\"}"}, [660, 300])
        ]
    },
    {
        "id": 53,
        "name": "Creative Asset Prompt & Cloudinary Uploader",
        "category": "07-social-media-marketing",
        "filename": "53-Creative-Asset-Prompt-Cloudinary-Uploader.json",
        "description": "Convert marketing copy into Midjourney/DALL-E image prompts with Gemini AI, process output, and organize on Cloudinary CDN.",
        "integrations": "Google Gemini + Cloudinary API",
        "department": "Marketing / Design",
        "nodes": [
            ("Marketing Campaign Trigger", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "generate-creative-assets"}, [220, 300]),
            ("Gemini Image Prompt Architect", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Transform this marketing angle: '{{ $json.body.campaign_concept }}' into 3 cinematic photorealistic Midjourney prompts with lighting, camera angles, and color palettes."}, [440, 300]),
            ("Save to Assets Tracker", "n8n-nodes-base.googleSheets", 4.5, {"operation": "append", "documentId": {"__rl": True, "value": "CREATIVE_ASSETS_SHEET", "mode": "id"}, "sheetName": {"__rl": True, "value": "Prompts", "mode": "name"}}, [660, 300])
        ]
    },
    {
        "id": 54,
        "name": "Trello Board Auto-Archiver & Weekly Digest",
        "category": "04-productivity-tasks",
        "filename": "54-Trello-Board-Auto-Archiver-Weekly-Digest.json",
        "description": "Clean completed cards from Trello 'Done' columns automatically every Friday and dispatch summary of completed deliverables via email.",
        "integrations": "Trello + Gmail",
        "department": "Project Management",
        "nodes": [
            ("Friday 5 PM Schedule", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "weeks", "weeksInterval": 1}]}}, [220, 300]),
            ("Get Completed Cards from Trello", "n8n-nodes-base.trello", 1, {"operation": "getAll", "listId": "TRELLO_DONE_LIST_ID"}, [440, 300]),
            ("Archive Completed Cards", "n8n-nodes-base.trello", 1, {"operation": "update", "id": "={{ $json.id }}", "closed": True}, [660, 300]),
            ("Email Weekly Accomplishments", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "team@example.com", "subject": "🎉 Weekly Team Completed Deliverables", "message": "All cards in Done list archived successfully for sprint wrap."}, [880, 300])
        ]
    },
    {
        "id": 55,
        "name": "Typeform NPS Survey Sentiment Dashboard",
        "category": "03-lead-generation-crm",
        "filename": "55-Typeform-NPS-Survey-Sentiment-Dashboard.json",
        "description": "Receive new Typeform Net Promoter Score (NPS) surveys, classify detractors vs promoters with Gemini AI, and log in Google Sheets.",
        "integrations": "Typeform + Google Gemini + Google Sheets",
        "department": "Customer Success",
        "nodes": [
            ("Typeform Submission Webhook", "n8n-nodes-base.typeformTrigger", 1, {"formId": "NPS_FORM_ID"}, [220, 300]),
            ("Gemini Detractor / Promoter Tagger", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Evaluate NPS response score {{ $json.score }} and comment: '{{ $json.comment }}'. Recommend immediate retention steps if score < 7."}, [440, 300]),
            ("Update NPS Master Sheet", "n8n-nodes-base.googleSheets", 4.5, {"operation": "append", "documentId": {"__rl": True, "value": "NPS_DASHBOARD_SHEET", "mode": "id"}, "sheetName": {"__rl": True, "value": "Scores", "mode": "name"}}, [660, 300])
        ]
    },
    {
        "id": 56,
        "name": "Google Drive Duplicate File Cleanup Helper",
        "category": "06-document-processing-rag",
        "filename": "56-Google-Drive-Duplicate-File-Cleanup-Helper.json",
        "description": "Scan designated Google Drive shared drives, detect duplicate files by MD5 checksum and filename, and generate cleanup report.",
        "integrations": "Google Drive + Code Node",
        "department": "IT / Operations",
        "nodes": [
            ("Weekly Drive Scan Schedule", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "weeks", "weeksInterval": 1}]}}, [220, 300]),
            ("List All Files in Drive", "n8n-nodes-base.googleDrive", 3, {"operation": "list", "useSharedDrive": True}, [440, 300]),
            ("Detect Duplicate Checksums", "n8n-nodes-base.code", 2, {"mode": "runOnceForAllItems", "jsCode": "const items = $input.all();\nconst seen = new Map();\nconst duplicates = [];\nfor (const item of items) {\n  const hash = item.json.md5Checksum || item.json.name;\n  if (seen.has(hash)) {\n    duplicates.push({ original: seen.get(hash), duplicate: item.json });\n  } else {\n    seen.set(hash, item.json);\n  }\n}\nreturn [{ json: { duplicates, count: duplicates.length } }];"}, [660, 300]),
            ("Email IT Cleanup Report", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "admin@example.com", "subject": "🧹 Google Drive Duplicate Audit Results", "message": "Found {{ $json.count }} potential duplicates for review."}, [880, 300])
        ]
    },
    {
        "id": 57,
        "name": "Real Estate Listing Scraper & Lead Matcher",
        "category": "09-finance-ecommerce",
        "filename": "57-Real-Estate-Listing-Scraper-Lead-Matcher.json",
        "description": "Monitor property listings via API / scraping, match features against buyer criteria with Gemini, and dispatch instant Telegram alerts.",
        "integrations": "HTTP Request + Google Gemini + Telegram",
        "department": "Real Estate / Sales",
        "nodes": [
            ("Every 2 Hours Schedule", "n8n-nodes-base.scheduleTrigger", 1.2, {"rule": {"interval": [{"field": "hours", "hoursInterval": 2}]}}, [220, 300]),
            ("Fetch New Listings API", "n8n-nodes-base.httpRequest", 4.2, {"url": "https://api.propertydata.example/feed"}, [440, 300]),
            ("Gemini Buyer Preference Match", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Compare new listing (Price: ${{ $json.price }}, Location: {{ $json.city }}, Beds: {{ $json.beds }}) against buyer profiles. Find high-match buyers."}, [660, 300]),
            ("Alert Agent on Telegram", "n8n-nodes-base.telegram", 1.2, {"operation": "sendMessage", "chatId": "@property_leads", "text": "🏡 *High Match Property Match Found:*\\n{{ $json.output }}"}, [880, 300])
        ]
    },
    {
        "id": 58,
        "name": "Employee Onboarding Automation Pipeline",
        "category": "04-productivity-tasks",
        "filename": "58-Employee-Onboarding-Automation-Pipeline.json",
        "description": "Triggered when candidate signs offer letter: creates Google Workspace account, invites to Slack channels, and provisions Notion onboarding page.",
        "integrations": "Google Forms + Google Workspace + Slack + Notion",
        "department": "HR / People Ops",
        "nodes": [
            ("New Hire Form Webhook", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "new-hire-onboarding"}, [220, 300]),
            ("Create Slack User Account / Invite", "n8n-nodes-base.slack", 2.2, {"operation": "postMessage", "channel": "#hr-internal", "text": "👋 Starting onboarding for {{ $json.body.first_name }} {{ $json.body.last_name }} (Role: {{ $json.body.role }})"}, [440, 300]),
            ("Provision Notion Onboarding Hub", "n8n-nodes-base.notion", 2.2, {"resource": "databasePage", "operation": "create", "databaseId": "NOTION_ONBOARDING_DB"}, [660, 300]),
            ("Send Welcome Kit Email", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "={{ $json.body.personal_email }}", "subject": "Welcome to the Team! 🚀 Your First Week Guide", "message": "Hi {{ $json.body.first_name }}, we are thrilled to welcome you! Check your onboarding plan here."}, [880, 300])
        ]
    },
    {
        "id": 59,
        "name": "LinkedIn Connection Request Follow-Up Scheduler",
        "category": "03-lead-generation-crm",
        "filename": "59-LinkedIn-Connection-Request-Follow-Up-Scheduler.json",
        "description": "Schedule staggered, personalized follow-up sequences for prospective LinkedIn connections and log touchpoints in Google Sheets.",
        "integrations": "Webhook + Google Sheets + LinkedIn",
        "department": "Sales / Outbound",
        "nodes": [
            ("Connection Accepted Webhook", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "linkedin-connected"}, [220, 300]),
            ("Log in Outbound Sequences Sheet", "n8n-nodes-base.googleSheets", 4.5, {"operation": "append", "documentId": {"__rl": True, "value": "OUTBOUND_SHEET_ID", "mode": "id"}, "sheetName": {"__rl": True, "value": "Outreach", "mode": "name"}}, [440, 300]),
            ("Wait 3 Business Days", "n8n-nodes-base.wait", 1.1, {"unit": "days", "amount": 3}, [660, 300]),
            ("Dispatch Tailored Follow-up Note", "n8n-nodes-base.googleSheets", 4.5, {"operation": "update", "documentId": {"__rl": True, "value": "OUTBOUND_SHEET_ID", "mode": "id"}, "sheetName": {"__rl": True, "value": "Outreach", "mode": "name"}}, [880, 300])
        ]
    },
    {
        "id": 60,
        "name": "E-Commerce Abandoned Cart Recovery Sequence",
        "category": "09-finance-ecommerce",
        "filename": "60-Ecommerce-Abandoned-Cart-Recovery-Sequence.json",
        "description": "Detect abandoned checkouts in Shopify/WooCommerce, wait 2 hours, and dispatch a 10% discount recovery email sequence.",
        "integrations": "Shopify / WooCommerce + Gmail + Delay Timers",
        "department": "E-Commerce / Marketing",
        "nodes": [
            ("Cart Abandoned Webhook", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "cart-abandoned"}, [220, 300]),
            ("Wait 2 Hours", "n8n-nodes-base.wait", 1.1, {"unit": "hours", "amount": 2}, [440, 300]),
            ("Verify Still Unpaid", "n8n-nodes-base.if", 2.2, {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict"}, "conditions": [{"id": "c1", "leftValue": "={{ $json.body.completed }}", "rightValue": False, "operator": {"type": "boolean", "operation": "equals"}}], "combinator": "and"}}, [660, 300]),
            ("Send Recovery Offer Email", "n8n-nodes-base.gmail", 2.1, {"operation": "send", "sendTo": "={{ $json.body.email }}", "subject": "Did you forget something? Here is 10% off your cart!", "message": "Hi {{ $json.body.name }}, your items are waiting. Use code RECOVER10 to complete checkout: {{ $json.body.cart_url }}"}, [880, 200])
        ]
    },
    {
        "id": 61,
        "name": "Notion Knowledge Base RAG Assistant",
        "category": "06-document-processing-rag",
        "filename": "61-Notion-Knowledge-Base-RAG-Assistant.json",
        "description": "Index Notion workspace documents into Qdrant/Pinecone vector embeddings; query company policies via conversational Telegram/Slack bot.",
        "integrations": "Notion + Google Gemini + Qdrant/Pinecone + Telegram",
        "department": "Operations / AI",
        "nodes": [
            ("Telegram Question Received", "n8n-nodes-base.telegramTrigger", 1.1, {"updates": ["message"]}, [220, 300]),
            ("Retrieve Notion Knowledge Base", "n8n-nodes-base.notion", 2.2, {"resource": "databasePage", "operation": "getAll", "databaseId": "NOTION_KNOWLEDGE_BASE_ID"}, [440, 300]),
            ("Gemini RAG Reasoning Engine", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Context from Notion Company Knowledge Base:\\n{{ $json.results }}\\n\\nQuestion: {{ $('Telegram Question Received').item.json.message.text }}\\nAnswer factually with direct citations."}, [660, 300]),
            ("Send Telegram Answer", "n8n-nodes-base.telegram", 1.2, {"operation": "sendMessage", "chatId": "={{ $('Telegram Question Received').item.json.message.chat.id }}", "text": "={{ $json.output }}"}, [880, 300])
        ]
    },
    {
        "id": 62,
        "name": "Autonomous AI Deep Web Research Agent",
        "category": "07-social-media-marketing",
        "filename": "62-Autonomous-AI-Deep-Web-Research-Agent.json",
        "description": "Autonomous multi-step research agent: takes a research question, performs live web queries via SerpAPI, synthesizes findings with Gemini, and produces an executive Google Doc.",
        "integrations": "SerpAPI + Google Gemini + Google Docs / Drive",
        "department": "Research / Strategy",
        "nodes": [
            ("Research Query Webhook", "n8n-nodes-base.webhook", 2, {"httpMethod": "POST", "path": "deep-research", "responseMode": "lastNode"}, [220, 300]),
            ("SerpAPI Web Search", "n8n-nodes-base.httpRequest", 4.2, {"url": "=https://serpapi.com/search.json?q={{ encodeURIComponent($json.body.topic) }}&engine=google"}, [440, 300]),
            ("Gemini Deep Synthesis Agent", "@n8n/n8n-nodes-langchain.agent", 1.7, {"promptType": "define", "text": "=Conduct in-depth market research analysis on '{{ $('Research Query Webhook').item.json.body.topic }}' using search results: {{ JSON.stringify($json.organic_results) }}. Include executive summary, competitor matrix, market trends, and risk factors."}, [660, 300]),
            ("Create Research Brief in Google Drive", "n8n-nodes-base.googleDrive", 3, {"operation": "createFromText", "name": "=Deep Research - {{ $('Research Query Webhook').item.json.body.topic }}.doc"}, [880, 300]),
            ("Return Completed Report Response", "n8n-nodes-base.respondToWebhook", 1.1, {"options": {"responseCode": 200}, "respondWith": "json", "responseBody": "{\"status\": \"completed\", \"summary\": \"{{ $('Gemini Deep Synthesis Agent').item.json.output }}\"}"}, [1100, 300])
        ]
    }
]

def build_n8n_json(wf):
    nodes = []
    node_name_map = {}
    
    for idx, item in enumerate(wf["nodes"]):
        node_name, node_type, type_version, params, pos = item
        node_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{wf['id']}-{node_name}"))
        node_obj = {
            "parameters": params,
            "id": node_id,
            "name": node_name,
            "type": node_type,
            "typeVersion": type_version,
            "position": pos
        }
        nodes.append(node_obj)
        node_name_map[idx] = node_name

    # Build linear connections
    connections = {}
    for i in range(len(wf["nodes"]) - 1):
        src_name = node_name_map[i]
        dst_name = node_name_map[i + 1]
        
        # If source is an IF node, connect to output index 0 (true branch)
        if "if" in wf["nodes"][i][1].lower():
            connections[src_name] = {
                "main": [
                    [
                        {
                            "node": dst_name,
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            }
        else:
            connections[src_name] = {
                "main": [
                    [
                        {
                            "node": dst_name,
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            }

    data = {
        "name": wf["name"],
        "nodes": nodes,
        "pinData": {},
        "connections": connections,
        "active": False,
        "settings": {
            "executionOrder": "v1"
        },
        "versionId": str(uuid.uuid5(uuid.NAMESPACE_DNS, f"version-{wf['id']}")),
        "meta": {
            "templateCredsSetupCompleted": True,
            "instanceId": "awesome-n8n-collection"
        },
        "id": f"wf-{wf['id']:03d}",
        "tags": [
            {
                "name": wf["category"].replace("-", " ").title(),
                "id": f"tag-{wf['category']}"
            }
        ]
    }
    return data

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    templates_dir = os.path.join(base_dir, "templates")
    os.makedirs(templates_dir, exist_ok=True)
    
    generated_count = 0
    for wf in WORKFLOWS:
        cat_dir = os.path.join(templates_dir, wf["category"])
        os.makedirs(cat_dir, exist_ok=True)
        filepath = os.path.join(cat_dir, wf["filename"])
        
        wf_json = build_n8n_json(wf)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(wf_json, f, indent=2, ensure_ascii=False)
        generated_count += 1
        
    print(f"Successfully generated {generated_count} n8n workflow templates.")

if __name__ == "__main__":
    main()
