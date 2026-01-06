# AIMeetingToJira
This project automates post-meeting follow-ups by turning raw meeting notes into structured action items and automatically creating Jira tickets. A serverless AWS backend uses an AI model to extract tasks with owners and due dates, reducing manual admin work and preventing missed follow-ups.


# Meeting Notes → Jira Automation

## Overview
This project automates post-meeting follow-ups by turning raw meeting notes into structured action items and automatically creating Jira tickets. A serverless AWS backend uses GPT to extract tasks with owners and due dates, reducing manual administrative work and preventing missed follow-ups.

---

## Problem
After meetings, teams often spend time manually reviewing notes, identifying action items, and creating Jira tickets. This process is repetitive, error-prone, and leads to missed or delayed follow-ups.

---

## Solution
The application accepts meeting notes through an HTTP endpoint, uses GPT to extract structured action items, and creates corresponding Jira tickets automatically. The system is designed to be simple, reliable, and easy to extend.

---

## Architecture
- **AWS Lambda** – core backend logic
- **AWS API Gateway (HTTP API)** – public interface
- **GPT API** – action item extraction
- **Jira REST API** – ticket creation
- **SendGrid** – email summary delivery
- **AWS CloudWatch** – logging and monitoring

**Flow:**
1. User submits meeting notes
2. Lambda extracts action items using GPT
3. Parsed tasks are validated
4. Jira tickets are created automatically
5. A summary of created tickets is returned (and optionally emailed)

---

## Tech Stack
- **Backend:** AWS Lambda (Python)
- **API:** AWS API Gateway
- **AI:** OpenAI GPT API
- **Integrations:** Jira REST API, SendGrid
- **Logging:** AWS CloudWatch

---

## Example

### Input
Discussed Q2 launch timeline.
Alex will prepare the marketing deck by April 10.
Jamie to follow up with the design team next week.

### Output
```json
{
  "summary": "Discussion of Q2 launch planning and next steps.",
  "action_items": [
    {
      "task": "Prepare marketing deck",
      "owner": "Alex",
      "due_date": "2024-04-10"
    },
    {
      "task": "Follow up with design team",
      "owner": "Jamie",
      "due_date": null
    }
  ]
}
