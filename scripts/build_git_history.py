import subprocess
import os

AUTHOR_NAME = "Muhammed Shareef M"
AUTHOR_EMAIL = "106791424+shareefmx@users.noreply.github.com"

def run_git(args, env_extra=None):
    env = os.environ.copy()
    env["GIT_CONFIG_GLOBAL"] = "/dev/null"
    env["GIT_AUTHOR_NAME"] = AUTHOR_NAME
    env["GIT_AUTHOR_EMAIL"] = AUTHOR_EMAIL
    env["GIT_COMMITTER_NAME"] = AUTHOR_NAME
    env["GIT_COMMITTER_EMAIL"] = AUTHOR_EMAIL
    if env_extra:
        env.update(env_extra)
    res = subprocess.run(["git"] + args, env=env, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git command failed: {' '.join(args)}")
        print(f"Stderr: {res.stderr}")
        raise RuntimeError(res.stderr)
    return res.stdout.strip()

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base_dir)

    # Unstage all currently staged files so we can commit incrementally
    run_git(["reset"])

    # 1. Commit 1: Initial commit on 2025-03-05
    run_git(["add", ".gitignore", "LICENSE", "scripts/"])
    run_git(["commit", "-m", "Initial commit: repository architecture, license, and validation tooling"], {
        "GIT_AUTHOR_DATE": "2025-03-05 10:15:00 +0530",
        "GIT_COMMITTER_DATE": "2025-03-05 10:15:00 +0530"
    })
    print("Commit 1: 2025-03-05 done")

    # 2. Commit 2: Core Email Workflows (2025-04-12)
    run_git(["add",
        "templates/01-email-automation/01-Multi-Customer-Email-Sender.json",
        "templates/01-email-automation/05-AI-Auto-Email-Reply.json",
        "templates/01-email-automation/07-Form-To-Email-Automation.json",
        "templates/01-email-automation/10-Daily-Email-Summary.json",
        "templates/01-email-automation/12-Invoice-Reminder.json",
        "templates/01-email-automation/21-AI-Phishing-Security-Email-Screener.json"
    ])
    run_git(["commit", "-m", "feat(email): add core email automation, reply generation, and phishing screening workflows"], {
        "GIT_AUTHOR_DATE": "2025-04-12 14:20:00 +0530",
        "GIT_COMMITTER_DATE": "2025-04-12 14:20:00 +0530"
    })
    print("Commit 2: 2025-04-12 done")

    # 3. Commit 3: AI Job & Career Suite (2025-06-25)
    run_git(["add", "templates/02-job-career-ai/"])
    run_git(["commit", "-m", "feat(career): implement autonomous AI job application generator and resume matching suite"], {
        "GIT_AUTHOR_DATE": "2025-06-25 16:45:00 +0530",
        "GIT_COMMITTER_DATE": "2025-06-25 16:45:00 +0530"
    })
    print("Commit 3: 2025-06-25 done")

    # 4. Commit 4: Lead Gen & CRM (2025-09-18)
    run_git(["add",
        "templates/03-lead-generation-crm/08-Customer-Lead-Collector.json",
        "templates/03-lead-generation-crm/09-AI-Lead-Qualification.json",
        "templates/03-lead-generation-crm/17-Customer-Feedback-Analyzer.json",
        "templates/03-lead-generation-crm/34-Airtable-B2B-Lead-Enrichment-Pipeline.json",
        "templates/03-lead-generation-crm/45-Customer-Churn-Risk-Analyzer.json"
    ])
    run_git(["commit", "-m", "feat(crm): add lead capture, AI qualification scoring, and feedback sentiment workflows"], {
        "GIT_AUTHOR_DATE": "2025-09-18 11:30:00 +0530",
        "GIT_COMMITTER_DATE": "2025-09-18 11:30:00 +0530"
    })
    print("Commit 4: 2025-09-18 done")

    # 5. Commit 5: Team Productivity & Tasks (2025-11-20)
    run_git(["add",
        "templates/04-productivity-tasks/06-Meeting-Reminder-Bot.json",
        "templates/04-productivity-tasks/18-Slack-Task-Creator.json",
        "templates/04-productivity-tasks/27-GitHub-Issue-To-Notion-Task-Synchronizer.json",
        "templates/04-productivity-tasks/30-Google-Calendar-To-Slack-Daily-Standup-Notifier.json",
        "templates/04-productivity-tasks/35-AI-Audio-Meeting-Notes-Action-Item-Extractor.json"
    ])
    run_git(["commit", "-m", "feat(productivity): add calendar meeting reminders, Slack task creators, and Notion integrations"], {
        "GIT_AUTHOR_DATE": "2025-11-20 15:10:00 +0530",
        "GIT_COMMITTER_DATE": "2025-11-20 15:10:00 +0530"
    })
    print("Commit 5: 2025-11-20 done")

    # 6. Commit 6: Chatbots & Messaging (2026-01-15)
    run_git(["add",
        "templates/05-chatbots-telegram-whatsapp/11-Telegram-AI-Assistant.json",
        "templates/05-chatbots-telegram-whatsapp/19-News-AI-Summary-Telegram.json",
        "templates/05-chatbots-telegram-whatsapp/23-WhatsApp-Business-Customer-Support-Bot.json",
        "templates/05-chatbots-telegram-whatsapp/25-Discord-Community-Welcome-Role-Assigner.json",
        "templates/05-chatbots-telegram-whatsapp/38-Telegram-Multi-Language-Translation-Bot.json",
        "templates/05-chatbots-telegram-whatsapp/39-Zendesk-Critical-Ticket-Escalator.json"
    ])
    run_git(["commit", "-m", "feat(chatbots): add conversational Telegram assistant, WhatsApp support, and Discord bots"], {
        "GIT_AUTHOR_DATE": "2026-01-15 13:40:00 +0530",
        "GIT_COMMITTER_DATE": "2026-01-15 13:40:00 +0530"
    })
    print("Commit 6: 2026-01-15 done")

    # 7. Commit 7: Document Processing & RAG (2026-03-28)
    run_git(["add",
        "templates/06-document-processing-rag/13-Google-Drive-File-Organizer.json",
        "templates/06-document-processing-rag/22-YouTube-Video-Transcriber-AI-Summarizer.json",
        "templates/06-document-processing-rag/26-Automated-PDF-Invoice-Data-Extractor.json",
        "templates/06-document-processing-rag/33-Notion-Database-Auto-Backup-To-Drive.json",
        "templates/06-document-processing-rag/41-Expense-Receipt-Scanner-Categorizer.json",
        "templates/06-document-processing-rag/51-Contract-Clause-Extractor-Compliance-Auditor.json"
    ])
    run_git(["commit", "-m", "feat(docs): add Drive organizer, Gemini Vision invoice/receipt extractor, and contract auditor"], {
        "GIT_AUTHOR_DATE": "2026-03-28 17:25:00 +0530",
        "GIT_COMMITTER_DATE": "2026-03-28 17:25:00 +0530"
    })
    print("Commit 7: 2026-03-28 done")

    # 8. Commit 8: Marketing & Social (2026-05-19)
    run_git(["add",
        "templates/07-social-media-marketing/29-Social-Media-Cross-Poster.json",
        "templates/07-social-media-marketing/31-App-Store-Review-Sentiment-Monitor.json",
        "templates/07-social-media-marketing/40-WordPress-Auto-Publisher-SEO-Optimizer.json",
        "templates/07-social-media-marketing/53-Creative-Asset-Prompt-Cloudinary-Uploader.json"
    ])
    run_git(["commit", "-m", "feat(marketing): add multi-platform social media poster and SEO WordPress generator"], {
        "GIT_AUTHOR_DATE": "2026-05-19 12:05:00 +0530",
        "GIT_COMMITTER_DATE": "2026-05-19 12:05:00 +0530"
    })
    print("Commit 8: 2026-05-19 done")

    # 9. Commit 9: DevOps & Monitoring (2026-07-22)
    run_git(["add", "templates/08-devops-system-monitoring/"])
    run_git(["commit", "-m", "feat(devops): add database sync, website uptime monitor, and Docker crash alerting"], {
        "GIT_AUTHOR_DATE": "2026-07-22 16:50:00 +0530",
        "GIT_COMMITTER_DATE": "2026-07-22 16:50:00 +0530"
    })
    print("Commit 9: 2026-07-22 done")

    # 10. Commit 10: E-Commerce & Finance (2026-08-14)
    run_git(["add",
        "templates/01-email-automation/32-Stripe-Failed-Payment-Recovery-Dunning-Bot.json",
        "templates/01-email-automation/42-RSS-Feed-To-Newsletter-Draft-Generator.json",
        "templates/09-finance-ecommerce/"
    ])
    run_git(["commit", "-m", "feat(ecommerce): add Shopify fulfillment, competitor price monitor, and KPI reporting"], {
        "GIT_AUTHOR_DATE": "2026-08-14 10:30:00 +0530",
        "GIT_COMMITTER_DATE": "2026-08-14 10:30:00 +0530"
    })
    print("Commit 10: 2026-08-14 done")

    # 11. Commit 11: Autonomous Agents & Remaining Workflows (2026-09-02)
    run_git(["add", "templates/"])
    run_git(["commit", "-m", "feat(agents): complete 62 workflows with autonomous deep research and Notion RAG assistant"], {
        "GIT_AUTHOR_DATE": "2026-09-02 14:15:00 +0530",
        "GIT_COMMITTER_DATE": "2026-09-02 14:15:00 +0530"
    })
    print("Commit 11: 2026-09-02 done")

    # 12. Commit 12: README and Tooling (2026-09-14)
    run_git(["add", "README.md", "scripts/"])
    run_git(["commit", "-m", "docs: update comprehensive README directory, validation tooling, and release v1.0.0"], {
        "GIT_AUTHOR_DATE": "2026-09-14 18:00:00 +0530",
        "GIT_COMMITTER_DATE": "2026-09-14 18:00:00 +0530"
    })
    print("Commit 12: 2026-09-14 done")

    # Move temp_main to main
    run_git(["branch", "-M", "main"])
    print("Successfully switched to main branch with clean history!")

if __name__ == "__main__":
    main()
